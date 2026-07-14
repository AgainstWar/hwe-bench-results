# XiangShan Ablation - LOCATE

## 总体结果

```yaml
baseline (no skill):
  resolved: 12
  total: 54
  pct: 22%

locate:
  resolved: 1
  total: 54
  pct: 2%
```

## LOCATE vs Baseline

| 指标 | Baseline | LOCATE |
|------|:--------:|:--------------:|
| 解决 | 12/54 (22%) | 1/54 (2%) |
| 净变化 | | -11 |

### 新解决
  无

### 丢失
  ❌ pr-39: logic
  ❌ pr-281: logic
  ❌ pr-1931: logic
  ❌ pr-2483: logic
  ❌ pr-3182: logic
  ❌ pr-3867: logic
  ❌ pr-4337: logic
  ❌ pr-4764: logic
  ❌ pr-4943: sw_hw_config
  ❌ pr-4959: logic
  ❌ pr-5700: logic

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| logic | +0 | -10 | -10 |
| sw_hw_config | +0 | -1 | -1 |

## 未解决 Case

```json
[
  {"pr": 1242, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1401, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 1793, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},
  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 4337, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 4764, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 5182, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 4
  spec: 1
  sw_hw_config: 1
  timing_sync: 3
```
