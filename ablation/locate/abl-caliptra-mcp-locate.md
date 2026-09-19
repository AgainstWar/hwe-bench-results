# Caliptra MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 16
  resolved_rate: 50.0%
  file_level_precision: 100.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 8/16 (50.0%) |
| File-Level Precision | 90.0% | 100.0% |

### 新解决
  pr-725

### 丢失
  pr-298, pr-633, pr-757, pr-786, pr-1073, pr-1089

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-506 | 100.0% | 1/1 |
| pr-594 | 100.0% | 1/1 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 100.0%
- **Average (per-task)**: 100.0%

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
    "pr": 298,
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
    "pr": 757,
    "test": "N/A",
    "type": "timing_sync",
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
  timing_sync: 1
  unknown: 7
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 451.8
  completion_k: 3.2
  cache_hit_pct: 91.1
  tool_calls: 15.9
  mcp_calls: 0.0
  other_skill_calls: 0.9
  ordinary_calls: 15.0
  cost_usd: 0.010459
  own_price_cost_usd: 0.125553
  tasks: 16
  resolved: 8
  unresolved: 8
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| caliptra-rtl-pr-1033 | unresolved | 336.1 | 3.9 | 0.0151 | 76.5 | 11 | 0 | 1 | 10 |
| caliptra-rtl-pr-1073 | unresolved | 97.7 | 2.2 | 0.0080 | 63.8 | 4 | 0 | 1 | 3 |
| caliptra-rtl-pr-1089 | unresolved | 102.2 | 1.9 | 0.0085 | 64.5 | 4 | 0 | 1 | 3 |
| caliptra-rtl-pr-134 | resolved | 720.0 | 6.4 | 0.0102 | 94.6 | 40 | 0 | 0 | 40 |
| caliptra-rtl-pr-195 | resolved | 755.0 | 3.8 | 0.0132 | 93.1 | 20 | 0 | 1 | 19 |
| caliptra-rtl-pr-252 | resolved | 128.2 | 1.5 | 0.0041 | 85.9 | 7 | 0 | 0 | 7 |
| caliptra-rtl-pr-298 | unresolved | 342.1 | 3.1 | 0.0084 | 89.7 | 14 | 0 | 1 | 13 |
| caliptra-rtl-pr-506 | resolved | 973.6 | 4.2 | 0.0157 | 94.7 | 20 | 0 | 1 | 19 |
| caliptra-rtl-pr-594 | resolved | 270.4 | 2.9 | 0.0075 | 89.9 | 20 | 0 | 1 | 19 |
| caliptra-rtl-pr-633 | unresolved | 643.4 | 4.1 | 0.0095 | 94.0 | 25 | 0 | 1 | 24 |
| caliptra-rtl-pr-70 | unresolved | 905.8 | 4.2 | 0.0208 | 93.6 | 27 | 0 | 1 | 26 |
| caliptra-rtl-pr-725 | resolved | 195.8 | 2.0 | 0.0057 | 87.0 | 10 | 0 | 1 | 9 |
| caliptra-rtl-pr-747 | resolved | 389.3 | 3.0 | 0.0077 | 92.9 | 15 | 0 | 1 | 14 |
| caliptra-rtl-pr-757 | unresolved | 1017.4 | 4.4 | 0.0167 | 96.3 | 20 | 0 | 1 | 19 |
| caliptra-rtl-pr-786 | unresolved | 120.8 | 2.0 | 0.0090 | 61.9 | 6 | 0 | 1 | 5 |
| caliptra-rtl-pr-963 | resolved | 231.4 | 2.3 | 0.0072 | 84.9 | 11 | 0 | 1 | 10 |
