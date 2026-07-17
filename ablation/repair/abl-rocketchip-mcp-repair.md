# Rocketchip MCP+Repair Analysis

## 总体结果

```yaml
baseline:
  resolved: 8/32 (25%)
mcp_alone:
  resolved: 12/32 (38%)
MCP+Repair:
  resolved: 12/32 (38%)
```

## MCP+Repair vs Baseline

| 指标 | Baseline | MCP+Repair |
|------|:--------:|:-------:|
| 解决 | 8/32 (25%) | 12/32 (38%) |
| 净变化 | | +4 |
### 新解决
  ✅ pr-177 (logic)
  ✅ pr-404 (logic)
  ✅ pr-1878 (spec)
  ✅ pr-2213 (interface)
  ✅ pr-2368 (config_integ)
  ✅ pr-2621 (config_integ)
### 丢失
  ❌ pr-576 (logic)
  ❌ pr-1069 (logic)
## MCP+Repair vs MCP alone

| 指标 | MCP alone | MCP+Repair |
|------|:--------:|:-------:|
| 解决 | 12/32 (38%) | 12/32 (38%) |
| 净变化 | | +0 |

### 相对 MCP 新解决
  ✅ pr-177: logic
  ✅ pr-2368: config_integ
  ✅ pr-2621: config_integ
  ✅ pr-3065: interface
### 相对 MCP 丢失
  ❌ pr-576: logic
  ❌ pr-1069: logic
  ❌ pr-1093: sw_hw_interact
  ❌ pr-1176: interface
## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +2 | -0 | +2 |
| interface | +1 | -0 | +1 |
| logic | +2 | -2 | +0 |
| spec | +1 | -0 | +1 |

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
