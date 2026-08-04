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

## File-Level Precision

- **Overall**: 87.5%
- **Average (per-task)**: 95.1%

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 50.0% | 1/2 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 100.0% | 1/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 96.4% | 27/28 |
| pr-2282 | 100.0% | 1/1 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 100.0% | 1/1 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2685 | 100.0% | 1/1 |
| pr-2711 | 100.0% | 1/1 |
| pr-2728 | 100.0% | 1/1 |
| pr-2802 | 100.0% | 1/1 |
| pr-2844 | 100.0% | 1/1 |
| pr-2916 | 100.0% | 1/1 |
| pr-2944 | 100.0% | 1/1 |
| pr-2945 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3042 | 100.0% | 1/1 |
| pr-3059 | 100.0% | 1/1 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3168 | 100.0% | 1/1 |
| pr-3171 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3204 | 100.0% | 1/1 |
| pr-3226 | 66.7% | 2/3 |
| pr-3231 | 100.0% | 1/1 |

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=54
  prompt_k: 1311.4
  completion_k: 5.2
  cache_hit_pct: 96.6
  tool_calls: 33.0
  cost_usd: 0.016408
```
