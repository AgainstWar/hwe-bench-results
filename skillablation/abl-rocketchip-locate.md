# RocketChip Ablation - LOCATE

## 总体结果

```yaml
baseline (no skill):
  resolved: 8
  total: 32
  pct: 25%

locate:
  resolved: 2
  total: 32
  pct: 6%
```

## LOCATE vs Baseline

| 指标 | Baseline | LOCATE |
|------|:--------:|:--------------:|
| 解决 | 8/32 (25%) | 2/32 (6%) |
| 净变化 | | -6 |

### 新解决
  无

### 丢失
  ❌ pr-576: logic
  ❌ pr-1069: logic
  ❌ pr-1330: logic
  ❌ pr-2984: logic
  ❌ pr-2988: logic
  ❌ pr-2994: logic

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| logic | +0 | -6 | -6 |

## 未解决 Case

```json
[
  {"pr": 177, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1330, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2368, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 2621, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  interface: 2
  logic: 3
```
