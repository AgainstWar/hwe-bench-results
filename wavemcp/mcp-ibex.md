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

## 未解决 Case

```json
[
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 155, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 293, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 475, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1135, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1469, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1816, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1865, "test": "N/A", "type": "interface", "desc": "N/A"}
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

```yaml
token_statistics:
  tasks: 38
  status: resolved=27 unresolved=11
  prompt_k: 1167.7
  completion_k: 4.0
  cache_hit_pct: 96.5
  tool_calls: 26.1
  cost_usd: 0.016043
```
