# CVA6 MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 27
  total: 35
  resolved_rate: 77.1%
  file_level_precision: 81.5%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 27/35 (77.1%) |
| File-Level Precision | 79.0% | 81.5% |

## 未解决 Case

```json
[
  {"pr": 2032, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2844, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  logic: 1
  spec: 2
```
