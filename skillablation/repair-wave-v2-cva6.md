# CVA6 Repair+Wave V2 Analysis

## 总体结果

```yaml
repair_wave_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair + wave (hdl-minimal-repair / wave)
  mcp: WAVES (WAVES_ENABLED=true)
  resolved: 35
  total: 35
  resolved_rate: 100.0%
  file_level_precision: 96.55%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair+Wave V2 |
|------|:-----------:|:--------------:|
| Resolved Rate | 35/35 (100.0%) | 35/35 (100.0%) |
| File-Level Precision | 94.83% | 96.55% |

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
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 100.0% | 1/1 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 85.7% | 6/7 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 100.0% | 1/1 |
| pr-2685 | 86.4% | 19/22 |
| pr-2711 | 100.0% | 21/21 |
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
| pr-3231 | 100.0% | 2/2 |

## File-Level Precision

- **Overall**: 96.5%
- **Average (per-task)**: 99.2%

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 2105.7
  completion_k: 6.2
  cache_hit_pct: 96.8
  tool_calls: 45.0
  mcp_calls: 0.0
  repair_skill_calls: 1.3
  wave_skill_calls: 0.0
  ordinary_calls: 43.7
  cost_usd: 0.026048
  tasks: 35
  resolved: 35
  unresolved: 0
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Wave Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|------------|----------|
| cva6-pr-1482__gebeFqz | resolved | 3539.3 | 8.8 | 0.0396 | 98.1 | 73 | 0 | 1 | 0 | 72 |
| cva6-pr-2017__afncmRq | resolved | 730.1 | 3.9 | 0.0128 | 95.5 | 31 | 0 | 2 | 0 | 29 |
| cva6-pr-2032__R4BiNGx | resolved | 1736.4 | 5.9 | 0.0241 | 97.3 | 49 | 0 | 1 | 0 | 48 |
| cva6-pr-2170__iKW4sfk | resolved | 9744.5 | 8.7 | 0.0778 | 98.2 | 95 | 0 | 0 | 0 | 95 |
| cva6-pr-2248__6fJjzan | resolved | 59.4 | 0.5 | 0.0026 | 77.8 | 6 | 0 | 0 | 0 | 6 |
| cva6-pr-2279__q58NZyR | resolved | 1901.0 | 3.8 | 0.0308 | 94.7 | 31 | 0 | 0 | 0 | 31 |
| cva6-pr-2282__3dV58es | resolved | 655.1 | 3.6 | 0.0146 | 94.9 | 25 | 0 | 1 | 0 | 24 |
| cva6-pr-2330__42AHMG8 | resolved | 2692.3 | 6.8 | 0.0379 | 97.2 | 52 | 0 | 1 | 0 | 51 |
| cva6-pr-2374__zosrfro | resolved | 551.6 | 2.1 | 0.0120 | 92.0 | 22 | 0 | 0 | 0 | 22 |
| cva6-pr-2375__99Ce2Nz | resolved | 2217.0 | 7.7 | 0.0250 | 97.7 | 60 | 0 | 2 | 0 | 58 |
| cva6-pr-2420__d4P6GDN | resolved | 965.7 | 2.7 | 0.0180 | 93.2 | 28 | 0 | 2 | 0 | 26 |
| cva6-pr-2468__324738a | resolved | 1669.3 | 4.8 | 0.0255 | 95.0 | 42 | 0 | 1 | 0 | 41 |
| cva6-pr-2469__UiLeqWc | resolved | 2448.5 | 5.8 | 0.0291 | 97.1 | 54 | 0 | 1 | 0 | 53 |
| cva6-pr-2476__j72tFRe | resolved | 3603.4 | 11.0 | 0.0543 | 94.9 | 64 | 0 | 1 | 0 | 63 |
| cva6-pr-2549__WzLx8Wz | resolved | 656.3 | 2.6 | 0.0156 | 91.9 | 26 | 0 | 1 | 0 | 25 |
| cva6-pr-2589__N7PdrBm | resolved | 1111.0 | 4.3 | 0.0185 | 96.3 | 31 | 0 | 2 | 0 | 29 |
| cva6-pr-2685__9MmC8Bm | resolved | 5595.9 | 28.8 | 0.0545 | 97.7 | 86 | 0 | 2 | 0 | 84 |
| cva6-pr-2711__SHvyc2c | resolved | 1298.5 | 3.1 | 0.0208 | 94.0 | 34 | 0 | 0 | 0 | 34 |
| cva6-pr-2728__RasPH7n | resolved | 2053.6 | 5.3 | 0.0272 | 96.9 | 41 | 0 | 2 | 0 | 39 |
| cva6-pr-2802__GeovHh8 | resolved | 757.6 | 3.0 | 0.0163 | 93.0 | 24 | 0 | 1 | 0 | 23 |
| cva6-pr-2844__uP9yg9X | resolved | 626.0 | 2.9 | 0.0135 | 91.8 | 28 | 0 | 2 | 0 | 26 |
| cva6-pr-2916__S8QcLqK | resolved | 1845.2 | 5.6 | 0.0219 | 96.8 | 48 | 0 | 2 | 0 | 46 |
| cva6-pr-2944__9yCHp3G | resolved | 2845.6 | 5.3 | 0.0299 | 97.2 | 52 | 0 | 2 | 0 | 50 |
| cva6-pr-2945__NwbT8kq | resolved | 1501.0 | 5.9 | 0.0176 | 97.5 | 48 | 0 | 1 | 0 | 47 |
| cva6-pr-2989__bJtWi5k | resolved | 2210.0 | 5.2 | 0.0245 | 97.0 | 44 | 0 | 2 | 0 | 42 |
| cva6-pr-3042__Qyrrbda | resolved | 1198.0 | 4.3 | 0.0193 | 95.2 | 44 | 0 | 1 | 0 | 43 |
| cva6-pr-3059__efpKr4e | resolved | 687.0 | 3.8 | 0.0127 | 94.8 | 26 | 0 | 2 | 0 | 24 |
| cva6-pr-3107__k923aW4 | resolved | 712.0 | 4.7 | 0.0120 | 96.3 | 34 | 0 | 2 | 0 | 32 |
| cva6-pr-3137__zgwNtUm | resolved | 1730.7 | 13.1 | 0.0238 | 95.8 | 39 | 0 | 1 | 0 | 38 |
| cva6-pr-3168__yJXcAxU | resolved | 1708.2 | 5.6 | 0.0224 | 97.3 | 45 | 0 | 1 | 0 | 44 |
| cva6-pr-3171__xRGuRkX | resolved | 4248.7 | 13.4 | 0.0442 | 98.2 | 79 | 0 | 2 | 0 | 77 |
| cva6-pr-3191__748Qvw7 | resolved | 1664.5 | 3.6 | 0.0221 | 95.7 | 38 | 0 | 1 | 0 | 37 |
| cva6-pr-3204__7odkkhZ | resolved | 934.3 | 3.8 | 0.0160 | 94.8 | 35 | 0 | 1 | 0 | 34 |
| cva6-pr-3226__bDivxGy | resolved | 5086.7 | 9.9 | 0.0449 | 98.4 | 82 | 0 | 2 | 0 | 80 |
| cva6-pr-3231__2uK4Zre | resolved | 2713.9 | 7.0 | 0.0298 | 97.1 | 59 | 0 | 2 | 0 | 57 |

