# Ibex MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 19
  total: 35
  resolved_rate: 54.3%
  file_level_precision: 80.5%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 19/35 (54.3%) |
| File-Level Precision | 79.2% | 80.5% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 2/2 |
| pr-104 | 100.0% | 3/3 |
| pr-122 | 100.0% | 1/1 |
| pr-155 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 0.0% | 0/1 |
| pr-974 | 0.0% | 0/1 |
| pr-1141 | 50.0% | 1/2 |
| pr-1229 | 100.0% | 2/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 100.0% | 2/2 |
| pr-1513 | 40.0% | 2/5 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 33.3% | 1/3 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 1/1 |
| pr-2232 | 100.0% | 2/2 |

## 未解决 Case

```json
[
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 293, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 377, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 974, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1141, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1469, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1735, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1865, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 3
  logic: 3
  spec: 2
  timing_sync: 1
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 32
  status: resolved=7 unresolved=25
  prompt_k: 895.0
  completion_k: 3.7
  cache_hit_pct: 95.8
  tool_calls: 25.5
  cost_usd: 0.013533
```
