# RocketChip MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 32
  resolved_rate: 37.5%
  file_level_precision: 86.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 12/32 (37.5%) |
| File-Level Precision | 87.0% | 86.0% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
| pr-387 | 100.0% | 3/3 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 71.4% | 5/7 |
| pr-542 | 100.0% | 1/1 |
| pr-576 | 100.0% | 1/1 |
| pr-745 | 100.0% | 1/1 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 1/1 |
| pr-1656 | 100.0% | 2/2 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 0.0% | 0/2 |
| pr-2621 | 100.0% | 2/2 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 100.0% | 1/1 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 100.0% | 1/1 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 100.0% | 1/1 |
| pr-3624 | 100.0% | 1/1 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 86.0%
- **Average (per-task)**: 89.4%

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
    "pr": 745,
    "test": "N/A",
    "type": "config_integ",
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
    "pr": 3004,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 3065,
    "test": "N/A",
    "type": "interface",
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
    "pr": 3600,
    "test": "N/A",
    "type": "unknown",
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
  config_integ: 4
  interface: 4
  logic: 6
  spec: 2
  timing_sync: 3
  unknown: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 843.0
  completion_k: 3.5
  cache_hit_pct: 95.9
  tool_calls: 23.3
  mcp_calls: 0.0
  skill_calls: 0.4
  ordinary_calls: 22.9
  cost_usd: 0.012307
  own_price_cost_usd: 0.231441
  tasks: 32
  resolved: 12
  unresolved: 20
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| rocket-chip-pr-1069 | resolved | 1305.9 | 6.9 | 0.0136 | 97.0 | 45 | 0 | 1 | 44 |
| rocket-chip-pr-1093 | resolved | 237.7 | 1.7 | 0.0082 | 89.9 | 10 | 0 | 1 | 9 |
| rocket-chip-pr-1176 | resolved | 105.1 | 1.3 | 0.0048 | 84.1 | 7 | 0 | 0 | 7 |
| rocket-chip-pr-1330 | resolved | 89.5 | 0.9 | 0.0039 | 78.6 | 6 | 0 | 1 | 5 |
| rocket-chip-pr-1493 | unresolved | 1246.1 | 4.2 | 0.0178 | 95.1 | 33 | 0 | 1 | 32 |
| rocket-chip-pr-1656 | unresolved | 480.1 | 3.1 | 0.0116 | 87.8 | 23 | 0 | 1 | 22 |
| rocket-chip-pr-1761 | unresolved | 138.7 | 1.2 | 0.0041 | 87.9 | 7 | 0 | 0 | 7 |
| rocket-chip-pr-177 | unresolved | 1033.4 | 5.4 | 0.0131 | 95.4 | 35 | 0 | 0 | 35 |
| rocket-chip-pr-1878 | resolved | 161.0 | 1.4 | 0.0046 | 86.8 | 11 | 0 | 1 | 10 |
| rocket-chip-pr-2018 | unresolved | 577.5 | 3.3 | 0.0086 | 95.0 | 24 | 0 | 0 | 24 |
| rocket-chip-pr-2036 | unresolved | 127.0 | 1.5 | 0.0032 | 87.5 | 9 | 0 | 0 | 9 |
| rocket-chip-pr-2167 | unresolved | 309.7 | 1.9 | 0.0087 | 90.6 | 12 | 0 | 0 | 12 |
| rocket-chip-pr-2213 | resolved | 2210.5 | 4.9 | 0.0340 | 97.3 | 38 | 0 | 0 | 38 |
| rocket-chip-pr-2368 | unresolved | 2701.2 | 5.6 | 0.0271 | 98.3 | 53 | 0 | 0 | 53 |
| rocket-chip-pr-2543 | unresolved | 2994.6 | 6.0 | 0.0345 | 98.2 | 57 | 0 | 0 | 57 |
| rocket-chip-pr-2621 | unresolved | 432.5 | 3.9 | 0.0067 | 94.5 | 27 | 0 | 0 | 27 |
| rocket-chip-pr-2984 | resolved | 177.4 | 1.6 | 0.0053 | 88.0 | 12 | 0 | 1 | 11 |
| rocket-chip-pr-2988 | resolved | 207.9 | 1.3 | 0.0041 | 89.5 | 10 | 0 | 1 | 9 |
| rocket-chip-pr-2994 | resolved | 1143.7 | 4.8 | 0.0159 | 95.6 | 32 | 0 | 0 | 32 |
| rocket-chip-pr-3004 | unresolved | 407.6 | 2.2 | 0.0115 | 90.2 | 11 | 0 | 0 | 11 |
| rocket-chip-pr-3065 | unresolved | 480.0 | 3.0 | 0.0071 | 95.7 | 20 | 0 | 0 | 20 |
| rocket-chip-pr-3256 | unresolved | 91.4 | 1.2 | 0.0038 | 78.7 | 6 | 0 | 1 | 5 |
| rocket-chip-pr-3526 | unresolved | 895.5 | 3.1 | 0.0142 | 95.8 | 22 | 0 | 1 | 21 |
| rocket-chip-pr-3600 | unresolved | 72.8 | 0.5 | 0.0143 | 57.3 | 3 | 0 | 0 | 3 |
| rocket-chip-pr-3624 | unresolved | 816.1 | 4.5 | 0.0097 | 95.9 | 38 | 0 | 1 | 37 |
| rocket-chip-pr-3651 | unresolved | 207.3 | 1.6 | 0.0060 | 88.8 | 11 | 0 | 0 | 11 |
| rocket-chip-pr-387 | unresolved | 1933.3 | 9.8 | 0.0251 | 97.7 | 41 | 0 | 0 | 41 |
| rocket-chip-pr-404 | resolved | 610.7 | 3.0 | 0.0083 | 95.3 | 25 | 0 | 1 | 24 |
| rocket-chip-pr-485 | unresolved | 4565.7 | 15.7 | 0.0401 | 98.0 | 76 | 0 | 1 | 75 |
| rocket-chip-pr-542 | resolved | 54.1 | 0.6 | 0.0025 | 73.6 | 3 | 0 | 0 | 3 |
| rocket-chip-pr-576 | resolved | 617.5 | 2.7 | 0.0132 | 94.5 | 18 | 0 | 0 | 18 |
| rocket-chip-pr-745 | unresolved | 543.8 | 2.6 | 0.0082 | 94.0 | 21 | 0 | 1 | 20 |
