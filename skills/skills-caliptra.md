# Caliptra SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 11
  total: 16
  resolved_rate: 68.8%
  file_level_precision: 76.2%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 11/16 (68.8%) |
| File-Level Precision | 90.0% | 76.2% |

## 未解决 Case

```json
[
  {"pr": 725, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 757, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1033, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 1
  sw_hw_config: 1
  timing_sync: 1
```
