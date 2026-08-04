# CVA6 MCP+REPAIR Analysis

## 总体结果

```yaml
mcp+repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 30
  total: 35
  resolved_rate: 85.7%
  file_level_precision: 81.8%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 30/35 (85.7%) |
| File-Level Precision | 79.0% | 81.8% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 0.0% | 0/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 91.7% | 11/12 |
| pr-2282 | 50.0% | 1/2 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 1/1 |
| pr-2420 | 100.0% | 1/1 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2685 | 100.0% | 1/1 |
| pr-2711 | 100.0% | 1/1 |
| pr-2728 | 100.0% | 1/1 |
| pr-2802 | 100.0% | 1/1 |
| pr-2844 | 100.0% | 1/1 |
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
| pr-3204 | 50.0% | 1/2 |
| pr-3226 | 100.0% | 2/2 |
| pr-3231 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 2032, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2170, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2844, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  logic: 1
  spec: 2
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=54
  prompt_k: 999.0
  completion_k: 4.0
  cache_hit_pct: 95.6
  tool_calls: 27.4
  cost_usd: 0.014582
```
