# Ibex MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 24
  total: 35
  resolved_rate: 68.6%
  file_level_precision: 88.2%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 24/35 (68.6%) |
| File-Level Precision | 79.2% | 88.2% |

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
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 1/1 |
| pr-475 | 0.0% | 0/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 1/1 |
| pr-974 | 100.0% | 2/2 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 100.0% | 1/1 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 75.0% | 3/4 |
| pr-1513 | 40.0% | 2/5 |
| pr-1584 | 100.0% | 4/4 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 2/2 |
| pr-2232 | 100.0% | 2/2 |

## File-Level Precision

- **Overall**: 88.2%
- **Average (per-task)**: 93.3%

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
    "pr": 293,
    "test": "N/A",
    "type": "interface",
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
    "pr": 1135,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 1229,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1469,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 1513,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1816,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 1865,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 4
  logic: 2
  spec: 4
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1267.8
  completion_k: 4.4
  cache_hit_pct: 96.5
  tool_calls: 28.4
  mcp_calls: 0.0
  skill_calls: 0.8
  ordinary_calls: 27.6
  cost_usd: 0.017418
  own_price_cost_usd: 0.347148
  tasks: 35
  resolved: 24
  unresolved: 11
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| ibex-pr-104 | unresolved | 2168.6 | 7.8 | 0.0217 | 96.6 | 41 | 0 | 0 | 41 |
| ibex-pr-1135 | unresolved | 1073.3 | 3.4 | 0.0178 | 95.5 | 25 | 0 | 1 | 24 |
| ibex-pr-1141 | resolved | 1708.9 | 5.3 | 0.0193 | 97.1 | 43 | 0 | 0 | 43 |
| ibex-pr-122 | resolved | 1180.7 | 4.1 | 0.0182 | 96.0 | 31 | 0 | 1 | 30 |
| ibex-pr-1229 | unresolved | 195.9 | 1.8 | 0.0061 | 82.7 | 14 | 0 | 1 | 13 |
| ibex-pr-1383 | resolved | 410.5 | 2.7 | 0.0077 | 93.8 | 18 | 0 | 1 | 17 |
| ibex-pr-1469 | unresolved | 5617.9 | 10.1 | 0.0454 | 98.4 | 70 | 0 | 1 | 69 |
| ibex-pr-1513 | unresolved | 3974.3 | 9.3 | 0.0308 | 97.5 | 42 | 0 | 0 | 42 |
| ibex-pr-155 | unresolved | 2053.3 | 4.2 | 0.0338 | 97.3 | 34 | 0 | 1 | 33 |
| ibex-pr-157 | resolved | 201.7 | 2.5 | 0.0105 | 84.6 | 7 | 0 | 1 | 6 |
| ibex-pr-1584 | resolved | 5039.6 | 9.1 | 0.0349 | 98.2 | 65 | 0 | 1 | 64 |
| ibex-pr-166 | resolved | 278.8 | 2.3 | 0.0048 | 92.4 | 16 | 0 | 0 | 16 |
| ibex-pr-167 | resolved | 810.4 | 4.5 | 0.0117 | 95.4 | 29 | 0 | 1 | 28 |
| ibex-pr-1735 | resolved | 449.7 | 3.5 | 0.0083 | 94.2 | 21 | 0 | 1 | 20 |
| ibex-pr-176 | resolved | 116.8 | 1.1 | 0.0030 | 86.4 | 7 | 0 | 0 | 7 |
| ibex-pr-1780 | resolved | 805.4 | 3.9 | 0.0097 | 96.9 | 26 | 0 | 0 | 26 |
| ibex-pr-1816 | unresolved | 734.8 | 4.0 | 0.0131 | 96.4 | 26 | 0 | 1 | 25 |
| ibex-pr-1865 | unresolved | 1144.7 | 5.6 | 0.0182 | 95.1 | 47 | 0 | 1 | 46 |
| ibex-pr-222 | resolved | 1101.9 | 3.9 | 0.0149 | 96.3 | 38 | 0 | 1 | 37 |
| ibex-pr-2232 | resolved | 635.7 | 4.4 | 0.0105 | 93.7 | 24 | 0 | 1 | 23 |
| ibex-pr-244 | resolved | 992.5 | 4.5 | 0.0198 | 93.3 | 21 | 0 | 1 | 20 |
| ibex-pr-276 | resolved | 1172.8 | 5.8 | 0.0324 | 93.6 | 26 | 0 | 2 | 24 |
| ibex-pr-282 | resolved | 269.2 | 2.1 | 0.0075 | 92.0 | 11 | 0 | 1 | 10 |
| ibex-pr-293 | unresolved | 308.4 | 2.4 | 0.0065 | 94.2 | 16 | 0 | 0 | 16 |
| ibex-pr-332 | resolved | 2183.7 | 6.5 | 0.0632 | 94.9 | 38 | 0 | 1 | 37 |
| ibex-pr-377 | resolved | 2223.4 | 6.2 | 0.0234 | 97.5 | 49 | 0 | 1 | 48 |
| ibex-pr-45 | resolved | 883.2 | 4.8 | 0.0095 | 96.7 | 35 | 0 | 1 | 34 |
| ibex-pr-465 | resolved | 448.2 | 2.4 | 0.0078 | 91.4 | 17 | 0 | 0 | 17 |
| ibex-pr-475 | unresolved | 455.3 | 3.4 | 0.0066 | 94.2 | 25 | 0 | 1 | 24 |
| ibex-pr-48 | resolved | 150.3 | 1.7 | 0.0042 | 86.6 | 7 | 0 | 1 | 6 |
| ibex-pr-54 | resolved | 192.5 | 2.1 | 0.0045 | 89.5 | 11 | 0 | 1 | 10 |
| ibex-pr-83 | resolved | 382.7 | 3.1 | 0.0066 | 93.3 | 21 | 0 | 1 | 20 |
| ibex-pr-882 | resolved | 2430.0 | 6.5 | 0.0354 | 98.2 | 36 | 0 | 1 | 35 |
| ibex-pr-907 | unresolved | 634.4 | 2.9 | 0.0147 | 95.6 | 15 | 0 | 0 | 15 |
| ibex-pr-974 | resolved | 1944.6 | 5.7 | 0.0271 | 96.9 | 41 | 0 | 1 | 40 |
