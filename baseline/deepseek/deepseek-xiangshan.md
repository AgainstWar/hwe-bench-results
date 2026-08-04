# XiangShan BASELINE Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 54
  resolved_rate: 22.2%
  file_level_precision: 89.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | BASELINE |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 12/54 (22.2%) |
| File-Level Precision | 89.7% | 89.7% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 1/1 |
| pr-739 | 100.0% | 1/1 |
| pr-1242 | 100.0% | 1/1 |
| pr-1323 | 100.0% | 1/1 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 100.0% | 1/1 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 2/2 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2195 | 100.0% | 1/1 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 100.0% | 2/2 |
| pr-2483 | 100.0% | 1/1 |
| pr-2513 | 100.0% | 1/1 |
| pr-2781 | 100.0% | 1/1 |
| pr-2845 | 100.0% | 1/1 |
| pr-2997 | 100.0% | 1/1 |
| pr-3182 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3329 | 100.0% | 1/1 |
| pr-3555 | 100.0% | 1/1 |
| pr-3636 | 100.0% | 1/1 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 71.4% | 5/7 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 100.0% | 1/1 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 50.0% | 1/2 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 88.9% | 8/9 |
| pr-5182 | 50.0% | 1/2 |
| pr-5496 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 655, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 739, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1242, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1323, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1395, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1401, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1679, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1694, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1793, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1820, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2095, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2246, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2351, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2781, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2997, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3329, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3555, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3717, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3753, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3859, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3955, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4166, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4426, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4442, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4533, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 4968, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 5182, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 10
  logic: 11
  spec: 7
  sw_hw_config: 3
  timing_sync: 7
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=54
  prompt_k: 861.5
  completion_k: 3.8
  cache_hit_pct: 96.1
  tool_calls: 25.1
  cost_usd: 0.012535
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| XiangShan-pr-1242__aF5fAYy | patch_submitted | 154.2 | 1.1 | 0.0064 | 80.4 | 6 |
| XiangShan-pr-1323__vj2rHeX | patch_submitted | 2144.4 | 5.6 | 0.0202 | 97.7 | 52 |
| XiangShan-pr-1395__yCKpPAG | patch_submitted | 461.0 | 3.1 | 0.0097 | 94.6 | 23 |
| XiangShan-pr-1401__DxTPzit | patch_submitted | 2070.1 | 6.9 | 0.0277 | 97.1 | 42 |
| XiangShan-pr-1602__996T8GU | patch_submitted | 2598.6 | 10.4 | 0.0341 | 97.3 | 29 |
| XiangShan-pr-1679__sP8aZod | patch_submitted | 431.6 | 2.1 | 0.0130 | 93.9 | 15 |
| XiangShan-pr-1694__H4JqNaf | patch_submitted | 297.4 | 1.9 | 0.0093 | 88.7 | 12 |
| XiangShan-pr-1793__rbA398U | patch_submitted | 2620.3 | 6.1 | 0.0354 | 97.8 | 51 |
| XiangShan-pr-1820__VG7h7N8 | patch_submitted | 116.5 | 1.2 | 0.0040 | 88.3 | 7 |
| XiangShan-pr-1907__Bkio49D | patch_submitted | 456.2 | 3.0 | 0.0084 | 93.8 | 21 |
| XiangShan-pr-1931__TUNhZ4K | patch_submitted | 1092.3 | 3.0 | 0.0189 | 95.6 | 19 |
| XiangShan-pr-2095__qMasKdu | patch_submitted | 174.8 | 1.5 | 0.0049 | 88.7 | 10 |
| XiangShan-pr-2195__7LERRRy | patch_submitted | 160.8 | 1.4 | 0.0047 | 86.2 | 7 |
| XiangShan-pr-2246__WQYPUsh | patch_submitted | 66.7 | 0.9 | 0.0027 | 77.7 | 4 |
| XiangShan-pr-2351__zkW6jeQ | patch_submitted | 1915.1 | 7.2 | 0.0241 | 97.2 | 47 |
| XiangShan-pr-2483__Bz29FPP | patch_submitted | 65.9 | 1.5 | 0.0031 | 80.2 | 4 |
| XiangShan-pr-2513__scMvykx | patch_submitted | 1113.0 | 7.5 | 0.0121 | 97.2 | 30 |
| XiangShan-pr-2781__AKXsP8s | patch_submitted | 1747.0 | 6.5 | 0.0198 | 97.3 | 39 |
| XiangShan-pr-281__gXQYzkD | patch_submitted | 110.1 | 1.2 | 0.0036 | 89.7 | 7 |
| XiangShan-pr-2845__yyNr5fg | patch_submitted | 303.4 | 2.4 | 0.0052 | 93.8 | 17 |
| XiangShan-pr-2997__aQ62MBm | patch_submitted | 1308.9 | 4.1 | 0.0194 | 97.9 | 32 |
| XiangShan-pr-3182__PnB3Y3w | patch_submitted | 349.0 | 4.5 | 0.0069 | 92.9 | 29 |
| XiangShan-pr-3307__4TYnsGE | patch_submitted | 273.4 | 2.2 | 0.0059 | 91.8 | 18 |
| XiangShan-pr-3329__GJFwU23 | patch_submitted | 381.6 | 3.2 | 0.0097 | 92.5 | 15 |
| XiangShan-pr-3555__yjLnC3t | patch_submitted | 289.6 | 1.9 | 0.0072 | 88.0 | 13 |
| XiangShan-pr-3636__ErNFXCh | patch_submitted | 582.9 | 2.9 | 0.0128 | 93.5 | 20 |
| XiangShan-pr-3717__HP4ENwA | patch_submitted | 275.8 | 2.1 | 0.0051 | 92.7 | 13 |
| XiangShan-pr-3753__NWnYfos | patch_submitted | 332.1 | 2.5 | 0.0101 | 91.4 | 11 |
| XiangShan-pr-3859__RtBDSTz | patch_submitted | 2979.0 | 11.3 | 0.0241 | 98.2 | 81 |
| XiangShan-pr-3867__9QNxGH3 | patch_submitted | 587.2 | 3.0 | 0.0116 | 93.8 | 20 |
| XiangShan-pr-3907__Ztcpgof | patch_submitted | 58.4 | 0.7 | 0.0026 | 74.9 | 7 |
| XiangShan-pr-3955__rXcDyPV | patch_submitted | 1282.2 | 5.0 | 0.0173 | 97.2 | 36 |
| XiangShan-pr-39__edEA7sx | patch_submitted | 234.7 | 1.6 | 0.0063 | 90.8 | 10 |
| XiangShan-pr-4110__Mpi55gb | patch_submitted | 990.5 | 4.2 | 0.0115 | 96.5 | 41 |
| XiangShan-pr-4166__9weq9jz | patch_submitted | 1864.5 | 8.1 | 0.0192 | 97.4 | 53 |
| XiangShan-pr-4179__UcqXqnh | patch_submitted | 692.8 | 3.7 | 0.0114 | 93.4 | 27 |
| XiangShan-pr-4337__AqhYeFT | patch_submitted | 197.5 | 1.7 | 0.0083 | 87.9 | 10 |
| XiangShan-pr-4426__2dFTGTC | patch_submitted | 236.5 | 2.6 | 0.0091 | 90.0 | 15 |
| XiangShan-pr-4442__U8v7yZF | patch_submitted | 395.5 | 2.6 | 0.0077 | 94.2 | 20 |
| XiangShan-pr-4533__37hekoE | patch_submitted | 258.8 | 2.1 | 0.0069 | 91.3 | 11 |
| XiangShan-pr-4750__FeuooUK | patch_submitted | 1936.9 | 5.9 | 0.0332 | 96.0 | 48 |
| XiangShan-pr-4764__XZd33Mw | patch_submitted | 1692.3 | 6.3 | 0.0164 | 96.7 | 50 |
| XiangShan-pr-4943__yT34PKw | patch_submitted | 2942.1 | 11.7 | 0.0256 | 97.9 | 89 |
| XiangShan-pr-4959__j5aDrX3 | patch_submitted | 231.4 | 2.2 | 0.0062 | 92.6 | 11 |
| XiangShan-pr-4968__kApPtJD | patch_submitted | 1039.7 | 5.9 | 0.0151 | 94.6 | 42 |
| XiangShan-pr-5080__hpUbmPS | patch_submitted | 1367.5 | 8.5 | 0.0221 | 96.9 | 33 |
| XiangShan-pr-5182__VyMFV7c | patch_submitted | 485.2 | 3.5 | 0.0092 | 92.7 | 22 |
| XiangShan-pr-5189__srE4KfY | patch_submitted | 76.3 | 1.1 | 0.0026 | 81.3 | 7 |
| XiangShan-pr-5496__EeJkcu8 | patch_submitted | 50.8 | 0.9 | 0.0019 | 79.6 | 4 |
| XiangShan-pr-5593__Bp3q63v | patch_submitted | 19.3 | 0.3 | 0.0020 | 40.5 | 2 |

