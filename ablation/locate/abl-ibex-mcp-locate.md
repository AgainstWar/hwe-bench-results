# Ibex MCP+Locate Analysis

## 总体结果

```yaml
baseline:
  resolved: 27/35 (77%)
mcp_alone:
  resolved: 24/35 (69%)
MCP+Locate:
  resolved: 19/35 (54%)
```

## MCP+Locate vs Baseline

| 指标 | Baseline | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 27/35 (77%) | 19/35 (54%) |
| 净变化 | | -8 |
### 新解决
  ✅ pr-155 (logic)
  ✅ pr-1229 (interface)
### 丢失
  ❌ pr-222 (logic)
  ❌ pr-293 (interface)
  ❌ pr-377 (logic)
  ❌ pr-465 (logic)
  ❌ pr-882 (logic)
  ❌ pr-1135 (config_integ)
  ❌ pr-1469 (spec)
  ❌ pr-1584 (spec)
  ❌ pr-1735 (logic)
  ❌ pr-1865 (interface)
## MCP+Locate vs MCP alone

| 指标 | MCP alone | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 24/35 (69%) | 19/35 (54%) |
| 净变化 | | -5 |

### 相对 MCP 新解决
  ✅ pr-155: logic
  ✅ pr-1229: interface
  ✅ pr-1816: spec
### 相对 MCP 丢失
  ❌ pr-222: logic
  ❌ pr-377: logic
  ❌ pr-465: logic
  ❌ pr-882: logic
  ❌ pr-974: timing_sync
  ❌ pr-1141: interface
  ❌ pr-1584: spec
  ❌ pr-1735: logic
## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +0 | -1 | -1 |
| interface | +1 | -2 | -1 |
| logic | +1 | -5 | -4 |
| spec | +0 | -2 | -2 |

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
