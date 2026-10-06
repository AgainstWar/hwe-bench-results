# CVA6 Repair V2 Analysis

## 总体结果

```yaml
repair_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (hdl-minimal-repair, no MCP)
  resolved: 35
  total: 35
  resolved_rate: 100.0%
  file_level_precision: 89.90%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V2 |
|------|:-----------:|:---------:|
| Resolved Rate | 35/35 (100.0%) | 35/35 (100.0%) |
| File-Level Precision | 94.83% | 89.90% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 100.0% | 1/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 100.0% | 11/11 |
| pr-2282 | 100.0% | 1/1 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 100.0% | 1/1 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 85.7% | 6/7 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 12.5% | 1/8 |
| pr-2685 | 90.5% | 19/21 |
| pr-2711 | 100.0% | 19/19 |
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

- **Overall**: 89.9%
- **Average (per-task)**: 96.8%

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 6153.8
  completion_k: 45.0
  cache_hit_pct: 98.7
  tool_calls: 82.0
  mcp_calls: 0.0
  repair_skill_calls: 1.0
  ordinary_calls: 81.0
  cost_usd: 0.057152
  tasks: 35
  resolved: 35
  unresolved: 0
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| cva6-pr-1482__YoyS4tv | resolved | 978.5 | 23.6 | 0.0220 | 96.6 | 38 | 0 | 1 | 37 |
| cva6-pr-2017__EyzGhQb | resolved | 4999.8 | 37.3 | 0.0472 | 98.7 | 104 | 0 | 1 | 103 |
| cva6-pr-2032__d6cmoS8 | resolved | 6871.1 | 42.6 | 0.0564 | 99.0 | 125 | 0 | 1 | 124 |
| cva6-pr-2170__Rvc6Kci | resolved | 12178.5 | 62.2 | 0.0921 | 99.0 | 117 | 0 | 1 | 116 |
| cva6-pr-2248__urTQJnR | resolved | 914.8 | 10.6 | 0.0148 | 95.8 | 39 | 0 | 1 | 38 |
| cva6-pr-2279__gYUed3T | resolved | 19241.9 | 90.7 | 0.1616 | 98.3 | 152 | 0 | 1 | 151 |
| cva6-pr-2282__HTVvDt4 | resolved | 931.8 | 23.2 | 0.0209 | 97.0 | 30 | 0 | 1 | 29 |
| cva6-pr-2330__mpNwKUV | resolved | 8310.6 | 58.2 | 0.0729 | 98.9 | 130 | 0 | 1 | 129 |
| cva6-pr-2374__PAxYQqk | resolved | 15048.0 | 105.5 | 0.1256 | 99.2 | 124 | 0 | 1 | 123 |
| cva6-pr-2375__LpDoU35 | resolved | 4605.1 | 25.1 | 0.0408 | 98.2 | 71 | 0 | 1 | 70 |
| cva6-pr-2420__7PjPcsh | resolved | 1270.2 | 15.3 | 0.0214 | 95.5 | 40 | 0 | 1 | 39 |
| cva6-pr-2468__nruzCWS | resolved | 1173.9 | 14.7 | 0.0185 | 96.5 | 38 | 0 | 1 | 37 |
| cva6-pr-2469__WBVvpRb | resolved | 2895.3 | 29.0 | 0.0322 | 98.6 | 67 | 0 | 1 | 66 |
| cva6-pr-2476__CLKjoGN | resolved | 7380.1 | 58.6 | 0.0760 | 98.3 | 84 | 0 | 1 | 83 |
| cva6-pr-2549__VXdr7ZH | resolved | 922.5 | 16.6 | 0.0187 | 95.6 | 33 | 0 | 1 | 32 |
| cva6-pr-2589__gmJXNct | resolved | 5217.9 | 34.7 | 0.0498 | 98.3 | 85 | 0 | 1 | 84 |
| cva6-pr-2685__DkfmWeb | resolved | 8372.7 | 34.3 | 0.0649 | 98.4 | 125 | 0 | 1 | 124 |
| cva6-pr-2711__A62EfmX | resolved | 12799.3 | 47.1 | 0.0888 | 98.8 | 140 | 0 | 1 | 139 |
| cva6-pr-2728__snCNvS9 | resolved | 11070.1 | 75.5 | 0.0927 | 99.1 | 117 | 0 | 1 | 116 |
| cva6-pr-2802__DUZJHbU | resolved | 10838.5 | 93.8 | 0.1008 | 99.2 | 96 | 0 | 1 | 95 |
| cva6-pr-2844__NLPShUe | resolved | 3989.2 | 23.9 | 0.0339 | 98.7 | 95 | 0 | 1 | 94 |
| cva6-pr-2916__Xpav3fD | resolved | 5295.2 | 28.7 | 0.0421 | 98.8 | 94 | 0 | 1 | 93 |
| cva6-pr-2944__WWNiGRz | resolved | 2406.0 | 21.1 | 0.0285 | 97.6 | 48 | 0 | 1 | 47 |
| cva6-pr-2945__BoxKWJm | resolved | 1171.9 | 15.9 | 0.0197 | 96.2 | 39 | 0 | 1 | 38 |
| cva6-pr-2989__Y4aqBkg | resolved | 1639.7 | 21.8 | 0.0272 | 96.2 | 38 | 0 | 1 | 37 |
| cva6-pr-3042__6DCRanJ | resolved | 31728.2 | 309.4 | 0.2995 | 99.6 | 153 | 0 | 1 | 152 |
| cva6-pr-3059__ufJHj9f | resolved | 2645.1 | 36.8 | 0.0392 | 97.6 | 50 | 0 | 1 | 49 |
| cva6-pr-3107__DfMdjQx | resolved | 3699.7 | 22.4 | 0.0327 | 98.5 | 83 | 0 | 1 | 82 |
| cva6-pr-3137__DduHEqJ | resolved | 4032.0 | 31.9 | 0.0386 | 98.7 | 81 | 0 | 1 | 80 |
| cva6-pr-3168__wFfcHgp | resolved | 1502.5 | 18.2 | 0.0204 | 97.7 | 54 | 0 | 1 | 53 |
| cva6-pr-3171__EZqmywv | resolved | 8245.9 | 51.2 | 0.0680 | 99.0 | 118 | 0 | 1 | 117 |
| cva6-pr-3191__HSEj9SA | resolved | 1866.7 | 19.8 | 0.0274 | 96.4 | 40 | 0 | 1 | 39 |
| cva6-pr-3204__S2cVGUH | resolved | 991.8 | 13.4 | 0.0163 | 96.3 | 36 | 0 | 1 | 35 |
| cva6-pr-3226__yCtKaNA | resolved | 3400.2 | 23.4 | 0.0325 | 98.3 | 80 | 0 | 1 | 79 |
| cva6-pr-3231__meiRA8T | resolved | 6749.8 | 39.7 | 0.0563 | 98.8 | 105 | 0 | 1 | 104 |

