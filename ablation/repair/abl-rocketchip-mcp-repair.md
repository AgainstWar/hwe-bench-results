# RocketChip MCP+REPAIR Analysis

## 总体结果

```yaml
mcp+repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 32
  resolved_rate: 37.5%
  file_level_precision: 89.1%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 12/32 (37.5%) |
| File-Level Precision | 87.0% | 89.1% |

## 未解决 Case

```json
[
  {"pr": 387, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 485, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 576, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1069, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1093, "test": "N/A", "type": "sw_hw_interact", "desc": "N/A"},  {"pr": 1176, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2036, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3004, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3526, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3600, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3624, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  interface: 4
  logic: 7
  spec: 2
  sw_hw_interact: 1
  timing_sync: 4
```
