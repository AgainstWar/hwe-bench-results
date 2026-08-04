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

## File-Level Precision

- **Overall**: 23.1%
- **Average (per-task)**: 20.0%

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1242 | 0.0% | 0/1 |
| pr-1401 | 0.0% | 0/1 |
| pr-1793 | 0.0% | 0/1 |
| pr-2195 | 0.0% | 0/1 |
| pr-2845 | 100.0% | 1/1 |
| pr-4110 | 0.0% | 0/1 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 0.0% | 0/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-5182 | 0.0% | 0/1 |

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
