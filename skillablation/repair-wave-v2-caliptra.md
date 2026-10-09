# Caliptra Repair+Wave V2 Analysis

## 总体结果

```yaml
repair_wave_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair + wave (hdl-minimal-repair / wave)
  mcp: WAVES (WAVES_ENABLED=true)
  resolved: 15
  total: 16
  resolved_rate: 93.8%
  file_level_precision: 100.00%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair+Wave V2 |
|------|:-----------:|:--------------:|
| Resolved Rate | 15/16 (93.8%) | 15/16 (93.8%) |
| File-Level Precision | 93.33% | 100.00% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 100.0% | 1/1 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 7/7 |
| pr-506 | 100.0% | 5/5 |
| pr-594 | 100.0% | 1/1 |
| pr-633 | 100.0% | 4/4 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 100.0% | 4/4 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 100.0%
- **Average (per-task)**: 100.0%

## 未解决 Case

| PR |
|----|
| pr-594 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 2506.4
  completion_k: 6.2
  cache_hit_pct: 97.0
  tool_calls: 45.9
  mcp_calls: 0.0
  repair_skill_calls: 1.4
  wave_skill_calls: 0.1
  ordinary_calls: 44.4
  cost_usd: 0.030740
  tasks: 16
  resolved: 15
  unresolved: 1
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Wave Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|------------|----------|
| caliptra-rtl-pr-70__fMTwYr8 | resolved | 2329.5 | 5.6 | 0.0320 | 96.4 | 47 | 0 | 1 | 2 | 44 |
| caliptra-rtl-pr-134__XcA8nap | resolved | 1559.6 | 5.9 | 0.0244 | 94.2 | 47 | 0 | 2 | 0 | 45 |
| caliptra-rtl-pr-195__AkZPk5i | resolved | 5959.0 | 9.6 | 0.0543 | 98.1 | 62 | 0 | 1 | 0 | 61 |
| caliptra-rtl-pr-252__v9MMDY7 | resolved | 3682.9 | 10.1 | 0.0417 | 97.5 | 63 | 0 | 2 | 0 | 61 |
| caliptra-rtl-pr-298__DrSceh9 | resolved | 1576.7 | 8.2 | 0.0231 | 96.2 | 60 | 0 | 2 | 0 | 58 |
| caliptra-rtl-pr-506__GfEGotS | resolved | 3021.1 | 9.2 | 0.0384 | 97.2 | 66 | 0 | 1 | 0 | 65 |
| caliptra-rtl-pr-594__Bvz57DU | unresolved | 409.3 | 3.8 | 0.0102 | 94.3 | 18 | 0 | 1 | 0 | 17 |
| caliptra-rtl-pr-633__Cfgs9gn | resolved | 1959.8 | 5.8 | 0.0280 | 96.0 | 46 | 0 | 1 | 0 | 45 |
| caliptra-rtl-pr-725__n6JA3QD | resolved | 2300.7 | 5.7 | 0.0316 | 96.4 | 46 | 0 | 1 | 0 | 45 |
| caliptra-rtl-pr-747__NEZYdbL | resolved | 255.7 | 2.0 | 0.0092 | 89.2 | 15 | 0 | 1 | 0 | 14 |
| caliptra-rtl-pr-757__xYKWkMM | resolved | 879.7 | 4.3 | 0.0192 | 95.5 | 27 | 0 | 1 | 0 | 26 |
| caliptra-rtl-pr-786__BkiBzjU | resolved | 986.0 | 3.6 | 0.0186 | 93.7 | 32 | 0 | 2 | 0 | 30 |
| caliptra-rtl-pr-963__9q7aAL8 | resolved | 3196.9 | 5.9 | 0.0407 | 97.6 | 59 | 0 | 2 | 0 | 57 |
| caliptra-rtl-pr-1033__wePns5K | resolved | 9184.3 | 12.0 | 0.0769 | 98.3 | 80 | 0 | 0 | 0 | 80 |
| caliptra-rtl-pr-1073__KcyKtYb | resolved | 1273.7 | 3.5 | 0.0200 | 94.2 | 33 | 0 | 2 | 0 | 31 |
| caliptra-rtl-pr-1089__eTZydq5 | resolved | 1527.3 | 4.1 | 0.0236 | 95.5 | 33 | 0 | 2 | 0 | 31 |

