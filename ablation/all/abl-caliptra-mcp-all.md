# Caliptra MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 16
  resolved_rate: 50.0%
  file_level_precision: 78.6%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 8/16 (50.0%) |
| File-Level Precision | 90.0% | 78.6% |

### 新解决
  无

### 丢失
  pr-298, pr-506, pr-594, pr-1073, pr-1089

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 0.0% | 0/1 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-506 | 33.3% | 1/3 |
| pr-633 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 78.6%
- **Average (per-task)**: 83.3%

## 未解决 Case

```json
[
  {
    "pr": 70,
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
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 594,
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
  interface: 1
  logic: 1
  unknown: 6
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 591.4
  completion_k: 3.0
  cache_hit_pct: 93.1
  tool_calls: 17.1
  mcp_calls: 0.0
  other_skill_calls: 0.8
  ordinary_calls: 16.3
  cost_usd: 0.012533
  own_price_cost_usd: 0.162962
  tasks: 16
  resolved: 8
  unresolved: 8
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| caliptra-rtl-pr-1033 | unresolved | 674.5 | 3.1 | 0.0135 | 90.2 | 19 | 0 | 1 | 18 |
| caliptra-rtl-pr-1073 | unresolved | 66.6 | 0.5 | 0.0139 | 50.4 | 3 | 0 | 0 | 3 |
| caliptra-rtl-pr-1089 | unresolved | 160.9 | 1.9 | 0.0104 | 80.1 | 5 | 0 | 1 | 4 |
| caliptra-rtl-pr-134 | resolved | 538.4 | 5.4 | 0.0074 | 94.9 | 31 | 0 | 0 | 31 |
| caliptra-rtl-pr-195 | resolved | 772.0 | 3.6 | 0.0133 | 95.0 | 16 | 0 | 1 | 15 |
| caliptra-rtl-pr-252 | resolved | 332.4 | 2.2 | 0.0076 | 90.2 | 14 | 0 | 1 | 13 |
| caliptra-rtl-pr-298 | unresolved | 191.9 | 3.0 | 0.0062 | 85.5 | 10 | 0 | 1 | 9 |
| caliptra-rtl-pr-506 | unresolved | 1381.8 | 6.3 | 0.0182 | 95.9 | 41 | 0 | 2 | 39 |
| caliptra-rtl-pr-594 | unresolved | 21.7 | 0.1 | 0.0016 | 50.1 | 2 | 0 | 0 | 2 |
| caliptra-rtl-pr-633 | resolved | 558.7 | 3.1 | 0.0105 | 93.2 | 19 | 0 | 1 | 18 |
| caliptra-rtl-pr-70 | unresolved | 2343.5 | 4.7 | 0.0378 | 96.6 | 33 | 0 | 1 | 32 |
| caliptra-rtl-pr-725 | unresolved | 430.1 | 2.4 | 0.0136 | 83.0 | 13 | 0 | 1 | 12 |
| caliptra-rtl-pr-747 | resolved | 126.7 | 1.1 | 0.0061 | 84.1 | 6 | 0 | 0 | 6 |
| caliptra-rtl-pr-757 | resolved | 1143.2 | 5.6 | 0.0211 | 95.4 | 31 | 0 | 1 | 30 |
| caliptra-rtl-pr-786 | resolved | 329.1 | 2.7 | 0.0070 | 89.8 | 16 | 0 | 1 | 15 |
| caliptra-rtl-pr-963 | resolved | 391.3 | 1.9 | 0.0123 | 92.1 | 15 | 0 | 1 | 14 |
