# CVA6 BASELINE Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 28
  total: 35
  resolved_rate: 80.0%
  file_level_precision: 79.0%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | BASELINE |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 28/35 (80.0%) |
| File-Level Precision | 79.0% | 79.0% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 100.0% | 1/1 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 75.0% | 12/16 |
| pr-2282 | 100.0% | 1/1 |
| pr-2330 | 100.0% | 1/1 |
| pr-2374 | 100.0% | 1/1 |
| pr-2375 | 100.0% | 2/2 |
| pr-2420 | 33.3% | 1/3 |
| pr-2468 | 100.0% | 1/1 |
| pr-2469 | 100.0% | 1/1 |
| pr-2476 | 100.0% | 1/1 |
| pr-2549 | 100.0% | 1/1 |
| pr-2589 | 14.3% | 1/7 |
| pr-2685 | 100.0% | 3/3 |
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
| pr-3204 | 100.0% | 1/1 |
| pr-3226 | 66.7% | 2/3 |
| pr-3231 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 2279, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2420, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2844, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2989, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  interface: 1
  spec: 3
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 35
  status: unresolved=35
  prompt_k: 571.7
  completion_k: 8.7
  cache_hit_pct: 97.0
  tool_calls: 17.2
  cost_usd: 0.000000
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| cva6-pr-1482__qD989wt | resolved | 107.3 | 4.9 | 0.0000 | 84.2 | 7 |
| cva6-pr-2017__kjnXbTE | resolved | 61.2 | 2.2 | 0.0000 | 90.6 | 4 |
| cva6-pr-2032__QnqpYFK | resolved | 244.5 | 6.1 | 0.0000 | 92.0 | 16 |
| cva6-pr-2170__Q2sdsNd | unresolved | 2089.9 | 42.4 | 0.0000 | 97.6 | 47 |
| cva6-pr-2248__r5GwLzj | resolved | 38.0 | 0.8 | 0.0000 | 92.7 | 5 |
| cva6-pr-2279__Q8ReRta | unresolved | 9825.1 | 61.2 | 0.0000 | 99.2 | 126 |
| cva6-pr-2282__66NLTkL | resolved | 171.5 | 8.0 | 0.0000 | 93.4 | 13 |
| cva6-pr-2330__Ewyx4KS | resolved | 88.5 | 8.0 | 0.0000 | 94.1 | 5 |
| cva6-pr-2374__BvizxMh | resolved | 136.8 | 7.2 | 0.0000 | 91.5 | 8 |
| cva6-pr-2375__vxyruHz | resolved | 679.9 | 5.6 | 0.0000 | 95.5 | 24 |
| cva6-pr-2420__rECpYZc | unresolved | 775.4 | 15.2 | 0.0000 | 95.6 | 26 |
| cva6-pr-2468__Uhjob8P | resolved | 55.4 | 1.6 | 0.0000 | 91.8 | 7 |
| cva6-pr-2469__3hMUG2v | resolved | 105.9 | 2.8 | 0.0000 | 95.1 | 8 |
| cva6-pr-2476__afYXsC2 | resolved | 849.6 | 10.2 | 0.0000 | 95.4 | 29 |
| cva6-pr-2549__BoLcMEt | resolved | 73.0 | 2.1 | 0.0000 | 92.6 | 5 |
| cva6-pr-2589__4vWjeHP | resolved | 313.1 | 11.9 | 0.0000 | 92.9 | 51 |
| cva6-pr-2685__p6dkKL7 | resolved | 806.1 | 13.2 | 0.0000 | 96.5 | 29 |
| cva6-pr-2711__bgdu4fX | resolved | 203.3 | 5.5 | 0.0000 | 92.5 | 15 |
| cva6-pr-2728__hsgyT2x | resolved | 205.9 | 7.1 | 0.0000 | 93.6 | 11 |
| cva6-pr-2802__rNrhPyH | unresolved | 388.6 | 16.2 | 0.0000 | 94.1 | 15 |
| cva6-pr-2844__59q5edP | unresolved | 183.7 | 8.7 | 0.0000 | 93.5 | 11 |
| cva6-pr-2916__a8YvskZ | resolved | 72.6 | 1.7 | 0.0000 | 92.4 | 5 |
| cva6-pr-2944__NnvzGnP | resolved | 66.0 | 2.0 | 0.0000 | 73.9 | 3 |
| cva6-pr-2945__YHBpiUo | resolved | 82.5 | 1.5 | 0.0000 | 83.9 | 4 |
| cva6-pr-2989__pxAUryp | unresolved | 397.6 | 6.8 | 0.0000 | 94.8 | 17 |
| cva6-pr-3042__ge4jx36 | unresolved | 866.3 | 24.0 | 0.0000 | 95.2 | 35 |
| cva6-pr-3059__NqhHWGH | resolved | 44.6 | 1.6 | 0.0000 | 89.0 | 3 |
| cva6-pr-3107__4vfcwFm | resolved | 29.1 | 0.7 | 0.0000 | 88.1 | 2 |
| cva6-pr-3137__LxHLsqj | resolved | 92.8 | 3.2 | 0.0000 | 93.7 | 9 |
| cva6-pr-3168__tsVjTjv | resolved | 48.7 | 2.5 | 0.0000 | 88.3 | 3 |
| cva6-pr-3171__BDo2hby | resolved | 64.0 | 1.8 | 0.0000 | 78.8 | 4 |
| cva6-pr-3191__dGA2peQ | resolved | 449.3 | 6.4 | 0.0000 | 96.3 | 24 |
| cva6-pr-3204__5995owR | resolved | 52.5 | 1.3 | 0.0000 | 92.2 | 5 |
| cva6-pr-3226__HxWnfuj | resolved | 276.6 | 9.0 | 0.0000 | 94.8 | 19 |
| cva6-pr-3231__F99eNBY | resolved | 64.8 | 1.1 | 0.0000 | 93.0 | 6 |

