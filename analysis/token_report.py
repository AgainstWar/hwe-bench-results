#!/usr/bin/env python3
# Token report per HWE-Bench paper methodology.
# Reads every trial's result.json (prompt/completion/cache/cost)
# and trajectory.json (tool-call count) to produce per-task averages.

import argparse, glob, json, os

# ── Model pricing (USD per 1M tokens) ──────────────────────────────────────
# Price source: official provider pages / tokenflux pricing
MODEL_PRICES: dict[str, dict[str, float]] = {
    "deepseek-v4-flash": {"prompt": 0.27, "completion": 1.10},
    "deepseek-v4-pro":   {"prompt": 0.55, "completion": 2.19},
    "deepseek-v3.2":     {"prompt": 0.27, "completion": 0.28},
    "gpt-5.4":           {"prompt": 1.25, "completion": 10.00},
    "gpt-5.5":           {"prompt": 1.25, "completion": 10.00},
    "default":           {"prompt": 0.27, "completion": 1.10},
}

# ── Helpers ─────────────────────────────────────────────────────────────────
def extract_model(trial_name, data):
    """Best-effort model name extraction."""
    agent = data.get("agent_info") or {}
    model = agent.get("model_info", {}).get("name", "")
    if model:
        return model
    return "default"

def load_trials(job_dir):
    """Yield (trial_name, result_json, maybe_trajectory_json) for each trial."""
    for d in sorted(os.listdir(job_dir)):
        rpath = os.path.join(job_dir, d, "result.json")
        if not os.path.isfile(rpath):
            continue
        if d in ("result.json", "config.json", "job.log"):
            continue
        with open(rpath) as f:
            result = json.load(f)
        traj = None
        tpath = os.path.join(job_dir, d, "agent", "trajectory.json")
        if os.path.isfile(tpath):
            try:
                with open(tpath) as f:
                    traj = json.load(f)
            except Exception:
                pass
        yield d, result, traj

def count_tool_calls(traj):
    """Count tool-call events in an ATIF trajectory."""
    n = 0
    for step in traj.get("steps", []):
        n += len(step.get("tool_calls", []))
    return n


def load_resolved_ids(eval_dir):
    """Read final_report.json and return the set of resolved instance IDs."""
    rpath = os.path.join(eval_dir, "final_report.json")
    if not os.path.isfile(rpath):
        return set()
    with open(rpath) as f:
        data = json.load(f)
    return set(data.get("resolved_ids", []))

def map_trial_to_instance(trial_name):
    """Best-effort mapping from trial dir name (ibex-pr-104__xxx) to instance_id (lowRISC/ibex:pr-104)."""
    base = trial_name.split("__")[0]
    parts = base.split("-")
    if parts[0] in ("ibex", "cva6", "xiangshan"):
        name = parts[0]
        pr = parts[-1]
    elif parts[0] == "rocket":
        name = "rocket-chip"
        pr = parts[-1]
    elif parts[0] == "caliptra":
        name = "caliptra-rtl"
        pr = parts[-1]
    else:
        return None  # unable to map
    # org mapping
    org_map = {"ibex": "lowRISC", "cva6": "openhwgroup", "caliptra-rtl": "chipsalliance",
               "rocket-chip": "chipsalliance", "xiangshan": "OpenXiangShan"}
    org = org_map.get(name, name)
    return f"{org}/{name}:pr-{pr}"

def classify_status(result):
    """Return patch_submitted | error | no_patch.

    Harbor's verifier only checks whether a patch file was produced;
    the real resolved/unresolved status comes from the evaluator
    (final_report.json).  This function maps trial-level outcomes.
    """
    exc = result.get("exception_info")
    if exc:
        return "error"
    ar = result.get("agent_result") or {}
    if ar.get("n_input_tokens") is None and ar.get("cost_usd") is None:
        return "no_patch"
    return "patch_submitted"

# ── Report ──────────────────────────────────────────────────────────────────
def report(job_dir, eval_dir=None, show_details=False):
    resolved_ids = load_resolved_ids(eval_dir) if eval_dir else set()
    rows = []
    for name, result, traj in load_trials(job_dir):
        agent = result.get("agent_result") or {}
        inp  = agent.get("n_input_tokens")  or 0
        cch  = agent.get("n_cache_tokens")  or 0
        out  = agent.get("n_output_tokens") or 0
        cost = agent.get("cost_usd")        or 0.0

        model = extract_model(name, result)
        price = MODEL_PRICES.get(model, MODEL_PRICES["default"])
        own_cost = (inp / 1_000_000) * price["prompt"] + \
                   (out / 1_000_000) * price["completion"]

        tcalls = count_tool_calls(traj) if traj else None
        status = classify_status(result)
        # Correlate with evaluator if available
        if status == "patch_submitted" and resolved_ids is not None:
            iid = map_trial_to_instance(name)
            if iid:
                status = "resolved" if iid in resolved_ids else "unresolved"

        rows.append({
            "trial": name,
            "prompt": inp,
            "cache": cch,
            "completion": out,
            "cost": cost,
            "own_cost": own_cost,
            "tool_calls": tcalls,
            "status": status,
        })

    if not rows:
        print("No trials found.")
        return

    # ── Overall averages ─────────────────────────────────────────────────────
    n = len(rows)
    total_prompt = sum(r["prompt"] for r in rows)
    total_completion = sum(r["completion"] for r in rows)
    total_cache = sum(r["cache"] for r in rows)
    total_cost = sum(r["cost"] for r in rows)
    total_own = sum(r["own_cost"] for r in rows)

    # 缓存命中比 = cache / prompt（只有当 cache ≤ prompt 时才有意义）
    total_cache_pct = (total_cache / total_prompt * 100) if total_prompt else 0
    # 平均工具调用（排除 None）
    tc_vals = [r["tool_calls"] for r in rows if r["tool_calls"] is not None]
    avg_tc = sum(tc_vals) / len(tc_vals) if tc_vals else 0

    # 状态计数
    status_cnt = {}
    for r in rows:
        status_cnt[r["status"]] = status_cnt.get(r["status"], 0) + 1

    print(f"\n{'='*80}")
    print(f"  HWE-bench Token Consumption Report")
    print(f"{'='*80}")
    print(f"  Tasks       : {n}")
    print(f"  Status      : ", end="")
    for s in ["resolved", "unresolved", "patch_submitted", "error", "no_patch"]:
        if s in status_cnt:
            print(f"{s}={status_cnt[s]} ", end="")
    print()
    print(f"\n  {'Metric':<25}{'Avg / Task (K=tokens)':<25}{'Total':>20}")
    print(f"  {'-'*25}{'-'*25}{'-'*20}")
    print(f"  {'Prompt (K)':<25}{(total_prompt / n / 1000):<25.1f}{total_prompt:>20,}")
    print(f"  {'Completion (K)':<25}{(total_completion / n / 1000):<25.1f}{total_completion:>20,}")
    print(f"  {'Cache hits (%)':<25}{total_cache_pct:<25.1f}{total_cache:>20,}")
    print(f"  {'Tool calls':<25}{avg_tc:<25.1f}{'':>20}")
    print(f"  {'Cost ($)':<25}{'$' + f'{total_cost / n:.6f}':<25}{'$' + f'{total_cost:.4f}':>20}")
    if total_own > 0:
        print(f"  {'Own-price Cost ($)':<25}{'$' + f'{total_own / n:.6f}':<25}{'$' + f'{total_own:.4f}':>20}")
    print()
    if total_prompt > 0:
        ratio = total_cache / total_prompt * 100
        print(f"  Cache hit ratio = {ratio:.1f}%   (cached tokens / prompt tokens)")
    print(f"{'='*80}\n")

    # ── Per-task details ─────────────────────────────────────────────────────
    if show_details:
        print(f"  {'Trial':<50} {'Status':<14} {'Prompt(K)':>10} {'Comp(K)':>9} {'Cost($)':>9} {'Cache%':>7} {'Calls':>6}")
        print(f"  {'-'*50} {'-'*14} {'-'*10} {'-'*9} {'-'*9} {'-'*7} {'-'*6}")
        for r in rows:
            pk = r["prompt"] / 1000
            ck = r["completion"] / 1000
            cpct = r["cache"] / r["prompt"] * 100 if r["prompt"] else 0
            tc = r["tool_calls"] if r["tool_calls"] is not None else "-"
            print(f"  {r['trial']:<50} {r['status']:<14} {pk:>10.1f} {ck:>9.1f} {r['cost']:>9.4f} {cpct:>6.1f} {str(tc):>6}")
        print()

def main():
    parser = argparse.ArgumentParser(description="Token report per HWE-Bench paper methodology")
    parser.add_argument("job_dir", help="Path to Harbor job directory")
    parser.add_argument("--eval", type=str, default=None,
                        help="Path to eval/ directory from hwe-bench.evaluator"
                             " (used to tag tasks as resolved/unresolved)")
    parser.add_argument("--details", action="store_true", help="Show per-task breakdown")
    args = parser.parse_args()
    report(args.job_dir, eval_dir=args.eval, show_details=args.details)

if __name__ == "__main__":
    main()
