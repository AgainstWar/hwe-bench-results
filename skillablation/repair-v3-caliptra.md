# Caliptra Repair V3 Analysis

## 总体结果

```yaml
repair_v3:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (revised, hdl-minimal-repair)
  resolved: 16
  total: 16
  resolved_rate: 100.0%
  file_level_precision: 91.67%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V3 |
|------|:-----------:|:---------:|
| Resolved Rate | 15/16 (93.8%) | 16/16 (100.0%) |
| File-Level Precision | 93.33% | 91.67% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 100.0% | 1/1 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 3/3 |
| pr-506 | 100.0% | 1/1 |
| pr-594 | 100.0% | 1/1 |
| pr-633 | 100.0% | 1/1 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 60.0% | 3/5 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 91.7%
- **Average (per-task)**: 97.5%

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 5548.0
  completion_k: 36.3
  cache_hit_pct: 0.0
  tool_calls: 58.2
  mcp_calls: 0.0
  repair_skill_calls: 1.5
  ordinary_calls: 56.7
  cost_usd: 0.054203
  tasks: 16
  resolved: 16
  unresolved: 0
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| caliptra-rtl-pr-70__rEuj4ZE | resolved | 6484.0 | 38.7 | 0.0626 | 98.2 | 87 | 0 | 2 | 85 |
| caliptra-rtl-pr-134__LsEGBNq | resolved | 878.2 | 11.6 | 0.0165 | 94.8 | 42 | 0 | 2 | 40 |
| caliptra-rtl-pr-195__ZJzgcmk | resolved | 2132.5 | 5.7 | 0.0324 | 96.5 | 44 | 0 | 2 | 42 |
| caliptra-rtl-pr-252__eeqoyJq | resolved | 5118.6 | 52.1 | 0.0688 | 97.3 | 66 | 0 | 2 | 64 |
| caliptra-rtl-pr-298__HKspKw6 | resolved | 5708.0 | 71.1 | 0.0827 | 97.9 | 72 | 0 | 1 | 71 |
| caliptra-rtl-pr-506__iBYoj9C | resolved | 4115.9 | 35.9 | 0.0473 | 97.8 | 75 | 0 | 1 | 74 |
| caliptra-rtl-pr-594__JPmgjh6 | resolved | 735.9 | 4.1 | 0.0152 | 95.9 | 32 | 0 | 1 | 31 |
| caliptra-rtl-pr-633__AioPMkt | resolved | 486.5 | 10.7 | 0.0138 | 92.7 | 25 | 0 | 2 | 23 |
| caliptra-rtl-pr-725__P6jscNM | resolved | 1498.0 | 10.6 | 0.0290 | 93.1 | 36 | 0 | 2 | 34 |
| caliptra-rtl-pr-747__JERnMJg | resolved | 744.8 | 22.0 | 0.0235 | 93.8 | 32 | 0 | 1 | 31 |
| caliptra-rtl-pr-757__kYF4ynt | resolved | 857.5 | 14.6 | 0.0251 | 92.4 | 31 | 0 | 1 | 30 |
| caliptra-rtl-pr-786__prpGohX | resolved | 3647.4 | 27.5 | 0.0453 | 97.1 | 65 | 0 | 2 | 63 |
| caliptra-rtl-pr-963__zsPJquL | resolved | 1997.3 | 31.2 | 0.0322 | 97.6 | 50 | 0 | 1 | 49 |
| caliptra-rtl-pr-1033__vU9oVvj | resolved | 52267.6 | 224.2 | 0.3246 | 99.6 | 212 | 0 | 1 | 211 |
| caliptra-rtl-pr-1073__FN7W8aN | resolved | 1134.5 | 5.7 | 0.0284 | 90.2 | 34 | 0 | 1 | 33 |
| caliptra-rtl-pr-1089__iqNENFQ | resolved | 960.8 | 14.9 | 0.0197 | 94.4 | 28 | 0 | 2 | 26 |

