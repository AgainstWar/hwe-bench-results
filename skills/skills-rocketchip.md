# RocketChip Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 32
  pct: 25%
  infra_errors: 0

skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skills: locate + repair
  resolved: 9
  total: 32
  pct: 28%
  infra_errors: 0
```

## Skills vs Baseline

| 指标 | Baseline | Skills |
|------|:--------:|:------:|
| 解决 | 8/32 (25%) | 9/32 (28%) |
| 净变化 | | +1 |
| 基础设施错误 | 0 | 0 |

### 新解决
  ✅ pr-404: logic
  ✅ pr-1093: sw_hw_interact
  ✅ pr-1176: interface
  ✅ pr-1878: spec
  ✅ pr-2621: config_integ

### 丢失
  ❌ pr-576: logic
  ❌ pr-1330: logic
  ❌ pr-2984: logic
  ❌ pr-3065: interface

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +1 | -0 | +1 |
| interface | +1 | -1 | +0 |
| logic | +1 | -3 | -2 |
| spec | +1 | -0 | +1 |
| sw_hw_interact | +1 | -0 | +1 |

## 未解决 Case

```json
[
  {"pr": 177, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 387, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 485, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 576, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2036, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 2213, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2368, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3004, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 3065, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3600, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 3624, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 3
  interface: 5
  logic: 6
  spec: 2
  timing_sync: 4
```

## 结论

Skills 在该项目上正收益。 基础设施错误为 0。
