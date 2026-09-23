# CVA6 MCP V2 Analysis

## 总体结果

```yaml
mcp_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES (WAVES_ENABLED=true, no skills)
  resolved: 34
  total: 35
  resolved_rate: 97.1%
  file_level_precision: 88.54%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | MCP V2 |
|------|:-----------:|:------:|
| Resolved Rate | 35/35 (100.0%) | 34/35 (97.1%) |
| File-Level Precision | 94.83% | 88.54% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 0.0% | 0/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 85.7% | 12/14 |
| pr-2282 | 100.0% | 1/1 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 100.0% | 1/1 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2685 | 100.0% | 19/19 |
| pr-2711 | 100.0% | 20/20 |
| pr-2728 | 33.3% | 1/3 |
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

- **Overall**: 88.5%
- **Average (per-task)**: 92.4%

## 未解决 Case

| PR |
|----|
| pr-2170 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 4196.5
  completion_k: 26.1
  cache_hit_pct: 98.5
  tool_calls: 59.3
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 59.3
  cost_usd: 0.037451
  tasks: 35
  resolved: 34
  unresolved: 1
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------------|----------|
| cva6-pr-1482__pihjM9m | resolved | 774.4 | 10.3 | 0.0136 | 95.6 | 29 | 0 | 0 | 29 |
| cva6-pr-2017__tSUgT7T | resolved | 227.7 | 6.7 | 0.0078 | 90.9 | 18 | 0 | 0 | 18 |
| cva6-pr-2032__GzXeSMV | resolved | 2206.5 | 20.1 | 0.0275 | 97.3 | 54 | 0 | 0 | 54 |
| cva6-pr-2170__JzzSmMX | unresolved | 21059.1 | 143.2 | 0.1706 | 99.3 | 137 | 0 | 0 | 137 |
| cva6-pr-2248__v6SVip8 | resolved | 131.3 | 2.0 | 0.0039 | 88.3 | 12 | 0 | 0 | 12 |
| cva6-pr-2279__yejNumj | resolved | 17990.7 | 83.4 | 0.1266 | 99.1 | 157 | 0 | 0 | 157 |
| cva6-pr-2282__RKgwScu | resolved | 1181.6 | 12.9 | 0.0192 | 95.4 | 36 | 0 | 0 | 36 |
| cva6-pr-2330__iz9SCBC | resolved | 207.7 | 12.9 | 0.0115 | 89.6 | 12 | 0 | 0 | 12 |
| cva6-pr-2374__2i2fdPN | resolved | 1406.9 | 17.5 | 0.0232 | 95.9 | 33 | 0 | 0 | 33 |
| cva6-pr-2375__7ZCHFJh | resolved | 5735.5 | 35.1 | 0.0519 | 98.4 | 85 | 0 | 0 | 85 |
| cva6-pr-2420__ccRYW4L | resolved | 930.1 | 8.0 | 0.0155 | 94.2 | 31 | 0 | 0 | 31 |
| cva6-pr-2468__veJwK3Y | resolved | 2518.7 | 13.6 | 0.0294 | 96.3 | 57 | 0 | 0 | 57 |
| cva6-pr-2469__nASGQbz | resolved | 1214.9 | 13.6 | 0.0196 | 95.6 | 41 | 0 | 0 | 41 |
| cva6-pr-2476__uXSxy6V | resolved | 20486.1 | 108.8 | 0.1473 | 99.3 | 157 | 0 | 0 | 157 |
| cva6-pr-2549__gsKDjNn | resolved | 569.5 | 8.8 | 0.0117 | 94.4 | 24 | 0 | 0 | 24 |
| cva6-pr-2589__uF6DAPE | resolved | 1519.6 | 16.6 | 0.0234 | 96.0 | 45 | 0 | 0 | 45 |
| cva6-pr-2685__aZ8b2Tc | resolved | 6248.4 | 35.8 | 0.0519 | 98.7 | 127 | 0 | 0 | 127 |
| cva6-pr-2711__zYA2UM2 | resolved | 19458.2 | 48.8 | 0.1096 | 99.2 | 172 | 0 | 0 | 172 |
| cva6-pr-2728__v4swZDF | resolved | 16084.7 | 72.6 | 0.1093 | 99.3 | 184 | 0 | 0 | 184 |
| cva6-pr-2802__p3REK9G | resolved | 4805.6 | 56.6 | 0.0595 | 98.4 | 68 | 0 | 0 | 68 |
| cva6-pr-2844__Hos24S2 | resolved | 1949.1 | 9.7 | 0.0194 | 97.3 | 58 | 0 | 0 | 58 |
| cva6-pr-2916__8mz556d | resolved | 172.8 | 1.7 | 0.0063 | 81.4 | 11 | 0 | 0 | 11 |
| cva6-pr-2944__gA65Whd | resolved | 1673.1 | 10.6 | 0.0208 | 96.2 | 38 | 0 | 0 | 38 |
| cva6-pr-2945__bQaXaTd | resolved | 379.5 | 7.2 | 0.0102 | 91.5 | 17 | 0 | 0 | 17 |
| cva6-pr-2989__3WWzhBE | resolved | 659.2 | 9.4 | 0.0156 | 91.7 | 20 | 0 | 0 | 20 |
| cva6-pr-3042__AeFHKgj | resolved | 4407.5 | 29.8 | 0.0468 | 97.6 | 73 | 0 | 0 | 73 |
| cva6-pr-3059__AbS33Z2 | resolved | 2521.1 | 25.9 | 0.0308 | 97.9 | 47 | 0 | 0 | 47 |
| cva6-pr-3107__MjmEsFg | resolved | 53.0 | 0.9 | 0.0014 | 91.7 | 5 | 0 | 0 | 5 |
| cva6-pr-3137__LPHqgQf | resolved | 2346.7 | 15.3 | 0.0223 | 98.2 | 74 | 0 | 0 | 74 |
| cva6-pr-3168__qxuua4K | resolved | 816.4 | 12.8 | 0.0167 | 94.5 | 27 | 0 | 0 | 27 |
| cva6-pr-3171__D8DSbAY | resolved | 1124.2 | 14.0 | 0.0155 | 97.7 | 47 | 0 | 0 | 47 |
| cva6-pr-3191__kp9iLvC | resolved | 1098.7 | 8.9 | 0.0158 | 95.6 | 30 | 0 | 0 | 30 |
| cva6-pr-3204__BPCkiDT | resolved | 972.6 | 9.2 | 0.0133 | 96.6 | 33 | 0 | 0 | 33 |
| cva6-pr-3226__FyZMNf4 | resolved | 2656.9 | 16.4 | 0.0254 | 98.1 | 70 | 0 | 0 | 70 |
| cva6-pr-3231__NP6MXm4 | resolved | 1290.1 | 13.4 | 0.0177 | 96.9 | 47 | 0 | 0 | 47 |

