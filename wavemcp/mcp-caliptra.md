# Caliptra MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 16
  resolved_rate: 75.0%
  file_level_precision: 86.4%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 12/16 (75.0%) |
| File-Level Precision | 90.0% | 86.4% |

## 未解决 Case

```json
[
  {"pr": 70, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 633, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 725, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1033, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 3
  sw_hw_config: 1
```
