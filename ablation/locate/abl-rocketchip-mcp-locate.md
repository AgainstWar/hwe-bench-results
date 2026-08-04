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

## 未解决 Case

```json
[
  {"pr": 387, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 404, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1093, "test": "N/A", "type": "sw_hw_interact", "desc": "N/A"},  {"pr": 1176, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2036, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2213, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2368, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2621, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 3065, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3526, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
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
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=52 error=2
  prompt_k: 797.0
  completion_k: 3.7
  cache_hit_pct: 94.5
  tool_calls: 22.5
  cost_usd: 0.013089
```
