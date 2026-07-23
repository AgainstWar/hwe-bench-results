# Ibex MCP + All Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  resolved: 27/35 (77%)
mcp_alone:
  resolved: 24/35 (69%)
mcp_all:
  resolved: 23/35 (66%)
```

## MCP + All vs Baseline

| 指标 | Baseline | MCP + All |
|------|:--------:|:---------:|
| 解决 | 27/35 (77%) | 23/35 (66%) |
| 净变化 | | -4 |

### 新解决
  ✅ pr-907: interface
  ✅ pr-974: timing_sync

### 丢失
  ❌ pr-122: logic
  ❌ pr-276: timing_sync
  ❌ pr-465: logic
  ❌ pr-882: logic
  ❌ pr-1584: spec
  ❌ pr-1780: logic

## MCP + All vs MCP alone

| 指标 | MCP alone | MCP + All |
|------|:--------:|:----------:|
| 解决 | 24/35 (69%) | 23/35 (66%) |
| 净变化 | | -1 |

### 相对 MCP 新解决
  ✅ pr-293: interface
  ✅ pr-907: interface
  ✅ pr-1135: config_integ
  ✅ pr-1469: spec
  ✅ pr-1816: spec
  ✅ pr-1865: interface

### 相对 MCP 丢失
  ❌ pr-122: logic
  ❌ pr-276: timing_sync
  ❌ pr-465: logic
  ❌ pr-882: logic
  ❌ pr-1141: interface
  ❌ pr-1584: spec
  ❌ pr-1780: logic

## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +1 | -0 | +1 |
| logic | +0 | -4 | -4 |
| spec | +0 | -1 | -1 |
| timing_sync | +1 | -1 | +0 |

## 未解决 Case

```json
[
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 155, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 475, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 882, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1141, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 2
  logic: 3
  spec: 2
```
