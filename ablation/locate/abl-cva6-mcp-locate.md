# CVA6 MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 24
  total: 35
  resolved_rate: 68.6%
  file_level_precision: 82.1%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 24/35 (68.6%) |
| File-Level Precision | 79.0% | 82.1% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 0.0% | 0/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 96.7% | 29/30 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2685 | 100.0% | 1/1 |
| pr-2711 | 100.0% | 1/1 |
| pr-2728 | 50.0% | 1/2 |
| pr-2802 | 0.0% | 0/1 |
| pr-2944 | 0.0% | 0/1 |
| pr-2945 | 100.0% | 1/1 |
| pr-2989 | 100.0% | 1/1 |
| pr-3042 | 100.0% | 1/1 |
| pr-3059 | 100.0% | 1/1 |
| pr-3107 | 100.0% | 1/1 |
| pr-3137 | 100.0% | 1/1 |
| pr-3171 | 100.0% | 1/1 |
| pr-3191 | 100.0% | 1/1 |
| pr-3204 | 100.0% | 1/1 |
| pr-3226 | 66.7% | 2/3 |
| pr-3231 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 2170, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2944, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  logic: 1
  spec: 1
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 32
  status: resolved=7 unresolved=25
  prompt_k: 895.0
  completion_k: 3.7
  cache_hit_pct: 95.8
  tool_calls: 25.5
  cost_usd: 0.013533
```
