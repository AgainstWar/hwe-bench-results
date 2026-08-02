# CVA6 SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 25
  total: 35
  resolved_rate: 71.4%
  file_level_precision: 74.6%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 25/35 (71.4%) |
| File-Level Precision | 79.0% | 74.6% |

## 未解决 Case

```json
[
  {"pr": 2170, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2420, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2711, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2916, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 3
  interface: 1
  spec: 2
```
