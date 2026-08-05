# CVA6 MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 24
  total: 35
  resolved_rate: 68.6%
  file_level_precision: 82.1%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 24/35 (68.6%) |
| File-Level Precision | 79.0% | 82.1% |

### 新解决
  pr-2279, pr-2989

### 丢失
  pr-2017, pr-2282, pr-2468, pr-2916, pr-2944, pr-3168

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 0.0% | 0/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 96.7% | 29/30 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2685 | 100.0% | 1/1 |
| pr-2711 | 100.0% | 1/1 |
| pr-2728 | 50.0% | 1/2 |
| pr-2802 | 0.0% | 0/1 |
| pr-2944 | 0.0% | 0/1 |
| pr-2945 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3042 | 100.0% | 1/1 |
| pr-3059 | 100.0% | 1/1 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3171 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3204 | 100.0% | 1/1 |
| pr-3226 | 66.7% | 2/3 |
| pr-3231 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 82.1%
- **Average (per-task)**: 83.1%

## 未解决 Case

```json
[
  {
    "pr": 2017,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2170,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2282,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2420,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2468,
    "test": "N/A",
    "type": "unknown",
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
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2944,
    "test": "N/A",
    "type": "logic",
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
  config_integ: 2
  logic: 1
  spec: 1
  unknown: 7
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 802.1
  completion_k: 3.8
  cache_hit_pct: 95.2
  tool_calls: 23.2
  cost_usd: 0.010894
  own_price_cost_usd: 0.220758
  tasks: 35
  resolved: 24
  unresolved: 11
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| cva6-pr-1482 | resolved | 209.0 | 2.0 | 0.0084 | 87.0 | 8 |
| cva6-pr-2017 | unresolved | 240.4 | 3.3 | 0.0058 | 88.7 | 12 |
| cva6-pr-2032 | resolved | 843.9 | 5.1 | 0.0117 | 95.0 | 30 |
| cva6-pr-2170 | unresolved | 1839.5 | 5.1 | 0.0225 | 95.6 | 37 |
| cva6-pr-2248 | resolved | 58.0 | 0.6 | 0.0026 | 73.2 | 3 |
| cva6-pr-2279 | resolved | 6618.6 | 24.3 | 0.0447 | 98.8 | 117 |
| cva6-pr-2282 | unresolved | 205.5 | 2.3 | 0.0057 | 87.2 | 11 |
| cva6-pr-2330 | resolved | 297.8 | 2.4 | 0.0069 | 92.6 | 15 |
| cva6-pr-2374 | resolved | 576.3 | 3.2 | 0.0106 | 90.9 | 15 |
| cva6-pr-2375 | resolved | 700.5 | 3.1 | 0.0106 | 92.8 | 22 |
| cva6-pr-2420 | unresolved | 1116.1 | 4.4 | 0.0148 | 94.8 | 33 |
| cva6-pr-2468 | unresolved | 99.6 | 1.6 | 0.0045 | 75.5 | 6 |
| cva6-pr-2469 | resolved | 240.4 | 1.6 | 0.0057 | 88.2 | 11 |
| cva6-pr-2476 | resolved | 774.4 | 4.0 | 0.0148 | 93.3 | 21 |
| cva6-pr-2549 | resolved | 175.7 | 1.3 | 0.0055 | 84.6 | 9 |
| cva6-pr-2589 | resolved | 1501.3 | 8.5 | 0.0133 | 97.5 | 68 |
| cva6-pr-2685 | resolved | 232.6 | 1.7 | 0.0061 | 88.0 | 15 |
| cva6-pr-2711 | resolved | 1490.3 | 5.5 | 0.0149 | 97.2 | 45 |
| cva6-pr-2728 | resolved | 711.7 | 3.8 | 0.0112 | 94.8 | 19 |
| cva6-pr-2802 | unresolved | 444.2 | 3.4 | 0.0127 | 90.5 | 16 |
| cva6-pr-2844 | unresolved | 136.0 | 2.4 | 0.0052 | 80.8 | 12 |
| cva6-pr-2916 | unresolved | 291.8 | 3.7 | 0.0066 | 89.5 | 13 |
| cva6-pr-2944 | unresolved | 298.6 | 2.5 | 0.0065 | 90.0 | 15 |
| cva6-pr-2945 | resolved | 624.7 | 3.6 | 0.0120 | 92.8 | 19 |
| cva6-pr-2989 | resolved | 1178.3 | 4.2 | 0.0188 | 94.1 | 24 |
| cva6-pr-3042 | unresolved | 3586.0 | 6.9 | 0.0344 | 97.6 | 73 |
| cva6-pr-3059 | resolved | 237.1 | 2.2 | 0.0052 | 89.6 | 12 |
| cva6-pr-3107 | resolved | 232.0 | 1.6 | 0.0049 | 89.3 | 12 |
| cva6-pr-3137 | resolved | 437.0 | 2.1 | 0.0077 | 92.4 | 18 |
| cva6-pr-3168 | unresolved | 383.3 | 2.8 | 0.0101 | 90.1 | 12 |
| cva6-pr-3171 | resolved | 430.9 | 2.9 | 0.0072 | 93.2 | 16 |
| cva6-pr-3191 | resolved | 494.1 | 2.2 | 0.0086 | 92.7 | 17 |
| cva6-pr-3204 | resolved | 221.8 | 1.5 | 0.0053 | 88.4 | 12 |
| cva6-pr-3226 | resolved | 1055.6 | 6.5 | 0.0128 | 96.2 | 36 |
| cva6-pr-3231 | resolved | 88.7 | 1.3 | 0.0031 | 82.8 | 8 |
