# Ibex Ablation - REPAIR

## 总体结果

```yaml
baseline (no skill):
  resolved: 27
  total: 35
  pct: 77%

repair:
  resolved: 25
  total: 35
  pct: 71%
```

## REPAIR vs Baseline

| 指标 | Baseline | REPAIR |
|------|:--------:|:--------------:|
| 解决 | 27/35 (77%) | 25/35 (71%) |
| 净变化 | | -2 |

### 新解决
  ✅ pr-475: spec
  ✅ pr-1141: interface

### 丢失
  ❌ pr-54: logic
  ❌ pr-332: spec
  ❌ pr-882: logic
  ❌ pr-1135: config_integ

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +0 | -1 | -1 |
| interface | +1 | -0 | +1 |
| logic | +0 | -2 | -2 |
| spec | +1 | -1 | +0 |

## 未解决 Case

```json
[
  {"pr": 54, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 332, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 974, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 1135, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 2
  logic: 2
  spec: 2
  timing_sync: 1
```
