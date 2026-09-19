# Caliptra Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 16
  total: 16
  resolved_rate: 100.0%
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 16
  total: 16
  resolved_rate: 100.0%
  file_level_precision: 59.0%
  infra_errors: 0
```

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 50.0% | 1/2 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 50.0% | 1/2 |
| pr-252 | 33.3% | 1/3 |
| pr-298 | 100.0% | 3/3 |
| pr-506 | 66.7% | 2/3 |
| pr-594 | 25.0% | 1/4 |
| pr-633 | 75.0% | 3/4 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 25.0% | 1/4 |
| pr-786 | 50.0% | 1/2 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 25.0% | 1/4 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 59.0%
- **Average (per-task)**: 68.8%

## 未解决 Case

```json
[]
```

## Bug 类型分布

```yaml
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 2170.0
  completion_k: 6.8
  cache_hit_pct: 94.5
  tool_calls: 58.2
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 58.2
  cost_usd: 1.102473
  own_price_cost_usd: 2.780646
  tasks: 16
  resolved: 16
  unresolved: 0
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| caliptra-rtl-pr-1033 | resolved | 6279.5 | 13.4 | 2.7814 | 96.3 | 92 | 0 | 0 | 92 |
| caliptra-rtl-pr-1073 | resolved | 2765.2 | 9.7 | 1.2893 | 95.4 | 64 | 0 | 0 | 64 |
| caliptra-rtl-pr-1089 | resolved | 1346.2 | 6.1 | 0.7684 | 93.2 | 42 | 0 | 0 | 42 |
| caliptra-rtl-pr-134 | resolved | 1395.2 | 5.3 | 0.7544 | 92.3 | 61 | 0 | 0 | 61 |
| caliptra-rtl-pr-195 | resolved | 1323.1 | 4.3 | 0.7449 | 92.3 | 44 | 0 | 0 | 44 |
| caliptra-rtl-pr-252 | resolved | 3272.8 | 8.6 | 1.5613 | 94.8 | 68 | 0 | 0 | 68 |
| caliptra-rtl-pr-298 | resolved | 724.3 | 3.7 | 0.4511 | 94.0 | 42 | 0 | 0 | 42 |
| caliptra-rtl-pr-506 | resolved | 1843.7 | 6.9 | 1.0692 | 94.1 | 70 | 0 | 0 | 70 |
| caliptra-rtl-pr-594 | resolved | 773.5 | 6.9 | 0.5850 | 93.7 | 41 | 0 | 0 | 41 |
| caliptra-rtl-pr-633 | resolved | 2164.3 | 8.0 | 1.3075 | 90.8 | 67 | 0 | 0 | 67 |
| caliptra-rtl-pr-70 | resolved | 6633.3 | 10.7 | 2.8875 | 95.2 | 97 | 0 | 0 | 97 |
| caliptra-rtl-pr-725 | resolved | 1205.5 | 4.5 | 0.6701 | 93.5 | 40 | 0 | 0 | 40 |
| caliptra-rtl-pr-747 | resolved | 649.8 | 5.2 | 0.4587 | 93.8 | 45 | 0 | 0 | 45 |
| caliptra-rtl-pr-757 | resolved | 1410.8 | 6.6 | 0.8120 | 94.4 | 49 | 0 | 0 | 49 |
| caliptra-rtl-pr-786 | resolved | 2177.1 | 6.0 | 1.0598 | 94.5 | 65 | 0 | 0 | 65 |
| caliptra-rtl-pr-963 | resolved | 755.4 | 3.2 | 0.4387 | 93.3 | 44 | 0 | 0 | 44 |
