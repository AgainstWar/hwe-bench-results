#!/usr/bin/env python3
"""Compute File-Level Precision for HWE-Bench evaluation results.

File-Level Precision = |agent_files ∩ ground_truth_files| / |agent_files|

Where:
  agent_files       = files modified by the agent's patch (parsed from fix_patch in patches.jsonl)
  ground_truth_files = files modified in the original PR (from modified_files in dataset JSONL)

Reference: HWE-Bench paper Table 3, Section 4.1 Metrics.
"""

import json
import argparse
from pathlib import Path
from unidiff import PatchSet


def extract_files_from_patch(patch_text: str) -> set[str]:
    """Extract modified file paths from a unified diff patch string.

    Uses unidiff.PatchSet to parse the patch, then extracts the file paths
    from each hunks' header, stripping the a/ or b/ prefix convention.
    """
    files: set[str] = set()
    try:
        patch_set = PatchSet(patch_text)
    except Exception:
        # Fallback: manually scan for diff --git or +++ lines
        for line in patch_text.splitlines():
            if line.startswith("diff --git "):
                parts = line.split()
                if len(parts) >= 4:
                    path = parts[3]
                    if path.startswith("b/"):
                        path = path[2:]
                    if path != "/dev/null":
                        files.add(path)
            elif line.startswith("+++ "):
                path = line[4:].strip()
                if path.startswith("b/"):
                    path = path[2:]
                if path != "/dev/null":
                    files.add(path)
        return files

    for patched_file in patch_set:
        if patched_file.source_file != "/dev/null":
            path = patched_file.source_file
        else:
            path = patched_file.target_file
        if path.startswith("a/") or path.startswith("b/"):
            path = path[2:]
        files.add(path)
    return files


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute File-Level Precision for HWE-Bench evaluation results."
    )
    parser.add_argument(
        "--patches", type=Path, required=True,
        help="Agent patches.jsonl file (output of verify_bridge).",
    )
    parser.add_argument(
        "--dataset", type=Path, required=True,
        help="Dataset JSONL file containing modified_files field.",
    )
    parser.add_argument(
        "--repo", type=str, default=None,
        help="Filter to a specific repo (e.g. 'ibex', 'cva6', 'xiangshan').",
    )
    args = parser.parse_args()

    # ------------------------------------------------------------------
    # 1. Load ground-truth modified_files from dataset JSONL
    # ------------------------------------------------------------------
    gt_files: dict[str, set[str]] = {}
    with open(args.dataset, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            rec_id = f"{rec['org']}/{rec['repo']}:pr-{rec['number']}"
            if args.repo and rec["repo"].lower() != args.repo.lower():
                continue
            mf = rec.get("modified_files", [])
            gt_files[rec_id] = set(
                mf if isinstance(mf, list) else [m.strip() for m in str(mf).split(",")]
            )

    if not gt_files:
        print(f"No matching cases found in dataset for repo={args.repo}")
        return

    # ------------------------------------------------------------------
    # 2. Load agent patches and compute precision
    # ------------------------------------------------------------------
    total_agent_files = 0
    matched_files = 0
    per_case: list[tuple[str, int, int, float]] = []
    empty_patch_count = 0
    no_gt_count = 0

    with open(args.patches, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            rec_id = f"{rec['org']}/{rec['repo']}:pr-{rec['number']}"
            if args.repo and rec["repo"].lower() != args.repo.lower():
                continue
            if rec_id not in gt_files:
                no_gt_count += 1
                continue

            agent_files = extract_files_from_patch(rec.get("fix_patch", ""))
            truth_files = gt_files[rec_id]

            n_agent = len(agent_files)
            if n_agent == 0:
                empty_patch_count += 1
                continue

            n_match = len(agent_files & truth_files)
            prec = n_match / n_agent

            total_agent_files += n_agent
            matched_files += n_match
            per_case.append((rec_id, n_match, n_agent, prec))

    # ------------------------------------------------------------------
    # 3. Report results
    # ------------------------------------------------------------------
    overall_precision = (
        matched_files / total_agent_files if total_agent_files > 0 else 0.0
    )
    avg_precision = (
        sum(p for _, _, _, p in per_case) / len(per_case) if per_case else 0.0
    )

    print(f"{'='*70}")
    print(f"  File-Level Precision Report")
    print(f"{'='*70}")
    print(f"  Cases with patches:           {len(per_case)}")
    print(f"  Empty patches (skipped):      {empty_patch_count}")
    print(f"  No ground-truth match:        {no_gt_count}")
    print(f"  Overall File-Level Precision: {overall_precision:.4f}")
    print(f"  Average (per-case) Precision: {avg_precision:.4f}")
    print()
    print(f"  Per-case detail:")
    print(f"  {'instance_id':<45} {'match':>6} {'total':>6} {'precision':>10}")
    print(f"  {'-'*45} {'-'*6} {'-'*6} {'-'*10}")
    for rec_id, n_match, n_agent, prec in sorted(per_case):
        bar = "█" * int(prec * 10) + "░" * (10 - int(prec * 10))
        print(f"  {rec_id:<45} {n_match:>6} {n_agent:>6} {prec:>9.4f}  {bar}")
    print(f"{'='*70}")
    print()
    print("Note: Overall Precision (aggregated across all cases) matches")
    print("      the paper's Table 3 calculation method.")


if __name__ == "__main__":
    main()
