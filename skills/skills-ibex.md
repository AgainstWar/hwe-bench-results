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
