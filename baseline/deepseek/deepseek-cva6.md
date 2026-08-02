# CVA6 BASELINE Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 28
  total: 35
  resolved_rate: 80.0%
  file_level_precision: 79.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | BASELINE |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 28/35 (80.0%) |
| File-Level Precision | 79.0% | 79.0% |

## 未解决 Case

```json
[
  {"pr": 2279, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2420, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2844, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2989, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  interface: 1
  spec: 3
```
