# CVA6 MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 27
  total: 35
  resolved_rate: 77.1%
  file_level_precision: 81.5%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 27/35 (77.1%) |
| File-Level Precision | 79.0% | 81.5% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 50.0% | 1/2 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 91.7% | 11/12 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 100.0% | 1/1 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2685 | 100.0% | 1/1 |
| pr-2711 | 100.0% | 4/4 |
| pr-2728 | 100.0% | 1/1 |
| pr-2802 | 0.0% | 0/1 |
| pr-2844 | 100.0% | 1/1 |
| pr-2944 | 100.0% | 1/1 |
| pr-2945 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3042 | 50.0% | 1/2 |
| pr-3059 | 100.0% | 1/1 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3168 | 100.0% | 1/1 |
| pr-3171 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3204 | 100.0% | 1/1 |
| pr-3231 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 2032, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2844, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  logic: 1
  spec: 2
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 32
  status: resolved=6 unresolved=26
  prompt_k: 816.6
  completion_k: 3.8
  cache_hit_pct: 95.5
  tool_calls: 25.4
  cost_usd: 0.012653
```
