# Ibex Ablation - LOCATE

## 总体结果

```yaml
baseline (no skill):
  resolved: 27
  total: 35
  pct: 77%

locate:
  resolved: 7
  total: 35
  pct: 20%
```

## LOCATE vs Baseline

| 指标 | Baseline | LOCATE |
|------|:--------:|:--------------:|
| 解决 | 27/35 (77%) | 7/35 (20%) |
| 净变化 | | -20 |

### 新解决
  无

### 丢失
  ❌ pr-45: logic
  ❌ pr-48: logic
  ❌ pr-83: logic
  ❌ pr-157: logic
  ❌ pr-167: logic
  ❌ pr-176: logic
  ❌ pr-222: logic
  ❌ pr-276: timing_sync
  ❌ pr-282: logic
  ❌ pr-293: interface
  ❌ pr-332: spec
  ❌ pr-377: logic
  ❌ pr-465: logic
  ❌ pr-882: logic
  ❌ pr-1135: config_integ
  ❌ pr-1469: spec
  ❌ pr-1584: spec
  ❌ pr-1780: logic
  ❌ pr-1865: interface
  ❌ pr-2232: interface

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +0 | -1 | -1 |
| interface | +0 | -3 | -3 |
| logic | +0 | -12 | -12 |
| spec | +0 | -3 | -3 |
| timing_sync | +0 | -1 | -1 |

## 未解决 Case

```json
[
  {"pr": 83, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 293, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 882, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 2
  logic: 2
  spec: 1
```
