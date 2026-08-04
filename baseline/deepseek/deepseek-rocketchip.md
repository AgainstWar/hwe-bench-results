# RocketChip BASELINE Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 32
  resolved_rate: 25.0%
  file_level_precision: 87.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | BASELINE |
|------|:--------:|:-------------:|
| Resolved Rate | 8/32 (25.0%) | 8/32 (25.0%) |
| File-Level Precision | 87.0% | 87.0% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
| pr-387 | 100.0% | 3/3 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 100.0% | 6/6 |
| pr-542 | 100.0% | 1/1 |
| pr-576 | 100.0% | 1/1 |
| pr-745 | 100.0% | 1/1 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 1/1 |
| pr-1656 | 100.0% | 2/2 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 0.0% | 0/1 |
| pr-2621 | 100.0% | 3/3 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 100.0% | 1/1 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 100.0% | 1/1 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 100.0% | 1/1 |
| pr-3600 | 25.0% | 1/4 |
| pr-3624 | 100.0% | 1/1 |
| pr-3651 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 177, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 387, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 404, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 485, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 745, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1093, "test": "N/A", "type": "sw_hw_interact", "desc": "N/A"},  {"pr": 1176, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1493, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1656, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1761, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1878, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2018, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2036, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2167, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2213, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2368, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2543, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2621, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 3004, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3256, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3526, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3600, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3624, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3651, "test": "N/A", "type": "spec", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 4
  interface: 5
  logic: 7
  spec: 3
  sw_hw_interact: 1
  timing_sync: 4
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 32
  status: unresolved=32
  prompt_k: 671.5
  completion_k: 3.4
  cache_hit_pct: 95.7
  tool_calls: 22.8
  cost_usd: 0.010688
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| rocket-chip-pr-1069__RzBBRGZ | resolved | 943.7 | 6.8 | 0.0117 | 95.6 | 44 |
| rocket-chip-pr-1093__zVCGgoE | unresolved | 126.6 | 1.5 | 0.0033 | 89.6 | 13 |
| rocket-chip-pr-1176__c86KfsQ | unresolved | 288.3 | 2.2 | 0.0070 | 90.7 | 16 |
| rocket-chip-pr-1330__6DBRoe6 | resolved | 55.2 | 0.7 | 0.0025 | 79.1 | 4 |
| rocket-chip-pr-1493__A38eD6M | unresolved | 419.5 | 2.4 | 0.0073 | 93.1 | 21 |
| rocket-chip-pr-1656__Y2HKrJQ | unresolved | 222.3 | 2.3 | 0.0049 | 91.8 | 15 |
| rocket-chip-pr-1761__e7BdZUZ | unresolved | 148.1 | 1.5 | 0.0062 | 86.3 | 11 |
| rocket-chip-pr-177__yWZbdvx | unresolved | 1434.2 | 5.3 | 0.0174 | 96.8 | 40 |
| rocket-chip-pr-1878__6tabmNw | unresolved | 155.7 | 1.4 | 0.0041 | 88.6 | 14 |
| rocket-chip-pr-2018__DuXHNcY | unresolved | 591.2 | 3.6 | 0.0103 | 94.7 | 27 |
| rocket-chip-pr-2036__wW59DHj | unresolved | 130.3 | 1.5 | 0.0035 | 88.1 | 12 |
| rocket-chip-pr-2167__pytpqnB | unresolved | 456.1 | 2.2 | 0.0107 | 93.0 | 18 |
| rocket-chip-pr-2213__pBbULqz | unresolved | 1013.0 | 5.4 | 0.0222 | 95.9 | 37 |
| rocket-chip-pr-2368__cgc68AM | unresolved | 1303.6 | 4.1 | 0.0199 | 96.4 | 35 |
| rocket-chip-pr-2543__JuK5es8 | unresolved | 1563.0 | 3.8 | 0.0251 | 97.4 | 30 |
| rocket-chip-pr-2621__Cyx7DXB | unresolved | 418.1 | 4.0 | 0.0066 | 94.8 | 37 |
| rocket-chip-pr-2984__FE58oWN | resolved | 241.7 | 2.6 | 0.0050 | 92.6 | 16 |
| rocket-chip-pr-2988__dK3wec6 | resolved | 100.9 | 1.2 | 0.0024 | 87.9 | 8 |
| rocket-chip-pr-2994__243Erip | resolved | 408.6 | 3.8 | 0.0100 | 92.9 | 26 |
| rocket-chip-pr-3004__85pv3An | unresolved | 470.2 | 2.5 | 0.0120 | 93.0 | 12 |
| rocket-chip-pr-3065__8gAheNS | resolved | 584.5 | 3.1 | 0.0123 | 94.8 | 21 |
| rocket-chip-pr-3256__Lmraw7K | unresolved | 103.2 | 1.3 | 0.0036 | 84.7 | 7 |
| rocket-chip-pr-3526__KiQNGmZ | unresolved | 547.2 | 2.5 | 0.0137 | 94.1 | 13 |
| rocket-chip-pr-3600__CRERGRu | unresolved | 1261.4 | 5.0 | 0.0147 | 97.2 | 41 |
| rocket-chip-pr-3624__AMvcQcr | unresolved | 278.3 | 3.0 | 0.0050 | 93.4 | 22 |
| rocket-chip-pr-3651__WEFdQA8 | unresolved | 133.3 | 1.4 | 0.0042 | 87.7 | 11 |
| rocket-chip-pr-387__Wm2iRdr | unresolved | 2486.2 | 10.7 | 0.0270 | 97.9 | 48 |
| rocket-chip-pr-404__uhs4aJc | unresolved | 291.5 | 1.8 | 0.0070 | 93.4 | 13 |
| rocket-chip-pr-485__eJXWz8X | unresolved | 4207.3 | 13.9 | 0.0388 | 97.7 | 73 |
| rocket-chip-pr-542__fPLj2mC | resolved | 60.2 | 0.8 | 0.0025 | 78.8 | 5 |
| rocket-chip-pr-576__TYdsUhD | resolved | 709.1 | 2.8 | 0.0141 | 96.9 | 21 |
| rocket-chip-pr-745__tZdMJwT | unresolved | 336.9 | 2.9 | 0.0067 | 92.4 | 18 |

