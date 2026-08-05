# XiangShan MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 25
  total: 54
  resolved_rate: 46.3%
  file_level_precision: 80.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 25/54 (46.3%) |
| File-Level Precision | 89.7% | 80.7% |

### 新解决
  pr-739, pr-1679, pr-1820, pr-2095, pr-2351, pr-2997, pr-3329, pr-3555, pr-3717, pr-3859, pr-3955, pr-4166, pr-4426, pr-4533, pr-5182, pr-5593

### 丢失
  pr-4943, pr-4959, pr-5700

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 1/1 |
| pr-739 | 100.0% | 1/1 |
| pr-1242 | 25.0% | 1/4 |
| pr-1323 | 50.0% | 1/2 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 0.0% | 0/1 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 33.3% | 1/3 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 4/4 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 50.0% | 1/2 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 100.0% | 1/1 |
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
| pr-3859 | 71.4% | 5/7 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 100.0% | 1/1 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 50.0% | 1/2 |
| pr-4764 | 25.0% | 1/4 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 90.0% | 9/10 |
| pr-5182 | 50.0% | 1/2 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 50.0% | 1/2 |

## File-Level Precision

- **Overall**: 80.7%
- **Average (per-task)**: 87.9%

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
    "pr": 2195,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2246,
    "test": "N/A",
    "type": "config_integ",
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
    "pr": 3307,
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
    "type": "unknown",
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
    "pr": 4179,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 4442,
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
    "type": "logic",
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
  interface: 3
  logic: 10
  spec: 3
  sw_hw_config: 3
  timing_sync: 5
  unknown: 4
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1028.3
  completion_k: 4.1
  cache_hit_pct: 95.7
  tool_calls: 25.9
  cost_usd: 0.014935
  own_price_cost_usd: 0.282107
  tasks: 54
  resolved: 25
  unresolved: 29
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| XiangShan-pr-1242 | unresolved | 3202.3 | 8.1 | 0.0378 | 98.1 | 63 |
| XiangShan-pr-1323 | unresolved | 1383.3 | 5.5 | 0.0142 | 96.9 | 52 |
| XiangShan-pr-1395 | unresolved | 169.7 | 1.4 | 0.0058 | 85.2 | 6 |
| XiangShan-pr-1401 | unresolved | 1631.5 | 4.1 | 0.0274 | 94.0 | 25 |
| XiangShan-pr-1602 | unresolved | 892.0 | 4.5 | 0.0152 | 94.9 | 23 |
| XiangShan-pr-1679 | resolved | 2053.1 | 7.3 | 0.0237 | 97.1 | 37 |
| XiangShan-pr-1694 | unresolved | 747.1 | 3.8 | 0.0187 | 92.9 | 19 |
| XiangShan-pr-1793 | unresolved | 1167.3 | 6.1 | 0.0146 | 96.2 | 42 |
| XiangShan-pr-1820 | resolved | 230.0 | 1.6 | 0.0078 | 87.3 | 8 |
| XiangShan-pr-1907 | unresolved | 1480.7 | 5.6 | 0.0219 | 96.4 | 31 |
| XiangShan-pr-1931 | resolved | 1308.2 | 4.6 | 0.0196 | 95.6 | 24 |
| XiangShan-pr-2095 | resolved | 211.6 | 1.3 | 0.0066 | 87.0 | 8 |
| XiangShan-pr-2195 | unresolved | 154.8 | 2.4 | 0.0057 | 82.4 | 7 |
| XiangShan-pr-2246 | unresolved | 116.1 | 1.2 | 0.0039 | 81.4 | 6 |
| XiangShan-pr-2351 | resolved | 1808.8 | 4.6 | 0.0248 | 95.4 | 28 |
| XiangShan-pr-2483 | resolved | 94.1 | 1.6 | 0.0046 | 80.3 | 4 |
| XiangShan-pr-2513 | unresolved | 701.4 | 7.6 | 0.0116 | 94.1 | 25 |
| XiangShan-pr-2781 | unresolved | 83.0 | 1.0 | 0.0027 | 83.0 | 5 |
| XiangShan-pr-281 | resolved | 91.3 | 0.9 | 0.0037 | 84.9 | 7 |
| XiangShan-pr-2845 | resolved | 170.6 | 1.6 | 0.0052 | 85.7 | 11 |
| XiangShan-pr-2997 | resolved | 1098.4 | 4.3 | 0.0170 | 96.7 | 36 |
| XiangShan-pr-3182 | resolved | 1406.1 | 6.1 | 0.0169 | 95.4 | 32 |
| XiangShan-pr-3307 | unresolved | 547.1 | 2.9 | 0.0096 | 94.2 | 22 |
| XiangShan-pr-3329 | resolved | 1658.3 | 4.7 | 0.0254 | 95.8 | 26 |
| XiangShan-pr-3555 | resolved | 160.6 | 1.7 | 0.0046 | 85.7 | 8 |
| XiangShan-pr-3636 | unresolved | 1124.0 | 3.8 | 0.0161 | 96.0 | 31 |
| XiangShan-pr-3717 | resolved | 257.8 | 1.7 | 0.0072 | 90.2 | 11 |
| XiangShan-pr-3753 | unresolved | 227.3 | 2.3 | 0.0126 | 85.8 | 7 |
| XiangShan-pr-3859 | resolved | 3619.6 | 11.4 | 0.0306 | 98.1 | 73 |
| XiangShan-pr-3867 | resolved | 1485.4 | 4.4 | 0.0184 | 96.7 | 35 |
| XiangShan-pr-39 | resolved | 427.6 | 2.7 | 0.0113 | 92.3 | 13 |
| XiangShan-pr-3907 | unresolved | 205.5 | 1.5 | 0.0040 | 90.6 | 11 |
| XiangShan-pr-3955 | resolved | 1555.7 | 5.8 | 0.0173 | 97.1 | 38 |
| XiangShan-pr-4110 | unresolved | 1128.0 | 4.2 | 0.0147 | 97.0 | 38 |
| XiangShan-pr-4166 | resolved | 1644.7 | 5.3 | 0.0187 | 95.6 | 36 |
| XiangShan-pr-4179 | unresolved | 585.4 | 3.6 | 0.0101 | 93.7 | 25 |
| XiangShan-pr-4337 | resolved | 135.0 | 1.4 | 0.0070 | 87.7 | 7 |
| XiangShan-pr-4426 | resolved | 825.0 | 2.6 | 0.0150 | 92.5 | 17 |
| XiangShan-pr-4442 | unresolved | 775.7 | 3.5 | 0.0112 | 95.4 | 23 |
| XiangShan-pr-4533 | resolved | 779.5 | 2.9 | 0.0122 | 95.8 | 21 |
| XiangShan-pr-4750 | unresolved | 510.6 | 2.8 | 0.0134 | 88.9 | 12 |
| XiangShan-pr-4764 | resolved | 799.5 | 4.6 | 0.0105 | 95.0 | 31 |
| XiangShan-pr-4943 | unresolved | 2679.3 | 10.1 | 0.0235 | 97.5 | 69 |
| XiangShan-pr-4959 | unresolved | 650.7 | 2.9 | 0.0116 | 95.3 | 22 |
| XiangShan-pr-4968 | unresolved | 1675.3 | 5.9 | 0.0177 | 96.3 | 40 |
| XiangShan-pr-5080 | unresolved | 386.0 | 1.5 | 0.0237 | 92.8 | 16 |
| XiangShan-pr-5182 | resolved | 1073.7 | 4.2 | 0.0180 | 92.0 | 21 |
| XiangShan-pr-5189 | unresolved | 2582.3 | 7.1 | 0.0263 | 97.3 | 60 |
| XiangShan-pr-5496 | unresolved | 1721.7 | 6.5 | 0.0151 | 97.2 | 52 |
| XiangShan-pr-5593 | resolved | 823.8 | 4.5 | 0.0121 | 95.0 | 19 |
| XiangShan-pr-5687 | unresolved | 1713.0 | 5.3 | 0.0223 | 95.4 | 32 |
| XiangShan-pr-5700 | unresolved | 2147.3 | 5.8 | 0.0252 | 97.5 | 45 |
| XiangShan-pr-655 | unresolved | 603.7 | 2.2 | 0.0170 | 94.4 | 14 |
| XiangShan-pr-739 | resolved | 815.3 | 4.8 | 0.0149 | 94.7 | 27 |
