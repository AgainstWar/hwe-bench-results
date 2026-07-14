# Caliptra Ablation - LOCATE

## 总体结果

```yaml
baseline (no skill):
  resolved: 13
  total: 16
  pct: 81%

locate:
  resolved: 3
  total: 16
  pct: 19%
```

## LOCATE vs Baseline

| 指标 | Baseline | LOCATE |
|------|:--------:|:--------------:|
| 解决 | 13/16 (81%) | 3/16 (19%) |
| 净变化 | | -10 |

### 新解决
  无

### 丢失
  ❌ pr-195: logic
  ❌ pr-298: logic
  ❌ pr-506: interface
  ❌ pr-594: logic
  ❌ pr-633: logic
  ❌ pr-747: logic
  ❌ pr-757: timing_sync
  ❌ pr-786: logic
  ❌ pr-1073: logic
  ❌ pr-1089: logic

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +0 | -1 | -1 |
| logic | +0 | -8 | -8 |
| timing_sync | +0 | -1 | -1 |

## 未解决 Case

```json
[
  {"pr": 195, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 1
```
