# Caliptra MCP V2 Analysis

## 总体结果

```yaml
mcp_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES (WAVES_ENABLED=true, no skills)
  resolved: 14
  total: 14
  resolved_rate: 100.0%
  file_level_precision: 96.15%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | MCP V2 |
|------|:-----------:|:------:|
| Resolved Rate | 15/16 (93.8%) | 14/14 (100.0%) |
| File-Level Precision | 93.33% | 96.15% |

## 未完成 Trial（无 verifier 输出，未进入评估）

| PR | Trial |
|----|-------|
| pr-70 | caliptra-rtl-pr-70__wAESsk5 |
| pr-786 | caliptra-rtl-pr-786__6f8QrGK |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 5/5 |
| pr-506 | 100.0% | 1/1 |
| pr-594 | 50.0% | 1/2 |
| pr-633 | 100.0% | 3/3 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 100.0% | 4/4 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 96.2%
- **Average (per-task)**: 96.4%

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 4240.2
  completion_k: 40.2
  cache_hit_pct: 97.9
  tool_calls: 62.3
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 62.3
  cost_usd: 0.049825
  tasks: 14
  resolved: 14
  unresolved: 0
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------------|----------|
| caliptra-rtl-pr-134__KFdgPbA | resolved | 717.9 | 10.2 | 0.0130 | 95.5 | 40 | 0 | 0 | 40 |
| caliptra-rtl-pr-195__iKLEKBF | resolved | 6875.7 | 40.6 | 0.0662 | 97.9 | 71 | 0 | 0 | 71 |
| caliptra-rtl-pr-252__KFesMwU | resolved | 6395.8 | 57.2 | 0.0653 | 98.8 | 81 | 0 | 0 | 81 |
| caliptra-rtl-pr-298__xZqktYg | resolved | 1047.5 | 11.8 | 0.0140 | 97.6 | 43 | 0 | 0 | 43 |
| caliptra-rtl-pr-506__23zeyJC | resolved | 4662.9 | 37.0 | 0.0615 | 96.3 | 64 | 0 | 0 | 64 |
| caliptra-rtl-pr-594__BNspurB | resolved | 1245.9 | 19.9 | 0.0210 | 97.1 | 38 | 0 | 0 | 38 |
| caliptra-rtl-pr-633__2cjYTBR | resolved | 2964.0 | 28.5 | 0.0494 | 94.7 | 71 | 0 | 0 | 71 |
| caliptra-rtl-pr-725__XmkeB88 | resolved | 1670.9 | 26.2 | 0.0301 | 96.2 | 37 | 0 | 0 | 37 |
| caliptra-rtl-pr-747__RZmGkQh | resolved | 1799.1 | 39.8 | 0.0352 | 97.8 | 45 | 0 | 0 | 45 |
| caliptra-rtl-pr-757__vwx6pYf | resolved | 2938.6 | 49.9 | 0.0483 | 97.8 | 57 | 0 | 0 | 57 |
| caliptra-rtl-pr-963__xaZPCaK | resolved | 2483.2 | 39.9 | 0.0404 | 97.5 | 56 | 0 | 0 | 56 |
| caliptra-rtl-pr-1033__6nkLk43 | resolved | 15731.0 | 50.8 | 0.1002 | 99.0 | 125 | 0 | 0 | 125 |
| caliptra-rtl-pr-1073__6EFB6SP | resolved | 5491.3 | 64.2 | 0.0659 | 98.7 | 73 | 0 | 0 | 73 |
| caliptra-rtl-pr-1089__Q5L3sBm | resolved | 5339.3 | 87.3 | 0.0872 | 97.6 | 71 | 0 | 0 | 71 |

