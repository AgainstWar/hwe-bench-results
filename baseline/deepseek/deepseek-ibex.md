# Ibex BASELINE Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 27
  total: 35
  resolved_rate: 77.1%
  file_level_precision: 79.2%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | BASELINE |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 27/35 (77.1%) |
| File-Level Precision | 79.2% | 79.2% |

## 未解决 Case

```json
[
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 155, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 475, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 974, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1141, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 3
  logic: 2
  spec: 2
  timing_sync: 1
```
