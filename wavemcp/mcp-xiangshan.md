# XiangShan MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 18
  total: 54
  resolved_rate: 33.3%
  file_level_precision: 87.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 18/54 (33.3%) |
| File-Level Precision | 89.7% | 87.7% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 1/1 |
| pr-739 | 33.3% | 1/3 |
| pr-1242 | 100.0% | 6/6 |
| pr-1323 | 100.0% | 1/1 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 100.0% | 1/1 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 1/1 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2195 | 50.0% | 1/2 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 100.0% | 2/2 |
| pr-2483 | 100.0% | 1/1 |
| pr-2513 | 100.0% | 1/1 |
| pr-2781 | 100.0% | 1/1 |
| pr-2845 | 100.0% | 1/1 |
| pr-2997 | 100.0% | 1/1 |
| pr-3182 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3329 | 100.0% | 1/1 |
| pr-3555 | 100.0% | 1/1 |
| pr-3636 | 100.0% | 1/1 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 71.4% | 5/7 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 50.0% | 1/2 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 3/3 |
| pr-5182 | 50.0% | 1/2 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 87.7%
- **Average (per-task)**: 93.5%

## 未解决 Case

```json
[
  {
    "pr": 655,
    "test": "N/A",
    "type": "logic",
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
    "type": "logic",
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
    "pr": 1694,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1793,
    "test": "N/A",
    "type": "timing_sync",
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
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2483,
    "test": "N/A",
    "type": "logic",
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
    "pr": 3859,
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
    "pr": 3955,
    "test": "N/A",
    "type": "interface",
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
    "pr": 4426,
    "test": "N/A",
    "type": "interface",
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
    "pr": 4968,
    "test": "N/A",
    "type": "timing_sync",
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
    "type": "logic",
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
  logic: 12
  spec: 5
  sw_hw_config: 3
  timing_sync: 6
  unknown: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1086.4
  completion_k: 4.1
  cache_hit_pct: 96.4
  tool_calls: 28.7
  mcp_calls: 0.4
  other_skill_calls: 0.0
  ordinary_calls: 28.3
  cost_usd: 0.014134
  own_price_cost_usd: 0.297883
  tasks: 54
  resolved: 18
  unresolved: 36
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| XiangShan-pr-1242 | unresolved | 3061.4 | 8.6 | 0.0304 | 98.0 | 55 | 1 | 0 | 54 |
| XiangShan-pr-1323 | unresolved | 1316.7 | 5.2 | 0.0151 | 96.9 | 39 | 0 | 0 | 39 |
| XiangShan-pr-1395 | unresolved | 171.5 | 2.1 | 0.0050 | 89.6 | 12 | 0 | 0 | 12 |
| XiangShan-pr-1401 | unresolved | 1134.5 | 3.2 | 0.0176 | 95.5 | 20 | 0 | 0 | 20 |
| XiangShan-pr-1602 | unresolved | 2580.2 | 6.4 | 0.0328 | 97.4 | 42 | 1 | 0 | 41 |
| XiangShan-pr-1679 | resolved | 1725.3 | 5.8 | 0.0208 | 97.4 | 45 | 0 | 0 | 45 |
| XiangShan-pr-1694 | unresolved | 1813.2 | 5.1 | 0.0278 | 96.6 | 36 | 1 | 0 | 35 |
| XiangShan-pr-1793 | unresolved | 979.2 | 4.2 | 0.0119 | 96.4 | 36 | 1 | 0 | 35 |
| XiangShan-pr-1820 | resolved | 540.8 | 3.1 | 0.0091 | 94.3 | 19 | 0 | 0 | 19 |
| XiangShan-pr-1907 | unresolved | 877.9 | 3.4 | 0.0160 | 94.8 | 22 | 0 | 0 | 22 |
| XiangShan-pr-1931 | resolved | 363.7 | 1.7 | 0.0084 | 90.3 | 12 | 1 | 0 | 11 |
| XiangShan-pr-2095 | unresolved | 268.4 | 1.9 | 0.0068 | 91.7 | 10 | 0 | 0 | 10 |
| XiangShan-pr-2195 | unresolved | 724.1 | 4.1 | 0.0098 | 94.9 | 25 | 0 | 0 | 25 |
| XiangShan-pr-2246 | unresolved | 452.0 | 3.0 | 0.0061 | 94.9 | 23 | 0 | 0 | 23 |
| XiangShan-pr-2351 | resolved | 4960.6 | 9.7 | 0.0364 | 98.4 | 68 | 1 | 0 | 67 |
| XiangShan-pr-2483 | unresolved | 78.2 | 1.2 | 0.0033 | 78.2 | 4 | 0 | 0 | 4 |
| XiangShan-pr-2513 | resolved | 808.5 | 4.8 | 0.0104 | 95.3 | 23 | 0 | 0 | 23 |
| XiangShan-pr-2781 | resolved | 569.3 | 4.1 | 0.0079 | 94.9 | 27 | 0 | 0 | 27 |
| XiangShan-pr-281 | resolved | 88.3 | 1.0 | 0.0056 | 75.9 | 5 | 0 | 0 | 5 |
| XiangShan-pr-2845 | resolved | 619.6 | 3.0 | 0.0087 | 94.8 | 26 | 1 | 0 | 25 |
| XiangShan-pr-2997 | resolved | 2024.6 | 5.4 | 0.0235 | 98.2 | 45 | 0 | 0 | 45 |
| XiangShan-pr-3182 | resolved | 1249.1 | 6.3 | 0.0126 | 97.1 | 44 | 1 | 0 | 43 |
| XiangShan-pr-3307 | unresolved | 900.3 | 3.4 | 0.0169 | 96.3 | 24 | 0 | 0 | 24 |
| XiangShan-pr-3329 | unresolved | 314.8 | 2.2 | 0.0070 | 90.8 | 14 | 1 | 0 | 13 |
| XiangShan-pr-3555 | resolved | 958.5 | 3.3 | 0.0161 | 93.9 | 24 | 0 | 0 | 24 |
| XiangShan-pr-3636 | unresolved | 2365.9 | 6.2 | 0.0253 | 97.6 | 51 | 0 | 0 | 51 |
| XiangShan-pr-3717 | resolved | 561.2 | 2.3 | 0.0128 | 95.1 | 15 | 0 | 0 | 15 |
| XiangShan-pr-3753 | unresolved | 1377.8 | 6.1 | 0.0179 | 96.7 | 28 | 1 | 0 | 27 |
| XiangShan-pr-3859 | unresolved | 6055.7 | 12.1 | 0.0395 | 98.6 | 90 | 1 | 0 | 89 |
| XiangShan-pr-3867 | unresolved | 233.0 | 2.1 | 0.0064 | 90.0 | 13 | 1 | 0 | 12 |
| XiangShan-pr-39 | resolved | 734.3 | 2.8 | 0.0132 | 96.1 | 18 | 1 | 0 | 17 |
| XiangShan-pr-3907 | unresolved | 122.1 | 0.9 | 0.0030 | 87.2 | 7 | 0 | 0 | 7 |
| XiangShan-pr-3955 | unresolved | 1053.8 | 4.7 | 0.0131 | 96.6 | 33 | 0 | 0 | 33 |
| XiangShan-pr-4110 | unresolved | 849.9 | 4.5 | 0.0140 | 95.8 | 39 | 0 | 0 | 39 |
| XiangShan-pr-4166 | unresolved | 2104.9 | 7.5 | 0.0241 | 97.3 | 52 | 0 | 0 | 52 |
| XiangShan-pr-4179 | unresolved | 701.3 | 4.2 | 0.0117 | 93.3 | 22 | 0 | 0 | 22 |
| XiangShan-pr-4337 | resolved | 922.0 | 3.9 | 0.0130 | 96.7 | 26 | 0 | 0 | 26 |
| XiangShan-pr-4426 | unresolved | 1035.7 | 2.9 | 0.0173 | 93.3 | 18 | 1 | 0 | 17 |
| XiangShan-pr-4442 | unresolved | 1231.4 | 4.1 | 0.0162 | 96.0 | 31 | 1 | 0 | 30 |
| XiangShan-pr-4533 | unresolved | 226.4 | 1.3 | 0.0066 | 88.9 | 8 | 0 | 0 | 8 |
| XiangShan-pr-4750 | unresolved | 856.9 | 4.1 | 0.0118 | 95.3 | 31 | 0 | 0 | 31 |
| XiangShan-pr-4764 | resolved | 696.6 | 3.3 | 0.0090 | 94.5 | 32 | 1 | 0 | 31 |
| XiangShan-pr-4943 | unresolved | 1293.8 | 9.1 | 0.0141 | 96.9 | 65 | 0 | 0 | 65 |
| XiangShan-pr-4959 | resolved | 626.0 | 3.4 | 0.0100 | 94.8 | 27 | 0 | 0 | 27 |
| XiangShan-pr-4968 | unresolved | 1063.2 | 4.3 | 0.0136 | 94.8 | 28 | 0 | 0 | 28 |
| XiangShan-pr-5080 | unresolved | 51.9 | 0.4 | 0.0129 | 59.5 | 4 | 1 | 0 | 3 |
| XiangShan-pr-5182 | resolved | 1252.1 | 4.6 | 0.0189 | 95.6 | 29 | 0 | 0 | 29 |
| XiangShan-pr-5189 | unresolved | 744.9 | 3.0 | 0.0089 | 96.3 | 27 | 1 | 0 | 26 |
| XiangShan-pr-5496 | unresolved | 1165.9 | 6.7 | 0.0127 | 96.8 | 48 | 0 | 0 | 48 |
| XiangShan-pr-5593 | unresolved | 376.8 | 3.5 | 0.0073 | 93.9 | 17 | 0 | 0 | 17 |
| XiangShan-pr-5687 | unresolved | 447.9 | 2.7 | 0.0113 | 90.4 | 16 | 1 | 0 | 15 |
| XiangShan-pr-5700 | unresolved | 989.9 | 4.1 | 0.0158 | 95.6 | 33 | 0 | 0 | 33 |
| XiangShan-pr-655 | unresolved | 430.8 | 3.4 | 0.0102 | 93.8 | 17 | 0 | 0 | 17 |
| XiangShan-pr-739 | resolved | 514.4 | 2.7 | 0.0069 | 94.2 | 23 | 1 | 0 | 22 |
