# RocketChip BASELINE Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 32
  resolved_rate: 25.0%
  file_level_precision: 87.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | BASELINE |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 8/32 (25.0%) |
| File-Level Precision | 87.0% | 87.0% |

## 未解决 Case

```json
[
  {"pr": 177, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 387, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 404, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 485, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1093, "test": "N/A", "type": "sw_hw_interact", "desc": "N/A"},  {"pr": 1176, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1878, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2036, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2213, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2368, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2621, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 3004, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3526, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3600, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3624, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 4
  interface: 5
  logic: 7
  spec: 3
  sw_hw_interact: 1
  timing_sync: 4
```
