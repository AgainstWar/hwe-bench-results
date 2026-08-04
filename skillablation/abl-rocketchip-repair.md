# RocketChip Ablation - REPAIR

## 总体结果

```yaml
baseline (no skill):
  resolved: 8
  total: 32
  pct: 25%

repair:
  resolved: 13
  total: 32
  pct: 41%
```

## REPAIR vs Baseline

| 指标 | Baseline | REPAIR |
|------|:--------:|:--------------:|
| 解决 | 8/32 (25%) | 13/32 (41%) |
| 净变化 | | +5 |

### 新解决
  ✅ pr-404: logic
  ✅ pr-1093: sw_hw_interact
  ✅ pr-1656: interface
  ✅ pr-2213: interface
  ✅ pr-2368: config_integ
  ✅ pr-3600: timing_sync

### 丢失
  ❌ pr-576: logic

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +1 | -0 | +1 |
| interface | +2 | -0 | +2 |
| logic | +1 | -1 | +0 |
| sw_hw_interact | +1 | -0 | +1 |
| timing_sync | +1 | -0 | +1 |

## 未解决 Case

```json
[
  {"pr": 177, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 387, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 485, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1176, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1878, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2036, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2621, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 3004, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3526, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 3624, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 3
  interface: 3
  logic: 6
  spec: 3
  timing_sync: 3
```

## File-Level Precision

- **Overall**: 76.7%
- **Average (per-task)**: 83.9%

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
| pr-387 | 100.0% | 2/2 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 0.0% | 0/3 |
| pr-542 | 100.0% | 1/1 |
| pr-745 | 100.0% | 1/1 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 1/1 |
| pr-1656 | 100.0% | 4/4 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 0.0% | 0/3 |
| pr-2621 | 100.0% | 2/2 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 100.0% | 1/1 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 50.0% | 1/2 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 50.0% | 1/2 |
| pr-3600 | 100.0% | 1/1 |
| pr-3624 | 100.0% | 1/1 |
| pr-3651 | 100.0% | 1/1 |

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
