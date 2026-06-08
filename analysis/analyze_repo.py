#!/usr/bin/env python3
"""
Analyze a single repo: list unresolved cases with test names and official comparison.
Usage: python3 analyze_repo.py <repo_name> <results_tarball_path> <official_results_dir>

Example: python3 analyze_repo.py rocketchip ../baseline/hwe-rocketchip-full.tar.gz ../../hwe-bench-artifacts/results/rocketchip/gpt5.4
"""

import json, os, sys, re, tarfile, tempfile

def extract_tarball(tarball_path):
    """Extract tarball to temp dir and return the path."""
    tmp = tempfile.mkdtemp(prefix="repo_analysis_")
    with tarfile.open(tarball_path) as tar:
        tar.extractall(path=tmp)
    return tmp

def find_report(extract_dir):
    """Find final_report.json in the extracted directory."""
    for root, dirs, files in os.walk(extract_dir):
        if "final_report.json" in files:
            return os.path.join(root, "final_report.json")
    return None

def find_evals(extract_dir, pr_num):
    """Find eval_workdir path."""
    for root, dirs, files in os.walk(extract_dir):
        if f"pr-{pr_num}" in dirs:
            return os.path.join(root, f"pr-{pr_num}")
    return None

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 analyze_repo.py <repo_name> <results_tarball_path> <official_results_dir>")
        sys.exit(1)

    repo = sys.argv[1]
    tarball = sys.argv[2]
    official_dir = sys.argv[3] if len(sys.argv) > 3 else None

    off_resolved = set()
    if official_dir:
        off_report = os.path.join(official_dir, "eval", "final_report.json")
        if os.path.exists(off_report):
            with open(off_report) as f:
                off = json.load(f)
            off_resolved = set(off["resolved_ids"])

    tmp = extract_tarball(tarball)
    our_report_path = find_report(tmp)

    if not our_report_path:
        print(f"ERROR: Could not find final_report.json in {tarball}")
        sys.exit(1)

    with open(our_report_path) as f:
        our = json.load(f)

    resolved = set(our["resolved_ids"])
    unresolved = set(our["unresolved_ids"])

    print(f"\n{'='*60}")
    print(f"  {repo}")
    print(f"{'='*60}")
    print(f"  Resolved: {len(resolved)}/{our['total_instances']} ({len(resolved)/our['total_instances']*100:.0f}%)")
    print(f"  Infrastructure errors: {our['error_instances']}")
    print(f"\n  Unresolved cases ({len(unresolved)}):")
    print(f"  {'PR':<12} {'Test Name':<50} {'Official Status'}")

    for iid in sorted(unresolved):
        pr = iid.split(":pr-")[1]
        evals_dir = find_evals(tmp, pr)
        test_name = "unknown"

        if evals_dir:
            report_path = os.path.join(evals_dir, "report.json")
            if os.path.exists(report_path):
                with open(report_path) as f:
                    r = json.load(f)
                msg = r.get("error_msg", "")
                m = re.search(r"fix phase: `([^`]+)`", msg)
                test_name = m.group(1) if m else "unknown"

        off_status = "✅ 官方解了" if iid in off_resolved else "❌ 官方也没解"
        print(f"  pr-{pr:<8} {test_name:<50} {off_status}")

    off_only = off_resolved - resolved
    neither = unresolved - off_resolved
    both = resolved & off_resolved

    print(f"\n  都解了: {len(both)}")
    print(f"  官方解我们没解: {len(off_only)}")
    print(f"  都没解: {len(neither)}")

if __name__ == "__main__":
    main()
