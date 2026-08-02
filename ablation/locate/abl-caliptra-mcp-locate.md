# Caliptra MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 16
  resolved_rate: 50.0%
  file_level_precision: 100.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 8/16 (50.0%) |
| File-Level Precision | 90.0% | 100.0% |

## 未解决 Case

```json
[
  {"pr": 757, "test": "N/A", "type": "timing_sync", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  timing_sync: 1
```
