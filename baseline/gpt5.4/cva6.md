# CVA6 Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 34
  total: 35
  resolved_rate: 97.1%
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 33
  total: 35
  resolved_rate: 94.3%
  file_level_precision: 72.2%
  infra_errors: 0
```

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2017 | 33.3% | 1/3 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 0.0% | 0/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 85.7% | 12/14 |
| pr-2282 | 100.0% | 1/1 |
| pr-2330 | 25.0% | 1/4 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 4/4 |
| pr-2420 | 100.0% | 1/1 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 12.5% | 1/8 |
| pr-2685 | 100.0% | 1/1 |
| pr-2711 | 87.5% | 21/24 |
| pr-2728 | 100.0% | 1/1 |
| pr-2802 | 100.0% | 1/1 |
| pr-2844 | 100.0% | 2/2 |
| pr-2916 | 100.0% | 1/1 |
| pr-2944 | 100.0% | 1/1 |
| pr-2945 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3042 | 25.0% | 1/4 |
| pr-3059 | 25.0% | 1/4 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3168 | 100.0% | 1/1 |
| pr-3171 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3204 | 25.0% | 1/4 |
| pr-3226 | 100.0% | 2/2 |
| pr-3231 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 72.2%
- **Average (per-task)**: 83.4%

## 未解决 Case

```json
[
  {
    "pr": 2170,
    "test": "unknown",
    "type": "config_integ",
    "desc": "WB cache 在 32-bit CVA6 构建中对齐错误, 64-bit AXI 总线宽度不匹配"
  },
  {
    "pr": 3042,
    "test": "unknown",
    "type": "config_integ",
    "desc": "AXI 参数宏无法从配置文件覆盖, 可能使用不一致的总线设置构建"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 2
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1921.7
  completion_k: 5.1
  cache_hit_pct: 94.8
  tool_calls: 59.7
  cost_usd: 0.902463
  own_price_cost_usd: 2.453382
  tasks: 35
  resolved: 33
  unresolved: 2
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| cva6-pr-1482 | resolved | 2022.8 | 6.8 | 0.9612 | 95.0 | 77 |
| cva6-pr-2017 | resolved | 2311.9 | 6.8 | 1.0359 | 96.0 | 81 |
| cva6-pr-2032 | resolved | 799.6 | 2.8 | 0.4936 | 90.7 | 35 |
| cva6-pr-2170 | unresolved | 2933.5 | 6.8 | 1.4486 | 93.3 | 75 |
| cva6-pr-2248 | resolved | 171.1 | 1.5 | 0.1461 | 86.5 | 19 |
| cva6-pr-2279 | resolved | 8653.0 | 17.1 | 3.2926 | 97.8 | 138 |
| cva6-pr-2282 | resolved | 2074.9 | 7.5 | 0.9786 | 94.9 | 67 |
| cva6-pr-2330 | resolved | 3739.6 | 10.0 | 1.6258 | 96.3 | 112 |
| cva6-pr-2374 | resolved | 1783.6 | 3.8 | 0.9005 | 94.3 | 43 |
| cva6-pr-2375 | resolved | 2006.5 | 5.1 | 0.9006 | 94.9 | 60 |
| cva6-pr-2420 | resolved | 836.0 | 3.2 | 0.4631 | 92.8 | 42 |
| cva6-pr-2468 | resolved | 1359.1 | 3.4 | 0.6637 | 93.4 | 50 |
| cva6-pr-2469 | resolved | 1442.1 | 3.9 | 0.7613 | 92.8 | 57 |
| cva6-pr-2476 | resolved | 2212.3 | 4.2 | 1.0138 | 94.5 | 56 |
| cva6-pr-2549 | resolved | 376.3 | 2.1 | 0.2823 | 84.9 | 27 |
| cva6-pr-2589 | resolved | 1506.0 | 5.3 | 0.8043 | 94.1 | 59 |
| cva6-pr-2685 | resolved | 1591.1 | 4.4 | 0.7863 | 94.7 | 63 |
| cva6-pr-2711 | resolved | 5906.2 | 15.9 | 2.3686 | 97.1 | 133 |
| cva6-pr-2728 | resolved | 616.7 | 2.9 | 0.4306 | 86.5 | 34 |
| cva6-pr-2802 | resolved | 918.3 | 2.7 | 0.5312 | 91.9 | 37 |
| cva6-pr-2844 | resolved | 1146.4 | 4.3 | 0.5980 | 93.3 | 72 |
| cva6-pr-2916 | resolved | 1022.0 | 3.1 | 0.5260 | 91.7 | 45 |
| cva6-pr-2944 | resolved | 447.8 | 2.0 | 0.2898 | 91.1 | 27 |
| cva6-pr-2945 | resolved | 814.7 | 2.9 | 0.5101 | 88.9 | 33 |
| cva6-pr-2989 | resolved | 1555.9 | 3.8 | 0.7478 | 94.5 | 47 |
| cva6-pr-3042 | unresolved | 3258.8 | 6.9 | 1.6603 | 93.0 | 86 |
| cva6-pr-3059 | resolved | 2556.9 | 8.4 | 1.1837 | 96.5 | 85 |
| cva6-pr-3107 | resolved | 147.4 | 1.4 | 0.1470 | 88.2 | 15 |
| cva6-pr-3137 | resolved | 386.2 | 2.0 | 0.2383 | 90.7 | 29 |
| cva6-pr-3168 | resolved | 1536.5 | 4.6 | 0.9185 | 90.5 | 51 |
| cva6-pr-3171 | resolved | 1291.2 | 3.7 | 0.6025 | 94.2 | 56 |
| cva6-pr-3191 | resolved | 1578.0 | 3.5 | 0.7688 | 93.9 | 48 |
| cva6-pr-3204 | resolved | 3315.8 | 8.0 | 1.4048 | 96.2 | 92 |
| cva6-pr-3226 | resolved | 3546.7 | 5.9 | 1.4205 | 96.2 | 89 |
| cva6-pr-3231 | resolved | 1393.1 | 3.1 | 0.6814 | 92.9 | 49 |
