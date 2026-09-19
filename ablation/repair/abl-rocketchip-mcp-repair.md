# RocketChip MCP+REPAIR Analysis

## 总体结果

```yaml
mcp+repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 32
  resolved_rate: 37.5%
  file_level_precision: 89.1%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 12/32 (37.5%) |
| File-Level Precision | 87.0% | 89.1% |

### 新解决
  pr-177, pr-404, pr-1878, pr-2213, pr-2368, pr-2621

### 丢失
  pr-576, pr-1069

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/2 |
| pr-387 | 100.0% | 3/3 |
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
| pr-1656 | 100.0% | 3/3 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 0.0% | 0/2 |
| pr-2621 | 100.0% | 3/3 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 100.0% | 1/1 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 100.0% | 1/1 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 100.0% | 1/1 |
| pr-3600 | 100.0% | 1/1 |
| pr-3624 | 100.0% | 1/1 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 89.1%
- **Average (per-task)**: 90.6%

## 未解决 Case

```json
[
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
    "pr": 1069,
    "test": "N/A",
    "type": "logic",
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
    "pr": 3600,
    "test": "N/A",
    "type": "timing_sync",
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
  config_integ: 2
  interface: 4
  logic: 7
  spec: 2
  sw_hw_interact: 1
  timing_sync: 4
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1431.5
  completion_k: 4.7
  cache_hit_pct: 97.1
  tool_calls: 31.9
  mcp_calls: 0.0
  other_skill_calls: 0.7
  ordinary_calls: 31.2
  cost_usd: 0.016676
  own_price_cost_usd: 0.391729
  tasks: 32
  resolved: 12
  unresolved: 20
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| rocket-chip-pr-1069 | unresolved | 4712.4 | 14.6 | 0.0350 | 98.7 | 87 | 0 | 0 | 87 |
| rocket-chip-pr-1093 | unresolved | 701.8 | 3.2 | 0.0121 | 95.0 | 21 | 0 | 1 | 20 |
| rocket-chip-pr-1176 | unresolved | 1232.0 | 3.9 | 0.0160 | 96.7 | 35 | 0 | 0 | 35 |
| rocket-chip-pr-1330 | resolved | 107.5 | 1.3 | 0.0040 | 82.9 | 7 | 0 | 1 | 6 |
| rocket-chip-pr-1493 | unresolved | 977.0 | 3.6 | 0.0154 | 95.6 | 26 | 0 | 1 | 25 |
| rocket-chip-pr-1656 | unresolved | 659.7 | 3.9 | 0.0085 | 95.3 | 28 | 0 | 0 | 28 |
| rocket-chip-pr-1761 | unresolved | 384.4 | 2.5 | 0.0076 | 93.2 | 15 | 0 | 1 | 14 |
| rocket-chip-pr-177 | resolved | 1220.6 | 6.6 | 0.0132 | 96.6 | 41 | 0 | 1 | 40 |
| rocket-chip-pr-1878 | resolved | 197.5 | 1.7 | 0.0046 | 91.1 | 12 | 0 | 0 | 12 |
| rocket-chip-pr-2018 | unresolved | 1094.4 | 4.4 | 0.0141 | 96.8 | 34 | 0 | 1 | 33 |
| rocket-chip-pr-2036 | unresolved | 155.8 | 1.9 | 0.0046 | 84.9 | 13 | 0 | 1 | 12 |
| rocket-chip-pr-2167 | unresolved | 587.6 | 3.9 | 0.0106 | 92.8 | 20 | 0 | 1 | 19 |
| rocket-chip-pr-2213 | resolved | 1090.5 | 4.1 | 0.0192 | 95.8 | 36 | 0 | 1 | 35 |
| rocket-chip-pr-2368 | resolved | 4562.0 | 8.9 | 0.0426 | 98.4 | 70 | 0 | 1 | 69 |
| rocket-chip-pr-2543 | unresolved | 6972.1 | 10.4 | 0.0566 | 98.9 | 100 | 0 | 1 | 99 |
| rocket-chip-pr-2621 | resolved | 454.9 | 3.9 | 0.0071 | 94.9 | 24 | 0 | 0 | 24 |
| rocket-chip-pr-2984 | resolved | 249.7 | 2.5 | 0.0062 | 89.8 | 14 | 0 | 1 | 13 |
| rocket-chip-pr-2988 | resolved | 171.1 | 1.8 | 0.0054 | 83.4 | 9 | 0 | 1 | 8 |
| rocket-chip-pr-2994 | resolved | 735.7 | 3.4 | 0.0149 | 95.0 | 22 | 0 | 0 | 22 |
| rocket-chip-pr-3004 | unresolved | 2480.8 | 5.1 | 0.0332 | 96.9 | 38 | 0 | 1 | 37 |
| rocket-chip-pr-3065 | resolved | 752.1 | 3.4 | 0.0151 | 94.5 | 25 | 0 | 0 | 25 |
| rocket-chip-pr-3256 | unresolved | 1172.2 | 4.9 | 0.0130 | 97.0 | 32 | 0 | 1 | 31 |
| rocket-chip-pr-3526 | unresolved | 332.7 | 2.5 | 0.0071 | 92.0 | 14 | 0 | 1 | 13 |
| rocket-chip-pr-3600 | unresolved | 1727.0 | 4.9 | 0.0222 | 96.9 | 40 | 0 | 1 | 39 |
| rocket-chip-pr-3624 | unresolved | 366.0 | 3.0 | 0.0057 | 94.3 | 27 | 0 | 0 | 27 |
| rocket-chip-pr-3651 | unresolved | 260.1 | 1.8 | 0.0067 | 89.9 | 16 | 0 | 1 | 15 |
| rocket-chip-pr-387 | unresolved | 2560.9 | 11.7 | 0.0270 | 98.1 | 46 | 0 | 1 | 45 |
| rocket-chip-pr-404 | resolved | 895.9 | 3.6 | 0.0160 | 95.8 | 21 | 0 | 1 | 20 |
| rocket-chip-pr-485 | unresolved | 6817.0 | 16.2 | 0.0540 | 98.3 | 86 | 0 | 1 | 85 |
| rocket-chip-pr-542 | resolved | 93.5 | 1.0 | 0.0032 | 82.6 | 6 | 0 | 0 | 6 |
| rocket-chip-pr-576 | unresolved | 1192.0 | 4.1 | 0.0219 | 96.2 | 25 | 0 | 1 | 24 |
| rocket-chip-pr-745 | unresolved | 891.2 | 3.4 | 0.0108 | 95.7 | 31 | 0 | 0 | 31 |
