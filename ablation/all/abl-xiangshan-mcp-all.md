# XiangShan MCP + All Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  resolved: 12/54 (22%)
mcp_alone:
  resolved: 18/54 (33%)
mcp_all:
  resolved: 25/54 (46%)
```

## MCP + All vs Baseline

| 指标 | Baseline | MCP + All |
|------|:--------:|:---------:|
| 解决 | 12/54 (22%) | 25/54 (46%) |
| 净变化 | | +13 |

### 新解决
  ✅ pr-739: timing_sync
  ✅ pr-1679: interface
  ✅ pr-1820: sw_hw_config
  ✅ pr-2095: logic
  ✅ pr-2351: interface
  ✅ pr-2997: logic
  ✅ pr-3329: interface
  ✅ pr-3555: spec
  ✅ pr-3717: spec
  ✅ pr-3859: spec
  ✅ pr-3955: interface
  ✅ pr-4166: interface
  ✅ pr-4426: interface
  ✅ pr-4533: interface
  ✅ pr-5182: logic
  ✅ pr-5593: interface

### 丢失
  ❌ pr-4943: sw_hw_config
  ❌ pr-4959: logic
  ❌ pr-5700: logic

## MCP + All vs MCP alone

| 指标 | MCP alone | MCP + All |
|------|:--------:|:----------:|
| 解决 | 18/54 (33%) | 25/54 (46%) |
| 净变化 | | +7 |

### 相对 MCP 新解决
  ✅ pr-2095: logic
  ✅ pr-2483: logic
  ✅ pr-3329: interface
  ✅ pr-3859: spec
  ✅ pr-3867: logic
  ✅ pr-3955: interface
  ✅ pr-4166: interface
  ✅ pr-4426: interface
  ✅ pr-4533: interface
  ✅ pr-5593: interface

### 相对 MCP 丢失
  ❌ pr-2513: logic
  ❌ pr-2781: interface
  ❌ pr-4959: logic

## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +8 | -0 | +8 |
| logic | +3 | -2 | +1 |
| spec | +3 | -0 | +3 |
| sw_hw_config | +1 | -1 | +0 |
| timing_sync | +1 | -0 | +1 |

## 未解决 Case

```json
[
  {"pr": 655, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1242, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1323, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 1395, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1401, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 1694, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1793, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2246, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 2513, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2781, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 4442, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 4959, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 4968, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 5700, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 3
  logic: 10
  spec: 3
  sw_hw_config: 3
  timing_sync: 5
```
