# RocketChip Repair V3 Analysis

## 总体结果

```yaml
repair_v3:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (revised, hdl-minimal-repair)
  resolved: 25
  total: 32
  resolved_rate: 78.1%
  file_level_precision: 92.42%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V3 |
|------|:-----------:|:---------:|
| Resolved Rate | 20/32 (62.5%) | 25/32 (78.1%) |
| File-Level Precision | 94.52% | 92.42% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/2 |
| pr-387 | 100.0% | 2/2 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 100.0% | 9/9 |
| pr-542 | 100.0% | 1/1 |
| pr-576 | 100.0% | 1/1 |
| pr-745 | 100.0% | 2/2 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 87.5% | 7/8 |
| pr-1656 | 100.0% | 6/6 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 100.0% | 2/2 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 100.0% | 1/1 |
| pr-2621 | 100.0% | 4/4 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 33.3% | 1/3 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 100.0% | 2/2 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 100.0% | 1/1 |
| pr-3600 | 100.0% | 2/2 |
| pr-3624 | 100.0% | 3/3 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 92.4%
- **Average (per-task)**: 94.4%

## 未解决 Case

| PR |
|----|
| pr-387 |
| pr-1493 |
| pr-1761 |
| pr-2036 |
| pr-2167 |
| pr-3256 |
| pr-3624 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 3512.1
  completion_k: 15.3
  cache_hit_pct: 0.0
  tool_calls: 56.6
  mcp_calls: 0.0
  repair_skill_calls: 1.3
  ordinary_calls: 55.3
  cost_usd: 0.036150
  tasks: 32
  resolved: 25
  unresolved: 7
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| rocket-chip-pr-177__yisozSv | resolved | 1509.5 | 6.3 | 0.0206 | 97.1 | 52 | 0 | 1 | 51 |
| rocket-chip-pr-387__FMNenT8 | unresolved | 10456.5 | 92.1 | 0.1020 | 99.0 | 119 | 0 | 2 | 117 |
| rocket-chip-pr-404__2SqrdRR | resolved | 389.0 | 1.8 | 0.0109 | 91.3 | 20 | 0 | 1 | 19 |
| rocket-chip-pr-485__K9XYeTS | resolved | 6397.2 | 26.1 | 0.0760 | 96.8 | 102 | 0 | 1 | 101 |
| rocket-chip-pr-542__3snZB7b | resolved | 845.2 | 2.8 | 0.0145 | 94.9 | 28 | 0 | 2 | 26 |
| rocket-chip-pr-576__Lka5CHz | resolved | 1632.4 | 18.3 | 0.0286 | 95.8 | 51 | 0 | 1 | 50 |
| rocket-chip-pr-745__CX8YCxD | resolved | 4747.8 | 42.8 | 0.0538 | 98.1 | 88 | 0 | 1 | 87 |
| rocket-chip-pr-1069__mW6Ufb4 | resolved | 3824.0 | 8.8 | 0.0560 | 94.7 | 60 | 0 | 2 | 58 |
| rocket-chip-pr-1093__MrGqAFs | resolved | 2779.2 | 6.6 | 0.0336 | 97.8 | 63 | 0 | 1 | 62 |
| rocket-chip-pr-1176__ggbucLM | resolved | 434.1 | 2.3 | 0.0104 | 93.9 | 21 | 0 | 1 | 20 |
| rocket-chip-pr-1330__9LhSQmR | resolved | 425.3 | 5.0 | 0.0124 | 96.2 | 26 | 0 | 1 | 25 |
| rocket-chip-pr-1493__5ke7Yer | unresolved | 6310.5 | 8.1 | 0.0567 | 97.9 | 79 | 0 | 1 | 78 |
| rocket-chip-pr-1656__eSCxpsi | resolved | 5088.0 | 28.3 | 0.0544 | 97.3 | 81 | 0 | 1 | 80 |
| rocket-chip-pr-1761__2ZVJ5nY | unresolved | 313.9 | 5.5 | 0.0124 | 84.1 | 15 | 0 | 1 | 14 |
| rocket-chip-pr-1878__iCLj7wz | resolved | 969.2 | 14.0 | 0.0187 | 94.8 | 35 | 0 | 1 | 34 |
| rocket-chip-pr-2018__btf4ePm | resolved | 1740.5 | 4.7 | 0.0219 | 96.8 | 47 | 0 | 1 | 46 |
| rocket-chip-pr-2036__LyDhvgp | unresolved | 1694.3 | 6.6 | 0.0320 | 93.7 | 54 | 0 | 1 | 53 |
| rocket-chip-pr-2167__Lc9xTmo | unresolved | 739.2 | 5.8 | 0.0157 | 93.0 | 39 | 0 | 2 | 37 |
| rocket-chip-pr-2213__5jDnSYS | resolved | 4788.8 | 9.6 | 0.0498 | 98.3 | 82 | 0 | 2 | 80 |
| rocket-chip-pr-2368__zGn2YWe | resolved | 1717.6 | 5.5 | 0.0235 | 97.4 | 48 | 0 | 1 | 47 |
| rocket-chip-pr-2543__DQg5XhD | resolved | 37683.3 | 102.5 | 0.2109 | 99.4 | 205 | 0 | 2 | 203 |
| rocket-chip-pr-2621__NXk9uJU | resolved | 1083.5 | 4.0 | 0.0189 | 94.0 | 40 | 0 | 1 | 39 |
| rocket-chip-pr-2984__aB5tihM | resolved | 637.5 | 2.8 | 0.0120 | 93.2 | 32 | 0 | 1 | 31 |
| rocket-chip-pr-2988__6pxecDD | resolved | 6468.5 | 46.2 | 0.0589 | 98.8 | 137 | 0 | 1 | 136 |
| rocket-chip-pr-2994__5qSouEE | resolved | 1577.7 | 7.1 | 0.0224 | 97.0 | 49 | 0 | 1 | 48 |
| rocket-chip-pr-3004__8v5nL5C | resolved | 1409.6 | 4.3 | 0.0180 | 95.8 | 42 | 0 | 2 | 40 |
| rocket-chip-pr-3065__RYK6dZd | resolved | 1728.3 | 4.5 | 0.0228 | 96.8 | 35 | 0 | 2 | 33 |
| rocket-chip-pr-3256__RBdcHGK | unresolved | 378.7 | 2.0 | 0.0112 | 89.7 | 18 | 0 | 1 | 17 |
| rocket-chip-pr-3526__bxR3UTc | resolved | 579.5 | 2.6 | 0.0111 | 94.3 | 23 | 0 | 1 | 22 |
| rocket-chip-pr-3600__4F2fF2J | resolved | 2217.1 | 4.8 | 0.0330 | 97.5 | 44 | 0 | 1 | 43 |
| rocket-chip-pr-3624__mzD4JQU | unresolved | 1318.3 | 6.4 | 0.0199 | 96.2 | 59 | 0 | 2 | 57 |
| rocket-chip-pr-3651__A8hUTG2 | resolved | 502.7 | 1.9 | 0.0138 | 90.5 | 18 | 0 | 1 | 17 |

