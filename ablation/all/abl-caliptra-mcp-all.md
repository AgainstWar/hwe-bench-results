# Caliptra MCP+ALL Analysis

## 总体结果

```yaml
mcp+all:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 16
  resolved_rate: 50.0%
  file_level_precision: 78.6%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+ALL |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 8/16 (50.0%) |
| File-Level Precision | 90.0% | 78.6% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 0.0% | 0/1 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-506 | 33.3% | 1/3 |
| pr-633 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 70, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 506, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 1
  logic: 1
```

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=54
  prompt_k: 1028.3
  completion_k: 4.1
  cache_hit_pct: 95.7
  tool_calls: 25.9
  cost_usd: 0.014935
```
