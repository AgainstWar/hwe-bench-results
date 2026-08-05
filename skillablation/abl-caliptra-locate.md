# Caliptra Ablation - LOCATE

## 总体结果

```yaml
locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 3
  total: 16
  resolved_rate: 18.8%
  file_level_precision: 83.3%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 3/16 (18.8%) |
| File-Level Precision | 90.0% | 83.3% |

### 新解决
  无

### 丢失
  pr-195, pr-298, pr-506, pr-594, pr-633, pr-747, pr-757, pr-786, pr-1073, pr-1089

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-134 | 100.0% | 3/3 |
| pr-195 | 0.0% | 0/1 |
| pr-252 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 83.3%
- **Average (per-task)**: 75.0%

## 未解决 Case

```json
[
  {
    "pr": 70,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 195,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 298,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 506,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 594,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 633,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 725,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 747,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 757,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 786,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1033,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1073,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1089,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  logic: 1
  unknown: 12
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 370.3
  completion_k: 3.0
  cache_hit_pct: 89.0
  tool_calls: 13.2
  cost_usd: 0.010577
  own_price_cost_usd: 0.103265
  tasks: 16
  resolved: 3
  unresolved: 13
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| caliptra-rtl-pr-1033 | unresolved | 407.5 | 2.9 | 0.0134 | 80.8 | 12 |
| caliptra-rtl-pr-1073 | unresolved | 144.9 | 2.3 | 0.0079 | 74.6 | 5 |
| caliptra-rtl-pr-1089 | unresolved | 115.0 | 1.8 | 0.0082 | 72.6 | 4 |
| caliptra-rtl-pr-134 | resolved | 1284.3 | 7.4 | 0.0134 | 96.4 | 48 |
| caliptra-rtl-pr-195 | unresolved | 535.1 | 4.5 | 0.0139 | 91.5 | 18 |
| caliptra-rtl-pr-252 | resolved | 306.7 | 2.7 | 0.0109 | 85.1 | 12 |
| caliptra-rtl-pr-298 | unresolved | 75.2 | 2.0 | 0.0055 | 70.2 | 5 |
| caliptra-rtl-pr-506 | unresolved | 374.1 | 3.1 | 0.0075 | 92.1 | 16 |
| caliptra-rtl-pr-594 | unresolved | 99.7 | 2.0 | 0.0052 | 81.1 | 8 |
| caliptra-rtl-pr-633 | unresolved | 243.3 | 3.3 | 0.0073 | 86.0 | 15 |
| caliptra-rtl-pr-70 | unresolved | 1379.4 | 5.2 | 0.0298 | 95.4 | 31 |
| caliptra-rtl-pr-725 | unresolved | 189.7 | 2.4 | 0.0086 | 74.4 | 7 |
| caliptra-rtl-pr-747 | unresolved | 102.6 | 1.7 | 0.0060 | 77.6 | 6 |
| caliptra-rtl-pr-757 | unresolved | 174.4 | 2.5 | 0.0082 | 79.5 | 8 |
| caliptra-rtl-pr-786 | unresolved | 150.0 | 2.0 | 0.0104 | 62.9 | 6 |
| caliptra-rtl-pr-963 | resolved | 342.1 | 2.0 | 0.0129 | 89.9 | 11 |
