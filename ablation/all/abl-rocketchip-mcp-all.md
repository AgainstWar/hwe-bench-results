# RocketChip MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 6
  total: 32
  resolved_rate: 18.8%
  file_level_precision: 55.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 6/32 (18.8%) |
| File-Level Precision | 87.0% | 55.7% |

### 新解决
  pr-404

### 丢失
  pr-576, pr-2984, pr-2988

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 100.0% | 6/6 |
| pr-542 | 100.0% | 1/1 |
| pr-576 | 100.0% | 1/1 |
| pr-745 | 100.0% | 1/1 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 1/1 |
| pr-1656 | 16.7% | 4/24 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 25.0% | 1/4 |
| pr-2621 | 100.0% | 3/3 |
| pr-2994 | 100.0% | 1/1 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3600 | 100.0% | 1/1 |
| pr-3651 | 33.3% | 1/3 |

## File-Level Precision

- **Overall**: 55.7%
- **Average (per-task)**: 83.0%

## 未解决 Case

```json
[
  {
    "pr": 177,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 387,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 485,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 576,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 745,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 1093,
    "test": "N/A",
    "type": "sw_hw_interact",
    "desc": "N/A"
  },
  {
    "pr": 1176,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1493,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 1656,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1761,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1878,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 2018,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 2036,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2167,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 2213,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 2368,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2543,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2621,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2984,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2988,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3004,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3256,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 3526,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3600,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 3624,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3651,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 4
  interface: 5
  logic: 5
  spec: 2
  sw_hw_interact: 1
  timing_sync: 2
  unknown: 7
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 816.6
  completion_k: 3.8
  cache_hit_pct: 95.5
  tool_calls: 25.4
  cost_usd: 0.012653
  own_price_cost_usd: 0.224695
  tasks: 32
  resolved: 6
  unresolved: 26
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| rocket-chip-pr-1069 | resolved | 1418.1 | 6.7 | 0.0144 | 96.5 | 51 |
| rocket-chip-pr-1093 | unresolved | 237.6 | 1.7 | 0.0053 | 91.0 | 12 |
| rocket-chip-pr-1176 | unresolved | 1030.1 | 3.6 | 0.0171 | 95.7 | 33 |
| rocket-chip-pr-1330 | resolved | 443.6 | 2.1 | 0.0079 | 92.9 | 15 |
| rocket-chip-pr-1493 | unresolved | 948.6 | 5.0 | 0.0130 | 95.1 | 31 |
| rocket-chip-pr-1656 | unresolved | 2572.0 | 11.1 | 0.0203 | 98.3 | 71 |
| rocket-chip-pr-1761 | unresolved | 155.2 | 1.4 | 0.0052 | 87.2 | 12 |
| rocket-chip-pr-177 | unresolved | 614.1 | 4.4 | 0.0084 | 95.1 | 27 |
| rocket-chip-pr-1878 | unresolved | 533.5 | 2.6 | 0.0081 | 93.5 | 26 |
| rocket-chip-pr-2018 | unresolved | 399.6 | 2.9 | 0.0068 | 94.1 | 22 |
| rocket-chip-pr-2036 | unresolved | 94.9 | 1.9 | 0.0041 | 75.8 | 6 |
| rocket-chip-pr-2167 | unresolved | 611.9 | 3.0 | 0.0104 | 95.2 | 23 |
| rocket-chip-pr-2213 | unresolved | 1687.1 | 4.4 | 0.0328 | 97.0 | 31 |
| rocket-chip-pr-2368 | unresolved | 388.5 | 2.4 | 0.0070 | 92.5 | 21 |
| rocket-chip-pr-2543 | unresolved | 2995.4 | 6.5 | 0.0378 | 98.1 | 43 |
| rocket-chip-pr-2621 | unresolved | 179.8 | 3.0 | 0.0047 | 89.1 | 19 |
| rocket-chip-pr-2984 | unresolved | 229.7 | 3.2 | 0.0072 | 86.2 | 15 |
| rocket-chip-pr-2988 | unresolved | 401.6 | 2.5 | 0.0070 | 91.8 | 15 |
| rocket-chip-pr-2994 | resolved | 887.9 | 3.9 | 0.0153 | 95.6 | 29 |
| rocket-chip-pr-3004 | unresolved | 192.5 | 0.7 | 0.0177 | 74.4 | 6 |
| rocket-chip-pr-3065 | resolved | 1522.7 | 5.1 | 0.0192 | 97.1 | 37 |
| rocket-chip-pr-3256 | unresolved | 988.9 | 3.7 | 0.0119 | 95.9 | 36 |
| rocket-chip-pr-3526 | unresolved | 135.5 | 1.9 | 0.0119 | 74.7 | 5 |
| rocket-chip-pr-3600 | unresolved | 698.4 | 2.3 | 0.0174 | 94.2 | 13 |
| rocket-chip-pr-3624 | unresolved | 131.4 | 2.1 | 0.0050 | 79.5 | 8 |
| rocket-chip-pr-3651 | unresolved | 781.7 | 3.7 | 0.0086 | 97.0 | 34 |
| rocket-chip-pr-387 | unresolved | 319.2 | 4.0 | 0.0099 | 88.3 | 14 |
| rocket-chip-pr-404 | resolved | 1052.2 | 6.2 | 0.0137 | 96.2 | 33 |
| rocket-chip-pr-485 | unresolved | 2575.7 | 11.4 | 0.0289 | 96.6 | 54 |
| rocket-chip-pr-542 | resolved | 235.9 | 2.4 | 0.0050 | 92.5 | 12 |
| rocket-chip-pr-576 | unresolved | 544.5 | 2.4 | 0.0103 | 95.2 | 20 |
| rocket-chip-pr-745 | unresolved | 1122.7 | 4.6 | 0.0123 | 96.4 | 38 |
