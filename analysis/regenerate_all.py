#!/usr/bin/env python3
import json, tarfile, tempfile, os, subprocess, re, shutil, argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANALYSIS = os.path.join(BASE, 'analysis')
DATASETS = '/home/username/hwe-bench/datasets'
TOKEN_SCRIPT = os.path.join(ANALYSIS, 'token_report.py')
PRECISION_SCRIPT = os.path.join(ANALYSIS, 'compute_precision.py')
ANALYZE_SCRIPT = os.path.join(ANALYSIS, 'analyze_repo.py')
ARTIFACTS = '/home/username/hwe-bench-artifacts/results'

DS_MAP = {
    'ibex': ('lowRISC__ibex.jsonl', 'ibex'),
    'cva6': ('openhwgroup__cva6.jsonl', 'cva6'),
    'caliptra': ('chipsalliance__caliptra-rtl.jsonl', 'caliptra-rtl'),
    'rocketchip': ('chipsalliance__rocket-chip.jsonl', 'rocket-chip'),
    'xiangshan': ('OpenXiangShan__XiangShan.jsonl', 'XiangShan'),
}

def get_type(repo, pr):
    """Return bug type for a PR (cached from previous analysis)."""
    extra = {
        'ibex': {83:'logic',104:'spec',155:'logic',293:'interface',332:'spec',475:'spec',882:'logic',907:'interface',974:'timing_sync',1135:'config_integ',1141:'interface',1229:'interface',1469:'spec',1513:'logic',1584:'spec',1816:'spec',1865:'interface',2232:'interface'},
        'cva6': {2170:'interface',2279:'interface',2374:'spec',2420:'config_integ',2549:'logic',2589:'logic',2711:'spec',2802:'spec',2844:'spec',2916:'interface',2989:'spec',3042:'interface',3168:'logic',3231:'spec'},
        'caliptra': {70:'logic',134:'interface',195:'logic',244:'logic',506:'interface',633:'logic',725:'logic',757:'timing_sync',760:'sw_hw_config',963:'spec',1033:'sw_hw_config'},
        'rocketchip': {177:'logic',387:'timing_sync',404:'logic',485:'interface',542:'logic',576:'logic',745:'config_integ',1069:'logic',1093:'sw_hw_interact',1176:'interface',1330:'logic',1493:'config_integ',1656:'interface',1761:'logic',1878:'spec',2018:'interface',2036:'logic',2167:'timing_sync',2213:'interface',2368:'config_integ',2543:'logic',2621:'config_integ',2984:'logic',2988:'logic',2994:'logic',3004:'timing_sync',3065:'interface',3256:'logic',3526:'logic',3600:'timing_sync',3624:'spec',3651:'spec'},
        'xiangshan': {39:'logic',281:'logic',655:'logic',739:'timing_sync',1242:'logic',1323:'spec',1395:'logic',1401:'timing_sync',1602:'timing_sync',1679:'interface',1694:'logic',1793:'timing_sync',1820:'sw_hw_config',1907:'logic',1931:'logic',2095:'logic',2195:'timing_sync',2246:'config_integ',2351:'interface',2483:'logic',2513:'logic',2781:'interface',2845:'timing_sync',2997:'logic',3307:'interface',3329:'interface',3555:'spec',3636:'logic',3717:'spec',3753:'spec',3859:'spec',3867:'logic',3907:'spec',3955:'interface',4110:'sw_hw_config',4166:'interface',4179:'spec',4426:'interface',4442:'interface',4533:'interface',4750:'timing_sync',4943:'sw_hw_config',4968:'timing_sync',5182:'logic',5189:'logic',5496:'sw_hw_config',5593:'interface',5687:'logic',5700:'logic'},
    }
    return extra.get(repo, {}).get(pr, 'logic')

def run(cmd, timeout=60):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return r.stdout, r.stderr

def extract_tarball(tarball, tmp):
    """Extract tarball, return (jobs_dir, eval_dir, patches_file)."""
    with tarfile.open(tarball) as t: t.extractall(path=tmp)
    patches_file = None
    for root, dirs, files in os.walk(tmp):
        if 'patches.jsonl' in files: patches_file = os.path.join(root, 'patches.jsonl')
    # Find jobs subdir
    jobs_dir = None
    for root, dirs, files in os.walk(tmp):
        if os.path.basename(root) == 'jobs':
            for d in os.listdir(root):
                full = os.path.join(root, d)
                if os.path.isdir(full) and not d.startswith('.'):
                    for sub in os.listdir(full):
                        if os.path.isdir(os.path.join(full, sub)) and os.path.isfile(os.path.join(full, sub, 'result.json')):
                            jobs_dir = full; break
                if jobs_dir: break
    eval_dir = None
    for root, dirs, files in os.walk(tmp):
        if 'final_report.json' in files and '/eval' in root and 'eval_workdir' not in root:
            eval_dir = root; break
    return jobs_dir, eval_dir, patches_file

def parse_token_summary(out):
    s = {}
    for line in out.splitlines():
        if m := re.search(r'Tasks\s+:\s+(\d+)', line): s['tasks'] = m.group(1)
        if m := re.search(r'Status\s+:\s*(.+)', line): s['status'] = m.group(1).strip()
        if m := re.search(r'Prompt\s*\(K\)\s+([\d.]+)', line): s['prompt_k'] = m.group(1)
        if m := re.search(r'Completion\s*\(K\)\s+([\d.]+)', line): s['completion_k'] = m.group(1)
        if m := re.search(r'Cache hits\s*\(%\)\s+([\d.]+)', line): s['cache_pct'] = m.group(1)
        if m := re.search(r'Tool calls\s+([\d.]+)', line): s['tool_calls'] = m.group(1)
        if m := re.search(r'Own-price Cost.*?\$([\d.]+)', line): s['own_cost'] = m.group(1)
        costs = re.findall(r'Cost\s*\(\$\)\s+\$([\d.]+)', line)
        if costs: s['cost'] = costs[0]
    return s

def parse_token_details(out):
    rows = []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 7 and all(p.replace('.','').replace('-','').isdigit() for p in parts[2:7]):
            rows.append(parts[:7])
    return rows

def generate_report(config_name, repo, tarball, report_path, use_filter=False):
    tmp = tempfile.mkdtemp(dir='/tmp')
    try:
        jobs_dir, eval_dir, patches_file = extract_tarball(tarball, tmp)
        if not jobs_dir or not patches_file:
            return None
        
        ds_name, repo_filter = DS_MAP[repo]
        ds_path = os.path.join(DATASETS, ds_name)
        
        # 1. compute_precision
        prec_out, _ = run([sys.executable, PRECISION_SCRIPT, '--patches', patches_file, '--dataset', ds_path, '--repo', repo_filter])
        flp = None
        if m := re.search(r'Overall File-Level Precision:\s*([\d.]+)', prec_out): flp = f'{float(m.group(1))*100:.1f}%'
        
        # 2. token_report
        filter_arg = ['--filter', repo] if use_filter else []
        tok_out, _ = run([sys.executable, TOKEN_SCRIPT, jobs_dir, '--eval', eval_dir] + filter_arg + ['--details'])
        tok_sum = parse_token_summary(tok_out)
        tok_detail = parse_token_details(tok_out)
        
        # 3. Read eval/final_report.json
        resolved_ids = set()
        total = 0
        resolved = 0
        unresolved_ids = []
        if eval_dir:
            with open(os.path.join(eval_dir, 'final_report.json')) as f:
                eval_data = json.load(f)
            resolved_ids = set(eval_data.get('resolved_ids', []))
            total = eval_data.get('total_instances', 0)
            resolved = eval_data.get('resolved_instances', 0)
            unresolved_ids = eval_data.get('unresolved_ids', [])
        
        # 4. Build report
        rr = f'{resolved/total*100:.1f}%' if total > 0 else 'N/A'
        
        # Unresolved cases with bug types
        uc_lines = []
        tc = {}
        for rid in sorted(unresolved_ids, key=lambda x: int(x.split('pr-')[1])):
            pr = int(rid.split('pr-')[1])
            bt = get_type(repo, pr)
            uc_lines.append(f'  {{"pr": {pr}, "test": "N/A", "type": "{bt}", "desc": "N/A"}}')
            tc[bt] = tc.get(bt, 0) + 1
        
        md = f"""# {repo.title()} {config_name} Analysis

## Overall Results

```yaml
config: {config_name}
repo: {repo}
agent: OpenCode
model: DeepSeek V4 Flash
resolved: {resolved}
total: {total}
resolved_rate: {rr}
file_level_precision: {flp or 'N/A'}
infra_errors: 0
```

## Token Statistics (token_report.py)

### Average Metrics

```yaml
token_statistics:
  tasks: {tok_sum.get('tasks', 'N/A')}
  status: {tok_sum.get('status', 'N/A')}
  prompt_k: {tok_sum.get('prompt_k', 'N/A')}
  completion_k: {tok_sum.get('completion_k', 'N/A')}
  cache_hit_pct: {tok_sum.get('cache_pct', 'N/A')}
  tool_calls: {tok_sum.get('tool_calls', 'N/A')}
  cost_usd: {tok_sum.get('cost', 'N/A')}
  own_price_cost_usd: {tok_sum.get('own_cost', 'N/A')}
```

### Per-Task Detail

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
"""
        for row in tok_detail[:60]:
            md += f'| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} |\n'
        
        md += f"""
## Unresolved Cases

```json
[
{','.join(uc_lines) if uc_lines else ''}
]
```

## Bug Type Distribution

```yaml
{chr(10).join([f'  {k}: {v}' for k,v in sorted(tc.items())]) if tc else '  无'}
```

## File-Level Precision

- **Overall**: {flp or 'N/A'}
"""
        with open(report_path, 'w') as f:
            f.write(md)
        return {'resolved': resolved, 'total': total, 'flp': flp, 'tok': tok_sum}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

# Configs
configs = []
for repo in ['ibex','cva6','caliptra','rocketchip','xiangshan']:
    configs.append(('baseline', repo, f'{BASE}/baseline/deepseek/results-deepseek-{repo}.tar.gz',
                   f'{BASE}/baseline/deepseek/deepseek-{repo}.md', False))
mcp_f = {'ibex':'results-ds-mcp-ibex-final.tar.gz','cva6':'results-ds-mcp-cva6.tar.gz','caliptra':'results-ds-mcp-caliptra.tar.gz','rocketchip':'results-ds-mcp-rocketchip.tar.gz','xiangshan':'results-ds-mcp-xiangshan.tar.gz'}
for repo, fn in mcp_f.items():
    configs.append(('mcp', repo, f'{BASE}/wavemcp/{fn}', f'{BASE}/wavemcp/mcp-{repo}.md', False))
for repo in ['ibex','cva6','caliptra','rocketchip','xiangshan']:
    configs.append(('skills', repo, f'{BASE}/skills/results-test-skills-{repo}.tar.gz',
                   f'{BASE}/skills/skills-{repo}.md', False))
for subdir in ['locate','repair','all']:
    tb = f'{BASE}/ablation/{subdir}/results-abl-mcp-{subdir}.tar.gz'
    if os.path.exists(tb):
        for repo in ['ibex','cva6','caliptra','rocketchip','xiangshan']:
            rp = f'{BASE}/ablation/{subdir}/abl-{repo}-mcp-{subdir}.md'
            if os.path.exists(rp): configs.append((f'mcp+{subdir}', repo, tb, rp, True))
alone_tar = f'{BASE}/skillablation/results-abl-all.tar.gz'
if os.path.exists(alone_tar):
    for repo in ['ibex','cva6','caliptra','rocketchip','xiangshan']:
        for cfg in ['locate','repair']:
            rp = f'{BASE}/skillablation/abl-{repo}-{cfg}.md'
            if os.path.exists(rp): configs.append((f'{cfg}-alone', repo, alone_tar, rp, True))

if __name__ == '__main__':
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--config', type=str)
    parser.add_argument('--repo', type=str)
    args = parser.parse_args()
    
    todo = configs
    if args.config and args.repo:
        todo = [(c, r, tb, rp, f) for c, r, tb, rp, f in configs if c == args.config and r == args.repo]
    
    for cfg, repo, tarball, report_path, use_filter in todo:
        if not args.all and not (args.config and args.repo):
            continue
        print(f'{cfg:<12} {repo:<12}', end=' ', flush=True)
        try:
            result = generate_report(cfg, repo, tarball, report_path, use_filter)
            if result:
                print(f'✅ {result["resolved"]}/{result["total"]} | flp={result["flp"]} | pk={result["tok"].get("prompt_k","?")}K')
            else:
                print('❌ extraction failed')
        except Exception as e:
            print(f'❌ {e}')
