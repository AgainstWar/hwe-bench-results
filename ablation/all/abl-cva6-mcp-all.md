# CVA6 MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 27
  total: 35
  resolved_rate: 77.1%
  file_level_precision: 81.5%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 27/35 (77.1%) |
| File-Level Precision | 79.0% | 81.5% |

### 新解决
  pr-2279, pr-2420, pr-2989

### 丢失
  pr-2032, pr-2282, pr-2916, pr-3226

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 50.0% | 1/2 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 91.7% | 11/12 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 100.0% | 1/1 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2685 | 100.0% | 1/1 |
| pr-2711 | 100.0% | 4/4 |
| pr-2728 | 100.0% | 1/1 |
| pr-2802 | 0.0% | 0/1 |
| pr-2844 | 100.0% | 1/1 |
| pr-2944 | 100.0% | 1/1 |
| pr-2945 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3042 | 50.0% | 1/2 |
| pr-3059 | 100.0% | 1/1 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3168 | 100.0% | 1/1 |
| pr-3171 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3204 | 100.0% | 1/1 |
| pr-3231 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 81.5%
- **Average (per-task)**: 90.5%

## 未解决 Case

```json
[
  {
    "pr": 2032,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2170,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2282,
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
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 2916,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3042,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 3226,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  logic: 1
  spec: 2
  unknown: 4
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 819.6
  completion_k: 3.5
  cache_hit_pct: 95.0
  tool_calls: 23.6
  mcp_calls: 0.0
  other_skill_calls: 0.7
  ordinary_calls: 22.9
  cost_usd: 0.011474
  own_price_cost_usd: 0.225187
  tasks: 35
  resolved: 27
  unresolved: 8
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| cva6-pr-1482 | resolved | 453.6 | 2.3 | 0.0122 | 91.9 | 14 | 0 | 0 | 14 |
| cva6-pr-2017 | resolved | 177.1 | 1.6 | 0.0047 | 86.5 | 7 | 0 | 1 | 6 |
| cva6-pr-2032 | unresolved | 1378.2 | 5.4 | 0.0200 | 96.4 | 31 | 0 | 1 | 30 |
| cva6-pr-2170 | unresolved | 3905.5 | 6.3 | 0.0432 | 96.3 | 54 | 0 | 1 | 53 |
| cva6-pr-2248 | resolved | 51.4 | 0.6 | 0.0022 | 74.2 | 3 | 0 | 0 | 3 |
| cva6-pr-2279 | resolved | 4360.1 | 16.3 | 0.0344 | 98.4 | 101 | 0 | 2 | 99 |
| cva6-pr-2282 | unresolved | 311.1 | 3.0 | 0.0069 | 91.3 | 19 | 0 | 1 | 18 |
| cva6-pr-2330 | resolved | 80.7 | 0.9 | 0.0034 | 81.4 | 4 | 0 | 0 | 4 |
| cva6-pr-2374 | resolved | 303.0 | 1.6 | 0.0120 | 80.1 | 8 | 0 | 0 | 8 |
| cva6-pr-2375 | resolved | 574.3 | 2.6 | 0.0097 | 92.9 | 19 | 0 | 1 | 18 |
| cva6-pr-2420 | resolved | 727.5 | 4.2 | 0.0145 | 92.8 | 21 | 0 | 1 | 20 |
| cva6-pr-2468 | resolved | 498.7 | 3.2 | 0.0069 | 94.2 | 31 | 0 | 0 | 31 |
| cva6-pr-2469 | resolved | 398.5 | 2.5 | 0.0070 | 93.1 | 17 | 0 | 0 | 17 |
| cva6-pr-2476 | resolved | 1223.9 | 6.1 | 0.0140 | 96.8 | 48 | 0 | 0 | 48 |
| cva6-pr-2549 | resolved | 133.3 | 1.1 | 0.0036 | 87.7 | 8 | 0 | 0 | 8 |
| cva6-pr-2589 | resolved | 4317.5 | 11.4 | 0.0290 | 98.4 | 86 | 0 | 1 | 85 |
| cva6-pr-2685 | resolved | 235.9 | 1.4 | 0.0056 | 87.6 | 13 | 0 | 1 | 12 |
| cva6-pr-2711 | resolved | 930.0 | 4.9 | 0.0128 | 95.0 | 40 | 0 | 0 | 40 |
| cva6-pr-2728 | resolved | 432.2 | 3.5 | 0.0069 | 94.6 | 18 | 0 | 0 | 18 |
| cva6-pr-2802 | unresolved | 869.5 | 4.4 | 0.0199 | 92.2 | 15 | 0 | 1 | 14 |
| cva6-pr-2844 | unresolved | 356.7 | 3.9 | 0.0072 | 92.0 | 19 | 0 | 1 | 18 |
| cva6-pr-2916 | unresolved | 226.5 | 1.6 | 0.0047 | 89.9 | 10 | 0 | 1 | 9 |
| cva6-pr-2944 | resolved | 193.3 | 1.2 | 0.0067 | 79.8 | 7 | 0 | 1 | 6 |
| cva6-pr-2945 | resolved | 247.6 | 1.4 | 0.0048 | 90.2 | 12 | 0 | 0 | 12 |
| cva6-pr-2989 | resolved | 1021.3 | 3.5 | 0.0140 | 95.1 | 26 | 0 | 0 | 26 |
| cva6-pr-3042 | unresolved | 1119.0 | 3.1 | 0.0212 | 92.8 | 28 | 0 | 0 | 28 |
| cva6-pr-3059 | resolved | 262.0 | 2.0 | 0.0076 | 89.0 | 10 | 0 | 1 | 9 |
| cva6-pr-3107 | resolved | 181.9 | 1.4 | 0.0042 | 88.1 | 9 | 0 | 1 | 8 |
| cva6-pr-3137 | resolved | 673.6 | 4.1 | 0.0076 | 95.9 | 41 | 0 | 1 | 40 |
| cva6-pr-3168 | resolved | 577.3 | 2.7 | 0.0111 | 93.6 | 16 | 0 | 1 | 15 |
| cva6-pr-3171 | resolved | 210.2 | 1.7 | 0.0052 | 87.8 | 10 | 0 | 0 | 10 |
| cva6-pr-3191 | resolved | 965.7 | 4.2 | 0.0131 | 94.8 | 31 | 0 | 1 | 30 |
| cva6-pr-3204 | resolved | 418.1 | 2.1 | 0.0080 | 91.6 | 13 | 0 | 1 | 12 |
| cva6-pr-3226 | unresolved | 528.2 | 4.4 | 0.0098 | 92.7 | 23 | 0 | 1 | 22 |
| cva6-pr-3231 | resolved | 343.3 | 3.3 | 0.0072 | 90.4 | 13 | 0 | 2 | 11 |
