# CVA6 Ablation - REPAIR

## 总体结果

```yaml
baseline (no skill):
  resolved: 28
  total: 35
  pct: 80%

repair:
  resolved: 31
  total: 35
  pct: 89%
```

## REPAIR vs Baseline

| 指标 | Baseline | REPAIR |
|------|:--------:|:--------------:|
| 解决 | 28/35 (80%) | 31/35 (89%) |
| 净变化 | | +3 |

### 新解决
  ✅ pr-2170: config_integ
  ✅ pr-2279: interface
  ✅ pr-2420: config_integ
  ✅ pr-2989: spec

### 丢失
  ❌ pr-3231: spec

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +2 | -0 | +2 |
| interface | +1 | -0 | +1 |
| spec | +1 | -1 | +0 |

## 未解决 Case

```json
[
  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 2844, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 3231, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  spec: 3
```
