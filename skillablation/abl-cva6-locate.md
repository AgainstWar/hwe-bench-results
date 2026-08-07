# CVA6 Ablation - LOCATE

## 总体结果

```yaml
locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 11
  total: 35
  resolved_rate: 31.4%
  file_level_precision: 54.5%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 11/35 (31.4%) |
| File-Level Precision | 79.0% | 54.5% |

### 新解决
  pr-2989

### 丢失
  pr-1482, pr-2032, pr-2248, pr-2282, pr-2330, pr-2468, pr-2469, pr-2476, pr-2549, pr-2685, pr-2711, pr-2916, pr-2944, pr-2945, pr-3168, pr-3171, pr-3204, pr-3226

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 0.0% | 0/1 |
| pr-2170 | 0.0% | 0/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 0.0% | 0/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2711 | 0.0% | 0/1 |
| pr-2728 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3059 | 100.0% | 1/1 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3231 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 54.5%
- **Average (per-task)**: 67.6%

## 未解决 Case

```json
[
  {
    "pr": 1482,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2032,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2170,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2248,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2279,
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
    "pr": 2330,
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
    "pr": 2468,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2469,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2476,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2549,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2685,
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
    "type": "unknown",
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
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2945,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3042,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3168,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3171,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3204,
    "test": "N/A",
    "type": "unknown",
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
  config_integ: 2
  logic: 1
  spec: 1
  unknown: 20
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 389.5
  completion_k: 3.0
  cache_hit_pct: 91.6
  tool_calls: 16.8
  mcp_calls: 0.0
  skill_calls: 0.9
  ordinary_calls: 15.8
  cost_usd: 0.008175
  own_price_cost_usd: 0.108476
  tasks: 35
  resolved: 11
  unresolved: 24
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| cva6-pr-1482 | unresolved | 506.9 | 3.1 | 0.0134 | 92.1 | 17 | 0 | 1 | 16 |
| cva6-pr-2017 | resolved | 471.5 | 4.8 | 0.0076 | 94.1 | 21 | 0 | 1 | 20 |
| cva6-pr-2032 | unresolved | 401.8 | 3.9 | 0.0091 | 91.4 | 23 | 0 | 1 | 22 |
| cva6-pr-2170 | unresolved | 1448.9 | 5.2 | 0.0192 | 94.8 | 36 | 0 | 1 | 35 |
| cva6-pr-2248 | unresolved | 84.5 | 2.1 | 0.0039 | 75.3 | 6 | 0 | 1 | 5 |
| cva6-pr-2279 | unresolved | 231.2 | 2.9 | 0.0060 | 88.3 | 18 | 0 | 1 | 17 |
| cva6-pr-2282 | unresolved | 247.6 | 2.5 | 0.0065 | 87.8 | 15 | 0 | 1 | 14 |
| cva6-pr-2330 | unresolved | 129.7 | 2.8 | 0.0055 | 81.4 | 8 | 0 | 1 | 7 |
| cva6-pr-2374 | resolved | 264.5 | 2.3 | 0.0106 | 91.7 | 19 | 0 | 1 | 18 |
| cva6-pr-2375 | resolved | 394.4 | 3.1 | 0.0081 | 91.4 | 17 | 0 | 1 | 16 |
| cva6-pr-2420 | unresolved | 544.5 | 4.5 | 0.0098 | 93.2 | 25 | 0 | 1 | 24 |
| cva6-pr-2468 | unresolved | 64.4 | 1.6 | 0.0037 | 67.2 | 5 | 0 | 1 | 4 |
| cva6-pr-2469 | unresolved | 103.6 | 2.0 | 0.0041 | 81.2 | 6 | 0 | 1 | 5 |
| cva6-pr-2476 | unresolved | 150.3 | 2.1 | 0.0055 | 81.1 | 11 | 0 | 1 | 10 |
| cva6-pr-2549 | unresolved | 157.2 | 2.0 | 0.0059 | 83.6 | 8 | 0 | 1 | 7 |
| cva6-pr-2589 | resolved | 921.2 | 6.4 | 0.0128 | 95.8 | 48 | 0 | 1 | 47 |
| cva6-pr-2685 | unresolved | 106.3 | 1.9 | 0.0047 | 76.9 | 9 | 0 | 1 | 8 |
| cva6-pr-2711 | unresolved | 328.8 | 3.8 | 0.0078 | 89.8 | 24 | 0 | 1 | 23 |
| cva6-pr-2728 | resolved | 271.5 | 3.0 | 0.0061 | 91.2 | 11 | 0 | 1 | 10 |
| cva6-pr-2802 | unresolved | 1357.4 | 5.6 | 0.0214 | 95.6 | 34 | 0 | 1 | 33 |
| cva6-pr-2844 | unresolved | 425.9 | 3.5 | 0.0079 | 91.7 | 29 | 0 | 1 | 28 |
| cva6-pr-2916 | unresolved | 218.4 | 2.1 | 0.0070 | 83.0 | 9 | 0 | 1 | 8 |
| cva6-pr-2944 | unresolved | 249.0 | 2.7 | 0.0081 | 84.0 | 13 | 0 | 1 | 12 |
| cva6-pr-2945 | unresolved | 111.5 | 1.3 | 0.0059 | 69.0 | 5 | 0 | 1 | 4 |
| cva6-pr-2989 | resolved | 1077.8 | 4.2 | 0.0163 | 95.0 | 26 | 0 | 1 | 25 |
| cva6-pr-3042 | unresolved | 1543.4 | 5.4 | 0.0195 | 96.2 | 47 | 0 | 1 | 46 |
| cva6-pr-3059 | resolved | 230.8 | 2.1 | 0.0063 | 88.1 | 8 | 0 | 1 | 7 |
| cva6-pr-3107 | resolved | 30.1 | 0.5 | 0.0018 | 64.2 | 2 | 0 | 0 | 2 |
| cva6-pr-3137 | resolved | 327.0 | 3.2 | 0.0072 | 90.3 | 21 | 0 | 1 | 20 |
| cva6-pr-3168 | unresolved | 130.8 | 2.7 | 0.0073 | 75.3 | 6 | 0 | 1 | 5 |
| cva6-pr-3171 | unresolved | 78.9 | 1.9 | 0.0036 | 76.0 | 4 | 0 | 1 | 3 |
| cva6-pr-3191 | resolved | 41.9 | 0.6 | 0.0019 | 73.9 | 3 | 0 | 0 | 3 |
| cva6-pr-3204 | unresolved | 220.9 | 3.0 | 0.0052 | 89.9 | 15 | 0 | 1 | 14 |
| cva6-pr-3226 | unresolved | 322.2 | 3.0 | 0.0103 | 83.1 | 12 | 0 | 1 | 11 |
| cva6-pr-3231 | resolved | 438.0 | 3.2 | 0.0061 | 94.3 | 26 | 0 | 1 | 25 |
