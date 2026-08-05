# CVA6 SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 25
  total: 35
  resolved_rate: 71.4%
  file_level_precision: 74.5%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 25/35 (71.4%) |
| File-Level Precision | 79.0% | 74.5% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 0.0% | 0/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 92.3% | 12/13 |
| pr-2282 | 100.0% | 1/1 |
| pr-2330 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 33.3% | 1/3 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2685 | 100.0% | 1/1 |
| pr-2711 | 0.0% | 0/1 |
| pr-2728 | 100.0% | 1/1 |
| pr-2802 | 33.3% | 1/3 |
| pr-2916 | 0.0% | 0/1 |
| pr-2944 | 100.0% | 1/1 |
| pr-2945 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3042 | 100.0% | 1/1 |
| pr-3059 | 100.0% | 1/1 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3171 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3204 | 100.0% | 1/1 |
| pr-3226 | 100.0% | 2/2 |
| pr-3231 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 74.5%
- **Average (per-task)**: 83.0%

## 未解决 Case

```json
[
  {
    "pr": 2170,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2374,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2420,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2549,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2711,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 2802,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 2844,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2916,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 3042,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 3168,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 3
  interface: 1
  spec: 2
  unknown: 4
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 878.7
  completion_k: 4.0
  cache_hit_pct: 95.6
  tool_calls: 26.1
  cost_usd: 0.011276
  own_price_cost_usd: 0.241648
  tasks: 35
  resolved: 25
  unresolved: 10
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| cva6-pr-1482 | resolved | 175.6 | 1.8 | 0.0044 | 91.3 | 13 |
| cva6-pr-2017 | resolved | 513.6 | 3.6 | 0.0081 | 93.9 | 22 |
| cva6-pr-2032 | resolved | 871.1 | 4.3 | 0.0144 | 95.3 | 32 |
| cva6-pr-2170 | unresolved | 1809.8 | 3.9 | 0.0207 | 96.1 | 35 |
| cva6-pr-2248 | resolved | 47.2 | 0.7 | 0.0022 | 73.2 | 3 |
| cva6-pr-2279 | resolved | 8994.4 | 22.7 | 0.0509 | 99.0 | 142 |
| cva6-pr-2282 | resolved | 1013.4 | 5.7 | 0.0142 | 95.6 | 36 |
| cva6-pr-2330 | resolved | 163.3 | 1.4 | 0.0047 | 87.2 | 8 |
| cva6-pr-2374 | unresolved | 362.4 | 2.2 | 0.0133 | 81.1 | 10 |
| cva6-pr-2375 | resolved | 468.7 | 2.5 | 0.0092 | 92.3 | 18 |
| cva6-pr-2420 | unresolved | 1713.8 | 6.7 | 0.0202 | 96.4 | 41 |
| cva6-pr-2468 | resolved | 304.6 | 2.9 | 0.0064 | 90.6 | 20 |
| cva6-pr-2469 | resolved | 63.9 | 0.9 | 0.0029 | 75.3 | 6 |
| cva6-pr-2476 | resolved | 1058.2 | 3.2 | 0.0157 | 93.8 | 22 |
| cva6-pr-2549 | unresolved | 223.4 | 2.4 | 0.0087 | 88.7 | 15 |
| cva6-pr-2589 | resolved | 1505.4 | 10.8 | 0.0180 | 96.4 | 87 |
| cva6-pr-2685 | resolved | 455.2 | 2.3 | 0.0079 | 92.1 | 21 |
| cva6-pr-2711 | unresolved | 577.8 | 4.4 | 0.0089 | 93.9 | 31 |
| cva6-pr-2728 | resolved | 1137.5 | 5.2 | 0.0131 | 96.9 | 34 |
| cva6-pr-2802 | unresolved | 1963.1 | 5.9 | 0.0266 | 96.5 | 36 |
| cva6-pr-2844 | unresolved | 800.3 | 4.9 | 0.0125 | 94.1 | 31 |
| cva6-pr-2916 | unresolved | 312.1 | 3.4 | 0.0058 | 91.6 | 14 |
| cva6-pr-2944 | resolved | 309.0 | 2.0 | 0.0069 | 89.2 | 14 |
| cva6-pr-2945 | resolved | 941.9 | 4.5 | 0.0105 | 95.5 | 29 |
| cva6-pr-2989 | resolved | 419.8 | 2.6 | 0.0095 | 89.7 | 12 |
| cva6-pr-3042 | unresolved | 1054.7 | 4.1 | 0.0146 | 95.3 | 33 |
| cva6-pr-3059 | resolved | 453.1 | 3.6 | 0.0091 | 92.9 | 17 |
| cva6-pr-3107 | resolved | 377.3 | 2.6 | 0.0067 | 91.4 | 17 |
| cva6-pr-3137 | resolved | 53.7 | 1.1 | 0.0023 | 78.2 | 4 |
| cva6-pr-3168 | unresolved | 251.9 | 3.1 | 0.0089 | 86.7 | 10 |
| cva6-pr-3171 | resolved | 98.2 | 1.0 | 0.0032 | 81.1 | 5 |
| cva6-pr-3191 | resolved | 407.3 | 3.3 | 0.0072 | 92.5 | 24 |
| cva6-pr-3204 | resolved | 675.5 | 3.9 | 0.0108 | 94.3 | 27 |
| cva6-pr-3226 | resolved | 949.9 | 5.3 | 0.0115 | 95.8 | 33 |
| cva6-pr-3231 | resolved | 226.1 | 1.5 | 0.0046 | 89.9 | 10 |
