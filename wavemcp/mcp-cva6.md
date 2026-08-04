# CVA6 MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 31
  total: 35
  resolved_rate: 88.6%
  file_level_precision: 84.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 28/35 (80.0%) | 31/35 (88.6%) |
| File-Level Precision | 79.0% | 84.7% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-1482 | 50.0% | 1/2 |
| pr-2017 | 100.0% | 1/1 |
| pr-2032 | 100.0% | 1/1 |
| pr-2170 | 0.0% | 0/1 |
| pr-2248 | 100.0% | 1/1 |
| pr-2279 | 90.0% | 27/30 |
| pr-2282 | 100.0% | 1/1 |
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
| pr-3204 | 100.0% | 1/1 |
| pr-3226 | 100.0% | 2/2 |
| pr-3231 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 2170, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2844, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  spec: 2
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 35
  status: unresolved=35
  prompt_k: 939.3
  completion_k: 3.9
  cache_hit_pct: 96.2
  tool_calls: 25.7
  cost_usd: 0.010947
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| cva6-pr-1482__gN3eLuf | resolved | 1223.1 | 5.5 | 0.0165 | 96.1 | 29 |
| cva6-pr-2017__6M7nBym | resolved | 385.1 | 3.4 | 0.0068 | 92.1 | 17 |
| cva6-pr-2032__WXSY7gm | resolved | 762.3 | 4.1 | 0.0099 | 95.7 | 33 |
| cva6-pr-2170__f52nvwT | unresolved | 3009.9 | 4.7 | 0.0276 | 96.9 | 40 |
| cva6-pr-2248__dNwWnV9 | resolved | 60.5 | 0.7 | 0.0022 | 79.9 | 4 |
| cva6-pr-2279__X2rDsDK | resolved | 7429.0 | 27.9 | 0.0462 | 99.0 | 122 |
| cva6-pr-2282__QLX9kHm | resolved | 236.6 | 3.2 | 0.0055 | 91.6 | 16 |
| cva6-pr-2330__uxDM4ok | resolved | 71.5 | 1.0 | 0.0027 | 78.7 | 5 |
| cva6-pr-2374__9MokhVj | resolved | 349.7 | 1.9 | 0.0070 | 91.5 | 13 |
| cva6-pr-2375__jTe7pbY | resolved | 758.0 | 3.6 | 0.0104 | 95.3 | 27 |
| cva6-pr-2420__RfdVmWF | resolved | 2196.9 | 6.6 | 0.0237 | 97.3 | 47 |
| cva6-pr-2468__YqobCfJ | resolved | 515.8 | 3.3 | 0.0070 | 94.4 | 24 |
| cva6-pr-2469__haDKbTp | resolved | 166.2 | 1.8 | 0.0037 | 90.0 | 10 |
| cva6-pr-2476__ce3N8q7 | resolved | 2856.3 | 7.1 | 0.0293 | 97.6 | 55 |
| cva6-pr-2549__WX4LrLQ | resolved | 222.2 | 1.9 | 0.0046 | 90.1 | 12 |
| cva6-pr-2589__Lr2Aghx | resolved | 1239.3 | 6.7 | 0.0136 | 96.7 | 52 |
| cva6-pr-2685__ASqN6ff | resolved | 127.8 | 1.4 | 0.0035 | 86.2 | 11 |
| cva6-pr-2711__MHbMgNh | resolved | 1011.1 | 5.6 | 0.0129 | 95.7 | 46 |
| cva6-pr-2728__kpzhgZs | resolved | 232.4 | 2.0 | 0.0055 | 90.7 | 10 |
| cva6-pr-2802__q9vaC5n | unresolved | 1236.3 | 3.6 | 0.0189 | 95.2 | 28 |
| cva6-pr-2844__s72M4D3 | unresolved | 507.0 | 3.5 | 0.0071 | 94.1 | 21 |
| cva6-pr-2916__Ymo29P7 | resolved | 109.6 | 1.2 | 0.0040 | 80.0 | 7 |
| cva6-pr-2944__7SjzPE2 | resolved | 186.5 | 1.5 | 0.0042 | 89.7 | 13 |
| cva6-pr-2945__J6H5vbw | resolved | 510.0 | 2.2 | 0.0077 | 92.6 | 18 |
| cva6-pr-2989__Xe3s3YG | resolved | 825.7 | 3.9 | 0.0126 | 94.6 | 31 |
| cva6-pr-3042__AHTvDSE | unresolved | 2922.4 | 5.1 | 0.0305 | 97.6 | 50 |
| cva6-pr-3059__Y5Zmvx2 | resolved | 117.2 | 1.1 | 0.0033 | 84.5 | 6 |
| cva6-pr-3107__aQcCPYz | resolved | 52.0 | 0.6 | 0.0023 | 73.4 | 3 |
| cva6-pr-3137__nHtfx6c | resolved | 171.4 | 1.7 | 0.0045 | 87.1 | 14 |
| cva6-pr-3168__Ti3jkyu | resolved | 1350.5 | 5.6 | 0.0160 | 96.4 | 36 |
| cva6-pr-3171__8eEYsCV | resolved | 328.7 | 2.3 | 0.0061 | 92.0 | 14 |
| cva6-pr-3191__PLgWNj4 | resolved | 414.8 | 2.7 | 0.0070 | 92.9 | 18 |
| cva6-pr-3204__QwGRDdQ | resolved | 82.5 | 1.1 | 0.0032 | 78.3 | 6 |
| cva6-pr-3226__P4cyCwf | resolved | 976.7 | 5.3 | 0.0124 | 95.3 | 41 |
| cva6-pr-3231__GiSTVrq | resolved | 231.3 | 2.1 | 0.0047 | 90.7 | 19 |

