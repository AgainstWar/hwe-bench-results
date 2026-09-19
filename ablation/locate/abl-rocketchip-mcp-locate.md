# RocketChip MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 7
  total: 32
  resolved_rate: 21.9%
  file_level_precision: 76.2%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 7/32 (21.9%) |
| File-Level Precision | 87.0% | 76.2% |

### 新解决
  pr-485, pr-1878, pr-3600

### 丢失
  pr-576, pr-1330, pr-2984, pr-3065

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-387 | 100.0% | 3/3 |
| pr-404 | 0.0% | 0/1 |
| pr-485 | 83.3% | 5/6 |
| pr-542 | 100.0% | 1/1 |
| pr-745 | 50.0% | 1/2 |
| pr-1069 | 66.7% | 2/3 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 1/1 |
| pr-1656 | 100.0% | 2/2 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 0.0% | 0/4 |
| pr-2621 | 100.0% | 2/2 |
| pr-2988 | 100.0% | 1/1 |
| pr-2994 | 100.0% | 1/1 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 50.0% | 1/2 |
| pr-3600 | 100.0% | 1/1 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 76.2%
- **Average (per-task)**: 82.7%

## 未解决 Case

```json
[
  {
    "pr": 177,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 387,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 404,
    "test": "N/A",
    "type": "logic",
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
    "pr": 1330,
    "test": "N/A",
    "type": "unknown",
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
    "pr": 3004,
    "test": "N/A",
    "type": "unknown",
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
  logic: 6
  spec: 1
  sw_hw_interact: 1
  timing_sync: 2
  unknown: 6
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 895.0
  completion_k: 3.7
  cache_hit_pct: 95.8
  tool_calls: 25.5
  mcp_calls: 0.0
  other_skill_calls: 0.3
  ordinary_calls: 25.2
  cost_usd: 0.013533
  own_price_cost_usd: 0.245696
  tasks: 32
  resolved: 7
  unresolved: 25
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| rocket-chip-pr-1069 | resolved | 2015.8 | 6.8 | 0.0177 | 97.0 | 47 | 0 | 0 | 47 |
| rocket-chip-pr-1093 | unresolved | 73.1 | 0.7 | 0.0034 | 79.7 | 5 | 0 | 0 | 5 |
| rocket-chip-pr-1176 | unresolved | 118.6 | 1.4 | 0.0048 | 82.1 | 9 | 0 | 0 | 9 |
| rocket-chip-pr-1330 | unresolved | 90.5 | 1.8 | 0.0047 | 77.7 | 8 | 0 | 1 | 7 |
| rocket-chip-pr-1493 | unresolved | 655.8 | 3.5 | 0.0117 | 94.0 | 27 | 0 | 0 | 27 |
| rocket-chip-pr-1656 | unresolved | 455.4 | 2.8 | 0.0071 | 94.1 | 21 | 0 | 0 | 21 |
| rocket-chip-pr-1761 | unresolved | 185.7 | 1.5 | 0.0062 | 91.9 | 9 | 0 | 0 | 9 |
| rocket-chip-pr-177 | unresolved | 460.1 | 3.2 | 0.0149 | 87.4 | 16 | 0 | 1 | 15 |
| rocket-chip-pr-1878 | resolved | 440.1 | 2.7 | 0.0076 | 94.1 | 20 | 0 | 0 | 20 |
| rocket-chip-pr-2018 | unresolved | 515.4 | 2.8 | 0.0100 | 93.7 | 23 | 0 | 0 | 23 |
| rocket-chip-pr-2036 | unresolved | 343.0 | 2.3 | 0.0070 | 91.3 | 16 | 0 | 0 | 16 |
| rocket-chip-pr-2167 | unresolved | 454.9 | 2.6 | 0.0085 | 93.8 | 22 | 0 | 0 | 22 |
| rocket-chip-pr-2213 | unresolved | 782.4 | 3.1 | 0.0132 | 95.2 | 31 | 0 | 0 | 31 |
| rocket-chip-pr-2368 | unresolved | 1539.7 | 3.8 | 0.0269 | 95.9 | 33 | 0 | 1 | 32 |
| rocket-chip-pr-2543 | unresolved | 1853.3 | 4.2 | 0.0351 | 96.1 | 37 | 0 | 0 | 37 |
| rocket-chip-pr-2621 | unresolved | 341.8 | 3.7 | 0.0055 | 94.1 | 27 | 0 | 0 | 27 |
| rocket-chip-pr-2984 | unresolved | 258.5 | 2.9 | 0.0071 | 88.2 | 13 | 0 | 1 | 12 |
| rocket-chip-pr-2988 | resolved | 67.9 | 0.8 | 0.0024 | 79.2 | 4 | 0 | 0 | 4 |
| rocket-chip-pr-2994 | resolved | 621.0 | 3.3 | 0.0128 | 95.5 | 28 | 0 | 0 | 28 |
| rocket-chip-pr-3004 | unresolved | 402.5 | 3.0 | 0.0167 | 85.0 | 11 | 0 | 1 | 10 |
| rocket-chip-pr-3065 | unresolved | 388.0 | 2.1 | 0.0118 | 92.8 | 12 | 0 | 0 | 12 |
| rocket-chip-pr-3256 | unresolved | 1438.2 | 4.2 | 0.0139 | 96.4 | 36 | 0 | 1 | 35 |
| rocket-chip-pr-3526 | unresolved | 1600.7 | 3.7 | 0.0202 | 97.7 | 30 | 0 | 1 | 29 |
| rocket-chip-pr-3600 | resolved | 1765.4 | 5.1 | 0.0249 | 97.4 | 42 | 0 | 0 | 42 |
| rocket-chip-pr-3624 | unresolved | 705.4 | 3.9 | 0.0088 | 95.1 | 31 | 0 | 1 | 30 |
| rocket-chip-pr-3651 | unresolved | 521.4 | 2.4 | 0.0090 | 95.2 | 19 | 0 | 0 | 19 |
| rocket-chip-pr-387 | unresolved | 2338.7 | 9.5 | 0.0287 | 97.4 | 46 | 0 | 0 | 46 |
| rocket-chip-pr-404 | unresolved | 321.0 | 3.2 | 0.0105 | 87.8 | 17 | 0 | 1 | 16 |
| rocket-chip-pr-485 | resolved | 4750.3 | 13.7 | 0.0397 | 98.0 | 75 | 0 | 0 | 75 |
| rocket-chip-pr-542 | resolved | 163.6 | 1.9 | 0.0036 | 90.5 | 14 | 0 | 0 | 14 |
| rocket-chip-pr-576 | unresolved | 500.3 | 1.6 | 0.0198 | 93.8 | 18 | 0 | 0 | 18 |
| rocket-chip-pr-745 | unresolved | 2473.0 | 9.1 | 0.0189 | 98.2 | 70 | 0 | 0 | 70 |
