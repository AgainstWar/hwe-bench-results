# XiangShan SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 16
  total: 54
  resolved_rate: 29.6%
  file_level_precision: 71.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 16/54 (29.6%) |
| File-Level Precision | 89.7% | 71.7% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-1242 | 0.0% | 0/1 |
| pr-1323 | 50.0% | 1/2 |
| pr-1401 | 33.3% | 1/3 |
| pr-1602 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 0.0% | 0/1 |
| pr-2095 | 0.0% | 0/1 |
| pr-2195 | 50.0% | 1/2 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 0.0% | 0/1 |
| pr-2483 | 100.0% | 1/1 |
| pr-2513 | 100.0% | 1/1 |
| pr-2781 | 100.0% | 1/1 |
| pr-2845 | 0.0% | 0/1 |
| pr-2997 | 100.0% | 1/1 |
| pr-3182 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3329 | 0.0% | 0/1 |
| pr-3555 | 100.0% | 1/1 |
| pr-3636 | 66.7% | 2/3 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 100.0% | 5/5 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 100.0% | 1/1 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4426 | 100.0% | 1/1 |
| pr-4533 | 0.0% | 0/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 2/2 |
| pr-5182 | 50.0% | 1/2 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 0.0% | 0/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 71.7%
- **Average (per-task)**: 73.9%

## 未解决 Case

```json
[
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
    "type": "spec",
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
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1679,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1694,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1793,
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
    "pr": 1931,
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
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2351,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 2513,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2781,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 2845,
    "test": "N/A",
    "type": "timing_sync",
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
    "type": "interface",
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
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 4442,
    "test": "N/A",
    "type": "interface",
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
    "pr": 5080,
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
    "pr": 5687,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 5700,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 8
  logic: 10
  spec: 4
  sw_hw_config: 3
  timing_sync: 5
  unknown: 7
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 992.9
  completion_k: 4.3
  cache_hit_pct: 95.4
  tool_calls: 25.9
  mcp_calls: 0.0
  skill_calls: 0.9
  ordinary_calls: 24.9
  cost_usd: 0.015380
  own_price_cost_usd: 0.272847
  tasks: 54
  resolved: 16
  unresolved: 38
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| XiangShan-pr-1242 | unresolved | 1190.5 | 5.1 | 0.0199 | 95.6 | 33 | 0 | 1 | 32 |
| XiangShan-pr-1323 | unresolved | 1422.2 | 6.3 | 0.0158 | 96.7 | 55 | 0 | 2 | 53 |
| XiangShan-pr-1395 | unresolved | 225.0 | 2.7 | 0.0085 | 87.8 | 13 | 0 | 1 | 12 |
| XiangShan-pr-1401 | unresolved | 4866.3 | 10.7 | 0.0398 | 98.6 | 77 | 0 | 1 | 76 |
| XiangShan-pr-1602 | unresolved | 2605.7 | 6.6 | 0.0350 | 96.7 | 40 | 0 | 1 | 39 |
| XiangShan-pr-1679 | unresolved | 1088.8 | 4.5 | 0.0205 | 96.0 | 26 | 0 | 1 | 25 |
| XiangShan-pr-1694 | unresolved | 885.2 | 4.2 | 0.0171 | 93.8 | 17 | 0 | 1 | 16 |
| XiangShan-pr-1793 | unresolved | 197.6 | 3.0 | 0.0051 | 88.2 | 14 | 0 | 1 | 13 |
| XiangShan-pr-1820 | resolved | 1018.7 | 6.1 | 0.0145 | 94.9 | 28 | 0 | 2 | 26 |
| XiangShan-pr-1907 | unresolved | 370.3 | 2.6 | 0.0083 | 92.9 | 16 | 0 | 0 | 16 |
| XiangShan-pr-1931 | unresolved | 591.4 | 3.1 | 0.0144 | 91.0 | 17 | 0 | 1 | 16 |
| XiangShan-pr-2095 | unresolved | 143.6 | 2.4 | 0.0058 | 84.8 | 7 | 0 | 1 | 6 |
| XiangShan-pr-2195 | unresolved | 950.6 | 3.9 | 0.0112 | 95.4 | 27 | 0 | 1 | 26 |
| XiangShan-pr-2246 | unresolved | 889.8 | 3.3 | 0.0096 | 95.7 | 29 | 0 | 2 | 27 |
| XiangShan-pr-2351 | unresolved | 942.0 | 4.0 | 0.0259 | 92.1 | 17 | 0 | 1 | 16 |
| XiangShan-pr-2483 | resolved | 286.4 | 2.7 | 0.0054 | 92.6 | 12 | 0 | 0 | 12 |
| XiangShan-pr-2513 | unresolved | 1035.4 | 5.1 | 0.0122 | 95.7 | 25 | 0 | 2 | 23 |
| XiangShan-pr-2781 | unresolved | 337.6 | 1.9 | 0.0093 | 88.3 | 13 | 0 | 1 | 12 |
| XiangShan-pr-281 | resolved | 98.2 | 1.0 | 0.0033 | 86.1 | 7 | 0 | 0 | 7 |
| XiangShan-pr-2845 | unresolved | 191.6 | 2.7 | 0.0055 | 87.2 | 9 | 0 | 1 | 8 |
| XiangShan-pr-2997 | resolved | 1166.0 | 4.2 | 0.0192 | 95.8 | 31 | 0 | 0 | 31 |
| XiangShan-pr-3182 | resolved | 1091.7 | 6.2 | 0.0209 | 91.0 | 33 | 0 | 2 | 31 |
| XiangShan-pr-3307 | unresolved | 516.0 | 2.9 | 0.0101 | 95.6 | 24 | 0 | 0 | 24 |
| XiangShan-pr-3329 | unresolved | 1163.6 | 4.7 | 0.0154 | 96.4 | 31 | 0 | 1 | 30 |
| XiangShan-pr-3555 | resolved | 1055.1 | 3.5 | 0.0164 | 94.7 | 27 | 0 | 1 | 26 |
| XiangShan-pr-3636 | unresolved | 2186.1 | 5.7 | 0.0250 | 97.4 | 42 | 0 | 1 | 41 |
| XiangShan-pr-3717 | resolved | 223.5 | 2.1 | 0.0066 | 87.7 | 9 | 0 | 1 | 8 |
| XiangShan-pr-3753 | unresolved | 620.3 | 4.7 | 0.0159 | 90.8 | 14 | 0 | 1 | 13 |
| XiangShan-pr-3859 | resolved | 3060.3 | 7.5 | 0.0285 | 97.2 | 50 | 0 | 0 | 50 |
| XiangShan-pr-3867 | unresolved | 1953.9 | 6.5 | 0.0213 | 97.2 | 38 | 0 | 1 | 37 |
| XiangShan-pr-39 | resolved | 380.9 | 2.0 | 0.0115 | 90.2 | 12 | 0 | 0 | 12 |
| XiangShan-pr-3907 | unresolved | 442.5 | 2.9 | 0.0070 | 92.7 | 20 | 0 | 2 | 18 |
| XiangShan-pr-3955 | resolved | 877.9 | 5.9 | 0.0129 | 95.3 | 30 | 0 | 1 | 29 |
| XiangShan-pr-4110 | unresolved | 913.1 | 4.1 | 0.0135 | 96.2 | 38 | 0 | 0 | 38 |
| XiangShan-pr-4166 | unresolved | 2652.6 | 8.0 | 0.0272 | 97.7 | 57 | 0 | 0 | 57 |
| XiangShan-pr-4179 | unresolved | 1107.9 | 4.3 | 0.0118 | 96.5 | 31 | 0 | 0 | 31 |
| XiangShan-pr-4337 | unresolved | 274.4 | 3.1 | 0.0088 | 87.9 | 13 | 0 | 1 | 12 |
| XiangShan-pr-4426 | resolved | 457.2 | 3.7 | 0.0123 | 91.4 | 16 | 0 | 2 | 14 |
| XiangShan-pr-4442 | unresolved | 323.6 | 3.0 | 0.0107 | 84.5 | 13 | 0 | 1 | 12 |
| XiangShan-pr-4533 | unresolved | 448.9 | 3.3 | 0.0132 | 92.4 | 14 | 0 | 1 | 13 |
| XiangShan-pr-4750 | unresolved | 2240.2 | 4.9 | 0.0298 | 96.5 | 34 | 0 | 1 | 33 |
| XiangShan-pr-4764 | resolved | 716.3 | 4.5 | 0.0106 | 93.7 | 28 | 0 | 1 | 27 |
| XiangShan-pr-4943 | unresolved | 843.8 | 5.6 | 0.0127 | 94.0 | 38 | 0 | 1 | 37 |
| XiangShan-pr-4959 | resolved | 1099.9 | 6.4 | 0.0164 | 95.3 | 36 | 0 | 2 | 34 |
| XiangShan-pr-4968 | resolved | 2340.0 | 7.2 | 0.0277 | 96.5 | 39 | 0 | 1 | 38 |
| XiangShan-pr-5080 | unresolved | 150.4 | 0.7 | 0.0197 | 81.5 | 7 | 0 | 1 | 6 |
| XiangShan-pr-5182 | resolved | 906.6 | 5.1 | 0.0140 | 94.2 | 31 | 0 | 1 | 30 |
| XiangShan-pr-5189 | unresolved | 1244.4 | 6.0 | 0.0228 | 95.6 | 41 | 0 | 1 | 40 |
| XiangShan-pr-5496 | unresolved | 236.6 | 2.5 | 0.0049 | 91.5 | 15 | 0 | 0 | 15 |
| XiangShan-pr-5593 | resolved | 361.3 | 2.7 | 0.0086 | 91.0 | 14 | 0 | 0 | 14 |
| XiangShan-pr-5687 | unresolved | 681.9 | 4.8 | 0.0161 | 92.7 | 25 | 0 | 1 | 24 |
| XiangShan-pr-5700 | unresolved | 1645.5 | 5.4 | 0.0224 | 96.4 | 32 | 0 | 1 | 31 |
| XiangShan-pr-655 | unresolved | 592.5 | 4.1 | 0.0187 | 93.5 | 16 | 0 | 1 | 15 |
| XiangShan-pr-739 | unresolved | 305.0 | 3.7 | 0.0109 | 85.9 | 16 | 0 | 1 | 15 |
