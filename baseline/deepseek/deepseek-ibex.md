# Ibex Baseline (DeepSeek V4 Flash) Analysis

## 总体结果

```yaml
deepseek:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 27
  total: 35
  resolved_rate: 77.1%
  file_level_precision: 79.2%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | DEEPSEEK |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 27/35 (77.1%) |
| File-Level Precision | 79.2% | 79.2% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
| pr-104 | 100.0% | 3/3 |
| pr-122 | 100.0% | 1/1 |
| pr-155 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 25.0% | 1/4 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 2/2 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 1/1 |
| pr-475 | 0.0% | 0/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 1/1 |
| pr-974 | 100.0% | 1/1 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 100.0% | 1/1 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 50.0% | 1/2 |
| pr-1513 | 40.0% | 2/5 |
| pr-1584 | 100.0% | 4/4 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 33.3% | 1/3 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 1/1 |
| pr-2232 | 100.0% | 2/2 |

## File-Level Precision

- **Overall**: 79.2%
- **Average (per-task)**: 88.5%

## 未解决 Case

```json
[
  {
    "pr": 104,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 155,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 475,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 907,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 974,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1141,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1229,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1513,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  interface: 3
  logic: 2
  spec: 2
  timing_sync: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 856.3
  completion_k: 17.7
  cache_hit_pct: 97.0
  tool_calls: 23.2
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 23.2
  cost_usd: 0.000000
  own_price_cost_usd: 0.250615
  tasks: 35
  resolved: 27
  unresolved: 8
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| ibex-pr-104 | unresolved | 1488.0 | 12.5 | 0.0000 | 96.8 | 37 | 0 | 0 | 37 |
| ibex-pr-1135 | resolved | 598.0 | 24.4 | 0.0000 | 93.7 | 16 | 0 | 0 | 16 |
| ibex-pr-1141 | unresolved | 1313.9 | 20.6 | 0.0000 | 97.2 | 38 | 0 | 0 | 38 |
| ibex-pr-122 | resolved | 556.1 | 13.0 | 0.0000 | 96.4 | 21 | 0 | 0 | 21 |
| ibex-pr-1229 | unresolved | 459.2 | 8.5 | 0.0000 | 94.2 | 22 | 0 | 0 | 22 |
| ibex-pr-1383 | resolved | 209.8 | 4.9 | 0.0000 | 96.1 | 15 | 0 | 0 | 15 |
| ibex-pr-1469 | resolved | 2640.4 | 19.9 | 0.0000 | 97.2 | 41 | 0 | 0 | 41 |
| ibex-pr-1513 | unresolved | 2376.8 | 16.5 | 0.0000 | 97.2 | 55 | 0 | 0 | 55 |
| ibex-pr-155 | unresolved | 1512.0 | 45.5 | 0.0000 | 97.4 | 44 | 0 | 0 | 44 |
| ibex-pr-157 | resolved | 212.3 | 11.5 | 0.0000 | 94.1 | 10 | 0 | 0 | 10 |
| ibex-pr-1584 | resolved | 4969.1 | 41.4 | 0.0000 | 98.4 | 64 | 0 | 0 | 64 |
| ibex-pr-166 | resolved | 63.8 | 4.2 | 0.0000 | 89.9 | 4 | 0 | 0 | 4 |
| ibex-pr-167 | resolved | 2889.3 | 21.7 | 0.0000 | 98.3 | 67 | 0 | 0 | 67 |
| ibex-pr-1735 | resolved | 299.8 | 13.1 | 0.0000 | 95.7 | 15 | 0 | 0 | 15 |
| ibex-pr-176 | resolved | 62.5 | 1.7 | 0.0000 | 94.5 | 5 | 0 | 0 | 5 |
| ibex-pr-1780 | resolved | 352.0 | 8.4 | 0.0000 | 97.0 | 21 | 0 | 0 | 21 |
| ibex-pr-1816 | resolved | 857.7 | 33.2 | 0.0000 | 96.8 | 34 | 0 | 0 | 34 |
| ibex-pr-1865 | resolved | 198.8 | 9.3 | 0.0000 | 94.7 | 13 | 0 | 0 | 13 |
| ibex-pr-222 | resolved | 246.7 | 9.2 | 0.0000 | 94.7 | 15 | 0 | 0 | 15 |
| ibex-pr-2232 | resolved | 495.8 | 9.6 | 0.0000 | 95.4 | 24 | 0 | 0 | 24 |
| ibex-pr-244 | resolved | 712.5 | 29.3 | 0.0000 | 96.1 | 23 | 0 | 0 | 23 |
| ibex-pr-276 | resolved | 1625.2 | 56.4 | 0.0000 | 97.7 | 29 | 0 | 0 | 29 |
| ibex-pr-282 | resolved | 308.1 | 13.9 | 0.0000 | 95.1 | 18 | 0 | 0 | 18 |
| ibex-pr-293 | resolved | 186.3 | 9.7 | 0.0000 | 96.1 | 13 | 0 | 0 | 13 |
| ibex-pr-332 | resolved | 1554.1 | 55.8 | 0.0000 | 97.6 | 24 | 0 | 0 | 24 |
| ibex-pr-377 | resolved | 1187.5 | 20.6 | 0.0000 | 97.4 | 31 | 0 | 0 | 31 |
| ibex-pr-45 | resolved | 143.8 | 3.9 | 0.0000 | 93.8 | 11 | 0 | 0 | 11 |
| ibex-pr-465 | resolved | 59.3 | 1.5 | 0.0000 | 90.7 | 4 | 0 | 0 | 4 |
| ibex-pr-475 | unresolved | 241.0 | 7.3 | 0.0000 | 91.6 | 13 | 0 | 0 | 13 |
| ibex-pr-48 | resolved | 58.0 | 3.1 | 0.0000 | 92.1 | 4 | 0 | 0 | 4 |
| ibex-pr-54 | resolved | 60.7 | 4.4 | 0.0000 | 87.3 | 8 | 0 | 0 | 8 |
| ibex-pr-83 | resolved | 290.0 | 4.2 | 0.0000 | 96.0 | 17 | 0 | 0 | 17 |
| ibex-pr-882 | resolved | 801.6 | 36.2 | 0.0000 | 95.8 | 19 | 0 | 0 | 19 |
| ibex-pr-907 | unresolved | 592.2 | 33.3 | 0.0000 | 96.2 | 20 | 0 | 0 | 20 |
| ibex-pr-974 | unresolved | 347.2 | 9.5 | 0.0000 | 94.8 | 17 | 0 | 0 | 17 |
