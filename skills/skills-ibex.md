# Ibex SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 21
  total: 35
  resolved_rate: 60.0%
  file_level_precision: 84.9%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 21/35 (60.0%) |
| File-Level Precision | 79.2% | 84.9% |


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
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 4/4 |
| pr-475 | 0.0% | 0/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 1/1 |
| pr-974 | 100.0% | 2/2 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 100.0% | 2/2 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 60.0% | 3/5 |
| pr-1513 | 40.0% | 2/5 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 0.0% | 0/1 |
| pr-1865 | 100.0% | 2/2 |
| pr-2232 | 100.0% | 2/2 |

## 未解决 Case

```json
[
  {"pr": 83, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 155, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 293, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 332, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 475, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 882, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1469, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1816, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2232, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 4
  logic: 4
  spec: 5
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 35
  status: resolved=21 unresolved=14
  prompt_k: 1361.3
  completion_k: 5.3
  cache_hit_pct: 96.7
  tool_calls: 31.6
  cost_usd: 0.016751
```
