# Caliptra MCP+Repair Analysis

## 总体结果

```yaml
baseline:
  resolved: 13/16 (81%)
mcp_alone:
  resolved: 12/16 (75%)
MCP+Repair:
  resolved: 11/16 (69%)
```

## MCP+Repair vs Baseline

| 指标 | Baseline | MCP+Repair |
|------|:--------:|:-------:|
| 解决 | 13/16 (81%) | 11/16 (69%) |
| 净变化 | | -2 |
### 新解决
  无

### 丢失
  ❌ pr-594 (logic)
  ❌ pr-633 (logic)
## MCP+Repair vs MCP alone

| 指标 | MCP alone | MCP+Repair |
|------|:--------:|:-------:|
| 解决 | 12/16 (75%) | 11/16 (69%) |
| 净变化 | | -1 |

### 相对 MCP 新解决
  无

### 相对 MCP 丢失
  ❌ pr-594: logic
## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| logic | +0 | -2 | -2 |

## 未解决 Case

```json
[
  {"pr": 70, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 594, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 725, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1033, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 3
  sw_hw_config: 1
```
