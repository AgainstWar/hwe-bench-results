# Caliptra MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 16
  resolved_rate: 75.0%
  file_level_precision: 86.4%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 12/16 (75.0%) |
| File-Level Precision | 90.0% | 86.4% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 0.0% | 0/1 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 1/1 |
| pr-506 | 50.0% | 1/2 |
| pr-594 | 50.0% | 1/2 |
| pr-633 | 100.0% | 2/2 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 100.0% | 2/2 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 70, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 633, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 725, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1033, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 3
  sw_hw_config: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 16
  status: unresolved=16
  prompt_k: 803.2
  completion_k: 4.2
  cache_hit_pct: 95.0
  tool_calls: 22.8
  cost_usd: 0.012190
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| caliptra-rtl-pr-1033__qACeaKT | unresolved | 663.2 | 3.3 | 0.0124 | 93.7 | 22 |
| caliptra-rtl-pr-1073__FDdfikp | resolved | 642.8 | 2.7 | 0.0151 | 91.6 | 15 |
| caliptra-rtl-pr-1089__7wYq4pr | resolved | 539.9 | 2.7 | 0.0117 | 93.2 | 14 |
| caliptra-rtl-pr-134__hqK3jMA | resolved | 976.9 | 6.7 | 0.0117 | 95.4 | 40 |
| caliptra-rtl-pr-195__DWwc6TM | resolved | 227.5 | 2.0 | 0.0069 | 88.2 | 11 |
| caliptra-rtl-pr-252__DVV6fPj | resolved | 136.7 | 1.6 | 0.0037 | 87.0 | 8 |
| caliptra-rtl-pr-298__ygNLP36 | resolved | 222.2 | 1.9 | 0.0050 | 89.5 | 13 |
| caliptra-rtl-pr-506__thTxvCs | resolved | 694.6 | 3.3 | 0.0117 | 93.5 | 26 |
| caliptra-rtl-pr-594__Lzb9YD4 | resolved | 2279.2 | 16.8 | 0.0239 | 97.5 | 48 |
| caliptra-rtl-pr-633__ArmMvzT | unresolved | 463.1 | 3.5 | 0.0086 | 91.9 | 24 |
| caliptra-rtl-pr-70__dozjhmd | unresolved | 2821.1 | 6.1 | 0.0337 | 97.5 | 48 |
| caliptra-rtl-pr-725__XJzd2TP | unresolved | 1729.8 | 6.5 | 0.0171 | 96.6 | 34 |
| caliptra-rtl-pr-747__J2Eg593 | resolved | 238.7 | 1.8 | 0.0066 | 89.3 | 12 |
| caliptra-rtl-pr-757__LrVoPKj | resolved | 444.9 | 3.7 | 0.0108 | 93.1 | 19 |
| caliptra-rtl-pr-786__4BUS58m | resolved | 646.7 | 3.2 | 0.0121 | 91.5 | 23 |
| caliptra-rtl-pr-963__uXHeLnK | resolved | 124.6 | 1.0 | 0.0040 | 87.7 | 7 |

