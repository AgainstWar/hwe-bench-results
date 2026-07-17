# Rocketchip MCP+Locate Analysis

## 总体结果

```yaml
baseline:
  resolved: 8/32 (25%)
mcp_alone:
  resolved: 12/32 (38%)
MCP+Locate:
  resolved: 7/32 (22%)
```

## MCP+Locate vs Baseline

| 指标 | Baseline | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 8/32 (25%) | 7/32 (22%) |
| 净变化 | | -1 |
### 新解决
  ✅ pr-485 (interface)
  ✅ pr-1878 (spec)
  ✅ pr-3600 (timing_sync)
### 丢失
  ❌ pr-576 (logic)
  ❌ pr-1330 (logic)
  ❌ pr-2984 (logic)
  ❌ pr-3065 (interface)
## MCP+Locate vs MCP alone

| 指标 | MCP alone | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 12/32 (38%) | 7/32 (22%) |
| 净变化 | | -5 |

### 相对 MCP 新解决
  ✅ pr-485: interface
  ✅ pr-3600: timing_sync
### 相对 MCP 丢失
  ❌ pr-404: logic
  ❌ pr-576: logic
  ❌ pr-1093: sw_hw_interact
  ❌ pr-1176: interface
  ❌ pr-1330: logic
  ❌ pr-2213: interface
  ❌ pr-2984: logic
## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +1 | -1 | +0 |
| logic | +0 | -3 | -3 |
| spec | +1 | -0 | +1 |
| timing_sync | +1 | -0 | +1 |

## 未解决 Case

```json
[
  {"pr": 387, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 404, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1093, "test": "N/A", "type": "sw_hw_interact", "desc": "N/A"},  {"pr": 1176, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2036, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2213, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2368, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2621, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 3065, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3526, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 4
  interface: 5
  logic: 6
  spec: 1
  sw_hw_interact: 1
  timing_sync: 2
```
