# XiangShan MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 54
  resolved_rate: 14.8%
  file_level_precision: 80.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 8/54 (14.8%) |
| File-Level Precision | 89.7% | 80.0% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-281 | 100.0% | 1/1 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 100.0% | 1/1 |
| pr-1907 | 0.0% | 0/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2195 | 100.0% | 1/1 |
| pr-2513 | 100.0% | 1/1 |
| pr-2997 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3636 | 100.0% | 1/1 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 0.0% | 0/1 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-4110 | 50.0% | 1/2 |
| pr-4166 | 60.0% | 3/5 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 0.0% | 0/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4943 | 100.0% | 6/6 |
| pr-4968 | 88.9% | 8/9 |
| pr-5080 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2095, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2997, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3753, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3867, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4166, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4337, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 4533, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4968, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5593, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 4
  logic: 7
  spec: 3
  sw_hw_config: 3
  timing_sync: 4
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
