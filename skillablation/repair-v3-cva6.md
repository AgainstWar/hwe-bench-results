# CVA6 Repair V3 Analysis

## 总体结果

```yaml
repair_v3:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (revised, hdl-minimal-repair)
  resolved: 35
  total: 35
  resolved_rate: 100.0%
  file_level_precision: 100.00%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V3 |
|------|:-----------:|:---------:|
| Resolved Rate | 35/35 (100.0%) | 35/35 (100.0%) |
| File-Level Precision | 94.83% | 100.00% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 100.0% | 2/2 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 100.0% | 30/30 |
| pr-2282 | 100.0% | 1/1 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 4/4 |
| pr-2420 | 100.0% | 1/1 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 100.0% | 1/1 |
| pr-2685 | 100.0% | 21/21 |
| pr-2711 | 100.0% | 20/20 |
| pr-2728 | 100.0% | 1/1 |
| pr-2802 | 100.0% | 1/1 |
| pr-2844 | 100.0% | 2/2 |
| pr-2916 | 100.0% | 1/1 |
| pr-2944 | 100.0% | 1/1 |
| pr-2945 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3042 | 100.0% | 1/1 |
| pr-3059 | 100.0% | 1/1 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3168 | 100.0% | 1/1 |
| pr-3171 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3204 | 100.0% | 1/1 |
| pr-3226 | 100.0% | 2/2 |
| pr-3231 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 100.0%
- **Average (per-task)**: 100.0%

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 2651.9
  completion_k: 11.9
  cache_hit_pct: 0.0
  tool_calls: 48.7
  mcp_calls: 0.0
  repair_skill_calls: 1.5
  ordinary_calls: 47.3
  cost_usd: 0.029591
  tasks: 35
  resolved: 35
  unresolved: 0
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| cva6-pr-1482__LziEo4M | resolved | 3037.2 | 37.4 | 0.0414 | 97.8 | 73 | 0 | 1 | 72 |
| cva6-pr-2017__yFmbyQ4 | resolved | 9226.3 | 51.7 | 0.0758 | 98.7 | 130 | 0 | 1 | 129 |
| cva6-pr-2032__9JBF8CE | resolved | 1345.4 | 5.1 | 0.0193 | 97.2 | 43 | 0 | 1 | 42 |
| cva6-pr-2170__Kbfy7EY | resolved | 15503.4 | 36.4 | 0.1233 | 97.9 | 110 | 0 | 2 | 108 |
| cva6-pr-2248__VjMWBHm | resolved | 211.8 | 1.8 | 0.0052 | 91.6 | 20 | 0 | 1 | 19 |
| cva6-pr-2279__cyqp6kf | resolved | 5710.3 | 15.6 | 0.0555 | 97.1 | 86 | 0 | 1 | 85 |
| cva6-pr-2282__cVvPkVr | resolved | 991.0 | 3.7 | 0.0219 | 91.4 | 30 | 0 | 2 | 28 |
| cva6-pr-2330__xFjCwCp | resolved | 4536.0 | 30.6 | 0.0498 | 98.0 | 84 | 0 | 1 | 83 |
| cva6-pr-2374__nkrgWWU | resolved | 1375.5 | 3.2 | 0.0224 | 95.6 | 31 | 0 | 2 | 29 |
| cva6-pr-2375__TGFZ2f4 | resolved | 1493.8 | 4.9 | 0.0219 | 95.6 | 42 | 0 | 1 | 41 |
| cva6-pr-2420__x8TEwTk | resolved | 285.7 | 1.2 | 0.0086 | 86.9 | 14 | 0 | 1 | 13 |
| cva6-pr-2468__QCgc9fL | resolved | 122.3 | 1.1 | 0.0041 | 86.1 | 10 | 0 | 1 | 9 |
| cva6-pr-2469__HJBieeZ | resolved | 993.0 | 3.2 | 0.0203 | 92.6 | 34 | 0 | 2 | 32 |
| cva6-pr-2476__cw4bvNN | resolved | 5984.1 | 40.9 | 0.0641 | 97.6 | 62 | 0 | 1 | 61 |
| cva6-pr-2549__XSo7PbB | resolved | 448.6 | 2.1 | 0.0117 | 92.4 | 22 | 0 | 2 | 20 |
| cva6-pr-2589__pdALSDf | resolved | 2482.4 | 4.5 | 0.0322 | 96.2 | 50 | 0 | 2 | 48 |
| cva6-pr-2685__JDpqTUE | resolved | 3706.4 | 7.4 | 0.0355 | 97.8 | 68 | 0 | 1 | 67 |
| cva6-pr-2711__uKqNy4n | resolved | 7189.7 | 31.5 | 0.0597 | 98.3 | 130 | 0 | 2 | 128 |
| cva6-pr-2728__pLwyHP7 | resolved | 9247.6 | 45.6 | 0.0906 | 98.1 | 119 | 0 | 2 | 117 |
| cva6-pr-2802__ezkaD4c | resolved | 1075.2 | 3.1 | 0.0194 | 94.9 | 32 | 0 | 2 | 30 |
| cva6-pr-2844__bdaKv6L | resolved | 991.5 | 5.6 | 0.0190 | 92.5 | 43 | 0 | 1 | 42 |
| cva6-pr-2916__AtCVEdr | resolved | 127.0 | 0.8 | 0.0047 | 81.9 | 10 | 0 | 2 | 8 |
| cva6-pr-2944__WCMcaHz | resolved | 400.7 | 1.4 | 0.0082 | 91.9 | 14 | 0 | 1 | 13 |
| cva6-pr-2945__5LtFwUP | resolved | 1231.8 | 5.3 | 0.0201 | 97.0 | 42 | 0 | 2 | 40 |
| cva6-pr-2989__e2zyke5 | resolved | 347.9 | 1.2 | 0.0098 | 87.5 | 16 | 0 | 1 | 15 |
| cva6-pr-3042__tWPubYq | resolved | 2782.4 | 17.3 | 0.0375 | 95.8 | 55 | 0 | 1 | 54 |
| cva6-pr-3059__8Cbv9Ua | resolved | 893.0 | 5.5 | 0.0155 | 96.7 | 35 | 0 | 1 | 34 |
| cva6-pr-3107__83eNoEG | resolved | 68.7 | 0.6 | 0.0028 | 81.8 | 6 | 0 | 2 | 4 |
| cva6-pr-3137__8osJTCQ | resolved | 1692.4 | 9.4 | 0.0227 | 97.5 | 58 | 0 | 2 | 56 |
| cva6-pr-3168__Fj3z9LW | resolved | 438.2 | 1.9 | 0.0128 | 88.8 | 21 | 0 | 2 | 19 |
| cva6-pr-3171__zCCGDF5 | resolved | 450.9 | 2.9 | 0.0086 | 95.2 | 27 | 0 | 2 | 25 |
| cva6-pr-3191__oKNjmvL | resolved | 1348.1 | 4.7 | 0.0179 | 96.7 | 45 | 0 | 1 | 44 |
| cva6-pr-3204__UAjLEuR | resolved | 395.2 | 2.4 | 0.0069 | 94.5 | 22 | 0 | 2 | 20 |
| cva6-pr-3226__4iG9nkx | resolved | 5132.3 | 7.9 | 0.0434 | 98.0 | 70 | 0 | 1 | 69 |
| cva6-pr-3231__b84pSZu | resolved | 1551.0 | 17.0 | 0.0230 | 96.6 | 52 | 0 | 2 | 50 |

