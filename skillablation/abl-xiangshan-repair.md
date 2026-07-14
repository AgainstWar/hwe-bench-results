# XiangShan Ablation - REPAIR

## 总体结果

```yaml
baseline (no skill):
  resolved: 12
  total: 54
  pct: 22%

repair:
  resolved: 19
  total: 54
  pct: 35%
```

## REPAIR vs Baseline

| 指标 | Baseline | REPAIR |
|------|:--------:|:--------------:|
| 解决 | 12/54 (22%) | 19/54 (35%) |
| 净变化 | | +7 |

### 新解决
  ✅ pr-739: timing_sync
  ✅ pr-1679: interface
  ✅ pr-2095: logic
  ✅ pr-2513: logic
  ✅ pr-2781: interface
  ✅ pr-3555: spec
  ✅ pr-3717: spec
  ✅ pr-3859: spec
  ✅ pr-3907: spec
  ✅ pr-4968: timing_sync
  ✅ pr-5080: logic
  ✅ pr-5593: interface

### 丢失
  ❌ pr-1931: logic
  ❌ pr-3867: logic
  ❌ pr-4337: logic
  ❌ pr-4943: sw_hw_config
  ❌ pr-5700: logic

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +3 | -0 | +3 |
| logic | +3 | -4 | -1 |
| spec | +4 | -0 | +4 |
| sw_hw_config | +0 | -1 | -1 |
| timing_sync | +2 | -0 | +2 |

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
  {"pr": 1820, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1931, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 2246, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 2351, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 3329, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3753, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 3867, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3955, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 4166, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 4337, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 4426, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 4442, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 4533, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 5182, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 5189, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 5700, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 8
  logic: 13
  spec: 3
  sw_hw_config: 4
  timing_sync: 5
```
