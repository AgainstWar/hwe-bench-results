# Ibex SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 21
  total: 35
  resolved_rate: 60.0%
  file_level_precision: 84.9%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 21/35 (60.0%) |
| File-Level Precision | 79.2% | 84.9% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 2/2 |
| pr-104 | 100.0% | 3/3 |
| pr-122 | 100.0% | 1/1 |
| pr-155 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 4/4 |
| pr-475 | 0.0% | 0/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 1/1 |
| pr-974 | 100.0% | 2/2 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 100.0% | 2/2 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 60.0% | 3/5 |
| pr-1513 | 40.0% | 2/5 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 0.0% | 0/1 |
| pr-1865 | 100.0% | 2/2 |
| pr-2232 | 100.0% | 2/2 |

## 未解决 Case

```json
[
  {"pr": 83, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 155, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 293, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 332, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 475, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 882, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1469, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1816, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2232, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 4
  logic: 4
  spec: 5
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 35
  status: unresolved=35
  prompt_k: 1361.3
  completion_k: 5.3
  cache_hit_pct: 96.7
  tool_calls: 31.6
  cost_usd: 0.016751
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| ibex-pr-104__aBGbV4C | unresolved | 2960.6 | 7.6 | 0.0251 | 97.5 | 58 |
| ibex-pr-1135__RD9k2AG | resolved | 772.3 | 4.2 | 0.0126 | 94.4 | 23 |
| ibex-pr-1141__soBYUku | resolved | 2611.9 | 7.0 | 0.0233 | 97.7 | 62 |
| ibex-pr-1229__c2hZYko | unresolved | 1201.2 | 5.2 | 0.0161 | 95.4 | 32 |
| ibex-pr-122__TBABxkJ | resolved | 851.4 | 2.7 | 0.0148 | 94.7 | 23 |
| ibex-pr-1383__RusoDbq | resolved | 481.6 | 3.5 | 0.0080 | 95.2 | 30 |
| ibex-pr-1469__MnDrKQV | unresolved | 4218.2 | 11.3 | 0.0367 | 97.5 | 47 |
| ibex-pr-1513__UaybwUS | unresolved | 4891.0 | 11.6 | 0.0352 | 97.8 | 57 |
| ibex-pr-155__j5f8hzj | unresolved | 2085.3 | 5.4 | 0.0265 | 97.8 | 51 |
| ibex-pr-157__Zw5GGvG | resolved | 420.0 | 2.6 | 0.0098 | 92.1 | 14 |
| ibex-pr-1584__HACYYdo | unresolved | 873.3 | 5.9 | 0.0178 | 93.2 | 36 |
| ibex-pr-166__jEYtGfH | resolved | 156.1 | 1.2 | 0.0039 | 87.6 | 10 |
| ibex-pr-167__U6pdPFy | resolved | 843.1 | 4.3 | 0.0108 | 95.8 | 31 |
| ibex-pr-1735__MU2nSX4 | resolved | 2416.0 | 5.8 | 0.0242 | 96.9 | 36 |
| ibex-pr-176__oAhbvKt | resolved | 349.2 | 2.4 | 0.0056 | 92.7 | 22 |
| ibex-pr-1780__obmjvS9 | resolved | 1299.2 | 5.8 | 0.0168 | 96.4 | 30 |
| ibex-pr-1816__2wMS9FU | unresolved | 97.2 | 2.6 | 0.0044 | 77.5 | 8 |
| ibex-pr-1865__SmWEcKb | resolved | 1827.4 | 6.0 | 0.0181 | 97.4 | 45 |
| ibex-pr-222__abuv6et | resolved | 997.4 | 4.3 | 0.0142 | 96.3 | 30 |
| ibex-pr-2232__5GhiHGZ | unresolved | 1429.3 | 7.5 | 0.0150 | 96.8 | 43 |
| ibex-pr-244__yzJyfHd | resolved | 2816.4 | 8.7 | 0.0384 | 97.0 | 39 |
| ibex-pr-276__B9Muarx | resolved | 1547.6 | 5.9 | 0.0216 | 97.4 | 32 |
| ibex-pr-282__CzhCvu3 | resolved | 276.4 | 1.6 | 0.0083 | 91.7 | 12 |
| ibex-pr-293__WBwsQp7 | unresolved | 811.9 | 5.7 | 0.0179 | 96.5 | 16 |
| ibex-pr-332__cHaHjAk | unresolved | 1648.7 | 6.1 | 0.0211 | 97.3 | 30 |
| ibex-pr-377__kkkuy4w | resolved | 709.1 | 5.2 | 0.0130 | 95.3 | 25 |
| ibex-pr-45__FTzdcfL | resolved | 199.4 | 1.2 | 0.0055 | 87.2 | 12 |
| ibex-pr-465__jfnxPYw | resolved | 2224.6 | 9.1 | 0.0168 | 98.0 | 68 |
| ibex-pr-475__8aTJFbh | unresolved | 759.6 | 5.5 | 0.0116 | 94.7 | 23 |
| ibex-pr-48__2RyeV38 | resolved | 180.5 | 2.2 | 0.0046 | 90.6 | 11 |
| ibex-pr-54__aTTteEg | resolved | 455.2 | 5.0 | 0.0072 | 94.9 | 26 |
| ibex-pr-83__xkRvkom | unresolved | 1017.2 | 6.0 | 0.0116 | 96.9 | 32 |
| ibex-pr-882__x7wdhFP | unresolved | 1455.3 | 4.4 | 0.0252 | 95.8 | 26 |
| ibex-pr-907__LYSD6Zm | unresolved | 1228.6 | 4.9 | 0.0238 | 96.7 | 27 |
| ibex-pr-974__QQkCQNS | resolved | 1534.2 | 6.2 | 0.0206 | 97.3 | 38 |

