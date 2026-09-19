# RocketChip Ablation - REPAIR

## 总体结果

```yaml
repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 13
  total: 32
  resolved_rate: 40.6%
  file_level_precision: 76.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 13/32 (40.6%) |
| File-Level Precision | 87.0% | 76.7% |

### 新解决
  pr-404, pr-1093, pr-1656, pr-2213, pr-2368, pr-3600

### 丢失
  pr-576

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
| pr-387 | 100.0% | 2/2 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 0.0% | 0/3 |
| pr-542 | 100.0% | 1/1 |
| pr-745 | 100.0% | 1/1 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 1/1 |
| pr-1656 | 100.0% | 4/4 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 0.0% | 0/3 |
| pr-2621 | 100.0% | 2/2 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 100.0% | 1/1 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 50.0% | 1/2 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 50.0% | 1/2 |
| pr-3600 | 100.0% | 1/1 |
| pr-3624 | 100.0% | 1/1 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 76.7%
- **Average (per-task)**: 83.9%

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
    "type": "timing_sync",
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
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 745,
    "test": "N/A",
    "type": "config_integ",
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
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2167,
    "test": "N/A",
    "type": "timing_sync",
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
    "pr": 3004,
    "test": "N/A",
    "type": "timing_sync",
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
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 3624,
    "test": "N/A",
    "type": "spec",
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
  config_integ: 3
  interface: 3
  logic: 6
  spec: 3
  timing_sync: 3
  unknown: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1126.5
  completion_k: 4.8
  cache_hit_pct: 96.7
  tool_calls: 33.5
  mcp_calls: 0.0
  other_skill_calls: 0.9
  ordinary_calls: 32.6
  cost_usd: 0.014027
  own_price_cost_usd: 0.309403
  tasks: 32
  resolved: 13
  unresolved: 19
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| rocket-chip-pr-1069 | resolved | 1502.4 | 7.6 | 0.0148 | 97.7 | 57 | 0 | 1 | 56 |
| rocket-chip-pr-1093 | resolved | 612.5 | 4.4 | 0.0144 | 95.2 | 19 | 0 | 1 | 18 |
| rocket-chip-pr-1176 | unresolved | 1210.9 | 4.2 | 0.0191 | 96.1 | 33 | 0 | 1 | 32 |
| rocket-chip-pr-1330 | resolved | 339.2 | 2.7 | 0.0059 | 93.2 | 18 | 0 | 1 | 17 |
| rocket-chip-pr-1493 | unresolved | 643.7 | 3.5 | 0.0101 | 94.2 | 28 | 0 | 1 | 27 |
| rocket-chip-pr-1656 | resolved | 1736.6 | 7.3 | 0.0163 | 97.3 | 54 | 0 | 0 | 54 |
| rocket-chip-pr-1761 | unresolved | 430.6 | 2.7 | 0.0073 | 94.4 | 17 | 0 | 1 | 16 |
| rocket-chip-pr-177 | unresolved | 408.7 | 3.4 | 0.0056 | 94.8 | 26 | 0 | 0 | 26 |
| rocket-chip-pr-1878 | unresolved | 574.8 | 4.1 | 0.0087 | 94.8 | 30 | 0 | 1 | 29 |
| rocket-chip-pr-2018 | unresolved | 1170.7 | 5.1 | 0.0134 | 97.1 | 33 | 0 | 1 | 32 |
| rocket-chip-pr-2036 | unresolved | 383.3 | 2.9 | 0.0072 | 93.1 | 17 | 0 | 1 | 16 |
| rocket-chip-pr-2167 | unresolved | 873.7 | 4.3 | 0.0139 | 95.6 | 30 | 0 | 1 | 29 |
| rocket-chip-pr-2213 | resolved | 842.0 | 4.5 | 0.0180 | 92.7 | 26 | 0 | 1 | 25 |
| rocket-chip-pr-2368 | resolved | 358.0 | 3.5 | 0.0073 | 92.0 | 24 | 0 | 1 | 23 |
| rocket-chip-pr-2543 | unresolved | 1572.4 | 5.2 | 0.0270 | 96.6 | 43 | 0 | 1 | 42 |
| rocket-chip-pr-2621 | unresolved | 1043.6 | 5.2 | 0.0115 | 96.7 | 46 | 0 | 1 | 45 |
| rocket-chip-pr-2984 | resolved | 334.2 | 3.1 | 0.0072 | 91.8 | 21 | 0 | 1 | 20 |
| rocket-chip-pr-2988 | resolved | 671.5 | 3.7 | 0.0084 | 95.8 | 32 | 0 | 1 | 31 |
| rocket-chip-pr-2994 | resolved | 2488.9 | 8.9 | 0.0209 | 98.4 | 72 | 0 | 1 | 71 |
| rocket-chip-pr-3004 | unresolved | 2463.0 | 7.5 | 0.0279 | 97.9 | 42 | 0 | 1 | 41 |
| rocket-chip-pr-3065 | resolved | 5035.1 | 10.7 | 0.0349 | 98.9 | 80 | 0 | 1 | 79 |
| rocket-chip-pr-3256 | unresolved | 915.9 | 4.5 | 0.0117 | 96.0 | 29 | 0 | 1 | 28 |
| rocket-chip-pr-3526 | unresolved | 1226.0 | 5.7 | 0.0134 | 97.3 | 34 | 0 | 1 | 33 |
| rocket-chip-pr-3600 | resolved | 2050.9 | 5.6 | 0.0316 | 97.7 | 39 | 0 | 1 | 38 |
| rocket-chip-pr-3624 | unresolved | 805.3 | 5.1 | 0.0092 | 96.1 | 34 | 0 | 1 | 33 |
| rocket-chip-pr-3651 | unresolved | 345.8 | 2.4 | 0.0065 | 93.1 | 15 | 0 | 1 | 14 |
| rocket-chip-pr-387 | unresolved | 2345.7 | 8.5 | 0.0300 | 97.2 | 49 | 0 | 1 | 48 |
| rocket-chip-pr-404 | resolved | 482.3 | 3.4 | 0.0082 | 93.4 | 26 | 0 | 1 | 25 |
| rocket-chip-pr-485 | unresolved | 2038.0 | 6.3 | 0.0192 | 97.3 | 51 | 0 | 1 | 50 |
| rocket-chip-pr-542 | resolved | 207.1 | 1.8 | 0.0043 | 90.3 | 12 | 0 | 1 | 11 |
| rocket-chip-pr-576 | unresolved | 23.0 | 0.3 | 0.0030 | 34.5 | 3 | 0 | 1 | 2 |
| rocket-chip-pr-745 | unresolved | 911.7 | 4.6 | 0.0119 | 95.5 | 32 | 0 | 1 | 31 |
