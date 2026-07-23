# RocketChip MCP + All Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  resolved: 8/32 (25%)
mcp_alone:
  resolved: 12/32 (38%)
mcp_all:
  resolved: 6/32 (19%)
```

## MCP + All vs Baseline

| 指标 | Baseline | MCP + All |
|------|:--------:|:---------:|
| 解决 | 8/32 (25%) | 6/32 (19%) |
| 净变化 | | -2 |

### 新解决
  ✅ pr-404: logic

### 丢失
  ❌ pr-576: logic
  ❌ pr-2984: logic
  ❌ pr-2988: logic

## MCP + All vs MCP alone

| 指标 | MCP alone | MCP + All |
|------|:--------:|:----------:|
| 解决 | 12/32 (38%) | 6/32 (19%) |
| 净变化 | | -6 |

### 相对 MCP 新解决
  ✅ pr-3065: interface

### 相对 MCP 丢失
  ❌ pr-576: logic
  ❌ pr-1093: sw_hw_interact
  ❌ pr-1176: interface
  ❌ pr-1878: spec
  ❌ pr-2213: interface
  ❌ pr-2984: logic
  ❌ pr-2988: logic

## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| logic | +1 | -3 | -2 |

## 未解决 Case

```json
[
  {"pr": 177, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 485, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 576, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1093, "test": "N/A", "type": "sw_hw_interact", "desc": "N/A"},
  {"pr": 1176, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1878, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 2213, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2368, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2621, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3600, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 4
  interface: 5
  logic: 5
  spec: 2
  sw_hw_interact: 1
  timing_sync: 2
```
