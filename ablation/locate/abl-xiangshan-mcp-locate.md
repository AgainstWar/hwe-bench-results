# Xiangshan MCP+Locate Analysis

## 总体结果

```yaml
baseline:
  resolved: 12/54 (22%)
mcp_alone:
  resolved: 18/54 (33%)
MCP+Locate:
  resolved: 8/54 (15%)
```

## MCP+Locate vs Baseline

| 指标 | Baseline | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 12/54 (22%) | 8/54 (15%) |
| 净变化 | | -4 |
### 新解决
  ✅ pr-1679 (interface)
  ✅ pr-2513 (logic)
  ✅ pr-3717 (spec)
  ✅ pr-5080 (logic)
### 丢失
  ❌ pr-39 (logic)
  ❌ pr-2483 (logic)
  ❌ pr-2845 (timing_sync)
  ❌ pr-3182 (logic)
  ❌ pr-3867 (logic)
  ❌ pr-4337 (logic)
  ❌ pr-4943 (sw_hw_config)
  ❌ pr-4959 (logic)
## MCP+Locate vs MCP alone

| 指标 | MCP alone | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 18/54 (33%) | 8/54 (15%) |
| 净变化 | | -10 |

### 相对 MCP 新解决
  ✅ pr-5080: logic
  ✅ pr-5700: logic
### 相对 MCP 丢失
  ❌ pr-39: logic
  ❌ pr-739: timing_sync
  ❌ pr-1820: sw_hw_config
  ❌ pr-2351: interface
  ❌ pr-2781: interface
  ❌ pr-2845: timing_sync
  ❌ pr-2997: logic
  ❌ pr-3182: logic
  ❌ pr-3555: spec
  ❌ pr-4337: logic
  ❌ pr-4959: logic
  ❌ pr-5182: logic
## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +1 | -0 | +1 |
| logic | +2 | -6 | -4 |
| spec | +1 | -0 | +1 |
| sw_hw_config | +0 | -1 | -1 |
| timing_sync | +0 | -1 | -1 |

## 未解决 Case

```json
[
  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2095, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2997, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3753, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3867, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4166, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4337, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 4533, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4968, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5593, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 4
  logic: 7
  spec: 3
  sw_hw_config: 3
  timing_sync: 4
```
