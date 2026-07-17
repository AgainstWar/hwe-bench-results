# Ibex MCP+Repair Analysis

## 总体结果

```yaml
baseline:
  resolved: 27/35 (77%)
mcp_alone:
  resolved: 24/35 (69%)
MCP+Repair:
  resolved: 23/35 (66%)
```

## MCP+Repair vs Baseline

| 指标 | Baseline | MCP+Repair |
|------|:--------:|:-------:|
| 解决 | 27/35 (77%) | 23/35 (66%) |
| 净变化 | | -4 |
### 新解决
  ✅ pr-475 (spec)
  ✅ pr-974 (timing_sync)
  ✅ pr-1141 (interface)
### 丢失
  ❌ pr-176 (logic)
  ❌ pr-293 (interface)
  ❌ pr-332 (spec)
  ❌ pr-882 (logic)
  ❌ pr-1135 (config_integ)
  ❌ pr-1469 (spec)
  ❌ pr-1584 (spec)
## MCP+Repair vs MCP alone

| 指标 | MCP alone | MCP+Repair |
|------|:--------:|:-------:|
| 解决 | 24/35 (69%) | 23/35 (66%) |
| 净变化 | | -1 |

### 相对 MCP 新解决
  ✅ pr-475: spec
  ✅ pr-1816: spec
  ✅ pr-1865: interface
### 相对 MCP 丢失
  ❌ pr-176: logic
  ❌ pr-332: spec
  ❌ pr-882: logic
  ❌ pr-1584: spec
## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +0 | -1 | -1 |
| interface | +1 | -1 | +0 |
| logic | +0 | -2 | -2 |
| spec | +1 | -3 | -2 |
| timing_sync | +1 | -0 | +1 |

## 未解决 Case

```json
[
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 155, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 882, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1135, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1584, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 2
  logic: 3
  spec: 2
```
