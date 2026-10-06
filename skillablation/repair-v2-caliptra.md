# Caliptra Repair V2 Analysis

## 总体结果

```yaml
repair_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (hdl-minimal-repair, no MCP)
  resolved: 15
  total: 16
  resolved_rate: 93.8%
  file_level_precision: 93.33%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V2 |
|------|:-----------:|:---------:|
| Resolved Rate | 15/16 (93.8%) | 15/16 (93.8%) |
| File-Level Precision | 93.33% | 93.33% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 0.0% | 0/1 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 7/7 |
| pr-506 | 50.0% | 1/2 |
| pr-594 | 100.0% | 1/1 |
| pr-633 | 100.0% | 3/3 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 100.0% | 4/4 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 93.3%
- **Average (per-task)**: 90.6%

## 未解决 Case

| PR |
|----|
| pr-70 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 6357.9
  completion_k: 73.1
  cache_hit_pct: 98.7
  tool_calls: 70.2
  mcp_calls: 0.0
  repair_skill_calls: 1.0
  ordinary_calls: 69.2
  cost_usd: 0.075368
  tasks: 16
  resolved: 15
  unresolved: 1
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| caliptra-rtl-pr-70__FYGYe2n | unresolved | 13960.7 | 97.7 | 0.1206 | 99.0 | 99 | 0 | 1 | 98 |
| caliptra-rtl-pr-134__ydTtWEB | resolved | 2403.6 | 25.7 | 0.0308 | 97.7 | 58 | 0 | 1 | 57 |
| caliptra-rtl-pr-195__7VEjNz8 | resolved | 17401.0 | 155.1 | 0.1690 | 99.1 | 128 | 0 | 1 | 127 |
| caliptra-rtl-pr-252__ELX9aGo | resolved | 2974.8 | 44.0 | 0.0475 | 97.2 | 51 | 0 | 1 | 50 |
| caliptra-rtl-pr-298__iMuiHi9 | resolved | 4104.8 | 56.1 | 0.0556 | 98.4 | 77 | 0 | 1 | 76 |
| caliptra-rtl-pr-506__cnNtdsd | resolved | 2344.3 | 51.2 | 0.0455 | 97.8 | 45 | 0 | 1 | 44 |
| caliptra-rtl-pr-594__gGW2Kdo | resolved | 3707.3 | 51.2 | 0.0520 | 98.1 | 57 | 0 | 1 | 56 |
| caliptra-rtl-pr-633__GHd8Xjo | resolved | 6974.4 | 49.2 | 0.0627 | 98.8 | 99 | 0 | 1 | 98 |
| caliptra-rtl-pr-725__thkmN7H | resolved | 4055.6 | 57.6 | 0.0589 | 98.0 | 55 | 0 | 1 | 54 |
| caliptra-rtl-pr-747__pQHoQk6 | resolved | 2555.0 | 88.4 | 0.0681 | 98.0 | 37 | 0 | 1 | 36 |
| caliptra-rtl-pr-757__WWYQbgJ | resolved | 2967.5 | 83.3 | 0.0657 | 98.4 | 44 | 0 | 1 | 43 |
| caliptra-rtl-pr-786__aZAHDbX | resolved | 5305.7 | 54.0 | 0.0615 | 98.3 | 83 | 0 | 1 | 82 |
| caliptra-rtl-pr-963__GhFpVPF | resolved | 1859.8 | 34.6 | 0.0345 | 97.0 | 50 | 0 | 1 | 49 |
| caliptra-rtl-pr-1033__dcXcLCr | resolved | 23873.2 | 156.8 | 0.1914 | 99.3 | 151 | 0 | 1 | 150 |
| caliptra-rtl-pr-1073__Bh3GWXa | resolved | 4764.7 | 109.6 | 0.0933 | 98.1 | 47 | 0 | 1 | 46 |
| caliptra-rtl-pr-1089__CUAyRjp | resolved | 2473.5 | 55.8 | 0.0488 | 97.8 | 43 | 0 | 1 | 42 |

