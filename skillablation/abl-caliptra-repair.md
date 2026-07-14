# Caliptra Ablation - REPAIR

## 总体结果

```yaml
baseline (no skill):
  resolved: 13
  total: 16
  pct: 81%

repair:
  resolved: 13
  total: 16
  pct: 81%
```

## REPAIR vs Baseline

| 指标 | Baseline | REPAIR |
|------|:--------:|:--------------:|
| 解决 | 13/16 (81%) | 13/16 (81%) |
| 净变化 | | +0 |

### 新解决
  ✅ pr-725: logic
  ✅ pr-1033: sw_hw_config

### 丢失
  ❌ pr-195: logic
  ❌ pr-757: timing_sync

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| logic | +1 | -1 | +0 |
| sw_hw_config | +1 | -0 | +1 |
| timing_sync | +0 | -1 | -1 |

## 未解决 Case

```json
[
  {"pr": 195, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 757, "test": "N/A", "type": "timing_sync", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 1
  timing_sync: 1
```
