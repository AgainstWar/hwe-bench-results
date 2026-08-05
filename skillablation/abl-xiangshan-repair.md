# XiangShan Ablation - REPAIR

## 总体结果

```yaml
repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 19
  total: 54
  resolved_rate: 35.2%
  file_level_precision: 82.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 19/54 (35.2%) |
| File-Level Precision | 89.7% | 82.7% |

### 新解决
  pr-739, pr-1679, pr-2095, pr-2513, pr-2781, pr-3555, pr-3717, pr-3859, pr-3907, pr-4968, pr-5080, pr-5593

### 丢失
  pr-1931, pr-3867, pr-4337, pr-4943, pr-5700

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 66.7% | 2/3 |
| pr-739 | 50.0% | 1/2 |
| pr-1242 | 50.0% | 1/2 |
| pr-1323 | 100.0% | 1/1 |
| pr-1395 | 50.0% | 1/2 |
| pr-1401 | 25.0% | 1/4 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 1/1 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2195 | 100.0% | 1/1 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 100.0% | 1/1 |
| pr-2483 | 100.0% | 1/1 |
| pr-2513 | 100.0% | 1/1 |
| pr-2781 | 100.0% | 1/1 |
| pr-2845 | 100.0% | 1/1 |
| pr-3182 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3329 | 100.0% | 1/1 |
| pr-3555 | 100.0% | 1/1 |
| pr-3636 | 100.0% | 1/1 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 100.0% | 5/5 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 50.0% | 1/2 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 1/1 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 50.0% | 1/2 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 1/1 |
| pr-5080 | 100.0% | 1/1 |
| pr-5182 | 0.0% | 0/1 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 82.7%
- **Average (per-task)**: 89.5%

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
    "pr": 1820,
    "test": "N/A",
    "type": "sw_hw_config",
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
    "pr": 2997,
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
    "pr": 4337,
    "test": "N/A",
    "type": "logic",
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
    "type": "logic",
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
    "type": "logic",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 8
  logic: 13
  spec: 3
  sw_hw_config: 4
  timing_sync: 5
  unknown: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1311.4
  completion_k: 5.2
  cache_hit_pct: 96.6
  tool_calls: 33.0
  cost_usd: 0.016408
  own_price_cost_usd: 0.359755
  tasks: 54
  resolved: 19
  unresolved: 35
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| XiangShan-pr-1242 | unresolved | 565.3 | 3.3 | 0.0096 | 94.2 | 30 |
| XiangShan-pr-1323 | unresolved | 1090.4 | 5.5 | 0.0138 | 95.8 | 40 |
| XiangShan-pr-1395 | unresolved | 563.5 | 3.8 | 0.0144 | 92.2 | 19 |
| XiangShan-pr-1401 | unresolved | 5375.8 | 12.6 | 0.0378 | 98.8 | 79 |
| XiangShan-pr-1602 | unresolved | 4431.1 | 16.1 | 0.0541 | 97.9 | 53 |
| XiangShan-pr-1679 | resolved | 313.8 | 2.9 | 0.0073 | 92.9 | 19 |
| XiangShan-pr-1694 | unresolved | 1127.7 | 4.2 | 0.0180 | 95.8 | 29 |
| XiangShan-pr-1793 | unresolved | 477.0 | 3.8 | 0.0092 | 93.5 | 28 |
| XiangShan-pr-1820 | unresolved | 355.9 | 2.6 | 0.0070 | 91.3 | 14 |
| XiangShan-pr-1907 | unresolved | 1678.5 | 5.4 | 0.0245 | 97.0 | 34 |
| XiangShan-pr-1931 | unresolved | 1082.8 | 3.4 | 0.0202 | 93.2 | 18 |
| XiangShan-pr-2095 | resolved | 303.6 | 2.3 | 0.0084 | 86.2 | 14 |
| XiangShan-pr-2195 | unresolved | 634.2 | 4.1 | 0.0083 | 95.4 | 26 |
| XiangShan-pr-2246 | unresolved | 1961.5 | 5.5 | 0.0174 | 97.0 | 49 |
| XiangShan-pr-2351 | unresolved | 1267.7 | 4.8 | 0.0225 | 95.7 | 31 |
| XiangShan-pr-2483 | resolved | 258.4 | 2.6 | 0.0052 | 91.7 | 13 |
| XiangShan-pr-2513 | resolved | 777.4 | 3.4 | 0.0105 | 95.4 | 28 |
| XiangShan-pr-2781 | resolved | 1528.3 | 5.4 | 0.0185 | 97.1 | 38 |
| XiangShan-pr-281 | resolved | 567.6 | 3.1 | 0.0090 | 95.2 | 20 |
| XiangShan-pr-2845 | resolved | 484.4 | 3.6 | 0.0076 | 94.7 | 28 |
| XiangShan-pr-2997 | unresolved | 134.2 | 1.1 | 0.0049 | 83.5 | 11 |
| XiangShan-pr-3182 | resolved | 1404.0 | 7.4 | 0.0156 | 97.1 | 49 |
| XiangShan-pr-3307 | unresolved | 1083.1 | 5.1 | 0.0143 | 97.1 | 34 |
| XiangShan-pr-3329 | unresolved | 757.8 | 4.0 | 0.0140 | 93.9 | 23 |
| XiangShan-pr-3555 | resolved | 2338.3 | 9.0 | 0.0185 | 98.1 | 59 |
| XiangShan-pr-3636 | unresolved | 1424.2 | 4.8 | 0.0176 | 97.3 | 38 |
| XiangShan-pr-3717 | resolved | 161.1 | 2.1 | 0.0051 | 87.5 | 9 |
| XiangShan-pr-3753 | unresolved | 882.3 | 4.7 | 0.0186 | 95.1 | 20 |
| XiangShan-pr-3859 | resolved | 6171.6 | 11.2 | 0.0440 | 98.3 | 88 |
| XiangShan-pr-3867 | unresolved | 2182.9 | 5.8 | 0.0298 | 97.0 | 47 |
| XiangShan-pr-39 | resolved | 372.1 | 2.8 | 0.0104 | 91.0 | 12 |
| XiangShan-pr-3907 | resolved | 505.4 | 2.9 | 0.0079 | 94.2 | 28 |
| XiangShan-pr-3955 | unresolved | 727.4 | 4.8 | 0.0118 | 95.6 | 26 |
| XiangShan-pr-4110 | unresolved | 921.0 | 4.7 | 0.0116 | 96.6 | 41 |
| XiangShan-pr-4166 | unresolved | 1108.4 | 4.8 | 0.0184 | 93.8 | 23 |
| XiangShan-pr-4179 | unresolved | 1371.4 | 4.9 | 0.0175 | 96.2 | 43 |
| XiangShan-pr-4337 | unresolved | 774.1 | 4.7 | 0.0102 | 96.1 | 27 |
| XiangShan-pr-4426 | unresolved | 991.3 | 4.7 | 0.0172 | 95.9 | 31 |
| XiangShan-pr-4442 | unresolved | 1446.6 | 6.4 | 0.0206 | 96.8 | 39 |
| XiangShan-pr-4533 | unresolved | 1165.6 | 5.6 | 0.0149 | 96.6 | 33 |
| XiangShan-pr-4750 | unresolved | 458.7 | 3.7 | 0.0089 | 93.4 | 23 |
| XiangShan-pr-4764 | resolved | 800.8 | 4.8 | 0.0099 | 95.0 | 34 |
| XiangShan-pr-4943 | unresolved | 4161.3 | 12.1 | 0.0313 | 98.4 | 85 |
| XiangShan-pr-4959 | resolved | 931.2 | 5.2 | 0.0138 | 95.0 | 26 |
| XiangShan-pr-4968 | resolved | 999.3 | 4.7 | 0.0145 | 95.7 | 30 |
| XiangShan-pr-5080 | resolved | 1333.7 | 5.1 | 0.0219 | 96.3 | 30 |
| XiangShan-pr-5182 | unresolved | 1424.8 | 4.6 | 0.0224 | 95.9 | 26 |
| XiangShan-pr-5189 | unresolved | 686.1 | 4.2 | 0.0109 | 95.2 | 22 |
| XiangShan-pr-5496 | unresolved | 72.2 | 1.3 | 0.0033 | 74.4 | 7 |
| XiangShan-pr-5593 | resolved | 857.8 | 4.0 | 0.0170 | 96.0 | 25 |
| XiangShan-pr-5687 | unresolved | 1436.3 | 5.4 | 0.0186 | 96.8 | 33 |
| XiangShan-pr-5700 | unresolved | 1118.6 | 5.1 | 0.0147 | 96.3 | 35 |
| XiangShan-pr-655 | unresolved | 3356.3 | 9.5 | 0.0309 | 97.7 | 55 |
| XiangShan-pr-739 | resolved | 2413.1 | 8.3 | 0.0217 | 97.8 | 61 |
