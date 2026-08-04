# XiangShan MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 25
  total: 54
  resolved_rate: 46.3%
  file_level_precision: 80.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 25/54 (46.3%) |
| File-Level Precision | 89.7% | 80.7% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 1/1 |
| pr-739 | 100.0% | 1/1 |
| pr-1242 | 25.0% | 1/4 |
| pr-1323 | 50.0% | 1/2 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 0.0% | 0/1 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 33.3% | 1/3 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 4/4 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 50.0% | 1/2 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 100.0% | 1/1 |
| pr-2483 | 100.0% | 1/1 |
| pr-2513 | 100.0% | 1/1 |
| pr-2781 | 100.0% | 1/1 |
| pr-2845 | 100.0% | 1/1 |
| pr-2997 | 100.0% | 1/1 |
| pr-3182 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3329 | 100.0% | 1/1 |
| pr-3555 | 100.0% | 1/1 |
| pr-3636 | 100.0% | 1/1 |
| pr-3717 | 100.0% | 1/1 |
| pr-3859 | 71.4% | 5/7 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 100.0% | 1/1 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 50.0% | 1/2 |
| pr-4764 | 25.0% | 1/4 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 90.0% | 9/10 |
| pr-5182 | 50.0% | 1/2 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 50.0% | 1/2 |

## 未解决 Case

```json
[
  {"pr": 655, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1242, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1323, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1395, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1401, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1694, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1793, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2246, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2781, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4442, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4959, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 4968, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 5700, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 3
  logic: 10
  spec: 3
  sw_hw_config: 3
  timing_sync: 5
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
