# RocketChip SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 9
  total: 32
  resolved_rate: 28.1%
  file_level_precision: 73.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 9/32 (28.1%) |
| File-Level Precision | 87.0% | 73.7% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
| pr-387 | 100.0% | 1/1 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 0.0% | 0/3 |
| pr-542 | 100.0% | 1/1 |
| pr-576 | 100.0% | 1/1 |
| pr-745 | 0.0% | 0/1 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 1/1 |
| pr-1656 | 100.0% | 2/2 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/3 |
| pr-2368 | 50.0% | 1/2 |
| pr-2543 | 0.0% | 0/1 |
| pr-2621 | 100.0% | 3/3 |
| pr-2988 | 100.0% | 1/1 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 100.0% | 1/1 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3600 | 100.0% | 1/1 |
| pr-3624 | 100.0% | 1/1 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 73.7%
- **Average (per-task)**: 81.0%

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
    "pr": 2984,
    "test": "N/A",
    "type": "unknown",
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
  interface: 5
  logic: 6
  spec: 2
  timing_sync: 4
  unknown: 3
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 985.4
  completion_k: 4.0
  cache_hit_pct: 96.2
  tool_calls: 27.9
  mcp_calls: 0.0
  skill_calls: 0.9
  ordinary_calls: 27.1
  cost_usd: 0.013785
  own_price_cost_usd: 0.270502
  tasks: 32
  resolved: 9
  unresolved: 23
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| rocket-chip-pr-1069 | resolved | 551.9 | 5.7 | 0.0085 | 95.5 | 40 | 0 | 0 | 40 |
| rocket-chip-pr-1093 | resolved | 526.7 | 3.4 | 0.0080 | 94.9 | 29 | 0 | 0 | 29 |
| rocket-chip-pr-1176 | resolved | 203.1 | 1.2 | 0.0086 | 77.3 | 10 | 0 | 1 | 9 |
| rocket-chip-pr-1330 | unresolved | 147.8 | 2.2 | 0.0061 | 86.6 | 7 | 0 | 1 | 6 |
| rocket-chip-pr-1493 | unresolved | 1525.0 | 7.2 | 0.0172 | 96.1 | 42 | 0 | 2 | 40 |
| rocket-chip-pr-1656 | unresolved | 282.5 | 2.6 | 0.0062 | 90.7 | 22 | 0 | 0 | 22 |
| rocket-chip-pr-1761 | unresolved | 375.4 | 2.5 | 0.0071 | 94.2 | 14 | 0 | 1 | 13 |
| rocket-chip-pr-177 | unresolved | 982.4 | 3.8 | 0.0159 | 94.7 | 22 | 0 | 1 | 21 |
| rocket-chip-pr-1878 | resolved | 624.6 | 3.0 | 0.0118 | 92.9 | 24 | 0 | 0 | 24 |
| rocket-chip-pr-2018 | unresolved | 610.3 | 2.3 | 0.0164 | 93.2 | 17 | 0 | 1 | 16 |
| rocket-chip-pr-2036 | unresolved | 271.5 | 2.2 | 0.0058 | 89.6 | 15 | 0 | 2 | 13 |
| rocket-chip-pr-2167 | unresolved | 743.2 | 3.3 | 0.0107 | 95.5 | 25 | 0 | 1 | 24 |
| rocket-chip-pr-2213 | unresolved | 2596.8 | 7.2 | 0.0377 | 97.1 | 41 | 0 | 2 | 39 |
| rocket-chip-pr-2368 | unresolved | 806.6 | 3.4 | 0.0140 | 95.7 | 22 | 0 | 1 | 21 |
| rocket-chip-pr-2543 | unresolved | 3488.6 | 8.0 | 0.0358 | 98.0 | 60 | 0 | 2 | 58 |
| rocket-chip-pr-2621 | resolved | 907.4 | 6.1 | 0.0094 | 97.1 | 52 | 0 | 0 | 52 |
| rocket-chip-pr-2984 | unresolved | 412.8 | 4.5 | 0.0077 | 93.1 | 31 | 0 | 1 | 30 |
| rocket-chip-pr-2988 | resolved | 306.2 | 1.8 | 0.0056 | 90.4 | 15 | 0 | 1 | 14 |
| rocket-chip-pr-2994 | resolved | 1587.6 | 6.8 | 0.0156 | 97.9 | 44 | 0 | 0 | 44 |
| rocket-chip-pr-3004 | unresolved | 1335.3 | 4.7 | 0.0210 | 97.0 | 32 | 0 | 1 | 31 |
| rocket-chip-pr-3065 | unresolved | 575.3 | 3.0 | 0.0096 | 94.8 | 20 | 0 | 2 | 18 |
| rocket-chip-pr-3256 | unresolved | 580.4 | 3.3 | 0.0096 | 94.9 | 20 | 0 | 1 | 19 |
| rocket-chip-pr-3526 | unresolved | 191.3 | 2.6 | 0.0114 | 83.8 | 9 | 0 | 1 | 8 |
| rocket-chip-pr-3600 | unresolved | 1472.6 | 5.0 | 0.0223 | 96.4 | 37 | 0 | 0 | 37 |
| rocket-chip-pr-3624 | unresolved | 1166.3 | 5.3 | 0.0130 | 97.1 | 43 | 0 | 1 | 42 |
| rocket-chip-pr-3651 | unresolved | 350.2 | 1.8 | 0.0083 | 90.6 | 12 | 0 | 1 | 11 |
| rocket-chip-pr-387 | unresolved | 2902.3 | 6.8 | 0.0292 | 98.6 | 49 | 0 | 1 | 48 |
| rocket-chip-pr-404 | resolved | 421.2 | 2.5 | 0.0069 | 95.4 | 18 | 0 | 0 | 18 |
| rocket-chip-pr-485 | unresolved | 4072.8 | 9.4 | 0.0332 | 97.9 | 70 | 0 | 0 | 70 |
| rocket-chip-pr-542 | resolved | 362.7 | 2.9 | 0.0060 | 92.7 | 15 | 0 | 2 | 13 |
| rocket-chip-pr-576 | unresolved | 468.4 | 1.9 | 0.0118 | 94.7 | 14 | 0 | 0 | 14 |
| rocket-chip-pr-745 | unresolved | 682.9 | 2.8 | 0.0108 | 94.9 | 23 | 0 | 1 | 22 |
