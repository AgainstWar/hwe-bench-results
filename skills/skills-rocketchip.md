# RocketChip SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 9
  total: 32
  resolved_rate: 28.1%
  file_level_precision: 73.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 9/32 (28.1%) |
| File-Level Precision | 87.0% | 73.7% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
| pr-387 | 100.0% | 1/1 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 0.0% | 0/3 |
| pr-542 | 100.0% | 1/1 |
| pr-576 | 100.0% | 1/1 |
| pr-745 | 0.0% | 0/1 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 1/1 |
| pr-1656 | 100.0% | 2/2 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/3 |
| pr-2368 | 50.0% | 1/2 |
| pr-2543 | 0.0% | 0/1 |
| pr-2621 | 100.0% | 3/3 |
| pr-2988 | 100.0% | 1/1 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 100.0% | 1/1 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3600 | 100.0% | 1/1 |
| pr-3624 | 100.0% | 1/1 |
| pr-3651 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 177, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 387, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 485, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 576, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2036, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2213, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2368, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3004, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3065, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3600, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3624, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 3
  interface: 5
  logic: 6
  spec: 2
  timing_sync: 4
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 32
  status: resolved=9 unresolved=23
  prompt_k: 985.4
  completion_k: 4.0
  cache_hit_pct: 96.2
  tool_calls: 27.9
  cost_usd: 0.013785
```
