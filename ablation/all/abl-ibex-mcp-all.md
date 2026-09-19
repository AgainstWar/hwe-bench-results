# Ibex MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 23
  total: 35
  resolved_rate: 65.7%
  file_level_precision: 80.4%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 23/35 (65.7%) |
| File-Level Precision | 79.2% | 80.4% |

### 新解决
  pr-907, pr-974

### 丢失
  pr-122, pr-276, pr-465, pr-882, pr-1584, pr-1780

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
| pr-104 | 100.0% | 3/3 |
| pr-155 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 0.0% | 0/2 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 100.0% | 1/1 |
| pr-475 | 0.0% | 0/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 2/2 |
| pr-974 | 100.0% | 2/2 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 100.0% | 1/1 |
| pr-1229 | 25.0% | 1/4 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 100.0% | 3/3 |
| pr-1513 | 40.0% | 2/5 |
| pr-1735 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 2/2 |
| pr-2232 | 100.0% | 2/2 |

## File-Level Precision

- **Overall**: 80.4%
- **Average (per-task)**: 88.8%

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
    "pr": 122,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 155,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 276,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 465,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 475,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 882,
    "test": "N/A",
    "type": "logic",
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
  },
  {
    "pr": 1584,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1780,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  interface: 2
  logic: 3
  spec: 2
  unknown: 5
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1227.7
  completion_k: 4.9
  cache_hit_pct: 96.4
  tool_calls: 30.1
  mcp_calls: 0.0
  other_skill_calls: 1.0
  ordinary_calls: 29.0
  cost_usd: 0.015496
  own_price_cost_usd: 0.336826
  tasks: 35
  resolved: 23
  unresolved: 12
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| ibex-pr-104 | unresolved | 1783.6 | 7.7 | 0.0179 | 96.8 | 45 | 0 | 0 | 45 |
| ibex-pr-1135 | resolved | 2109.9 | 4.3 | 0.0292 | 96.8 | 27 | 0 | 1 | 26 |
| ibex-pr-1141 | unresolved | 3436.8 | 8.7 | 0.0260 | 98.5 | 85 | 0 | 0 | 85 |
| ibex-pr-122 | unresolved | 200.2 | 2.6 | 0.0123 | 84.9 | 9 | 0 | 1 | 8 |
| ibex-pr-1229 | unresolved | 1069.7 | 6.0 | 0.0134 | 94.7 | 38 | 0 | 2 | 36 |
| ibex-pr-1383 | resolved | 424.3 | 2.6 | 0.0080 | 93.7 | 20 | 0 | 1 | 19 |
| ibex-pr-1469 | resolved | 2438.4 | 7.3 | 0.0301 | 97.8 | 46 | 0 | 1 | 45 |
| ibex-pr-1513 | unresolved | 5043.9 | 15.5 | 0.0339 | 98.4 | 68 | 0 | 0 | 68 |
| ibex-pr-155 | unresolved | 980.2 | 5.1 | 0.0138 | 96.2 | 36 | 0 | 0 | 36 |
| ibex-pr-157 | resolved | 1206.5 | 4.2 | 0.0203 | 96.7 | 27 | 0 | 2 | 25 |
| ibex-pr-1584 | unresolved | 491.2 | 3.6 | 0.0088 | 91.4 | 25 | 0 | 1 | 24 |
| ibex-pr-166 | resolved | 474.7 | 5.3 | 0.0077 | 93.8 | 20 | 0 | 1 | 19 |
| ibex-pr-167 | resolved | 2059.0 | 6.2 | 0.0194 | 97.4 | 55 | 0 | 1 | 54 |
| ibex-pr-1735 | resolved | 1848.6 | 5.3 | 0.0199 | 96.4 | 34 | 0 | 1 | 33 |
| ibex-pr-176 | resolved | 360.9 | 2.1 | 0.0054 | 93.5 | 20 | 0 | 1 | 19 |
| ibex-pr-1780 | unresolved | 403.4 | 3.6 | 0.0105 | 89.9 | 20 | 0 | 1 | 19 |
| ibex-pr-1816 | resolved | 1216.5 | 5.3 | 0.0151 | 96.6 | 33 | 0 | 1 | 32 |
| ibex-pr-1865 | resolved | 1237.1 | 4.8 | 0.0145 | 96.2 | 38 | 0 | 2 | 36 |
| ibex-pr-222 | resolved | 887.4 | 4.4 | 0.0159 | 93.4 | 20 | 0 | 2 | 18 |
| ibex-pr-2232 | resolved | 1014.7 | 5.1 | 0.0127 | 95.3 | 33 | 0 | 1 | 32 |
| ibex-pr-244 | resolved | 3276.2 | 9.7 | 0.0363 | 97.6 | 46 | 0 | 2 | 44 |
| ibex-pr-276 | unresolved | 33.8 | 0.4 | 0.0036 | 33.0 | 3 | 0 | 1 | 2 |
| ibex-pr-282 | resolved | 442.9 | 3.1 | 0.0093 | 93.4 | 19 | 0 | 2 | 17 |
| ibex-pr-293 | resolved | 1813.7 | 5.9 | 0.0229 | 97.2 | 38 | 0 | 1 | 37 |
| ibex-pr-332 | resolved | 671.3 | 3.4 | 0.0120 | 95.6 | 23 | 0 | 0 | 23 |
| ibex-pr-377 | resolved | 695.2 | 3.0 | 0.0115 | 94.7 | 17 | 0 | 1 | 16 |
| ibex-pr-45 | resolved | 281.3 | 2.3 | 0.0047 | 93.3 | 20 | 0 | 1 | 19 |
| ibex-pr-465 | unresolved | 168.2 | 3.0 | 0.0060 | 83.6 | 15 | 0 | 1 | 14 |
| ibex-pr-475 | unresolved | 665.7 | 3.8 | 0.0112 | 92.2 | 20 | 0 | 1 | 19 |
| ibex-pr-48 | resolved | 318.1 | 2.8 | 0.0050 | 93.8 | 19 | 0 | 0 | 19 |
| ibex-pr-54 | resolved | 447.9 | 2.8 | 0.0097 | 92.7 | 26 | 0 | 1 | 25 |
| ibex-pr-83 | resolved | 399.8 | 4.1 | 0.0070 | 93.7 | 23 | 0 | 0 | 23 |
| ibex-pr-882 | unresolved | 407.7 | 2.0 | 0.0118 | 89.4 | 13 | 0 | 2 | 11 |
| ibex-pr-907 | resolved | 1896.4 | 6.3 | 0.0290 | 97.6 | 29 | 0 | 2 | 27 |
| ibex-pr-974 | resolved | 2765.8 | 7.5 | 0.0274 | 97.7 | 42 | 0 | 1 | 41 |
