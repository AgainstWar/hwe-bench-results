# XiangShan MCP+REPAIR Analysis

## 总体结果

```yaml
mcp+repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 23
  total: 54
  resolved_rate: 42.6%
  file_level_precision: 80.2%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 23/54 (42.6%) |
| File-Level Precision | 89.7% | 80.2% |

### 新解决
  pr-739, pr-1323, pr-1679, pr-1820, pr-2095, pr-2513, pr-2997, pr-3329, pr-3555, pr-3717, pr-3859, pr-3955, pr-4968, pr-5080, pr-5593

### 丢失
  pr-1931, pr-2483, pr-4943, pr-5700

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
| pr-1401 | 100.0% | 1/1 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 20.0% | 1/5 |
| pr-1793 | 100.0% | 4/4 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2195 | 50.0% | 1/2 |
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
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 83.3% | 5/6 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 50.0% | 1/2 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 33.3% | 1/3 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 1/1 |
| pr-5080 | 100.0% | 1/1 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 80.2%
- **Average (per-task)**: 90.6%

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
    "pr": 1931,
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
    "pr": 2483,
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
    "type": "spec",
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
    "pr": 5182,
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
    "pr": 5687,
    "test": "N/A",
    "type": "logic",
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
  config_integ: 1
  interface: 7
  logic: 10
  spec: 3
  sw_hw_config: 3
  timing_sync: 5
  unknown: 2
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 999.0
  completion_k: 4.0
  cache_hit_pct: 95.6
  tool_calls: 27.4
  cost_usd: 0.014582
  own_price_cost_usd: 0.274161
  tasks: 54
  resolved: 23
  unresolved: 31
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| XiangShan-pr-1242 | unresolved | 1216.9 | 5.0 | 0.0174 | 94.7 | 28 |
| XiangShan-pr-1323 | resolved | 1801.3 | 5.7 | 0.0183 | 97.1 | 51 |
| XiangShan-pr-1395 | unresolved | 305.2 | 2.9 | 0.0080 | 90.7 | 15 |
| XiangShan-pr-1401 | unresolved | 1911.8 | 4.6 | 0.0267 | 96.4 | 38 |
| XiangShan-pr-1602 | unresolved | 1033.3 | 4.6 | 0.0203 | 94.9 | 19 |
| XiangShan-pr-1679 | resolved | 898.7 | 3.6 | 0.0162 | 95.9 | 25 |
| XiangShan-pr-1694 | unresolved | 1889.9 | 4.3 | 0.0189 | 97.1 | 33 |
| XiangShan-pr-1793 | unresolved | 1154.7 | 6.4 | 0.0134 | 96.5 | 43 |
| XiangShan-pr-1820 | resolved | 408.4 | 2.6 | 0.0080 | 92.0 | 14 |
| XiangShan-pr-1907 | unresolved | 980.6 | 3.1 | 0.0203 | 96.1 | 20 |
| XiangShan-pr-1931 | unresolved | 1882.6 | 5.8 | 0.0299 | 97.8 | 32 |
| XiangShan-pr-2095 | resolved | 238.3 | 2.2 | 0.0055 | 89.2 | 14 |
| XiangShan-pr-2195 | unresolved | 831.9 | 4.1 | 0.0122 | 94.7 | 29 |
| XiangShan-pr-2246 | unresolved | 482.7 | 2.6 | 0.0087 | 92.4 | 24 |
| XiangShan-pr-2351 | unresolved | 1170.0 | 3.9 | 0.0196 | 95.6 | 29 |
| XiangShan-pr-2483 | unresolved | 349.5 | 3.1 | 0.0065 | 92.7 | 15 |
| XiangShan-pr-2513 | resolved | 513.9 | 2.4 | 0.0100 | 93.4 | 15 |
| XiangShan-pr-2781 | unresolved | 747.9 | 4.5 | 0.0106 | 94.5 | 32 |
| XiangShan-pr-281 | resolved | 402.9 | 2.7 | 0.0084 | 92.2 | 18 |
| XiangShan-pr-2845 | resolved | 402.7 | 2.9 | 0.0070 | 92.8 | 21 |
| XiangShan-pr-2997 | resolved | 1033.7 | 4.2 | 0.0164 | 95.3 | 29 |
| XiangShan-pr-3182 | resolved | 1253.7 | 5.9 | 0.0157 | 96.2 | 39 |
| XiangShan-pr-3307 | unresolved | 682.4 | 3.3 | 0.0138 | 94.0 | 23 |
| XiangShan-pr-3329 | resolved | 1085.6 | 4.3 | 0.0147 | 95.9 | 34 |
| XiangShan-pr-3555 | resolved | 478.2 | 3.3 | 0.0068 | 94.2 | 22 |
| XiangShan-pr-3636 | unresolved | 1585.6 | 5.5 | 0.0219 | 96.6 | 40 |
| XiangShan-pr-3717 | resolved | 171.4 | 1.6 | 0.0056 | 85.1 | 8 |
| XiangShan-pr-3753 | unresolved | 730.1 | 4.2 | 0.0179 | 93.9 | 17 |
| XiangShan-pr-3859 | resolved | 4826.7 | 11.2 | 0.0377 | 98.1 | 88 |
| XiangShan-pr-3867 | resolved | 1057.9 | 4.3 | 0.0193 | 95.5 | 27 |
| XiangShan-pr-39 | resolved | 290.9 | 2.2 | 0.0081 | 88.7 | 11 |
| XiangShan-pr-3907 | unresolved | 166.6 | 1.2 | 0.0038 | 89.0 | 9 |
| XiangShan-pr-3955 | resolved | 589.8 | 3.8 | 0.0100 | 94.1 | 20 |
| XiangShan-pr-4110 | unresolved | 859.9 | 4.2 | 0.0148 | 96.1 | 32 |
| XiangShan-pr-4166 | unresolved | 1938.2 | 6.7 | 0.0222 | 96.5 | 41 |
| XiangShan-pr-4179 | unresolved | 1215.5 | 5.4 | 0.0149 | 96.4 | 40 |
| XiangShan-pr-4337 | resolved | 1437.4 | 4.9 | 0.0208 | 95.8 | 38 |
| XiangShan-pr-4426 | unresolved | 1412.5 | 5.0 | 0.0228 | 94.8 | 35 |
| XiangShan-pr-4442 | unresolved | 1293.3 | 5.0 | 0.0178 | 96.0 | 32 |
| XiangShan-pr-4533 | unresolved | 601.7 | 2.5 | 0.0136 | 90.3 | 15 |
| XiangShan-pr-4750 | unresolved | 1354.4 | 4.7 | 0.0187 | 96.7 | 32 |
| XiangShan-pr-4764 | resolved | 1011.5 | 5.2 | 0.0124 | 95.6 | 35 |
| XiangShan-pr-4943 | unresolved | 1449.9 | 6.5 | 0.0164 | 96.2 | 38 |
| XiangShan-pr-4959 | resolved | 825.2 | 3.8 | 0.0116 | 96.0 | 31 |
| XiangShan-pr-4968 | resolved | 1478.2 | 4.5 | 0.0200 | 95.4 | 27 |
| XiangShan-pr-5080 | resolved | 288.6 | 2.2 | 0.0053 | 91.7 | 15 |
| XiangShan-pr-5182 | unresolved | 264.4 | 1.5 | 0.0097 | 85.8 | 15 |
| XiangShan-pr-5189 | unresolved | 2084.4 | 5.2 | 0.0264 | 95.9 | 52 |
| XiangShan-pr-5496 | unresolved | 186.1 | 2.0 | 0.0041 | 90.0 | 12 |
| XiangShan-pr-5593 | resolved | 741.2 | 3.9 | 0.0143 | 94.5 | 16 |
| XiangShan-pr-5687 | unresolved | 1245.8 | 4.2 | 0.0163 | 96.3 | 33 |
| XiangShan-pr-5700 | unresolved | 29.5 | 0.7 | 0.0033 | 36.9 | 5 |
| XiangShan-pr-655 | unresolved | 1124.1 | 4.7 | 0.0167 | 96.6 | 28 |
| XiangShan-pr-739 | resolved | 527.8 | 2.8 | 0.0076 | 94.5 | 23 |
