# Ibex Ablation - REPAIR

## 总体结果

```yaml
repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 25
  total: 35
  resolved_rate: 71.4%
  file_level_precision: 93.6%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 25/35 (71.4%) |
| File-Level Precision | 79.2% | 93.6% |

### 新解决
  pr-475, pr-1141

### 丢失
  pr-54, pr-332, pr-882, pr-1135

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
| pr-104 | 100.0% | 5/5 |
| pr-122 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 1/1 |
| pr-475 | 100.0% | 1/1 |
| pr-907 | 100.0% | 1/1 |
| pr-974 | 100.0% | 1/1 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 100.0% | 1/1 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 83.3% | 5/6 |
| pr-1513 | 50.0% | 1/2 |
| pr-1584 | 100.0% | 2/2 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 2/2 |
| pr-2232 | 100.0% | 2/2 |

## File-Level Precision

- **Overall**: 93.6%
- **Average (per-task)**: 96.5%

## 未解决 Case

```json
[
  {
    "pr": 54,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 104,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 155,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 332,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 882,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 907,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 974,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1135,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 1229,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1513,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 2
  logic: 2
  spec: 2
  timing_sync: 1
  unknown: 2
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1812.6
  completion_k: 5.8
  cache_hit_pct: 97.6
  tool_calls: 39.9
  cost_usd: 0.018359
  own_price_cost_usd: 0.495813
  tasks: 35
  resolved: 25
  unresolved: 10
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| ibex-pr-104 | unresolved | 4311.8 | 12.0 | 0.0309 | 98.3 | 70 |
| ibex-pr-1135 | unresolved | 1035.2 | 4.2 | 0.0142 | 96.5 | 27 |
| ibex-pr-1141 | resolved | 4313.7 | 9.6 | 0.0334 | 98.7 | 94 |
| ibex-pr-122 | resolved | 1155.8 | 3.2 | 0.0179 | 95.7 | 27 |
| ibex-pr-1229 | unresolved | 931.6 | 5.5 | 0.0119 | 95.4 | 41 |
| ibex-pr-1383 | resolved | 872.5 | 3.0 | 0.0116 | 95.1 | 26 |
| ibex-pr-1469 | resolved | 7219.4 | 14.5 | 0.0495 | 98.8 | 102 |
| ibex-pr-1513 | unresolved | 4378.9 | 8.4 | 0.0337 | 97.9 | 58 |
| ibex-pr-155 | unresolved | 70.0 | 0.9 | 0.0125 | 72.7 | 6 |
| ibex-pr-157 | resolved | 343.4 | 2.9 | 0.0099 | 91.5 | 13 |
| ibex-pr-1584 | resolved | 8147.3 | 19.3 | 0.0517 | 98.8 | 113 |
| ibex-pr-166 | resolved | 363.5 | 2.9 | 0.0064 | 93.1 | 19 |
| ibex-pr-167 | resolved | 2017.4 | 6.4 | 0.0225 | 97.4 | 45 |
| ibex-pr-1735 | resolved | 3955.6 | 9.5 | 0.0314 | 98.2 | 75 |
| ibex-pr-176 | resolved | 545.4 | 3.9 | 0.0074 | 95.2 | 30 |
| ibex-pr-1780 | resolved | 972.0 | 4.5 | 0.0110 | 96.7 | 31 |
| ibex-pr-1816 | resolved | 1770.4 | 6.9 | 0.0175 | 97.2 | 47 |
| ibex-pr-1865 | resolved | 1538.5 | 6.5 | 0.0176 | 96.7 | 55 |
| ibex-pr-222 | resolved | 576.7 | 4.2 | 0.0078 | 95.4 | 31 |
| ibex-pr-2232 | resolved | 1484.8 | 5.6 | 0.0184 | 95.2 | 33 |
| ibex-pr-244 | resolved | 1394.7 | 6.9 | 0.0181 | 97.1 | 32 |
| ibex-pr-276 | resolved | 3731.7 | 8.3 | 0.0367 | 98.6 | 50 |
| ibex-pr-282 | resolved | 587.0 | 3.4 | 0.0118 | 94.1 | 17 |
| ibex-pr-293 | resolved | 1291.6 | 5.3 | 0.0203 | 96.6 | 29 |
| ibex-pr-332 | unresolved | 1201.4 | 5.0 | 0.0187 | 97.8 | 31 |
| ibex-pr-377 | resolved | 844.7 | 5.7 | 0.0126 | 95.8 | 40 |
| ibex-pr-45 | resolved | 512.8 | 3.2 | 0.0067 | 95.3 | 29 |
| ibex-pr-465 | resolved | 616.2 | 4.6 | 0.0083 | 95.5 | 32 |
| ibex-pr-475 | resolved | 1192.7 | 4.7 | 0.0136 | 96.9 | 33 |
| ibex-pr-48 | resolved | 494.1 | 3.3 | 0.0065 | 95.7 | 23 |
| ibex-pr-54 | unresolved | 560.8 | 2.8 | 0.0124 | 94.6 | 18 |
| ibex-pr-83 | resolved | 938.3 | 4.6 | 0.0144 | 95.4 | 28 |
| ibex-pr-882 | unresolved | 25.0 | 0.6 | 0.0033 | 32.7 | 5 |
| ibex-pr-907 | unresolved | 2382.7 | 5.1 | 0.0241 | 98.1 | 42 |
| ibex-pr-974 | unresolved | 1662.3 | 6.5 | 0.0178 | 97.5 | 45 |
