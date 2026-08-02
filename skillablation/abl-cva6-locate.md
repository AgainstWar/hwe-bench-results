# CVA6 Ablation - LOCATE

## 总体结果

```yaml
baseline (no skill):
  resolved: 28
  total: 35
  pct: 80%

locate:
  resolved: 11
  total: 35
  pct: 31%
```

## LOCATE vs Baseline

| 指标 | Baseline | LOCATE |
|------|:--------:|:--------------:|
| 解决 | 28/35 (80%) | 11/35 (31%) |
| 净变化 | | -17 |

### 新解决
  ✅ pr-2989: spec

### 丢失
  ❌ pr-1482: logic
  ❌ pr-2032: logic
  ❌ pr-2248: logic
  ❌ pr-2282: logic
  ❌ pr-2330: logic
  ❌ pr-2468: logic
  ❌ pr-2469: logic
  ❌ pr-2476: logic
  ❌ pr-2549: logic
  ❌ pr-2685: logic
  ❌ pr-2711: spec
  ❌ pr-2916: interface
  ❌ pr-2944: logic
  ❌ pr-2945: logic
  ❌ pr-3168: logic
  ❌ pr-3171: logic
  ❌ pr-3204: logic
  ❌ pr-3226: logic

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +0 | -1 | -1 |
| logic | +0 | -16 | -16 |
| spec | +1 | -1 | +0 |

## 未解决 Case

```json
[
  {"pr": 2032, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2170, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 2420, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 2711, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  logic: 1
  spec: 1
```

## File-Level Precision

- **Overall**: 54.5%
- **Average (per-task)**: 67.6%

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 0.0% | 0/1 |
| pr-2170 | 0.0% | 0/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 0.0% | 0/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2711 | 0.0% | 0/1 |
| pr-2728 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3059 | 100.0% | 1/1 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3231 | 100.0% | 1/1 |

