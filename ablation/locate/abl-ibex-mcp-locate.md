# Ibex MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 19
  total: 35
  resolved_rate: 54.3%
  file_level_precision: 80.5%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 19/35 (54.3%) |
| File-Level Precision | 79.2% | 80.5% |

## 未解决 Case

```json
[
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 293, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 377, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 974, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1141, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1469, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1735, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1865, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 3
  logic: 3
  spec: 2
  timing_sync: 1
```
