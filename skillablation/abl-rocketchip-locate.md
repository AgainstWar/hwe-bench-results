# RocketChip Ablation - LOCATE

## 总体结果

```yaml
locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 2
  total: 32
  resolved_rate: 6.2%
  file_level_precision: 72.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 2/32 (6.2%) |
| File-Level Precision | 87.0% | 72.7% |

### 新解决
  无

### 丢失
  pr-576, pr-1069, pr-1330, pr-2984, pr-2988, pr-2994

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
| pr-542 | 100.0% | 1/1 |
| pr-1330 | 0.0% | 0/1 |
| pr-1656 | 100.0% | 2/2 |
| pr-2018 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2621 | 100.0% | 2/2 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 72.7%
- **Average (per-task)**: 66.7%

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
    "pr": 404,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 485,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 576,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 745,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1069,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1093,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1176,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1330,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1493,
    "test": "N/A",
    "type": "unknown",
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
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1878,
    "test": "N/A",
    "type": "unknown",
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
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2213,
    "test": "N/A",
    "type": "unknown",
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
    "type": "unknown",
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
    "pr": 2994,
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
    "type": "unknown",
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
    "type": "unknown",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  interface: 2
  logic: 3
  unknown: 23
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 540.3
  completion_k: 3.6
  cache_hit_pct: 93.4
  tool_calls: 19.1
  mcp_calls: 0.0
  other_skill_calls: 1.0
  ordinary_calls: 18.1
  cost_usd: 0.011171
  own_price_cost_usd: 0.149823
  tasks: 32
  resolved: 2
  unresolved: 30
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| rocket-chip-pr-1069 | unresolved | 83.5 | 2.2 | 0.0042 | 72.2 | 10 | 0 | 1 | 9 |
| rocket-chip-pr-1093 | unresolved | 297.1 | 2.8 | 0.0070 | 91.5 | 16 | 0 | 1 | 15 |
| rocket-chip-pr-1176 | unresolved | 288.4 | 3.1 | 0.0118 | 88.1 | 12 | 0 | 1 | 11 |
| rocket-chip-pr-1330 | unresolved | 122.0 | 2.2 | 0.0069 | 83.1 | 7 | 0 | 1 | 6 |
| rocket-chip-pr-1493 | unresolved | 662.3 | 3.8 | 0.0149 | 93.3 | 18 | 0 | 1 | 17 |
| rocket-chip-pr-1656 | unresolved | 526.4 | 3.0 | 0.0086 | 93.4 | 23 | 0 | 1 | 22 |
| rocket-chip-pr-1761 | unresolved | 80.6 | 2.1 | 0.0045 | 76.9 | 6 | 0 | 1 | 5 |
| rocket-chip-pr-177 | unresolved | 804.9 | 4.5 | 0.0166 | 93.1 | 21 | 0 | 1 | 20 |
| rocket-chip-pr-1878 | unresolved | 215.8 | 3.4 | 0.0056 | 88.2 | 13 | 0 | 1 | 12 |
| rocket-chip-pr-2018 | unresolved | 279.8 | 3.0 | 0.0076 | 91.8 | 15 | 0 | 1 | 14 |
| rocket-chip-pr-2036 | unresolved | 141.5 | 3.4 | 0.0055 | 80.8 | 12 | 0 | 1 | 11 |
| rocket-chip-pr-2167 | unresolved | 110.7 | 2.1 | 0.0046 | 78.5 | 7 | 0 | 1 | 6 |
| rocket-chip-pr-2213 | unresolved | 659.2 | 4.0 | 0.0156 | 93.3 | 26 | 0 | 1 | 25 |
| rocket-chip-pr-2368 | unresolved | 1423.1 | 4.6 | 0.0283 | 96.5 | 31 | 0 | 1 | 30 |
| rocket-chip-pr-2543 | unresolved | 974.4 | 5.3 | 0.0236 | 94.8 | 27 | 0 | 1 | 26 |
| rocket-chip-pr-2621 | unresolved | 3551.2 | 9.5 | 0.0261 | 98.1 | 82 | 0 | 1 | 81 |
| rocket-chip-pr-2984 | unresolved | 227.7 | 2.9 | 0.0074 | 88.3 | 16 | 0 | 1 | 15 |
| rocket-chip-pr-2988 | unresolved | 122.0 | 2.4 | 0.0044 | 82.3 | 8 | 0 | 1 | 7 |
| rocket-chip-pr-2994 | unresolved | 207.5 | 2.8 | 0.0067 | 89.3 | 13 | 0 | 1 | 12 |
| rocket-chip-pr-3004 | unresolved | 902.0 | 5.0 | 0.0186 | 93.7 | 33 | 0 | 1 | 32 |
| rocket-chip-pr-3065 | resolved | 2025.5 | 7.0 | 0.0258 | 96.9 | 39 | 0 | 1 | 38 |
| rocket-chip-pr-3256 | unresolved | 631.6 | 3.6 | 0.0113 | 93.4 | 24 | 0 | 1 | 23 |
| rocket-chip-pr-3526 | unresolved | 309.4 | 3.3 | 0.0117 | 88.9 | 12 | 0 | 1 | 11 |
| rocket-chip-pr-3600 | unresolved | 747.9 | 4.5 | 0.0153 | 93.8 | 27 | 0 | 1 | 26 |
| rocket-chip-pr-3624 | unresolved | 418.8 | 4.6 | 0.0076 | 92.5 | 32 | 0 | 1 | 31 |
| rocket-chip-pr-3651 | unresolved | 173.0 | 2.3 | 0.0094 | 75.6 | 9 | 0 | 1 | 8 |
| rocket-chip-pr-387 | unresolved | 126.9 | 2.6 | 0.0076 | 82.5 | 8 | 0 | 1 | 7 |
| rocket-chip-pr-404 | unresolved | 294.0 | 2.3 | 0.0117 | 85.1 | 11 | 0 | 1 | 10 |
| rocket-chip-pr-485 | unresolved | 245.1 | 4.5 | 0.0084 | 83.8 | 13 | 0 | 1 | 12 |
| rocket-chip-pr-542 | resolved | 193.0 | 2.4 | 0.0038 | 92.1 | 17 | 0 | 1 | 16 |
| rocket-chip-pr-576 | unresolved | 207.5 | 2.3 | 0.0104 | 83.0 | 8 | 0 | 1 | 7 |
| rocket-chip-pr-745 | unresolved | 237.2 | 3.3 | 0.0059 | 89.7 | 14 | 0 | 1 | 13 |
