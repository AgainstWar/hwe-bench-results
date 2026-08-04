# RocketChip MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 6
  total: 32
  resolved_rate: 18.8%
  file_level_precision: 55.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 6/32 (18.8%) |
| File-Level Precision | 87.0% | 55.7% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
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
| pr-1656 | 16.7% | 4/24 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 25.0% | 1/4 |
| pr-2621 | 100.0% | 3/3 |
| pr-2994 | 100.0% | 1/1 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3600 | 100.0% | 1/1 |
| pr-3651 | 33.3% | 1/3 |

## 未解决 Case

```json
[
  {"pr": 177, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 485, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 576, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1093, "test": "N/A", "type": "sw_hw_interact", "desc": "N/A"},  {"pr": 1176, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1878, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2213, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2368, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2621, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3600, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 4
  interface: 5
  logic: 5
  spec: 2
  sw_hw_interact: 1
  timing_sync: 2
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 32
  status: resolved=6 unresolved=26
  prompt_k: 816.6
  completion_k: 3.8
  cache_hit_pct: 95.5
  tool_calls: 25.4
  cost_usd: 0.012653
```
