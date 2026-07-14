# RocketChip Ablation - REPAIR

## 总体结果

```yaml
baseline (no skill):
  resolved: 8
  total: 32
  pct: 25%

repair:
  resolved: 13
  total: 32
  pct: 41%
```

## REPAIR vs Baseline

| 指标 | Baseline | REPAIR |
|------|:--------:|:--------------:|
| 解决 | 8/32 (25%) | 13/32 (41%) |
| 净变化 | | +5 |

### 新解决
  ✅ pr-404: logic
  ✅ pr-1093: sw_hw_interact
  ✅ pr-1656: interface
  ✅ pr-2213: interface
  ✅ pr-2368: config_integ
  ✅ pr-3600: timing_sync

### 丢失
  ❌ pr-576: logic

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +1 | -0 | +1 |
| interface | +2 | -0 | +2 |
| logic | +1 | -1 | +0 |
| sw_hw_interact | +1 | -0 | +1 |
| timing_sync | +1 | -0 | +1 |

## 未解决 Case

```json
[
  {"pr": 177, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 387, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 485, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1176, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1878, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2036, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2621, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 3004, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3526, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3624, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 3
  interface: 3
  logic: 6
  spec: 3
  timing_sync: 3
```
