# XiangShan Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 54
  pct: 22%
  infra_errors: 0

skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skills: locate + repair
  resolved: 16
  total: 54
  pct: 30%
  infra_errors: 0
```

## Skills vs Baseline

| 指标 | Baseline | Skills |
|------|:--------:|:------:|
| 解决 | 12/54 (22%) | 16/54 (30%) |
| 净变化 | | +4 |
| 基础设施错误 | 0 | 0 |

### 新解决
  ✅ pr-1820: sw_hw_config
  ✅ pr-2997: logic
  ✅ pr-3555: spec
  ✅ pr-3717: spec
  ✅ pr-3859: spec
  ✅ pr-3955: interface
  ✅ pr-4426: interface
  ✅ pr-4968: timing_sync
  ✅ pr-5182: logic
  ✅ pr-5593: interface

### 丢失
  ❌ pr-1931: logic
  ❌ pr-2845: timing_sync
  ❌ pr-3867: logic
  ❌ pr-4337: logic
  ❌ pr-4943: sw_hw_config
  ❌ pr-5700: logic

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +3 | -0 | +3 |
| logic | +2 | -4 | -2 |
| spec | +3 | -0 | +3 |
| sw_hw_config | +1 | -1 | +0 |
| timing_sync | +1 | -1 | +0 |

## 未解决 Case

```json
[
  {"pr": 1242, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1323, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 1401, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 1679, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1694, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1931, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2095, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 2246, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 2351, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2513, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2781, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2845, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 3329, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3753, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 3867, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 4166, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 4442, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 4533, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 5700, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 8
  logic: 10
  spec: 4
  sw_hw_config: 3
  timing_sync: 5
```

## 结论

Skills 在该项目上正收益。 基础设施错误为 0。
