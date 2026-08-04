# Ibex MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 24
  total: 35
  resolved_rate: 68.6%
  file_level_precision: 88.2%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 24/35 (68.6%) |
| File-Level Precision | 79.2% | 88.2% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
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
| pr-465 | 100.0% | 1/1 |
| pr-475 | 0.0% | 0/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 1/1 |
| pr-974 | 100.0% | 2/2 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 100.0% | 1/1 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 75.0% | 3/4 |
| pr-1513 | 40.0% | 2/5 |
| pr-1584 | 100.0% | 4/4 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 2/2 |
| pr-2232 | 100.0% | 2/2 |

## 未解决 Case

```json
[
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 155, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 293, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 475, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1135, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1469, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1816, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1865, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 4
  logic: 2
  spec: 4
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 38
  status: unresolved=38
  prompt_k: 1167.7
  completion_k: 4.0
  cache_hit_pct: 96.5
  tool_calls: 26.1
  cost_usd: 0.016043
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| ibex-pr-104__hPzG3fB | unresolved | 2168.6 | 7.8 | 0.0217 | 96.6 | 41 |
| ibex-pr-1135__Gvuct8L | unresolved | 1073.3 | 3.4 | 0.0178 | 95.5 | 25 |
| ibex-pr-1141__WPsiJHF | resolved | 1708.9 | 5.3 | 0.0193 | 97.1 | 43 |
| ibex-pr-1229__NEAENAR | unresolved | 195.9 | 1.8 | 0.0061 | 82.7 | 14 |
| ibex-pr-122__z7xo5yh | resolved | 1180.7 | 4.1 | 0.0182 | 96.0 | 31 |
| ibex-pr-1383__CrddTPq | resolved | 410.5 | 2.7 | 0.0077 | 93.8 | 18 |
| ibex-pr-1469__XsCChna | unresolved | 5617.9 | 10.1 | 0.0454 | 98.4 | 70 |
| ibex-pr-1513__Esrs4KS | unresolved | 3974.3 | 9.3 | 0.0308 | 97.5 | 42 |
| ibex-pr-155__Ti84kSp | unresolved | 2053.3 | 4.2 | 0.0338 | 97.3 | 34 |
| ibex-pr-157__KAiSLw4 | resolved | 201.7 | 2.5 | 0.0105 | 84.6 | 7 |
| ibex-pr-1584__W5xiTCS | resolved | 5039.6 | 9.1 | 0.0349 | 98.2 | 65 |
| ibex-pr-166__hEqpdRB | resolved | 278.8 | 2.3 | 0.0048 | 92.4 | 16 |
| ibex-pr-167__wCtKswp | resolved | 810.4 | 4.5 | 0.0117 | 95.4 | 29 |
| ibex-pr-1735__v2xFRu4 | resolved | 449.7 | 3.5 | 0.0083 | 94.2 | 21 |
| ibex-pr-176__ujCoUHT | resolved | 116.8 | 1.1 | 0.0030 | 86.4 | 7 |
| ibex-pr-1780__DBrfDLE | resolved | 805.4 | 3.9 | 0.0097 | 96.9 | 26 |
| ibex-pr-1816__V3SjxSA | unresolved | 734.8 | 4.0 | 0.0131 | 96.4 | 26 |
| ibex-pr-1865__SRKTLk3 | unresolved | 1144.7 | 5.6 | 0.0182 | 95.1 | 47 |
| ibex-pr-222__i9PQyAm | resolved | 1101.9 | 3.9 | 0.0149 | 96.3 | 38 |
| ibex-pr-2232__ZcowrU5 | resolved | 635.7 | 4.4 | 0.0105 | 93.7 | 24 |
| ibex-pr-244__asRg8bP | resolved | 992.5 | 4.5 | 0.0198 | 93.3 | 21 |
| ibex-pr-276__A4XfHAf | resolved | 71.7 | 0.4 | 0.0130 | 63.5 | 3 |
| ibex-pr-276__vJDGzx9 | resolved | 1101.1 | 5.4 | 0.0194 | 95.5 | 23 |
| ibex-pr-282__yWnozPs | resolved | 269.2 | 2.1 | 0.0075 | 92.0 | 11 |
| ibex-pr-293__2Q6m5U4 | unresolved | 308.4 | 2.4 | 0.0065 | 94.2 | 16 |
| ibex-pr-332__CwFWA7r | resolved | 112.1 | 0.6 | 0.0161 | 79.0 | 5 |
| ibex-pr-332__KNNib3e | resolved | 42.3 | 0.4 | 0.0118 | 55.1 | 3 |
| ibex-pr-332__WEXw5Cg | resolved | 2029.3 | 5.5 | 0.0352 | 96.6 | 30 |
| ibex-pr-377__2Jwv49J | resolved | 2223.4 | 6.2 | 0.0234 | 97.5 | 49 |
| ibex-pr-45__tievZ7B | resolved | 883.2 | 4.8 | 0.0095 | 96.7 | 35 |
| ibex-pr-465__7wdmkVh | resolved | 448.2 | 2.4 | 0.0078 | 91.4 | 17 |
| ibex-pr-475__eT93oZm | unresolved | 455.3 | 3.4 | 0.0066 | 94.2 | 25 |
| ibex-pr-48__44cACqi | resolved | 150.3 | 1.7 | 0.0042 | 86.6 | 7 |
| ibex-pr-54__DFq8TwW | resolved | 192.5 | 2.1 | 0.0045 | 89.5 | 11 |
| ibex-pr-83__4N52fjC | resolved | 382.7 | 3.1 | 0.0066 | 93.3 | 21 |
| ibex-pr-882__AuxNAU6 | resolved | 2430.0 | 6.5 | 0.0354 | 98.2 | 36 |
| ibex-pr-907__gdj4uKF | unresolved | 634.4 | 2.9 | 0.0147 | 95.6 | 15 |
| ibex-pr-974__GVPZN46 | resolved | 1944.6 | 5.7 | 0.0271 | 96.9 | 41 |

