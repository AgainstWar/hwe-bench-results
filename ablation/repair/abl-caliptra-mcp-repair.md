# Caliptra MCP+REPAIR Analysis

## 总体结果

```yaml
mcp+repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 11
  total: 16
  resolved_rate: 68.8%
  file_level_precision: 14.4%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 11/16 (68.8%) |
| File-Level Precision | 90.0% | 14.4% |

### 新解决
  无

### 丢失
  pr-594, pr-633

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 0.0% | 0/39 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 1/1 |
| pr-506 | 100.0% | 1/1 |
| pr-594 | 50.0% | 1/2 |
| pr-725 | 1.8% | 1/56 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 100.0% | 1/1 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 14.4%
- **Average (per-task)**: 83.5%

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
    "pr": 594,
    "test": "N/A",
    "type": "logic",
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
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1033,
    "test": "N/A",
    "type": "sw_hw_config",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  logic: 3
  sw_hw_config: 1
  unknown: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 929.3
  completion_k: 4.1
  cache_hit_pct: 95.8
  tool_calls: 25.2
  cost_usd: 0.013006
  own_price_cost_usd: 0.255400
  tasks: 16
  resolved: 11
  unresolved: 5
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| caliptra-rtl-pr-1033 | unresolved | 1068.3 | 5.3 | 0.0136 | 95.1 | 28 |
| caliptra-rtl-pr-1073 | resolved | 962.8 | 4.0 | 0.0180 | 94.7 | 24 |
| caliptra-rtl-pr-1089 | resolved | 2761.8 | 7.2 | 0.0261 | 98.0 | 47 |
| caliptra-rtl-pr-134 | resolved | 1226.8 | 7.8 | 0.0133 | 96.6 | 45 |
| caliptra-rtl-pr-195 | resolved | 861.1 | 5.1 | 0.0122 | 96.1 | 27 |
| caliptra-rtl-pr-252 | resolved | 241.0 | 2.6 | 0.0068 | 87.8 | 14 |
| caliptra-rtl-pr-298 | resolved | 500.2 | 3.9 | 0.0088 | 92.4 | 25 |
| caliptra-rtl-pr-506 | resolved | 771.4 | 3.8 | 0.0118 | 94.7 | 28 |
| caliptra-rtl-pr-594 | unresolved | 466.1 | 3.9 | 0.0082 | 93.8 | 19 |
| caliptra-rtl-pr-633 | unresolved | 135.1 | 1.0 | 0.0067 | 76.8 | 8 |
| caliptra-rtl-pr-70 | unresolved | 3242.1 | 6.6 | 0.0331 | 98.0 | 52 |
| caliptra-rtl-pr-725 | unresolved | 537.4 | 3.0 | 0.0101 | 94.7 | 18 |
| caliptra-rtl-pr-747 | resolved | 432.7 | 2.7 | 0.0077 | 92.8 | 16 |
| caliptra-rtl-pr-757 | resolved | 725.1 | 3.7 | 0.0124 | 95.7 | 24 |
| caliptra-rtl-pr-786 | resolved | 119.9 | 1.2 | 0.0069 | 76.5 | 4 |
| caliptra-rtl-pr-963 | resolved | 817.3 | 3.5 | 0.0123 | 95.2 | 25 |
