# XiangShan SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 16
  total: 54
  resolved_rate: 29.6%
  file_level_precision: 71.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 16/54 (29.6%) |
| File-Level Precision | 89.7% | 71.7% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-1242 | 0.0% | 0/1 |
| pr-1323 | 50.0% | 1/2 |
| pr-1401 | 33.3% | 1/3 |
| pr-1602 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 0.0% | 0/1 |
| pr-2095 | 0.0% | 0/1 |
| pr-2195 | 50.0% | 1/2 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 0.0% | 0/1 |
| pr-2483 | 100.0% | 1/1 |
| pr-2513 | 100.0% | 1/1 |
| pr-2781 | 100.0% | 1/1 |
| pr-2845 | 0.0% | 0/1 |
| pr-2997 | 100.0% | 1/1 |
| pr-3182 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3329 | 0.0% | 0/1 |
| pr-3555 | 100.0% | 1/1 |
| pr-3636 | 66.7% | 2/3 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 100.0% | 5/5 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 100.0% | 1/1 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4426 | 100.0% | 1/1 |
| pr-4533 | 0.0% | 0/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 2/2 |
| pr-5182 | 50.0% | 1/2 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 0.0% | 0/1 |
| pr-5700 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 1242, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1323, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1401, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1679, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1694, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1931, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2095, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2246, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2351, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2781, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2845, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3329, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3753, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3867, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4166, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4442, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4533, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 5700, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 8
  logic: 10
  spec: 4
  sw_hw_config: 3
  timing_sync: 5
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=54
  prompt_k: 992.9
  completion_k: 4.3
  cache_hit_pct: 95.4
  tool_calls: 25.9
  cost_usd: 0.015380
```
