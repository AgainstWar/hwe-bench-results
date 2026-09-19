# Caliptra MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 16
  resolved_rate: 75.0%
  file_level_precision: 86.4%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 12/16 (75.0%) |
| File-Level Precision | 90.0% | 86.4% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 0.0% | 0/1 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 1/1 |
| pr-506 | 50.0% | 1/2 |
| pr-594 | 50.0% | 1/2 |
| pr-633 | 100.0% | 2/2 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 100.0% | 2/2 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 86.4%
- **Average (per-task)**: 87.5%

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
    "pr": 633,
    "test": "N/A",
    "type": "logic",
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
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 803.2
  completion_k: 4.2
  cache_hit_pct: 95.0
  tool_calls: 22.8
  mcp_calls: 0.6
  other_skill_calls: 0.0
  ordinary_calls: 22.1
  cost_usd: 0.012190
  own_price_cost_usd: 0.221453
  tasks: 16
  resolved: 12
  unresolved: 4
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| caliptra-rtl-pr-1033 | unresolved | 663.2 | 3.3 | 0.0124 | 93.7 | 22 | 0 | 0 | 22 |
| caliptra-rtl-pr-1073 | resolved | 642.8 | 2.7 | 0.0151 | 91.6 | 15 | 1 | 0 | 14 |
| caliptra-rtl-pr-1089 | resolved | 539.9 | 2.7 | 0.0117 | 93.2 | 14 | 1 | 0 | 13 |
| caliptra-rtl-pr-134 | resolved | 976.9 | 6.7 | 0.0117 | 95.4 | 40 | 0 | 0 | 40 |
| caliptra-rtl-pr-195 | resolved | 227.5 | 2.0 | 0.0069 | 88.2 | 11 | 0 | 0 | 11 |
| caliptra-rtl-pr-252 | resolved | 136.7 | 1.6 | 0.0037 | 87.0 | 8 | 0 | 0 | 8 |
| caliptra-rtl-pr-298 | resolved | 222.2 | 1.9 | 0.0050 | 89.5 | 13 | 1 | 0 | 12 |
| caliptra-rtl-pr-506 | resolved | 694.6 | 3.3 | 0.0117 | 93.5 | 26 | 4 | 0 | 22 |
| caliptra-rtl-pr-594 | resolved | 2279.2 | 16.8 | 0.0239 | 97.5 | 48 | 1 | 0 | 47 |
| caliptra-rtl-pr-633 | unresolved | 463.1 | 3.5 | 0.0086 | 91.9 | 24 | 0 | 0 | 24 |
| caliptra-rtl-pr-70 | unresolved | 2821.1 | 6.1 | 0.0337 | 97.5 | 48 | 0 | 0 | 48 |
| caliptra-rtl-pr-725 | unresolved | 1729.8 | 6.5 | 0.0171 | 96.6 | 34 | 1 | 0 | 33 |
| caliptra-rtl-pr-747 | resolved | 238.7 | 1.8 | 0.0066 | 89.3 | 12 | 1 | 0 | 11 |
| caliptra-rtl-pr-757 | resolved | 444.9 | 3.7 | 0.0108 | 93.1 | 19 | 0 | 0 | 19 |
| caliptra-rtl-pr-786 | resolved | 646.7 | 3.2 | 0.0121 | 91.5 | 23 | 0 | 0 | 23 |
| caliptra-rtl-pr-963 | resolved | 124.6 | 1.0 | 0.0040 | 87.7 | 7 | 0 | 0 | 7 |
