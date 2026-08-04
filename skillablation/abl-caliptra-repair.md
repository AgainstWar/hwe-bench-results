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

## File-Level Precision

- **Overall**: 90.0%
- **Average (per-task)**: 93.3%

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 1/1 |
| pr-506 | 50.0% | 1/2 |
| pr-594 | 100.0% | 1/1 |
| pr-633 | 100.0% | 2/2 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 50.0% | 1/2 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 16
  status: resolved=13 unresolved=3
  prompt_k: (K)
  completion_k: (K)
  cache_hit_pct: (%)
  tool_calls: 29.5
  cost_usd: 0.2274
```
