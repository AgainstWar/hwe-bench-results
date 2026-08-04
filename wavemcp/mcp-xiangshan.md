# XiangShan MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 18
  total: 54
  resolved_rate: 33.3%
  file_level_precision: 87.6%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 18/54 (33.3%) |
| File-Level Precision | 89.7% | 87.6% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 1/1 |
| pr-739 | 33.3% | 1/3 |
| pr-1242 | 100.0% | 6/6 |
| pr-1323 | 100.0% | 1/1 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 100.0% | 1/1 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 1/1 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2195 | 50.0% | 1/2 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 100.0% | 2/2 |
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
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 71.4% | 5/7 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 50.0% | 1/2 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 3/3 |
| pr-5182 | 50.0% | 1/2 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 655, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1242, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1323, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1395, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1401, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1694, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1793, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2095, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2246, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2483, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3329, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3753, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3859, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3867, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3955, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4166, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4426, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4442, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4533, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4968, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 5189, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5593, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 5700, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 8
  logic: 12
  spec: 5
  sw_hw_config: 3
  timing_sync: 6
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=54
  prompt_k: 1086.4
  completion_k: 4.1
  cache_hit_pct: 96.4
  tool_calls: 28.7
  cost_usd: 0.014134
```
