# Caliptra BASELINE Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 13
  total: 16
  resolved_rate: 81.2%
  file_level_precision: 90.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | BASELINE |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 13/16 (81.2%) |
| File-Level Precision | 90.0% | 90.0% |

## 未解决 Case

```json
[
  {"pr": 70, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 725, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1033, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 2
  sw_hw_config: 1
```
