# Caliptra Baseline (DeepSeek V4 Flash) Analysis

## 总体结果

```yaml
deepseek:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 13
  total: 16
  resolved_rate: 81.2%
  file_level_precision: 90.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | DEEPSEEK |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 13/16 (81.2%) |
| File-Level Precision | 90.0% | 90.0% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 0.0% | 0/1 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 1/1 |
| pr-506 | 100.0% | 1/1 |
| pr-594 | 100.0% | 1/1 |
| pr-633 | 100.0% | 2/2 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 50.0% | 1/2 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 100.0% | 1/1 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 90.0%
- **Average (per-task)**: 90.6%

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
  logic: 2
  sw_hw_config: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 456.7
  completion_k: 11.7
  cache_hit_pct: 96.0
  tool_calls: 19.6
  mcp_calls: 0.0
  skill_calls: 0.0
  ordinary_calls: 19.6
  cost_usd: 0.000000
  own_price_cost_usd: 0.136154
  tasks: 16
  resolved: 13
  unresolved: 3
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| caliptra-rtl-pr-1033 | unresolved | 529.1 | 11.1 | 0.0000 | 95.9 | 29 | 0 | 0 | 29 |
| caliptra-rtl-pr-1073 | resolved | 1000.7 | 19.4 | 0.0000 | 97.1 | 34 | 0 | 0 | 34 |
| caliptra-rtl-pr-1089 | resolved | 951.2 | 17.1 | 0.0000 | 97.4 | 28 | 0 | 0 | 28 |
| caliptra-rtl-pr-134 | resolved | 1121.4 | 19.5 | 0.0000 | 96.9 | 49 | 0 | 0 | 49 |
| caliptra-rtl-pr-195 | resolved | 279.2 | 8.7 | 0.0000 | 93.0 | 14 | 0 | 0 | 14 |
| caliptra-rtl-pr-252 | resolved | 114.3 | 4.4 | 0.0000 | 93.3 | 8 | 0 | 0 | 8 |
| caliptra-rtl-pr-298 | resolved | 201.0 | 5.0 | 0.0000 | 95.4 | 12 | 0 | 0 | 12 |
| caliptra-rtl-pr-506 | resolved | 320.5 | 5.2 | 0.0000 | 95.0 | 20 | 0 | 0 | 20 |
| caliptra-rtl-pr-594 | resolved | 223.6 | 5.8 | 0.0000 | 95.3 | 18 | 0 | 0 | 18 |
| caliptra-rtl-pr-633 | resolved | 318.4 | 8.6 | 0.0000 | 94.4 | 21 | 0 | 0 | 21 |
| caliptra-rtl-pr-70 | unresolved | 1395.6 | 39.4 | 0.0000 | 97.5 | 32 | 0 | 0 | 32 |
| caliptra-rtl-pr-725 | unresolved | 290.3 | 9.9 | 0.0000 | 89.7 | 8 | 0 | 0 | 8 |
| caliptra-rtl-pr-747 | resolved | 84.5 | 4.4 | 0.0000 | 93.7 | 8 | 0 | 0 | 8 |
| caliptra-rtl-pr-757 | resolved | 102.3 | 12.3 | 0.0000 | 92.7 | 5 | 0 | 0 | 5 |
| caliptra-rtl-pr-786 | resolved | 152.2 | 4.4 | 0.0000 | 94.1 | 14 | 0 | 0 | 14 |
| caliptra-rtl-pr-963 | resolved | 222.2 | 11.8 | 0.0000 | 93.0 | 14 | 0 | 0 | 14 |
