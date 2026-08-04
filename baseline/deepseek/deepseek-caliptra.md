# Caliptra BASELINE Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 13
  total: 16
  resolved_rate: 81.2%
  file_level_precision: 90.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | BASELINE |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 13/16 (81.2%) |
| File-Level Precision | 90.0% | 90.0% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-70 | 0.0% | 0/1 |
| pr-134 | 100.0% | 3/3 |
| pr-195 | 100.0% | 1/1 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 1/1 |
| pr-506 | 100.0% | 1/1 |
| pr-594 | 100.0% | 1/1 |
| pr-633 | 100.0% | 2/2 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 50.0% | 1/2 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 100.0% | 1/1 |
| pr-1073 | 100.0% | 1/1 |
| pr-1089 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 70, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 725, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1033, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 2
  sw_hw_config: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 16
  status: unresolved=16
  prompt_k: 456.7
  completion_k: 11.7
  cache_hit_pct: 96.0
  tool_calls: 19.6
  cost_usd: 0.000000
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| caliptra-rtl-pr-1033__o9V6yaV | unresolved | 529.1 | 11.1 | 0.0000 | 95.9 | 29 |
| caliptra-rtl-pr-1073__upbZw9N | resolved | 1000.7 | 19.4 | 0.0000 | 97.1 | 34 |
| caliptra-rtl-pr-1089__hJTZSXX | resolved | 951.2 | 17.1 | 0.0000 | 97.4 | 28 |
| caliptra-rtl-pr-134__vDmsBiN | resolved | 1121.4 | 19.5 | 0.0000 | 96.9 | 49 |
| caliptra-rtl-pr-195__9MePQek | resolved | 279.2 | 8.7 | 0.0000 | 93.0 | 14 |
| caliptra-rtl-pr-252__PHtPJyG | resolved | 114.3 | 4.4 | 0.0000 | 93.3 | 8 |
| caliptra-rtl-pr-298__JpAJCjs | resolved | 201.0 | 5.0 | 0.0000 | 95.4 | 12 |
| caliptra-rtl-pr-506__LsSvQ7L | resolved | 320.5 | 5.2 | 0.0000 | 95.0 | 20 |
| caliptra-rtl-pr-594__MfLwvVb | resolved | 223.6 | 5.8 | 0.0000 | 95.3 | 18 |
| caliptra-rtl-pr-633__paZCbJn | resolved | 318.4 | 8.6 | 0.0000 | 94.4 | 21 |
| caliptra-rtl-pr-70__gp25zi8 | unresolved | 1395.6 | 39.4 | 0.0000 | 97.5 | 32 |
| caliptra-rtl-pr-725__H8aHhAW | unresolved | 290.3 | 9.9 | 0.0000 | 89.7 | 8 |
| caliptra-rtl-pr-747__Wtn6vkK | resolved | 84.5 | 4.4 | 0.0000 | 93.7 | 8 |
| caliptra-rtl-pr-757__wCGDGut | resolved | 102.3 | 12.3 | 0.0000 | 92.7 | 5 |
| caliptra-rtl-pr-786__QSuCuqa | resolved | 152.2 | 4.4 | 0.0000 | 94.1 | 14 |
| caliptra-rtl-pr-963__is3CuLJ | resolved | 222.2 | 11.8 | 0.0000 | 93.0 | 14 |

