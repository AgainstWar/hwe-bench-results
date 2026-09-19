# XiangShan MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 54
  resolved_rate: 14.8%
  file_level_precision: 80.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 8/54 (14.8%) |
| File-Level Precision | 89.7% | 80.0% |

### 新解决
  pr-1679, pr-2513, pr-3717, pr-5080

### 丢失
  pr-39, pr-2483, pr-2845, pr-3182, pr-3867, pr-4337, pr-4943, pr-4959

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-281 | 100.0% | 1/1 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 100.0% | 1/1 |
| pr-1907 | 0.0% | 0/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2195 | 100.0% | 1/1 |
| pr-2513 | 100.0% | 1/1 |
| pr-2997 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3636 | 100.0% | 1/1 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 0.0% | 0/1 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-4110 | 50.0% | 1/2 |
| pr-4166 | 60.0% | 3/5 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 0.0% | 0/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4943 | 100.0% | 6/6 |
| pr-4968 | 88.9% | 8/9 |
| pr-5080 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 80.0%
- **Average (per-task)**: 82.7%

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
    "type": "unknown",
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
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1602,
    "test": "N/A",
    "type": "timing_sync",
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
    "type": "unknown",
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
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2095,
    "test": "N/A",
    "type": "logic",
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
    "pr": 2781,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2845,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2997,
    "test": "N/A",
    "type": "logic",
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
    "type": "interface",
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
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 3753,
    "test": "N/A",
    "type": "spec",
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
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 3907,
    "test": "N/A",
    "type": "spec",
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
    "type": "interface",
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
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 4750,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 4943,
    "test": "N/A",
    "type": "sw_hw_config",
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
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 5182,
    "test": "N/A",
    "type": "unknown",
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
    "type": "sw_hw_config",
    "desc": "N/A"
  },
  {
    "pr": 5593,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 5687,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  interface: 4
  logic: 7
  spec: 3
  sw_hw_config: 3
  timing_sync: 4
  unknown: 25
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 797.0
  completion_k: 3.7
  cache_hit_pct: 94.5
  tool_calls: 21.7
  mcp_calls: 0.0
  other_skill_calls: 0.7
  ordinary_calls: 20.9
  cost_usd: 0.013089
  own_price_cost_usd: 0.219249
  tasks: 54
  resolved: 8
  unresolved: 46
  error: 2
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| XiangShan-pr-1242 | unresolved | 128.3 | 1.8 | 0.0075 | 70.6 | 7 | 0 | 1 | 6 |
| XiangShan-pr-1323 | unresolved | 208.2 | 2.9 | 0.0082 | 81.9 | 11 | 0 | 1 | 10 |
| XiangShan-pr-1395 | unresolved | 541.5 | 3.9 | 0.0170 | 89.4 | 23 | 0 | 1 | 22 |
| XiangShan-pr-1401 | unresolved | 793.0 | 4.7 | 0.0176 | 93.5 | 24 | 0 | 1 | 23 |
| XiangShan-pr-1602 | unresolved | 3765.4 | 7.0 | 0.0413 | 97.6 | 45 | 0 | 0 | 45 |
| XiangShan-pr-1679 | resolved | 1344.3 | 3.0 | 0.0229 | 95.9 | 23 | 0 | 0 | 23 |
| XiangShan-pr-1694 | unresolved | 247.4 | 2.8 | 0.0130 | 77.3 | 7 | 0 | 1 | 6 |
| XiangShan-pr-1793 | unresolved | 332.2 | 3.2 | 0.0057 | 91.8 | 18 | 0 | 1 | 17 |
| XiangShan-pr-1820 | unresolved | 112.2 | 2.1 | 0.0048 | 77.4 | 8 | 0 | 1 | 7 |
| XiangShan-pr-1907 | unresolved | 849.0 | 4.3 | 0.0202 | 90.5 | 23 | 0 | 1 | 22 |
| XiangShan-pr-1931 | resolved | 986.3 | 3.0 | 0.0171 | 94.8 | 16 | 0 | 1 | 15 |
| XiangShan-pr-2095 | unresolved | 551.8 | 3.0 | 0.0103 | 93.9 | 17 | 0 | 1 | 16 |
| XiangShan-pr-2195 | unresolved | 607.0 | 3.0 | 0.0094 | 93.3 | 22 | 0 | 1 | 21 |
| XiangShan-pr-2246 | error | 0.0 | 0.0 | 0.0000 | 0.0 | 0 | 0 | 0 | 0 |
| XiangShan-pr-2351 | error | 0.0 | 0.0 | 0.0000 | 0.0 | 0 | 0 | 0 | 0 |
| XiangShan-pr-2483 | unresolved | 151.7 | 2.3 | 0.0076 | 80.0 | 8 | 0 | 1 | 7 |
| XiangShan-pr-2513 | resolved | 1506.7 | 7.7 | 0.0157 | 96.9 | 34 | 0 | 1 | 33 |
| XiangShan-pr-2781 | unresolved | 292.9 | 3.2 | 0.0087 | 85.3 | 13 | 0 | 1 | 12 |
| XiangShan-pr-281 | resolved | 366.0 | 2.3 | 0.0071 | 92.6 | 13 | 0 | 1 | 12 |
| XiangShan-pr-2845 | unresolved | 133.6 | 1.9 | 0.0065 | 73.8 | 5 | 0 | 1 | 4 |
| XiangShan-pr-2997 | unresolved | 2332.3 | 5.6 | 0.0246 | 97.9 | 56 | 0 | 1 | 55 |
| XiangShan-pr-3182 | unresolved | 274.2 | 3.1 | 0.0077 | 87.0 | 12 | 0 | 1 | 11 |
| XiangShan-pr-3307 | unresolved | 540.2 | 2.7 | 0.0090 | 94.2 | 20 | 0 | 0 | 20 |
| XiangShan-pr-3329 | unresolved | 698.4 | 4.5 | 0.0171 | 92.1 | 19 | 0 | 1 | 18 |
| XiangShan-pr-3555 | unresolved | 712.3 | 3.2 | 0.0154 | 92.1 | 21 | 0 | 1 | 20 |
| XiangShan-pr-3636 | unresolved | 1114.8 | 3.6 | 0.0192 | 96.0 | 28 | 0 | 1 | 27 |
| XiangShan-pr-3717 | resolved | 404.0 | 2.9 | 0.0073 | 92.1 | 15 | 0 | 1 | 14 |
| XiangShan-pr-3753 | unresolved | 502.4 | 3.3 | 0.0141 | 90.3 | 14 | 0 | 1 | 13 |
| XiangShan-pr-3859 | unresolved | 600.1 | 4.9 | 0.0118 | 91.4 | 23 | 0 | 1 | 22 |
| XiangShan-pr-3867 | unresolved | 1428.1 | 4.5 | 0.0187 | 96.8 | 25 | 0 | 1 | 24 |
| XiangShan-pr-39 | unresolved | 69.0 | 1.6 | 0.0056 | 65.5 | 3 | 0 | 1 | 2 |
| XiangShan-pr-3907 | unresolved | 174.4 | 1.4 | 0.0041 | 88.5 | 9 | 0 | 0 | 9 |
| XiangShan-pr-3955 | unresolved | 656.8 | 3.9 | 0.0121 | 94.5 | 26 | 0 | 1 | 25 |
| XiangShan-pr-4110 | unresolved | 1115.2 | 4.9 | 0.0121 | 97.1 | 44 | 0 | 0 | 44 |
| XiangShan-pr-4166 | unresolved | 3379.0 | 10.1 | 0.0284 | 97.8 | 72 | 0 | 1 | 71 |
| XiangShan-pr-4179 | unresolved | 1131.5 | 4.9 | 0.0134 | 95.8 | 36 | 0 | 0 | 36 |
| XiangShan-pr-4337 | unresolved | 848.9 | 4.3 | 0.0132 | 95.2 | 27 | 0 | 1 | 26 |
| XiangShan-pr-4426 | unresolved | 717.2 | 4.6 | 0.0153 | 90.4 | 25 | 0 | 1 | 24 |
| XiangShan-pr-4442 | unresolved | 239.3 | 2.3 | 0.0116 | 74.1 | 7 | 0 | 1 | 6 |
| XiangShan-pr-4533 | unresolved | 327.8 | 1.7 | 0.0074 | 90.7 | 11 | 0 | 0 | 11 |
| XiangShan-pr-4750 | unresolved | 1100.6 | 4.3 | 0.0174 | 93.2 | 18 | 0 | 1 | 17 |
| XiangShan-pr-4764 | resolved | 583.8 | 3.7 | 0.0092 | 93.6 | 27 | 0 | 0 | 27 |
| XiangShan-pr-4943 | unresolved | 2682.1 | 9.9 | 0.0242 | 97.5 | 63 | 0 | 1 | 62 |
| XiangShan-pr-4959 | unresolved | 417.8 | 3.2 | 0.0085 | 92.1 | 20 | 0 | 1 | 19 |
| XiangShan-pr-4968 | unresolved | 1823.9 | 7.3 | 0.0181 | 97.1 | 45 | 0 | 0 | 45 |
| XiangShan-pr-5080 | resolved | 1121.7 | 3.5 | 0.0140 | 97.3 | 27 | 0 | 0 | 27 |
| XiangShan-pr-5182 | unresolved | 452.2 | 4.0 | 0.0129 | 90.8 | 15 | 0 | 1 | 14 |
| XiangShan-pr-5189 | unresolved | 1059.8 | 4.5 | 0.0204 | 95.5 | 32 | 0 | 1 | 31 |
| XiangShan-pr-5496 | unresolved | 1041.1 | 4.2 | 0.0142 | 96.1 | 34 | 0 | 0 | 34 |
| XiangShan-pr-5593 | unresolved | 500.9 | 2.8 | 0.0114 | 92.4 | 13 | 0 | 1 | 12 |
| XiangShan-pr-5687 | unresolved | 571.7 | 2.2 | 0.0145 | 88.5 | 13 | 0 | 0 | 13 |
| XiangShan-pr-5700 | resolved | 1042.8 | 4.3 | 0.0155 | 94.9 | 33 | 0 | 1 | 32 |
| XiangShan-pr-655 | unresolved | 125.1 | 2.5 | 0.0091 | 72.2 | 8 | 0 | 1 | 7 |
| XiangShan-pr-739 | unresolved | 331.3 | 2.9 | 0.0087 | 87.9 | 13 | 0 | 1 | 12 |
