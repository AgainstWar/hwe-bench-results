# Caliptra MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 16
  resolved_rate: 50.0%
  file_level_precision: 100.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 8/16 (50.0%) |
| File-Level Precision | 90.0% | 100.0% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-506 | 100.0% | 1/1 |
| pr-594 | 100.0% | 1/1 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 757, "test": "N/A", "type": "timing_sync", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  timing_sync: 1
```


## Token 统计（token_report.py）

### 平均指标



### 逐 Task 明细

注：此配置使用 combined tarball，token 数据为所有 repo 混合统计，无法拆分为 per-task 明细。

