# XiangShan Ablation - LOCATE

## 总体结果

```yaml
locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 1
  total: 54
  resolved_rate: 1.9%
  file_level_precision: 23.1%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 1/54 (1.9%) |
| File-Level Precision | 89.7% | 23.1% |

### 新解决
  无

### 丢失
  pr-39, pr-281, pr-1931, pr-2483, pr-3182, pr-3867, pr-4337, pr-4764, pr-4943, pr-4959, pr-5700

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1242 | 0.0% | 0/1 |
| pr-1401 | 0.0% | 0/1 |
| pr-1793 | 0.0% | 0/1 |
| pr-2195 | 0.0% | 0/1 |
| pr-2845 | 100.0% | 1/1 |
| pr-4110 | 0.0% | 0/1 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 0.0% | 0/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-5182 | 0.0% | 0/1 |

## File-Level Precision

- **Overall**: 23.1%
- **Average (per-task)**: 20.0%

## 未解决 Case

```json
[
  {
    "pr": 39,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 281,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 655,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 739,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1242,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1323,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1395,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1401,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1602,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1679,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1694,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1793,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1820,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1907,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1931,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2095,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2195,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 2246,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2351,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2483,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2513,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2781,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2997,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3182,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3307,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3329,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3555,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3636,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3717,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3753,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3859,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3867,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3907,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3955,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 4110,
    "test": "N/A",
    "type": "sw_hw_config",
    "desc": "N/A"
  },
  {
    "pr": 4166,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 4179,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 4337,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 4426,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 4442,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 4533,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 4750,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 4764,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 4943,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 4959,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 4968,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 5080,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 5182,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 5189,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 5496,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 5593,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 5687,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 5700,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  logic: 4
  spec: 1
  sw_hw_config: 1
  timing_sync: 3
  unknown: 44
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 570.2
  completion_k: 3.4
  cache_hit_pct: 92.2
  tool_calls: 18.1
  mcp_calls: 0.0
  skill_calls: 1.0
  ordinary_calls: 17.1
  cost_usd: 0.012455
  own_price_cost_usd: 0.157742
  tasks: 54
  resolved: 1
  unresolved: 53
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| XiangShan-pr-1242 | unresolved | 313.4 | 2.9 | 0.0089 | 86.9 | 11 | 0 | 1 | 10 |
| XiangShan-pr-1323 | unresolved | 248.5 | 3.8 | 0.0058 | 89.0 | 19 | 0 | 1 | 18 |
| XiangShan-pr-1395 | unresolved | 59.9 | 2.2 | 0.0036 | 67.8 | 6 | 0 | 1 | 5 |
| XiangShan-pr-1401 | unresolved | 842.5 | 5.1 | 0.0145 | 91.9 | 26 | 0 | 1 | 25 |
| XiangShan-pr-1602 | unresolved | 2255.5 | 4.7 | 0.0335 | 95.4 | 40 | 0 | 1 | 39 |
| XiangShan-pr-1679 | unresolved | 402.5 | 2.2 | 0.0110 | 89.2 | 11 | 0 | 1 | 10 |
| XiangShan-pr-1694 | unresolved | 337.2 | 3.7 | 0.0144 | 83.7 | 11 | 0 | 1 | 10 |
| XiangShan-pr-1793 | unresolved | 1324.8 | 5.7 | 0.0258 | 96.2 | 34 | 0 | 1 | 33 |
| XiangShan-pr-1820 | unresolved | 124.4 | 2.9 | 0.0067 | 79.0 | 7 | 0 | 1 | 6 |
| XiangShan-pr-1907 | unresolved | 696.5 | 4.3 | 0.0184 | 92.5 | 19 | 0 | 1 | 18 |
| XiangShan-pr-1931 | unresolved | 144.6 | 2.3 | 0.0096 | 75.2 | 9 | 0 | 1 | 8 |
| XiangShan-pr-2095 | unresolved | 163.1 | 2.1 | 0.0101 | 80.8 | 7 | 0 | 1 | 6 |
| XiangShan-pr-2195 | unresolved | 458.4 | 3.5 | 0.0089 | 91.5 | 20 | 0 | 1 | 19 |
| XiangShan-pr-2246 | unresolved | 761.4 | 5.2 | 0.0089 | 95.7 | 34 | 0 | 1 | 33 |
| XiangShan-pr-2351 | unresolved | 419.4 | 2.8 | 0.0194 | 83.5 | 12 | 0 | 1 | 11 |
| XiangShan-pr-2483 | unresolved | 61.6 | 1.6 | 0.0039 | 68.4 | 3 | 0 | 1 | 2 |
| XiangShan-pr-2513 | unresolved | 596.4 | 4.1 | 0.0176 | 92.9 | 13 | 0 | 1 | 12 |
| XiangShan-pr-2781 | unresolved | 100.0 | 2.4 | 0.0053 | 70.0 | 7 | 0 | 1 | 6 |
| XiangShan-pr-281 | unresolved | 117.8 | 1.7 | 0.0042 | 84.5 | 6 | 0 | 1 | 5 |
| XiangShan-pr-2845 | resolved | 152.4 | 1.5 | 0.0043 | 88.4 | 12 | 0 | 0 | 12 |
| XiangShan-pr-2997 | unresolved | 305.1 | 3.5 | 0.0143 | 89.2 | 18 | 0 | 1 | 17 |
| XiangShan-pr-3182 | unresolved | 200.7 | 2.2 | 0.0076 | 80.5 | 7 | 0 | 1 | 6 |
| XiangShan-pr-3307 | unresolved | 1644.9 | 6.1 | 0.0205 | 96.7 | 41 | 0 | 1 | 40 |
| XiangShan-pr-3329 | unresolved | 472.7 | 2.8 | 0.0170 | 83.4 | 9 | 0 | 1 | 8 |
| XiangShan-pr-3555 | unresolved | 1354.3 | 4.5 | 0.0235 | 92.7 | 27 | 0 | 1 | 26 |
| XiangShan-pr-3636 | unresolved | 360.6 | 3.8 | 0.0101 | 89.3 | 18 | 0 | 1 | 17 |
| XiangShan-pr-3717 | unresolved | 318.3 | 2.9 | 0.0095 | 87.9 | 14 | 0 | 1 | 13 |
| XiangShan-pr-3753 | unresolved | 208.1 | 2.5 | 0.0098 | 83.6 | 8 | 0 | 1 | 7 |
| XiangShan-pr-3859 | unresolved | 1038.6 | 4.6 | 0.0128 | 95.6 | 32 | 0 | 1 | 31 |
| XiangShan-pr-3867 | unresolved | 823.1 | 4.1 | 0.0153 | 93.6 | 25 | 0 | 1 | 24 |
| XiangShan-pr-39 | unresolved | 209.3 | 2.5 | 0.0065 | 88.8 | 11 | 0 | 1 | 10 |
| XiangShan-pr-3907 | unresolved | 116.4 | 1.8 | 0.0039 | 83.6 | 6 | 0 | 1 | 5 |
| XiangShan-pr-3955 | unresolved | 264.9 | 3.3 | 0.0089 | 88.6 | 17 | 0 | 1 | 16 |
| XiangShan-pr-4110 | unresolved | 938.9 | 4.5 | 0.0136 | 96.2 | 30 | 0 | 1 | 29 |
| XiangShan-pr-4166 | unresolved | 967.8 | 5.3 | 0.0146 | 93.7 | 38 | 0 | 1 | 37 |
| XiangShan-pr-4179 | unresolved | 2888.4 | 8.3 | 0.0257 | 97.9 | 54 | 0 | 1 | 53 |
| XiangShan-pr-4337 | unresolved | 1250.3 | 4.8 | 0.0198 | 96.0 | 31 | 0 | 1 | 30 |
| XiangShan-pr-4426 | unresolved | 641.1 | 3.4 | 0.0157 | 91.1 | 19 | 0 | 1 | 18 |
| XiangShan-pr-4442 | unresolved | 493.2 | 3.4 | 0.0108 | 90.5 | 18 | 0 | 1 | 17 |
| XiangShan-pr-4533 | unresolved | 423.7 | 3.8 | 0.0100 | 92.2 | 18 | 0 | 1 | 17 |
| XiangShan-pr-4750 | unresolved | 695.3 | 3.0 | 0.0186 | 88.0 | 15 | 0 | 1 | 14 |
| XiangShan-pr-4764 | unresolved | 407.8 | 3.3 | 0.0076 | 92.1 | 28 | 0 | 1 | 27 |
| XiangShan-pr-4943 | unresolved | 694.7 | 5.1 | 0.0102 | 94.0 | 35 | 0 | 1 | 34 |
| XiangShan-pr-4959 | unresolved | 138.9 | 2.3 | 0.0058 | 83.4 | 10 | 0 | 1 | 9 |
| XiangShan-pr-4968 | unresolved | 292.3 | 2.6 | 0.0096 | 83.1 | 12 | 0 | 1 | 11 |
| XiangShan-pr-5080 | unresolved | 107.3 | 0.5 | 0.0129 | 78.5 | 6 | 0 | 1 | 5 |
| XiangShan-pr-5182 | unresolved | 657.8 | 3.6 | 0.0140 | 89.6 | 19 | 0 | 1 | 18 |
| XiangShan-pr-5189 | unresolved | 579.0 | 3.1 | 0.0154 | 88.2 | 13 | 0 | 1 | 12 |
| XiangShan-pr-5496 | unresolved | 756.1 | 3.7 | 0.0153 | 93.2 | 26 | 0 | 1 | 25 |
| XiangShan-pr-5593 | unresolved | 152.0 | 2.5 | 0.0070 | 83.4 | 7 | 0 | 1 | 6 |
| XiangShan-pr-5687 | unresolved | 462.7 | 3.7 | 0.0128 | 89.8 | 15 | 0 | 1 | 14 |
| XiangShan-pr-5700 | unresolved | 662.3 | 4.2 | 0.0156 | 90.7 | 18 | 0 | 1 | 17 |
| XiangShan-pr-655 | unresolved | 531.4 | 2.8 | 0.0160 | 93.3 | 16 | 0 | 1 | 15 |
| XiangShan-pr-739 | unresolved | 153.6 | 2.3 | 0.0072 | 83.0 | 10 | 0 | 1 | 9 |
