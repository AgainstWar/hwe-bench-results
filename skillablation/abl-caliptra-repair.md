# Caliptra Ablation - REPAIR

## 总体结果

```yaml
repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 13
  total: 16
  resolved_rate: 81.2%
  file_level_precision: 90.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 13/16 (81.2%) |
| File-Level Precision | 90.0% | 90.0% |

### 新解决
  pr-725, pr-1033

### 丢失
  pr-195, pr-757

## Task 级 File-Level Precision

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

## File-Level Precision

- **Overall**: 90.0%
- **Average (per-task)**: 93.3%

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
    "pr": 757,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  logic: 1
  timing_sync: 1
  unknown: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1050.5
  completion_k: 5.0
  cache_hit_pct: 95.7
  tool_calls: 29.5
  mcp_calls: 0.0
  skill_calls: 1.0
  ordinary_calls: 28.5
  cost_usd: 0.014214
  own_price_cost_usd: 0.289177
  tasks: 16
  resolved: 13
  unresolved: 3
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| caliptra-rtl-pr-1033 | resolved | 3712.3 | 13.2 | 0.0287 | 98.0 | 72 | 0 | 1 | 71 |
| caliptra-rtl-pr-1073 | resolved | 1435.5 | 5.0 | 0.0192 | 95.3 | 27 | 0 | 1 | 26 |
| caliptra-rtl-pr-1089 | resolved | 740.7 | 3.9 | 0.0139 | 94.1 | 22 | 0 | 1 | 21 |
| caliptra-rtl-pr-134 | resolved | 707.8 | 5.5 | 0.0137 | 90.7 | 31 | 0 | 1 | 30 |
| caliptra-rtl-pr-195 | unresolved | 657.7 | 3.8 | 0.0122 | 93.0 | 21 | 0 | 1 | 20 |
| caliptra-rtl-pr-252 | resolved | 620.5 | 4.1 | 0.0093 | 93.9 | 22 | 0 | 1 | 21 |
| caliptra-rtl-pr-298 | resolved | 518.2 | 4.1 | 0.0099 | 92.9 | 20 | 0 | 1 | 19 |
| caliptra-rtl-pr-506 | resolved | 1042.8 | 4.9 | 0.0170 | 95.9 | 27 | 0 | 1 | 26 |
| caliptra-rtl-pr-594 | resolved | 746.0 | 4.0 | 0.0109 | 95.3 | 32 | 0 | 1 | 31 |
| caliptra-rtl-pr-633 | resolved | 770.7 | 4.7 | 0.0104 | 95.5 | 34 | 0 | 1 | 33 |
| caliptra-rtl-pr-70 | unresolved | 19.7 | 0.2 | 0.0020 | 39.0 | 1 | 0 | 1 | 0 |
| caliptra-rtl-pr-725 | resolved | 859.5 | 6.2 | 0.0123 | 95.2 | 29 | 0 | 1 | 28 |
| caliptra-rtl-pr-747 | resolved | 345.3 | 2.9 | 0.0077 | 91.5 | 17 | 0 | 1 | 16 |
| caliptra-rtl-pr-757 | unresolved | 1079.8 | 5.0 | 0.0161 | 96.7 | 29 | 0 | 1 | 28 |
| caliptra-rtl-pr-786 | resolved | 2113.1 | 8.3 | 0.0233 | 96.7 | 53 | 0 | 1 | 52 |
| caliptra-rtl-pr-963 | resolved | 1438.4 | 4.8 | 0.0208 | 96.8 | 35 | 0 | 1 | 34 |
