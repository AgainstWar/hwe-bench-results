# XiangShan MCP Analysis

## 总体结果

```yaml
mcp:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 18
  total: 54
  resolved_rate: 33.3%
  file_level_precision: 87.6%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 18/54 (33.3%) |
| File-Level Precision | 89.7% | 87.6% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 1/1 |
| pr-739 | 33.3% | 1/3 |
| pr-1242 | 100.0% | 6/6 |
| pr-1323 | 100.0% | 1/1 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 100.0% | 1/1 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 1/1 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2195 | 50.0% | 1/2 |
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
| pr-4110 | 50.0% | 1/2 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 3/3 |
| pr-5182 | 50.0% | 1/2 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 655, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1242, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1323, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1395, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1401, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1694, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1793, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2095, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2246, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2483, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3329, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3753, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3859, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3867, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3955, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4166, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4426, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4442, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4533, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4968, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 5189, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5593, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 5700, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 8
  logic: 12
  spec: 5
  sw_hw_config: 3
  timing_sync: 6
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=54
  prompt_k: 1086.4
  completion_k: 4.1
  cache_hit_pct: 96.4
  tool_calls: 28.7
  cost_usd: 0.014134
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| XiangShan-pr-1242__ns4PA5w | patch_submitted | 3061.4 | 8.6 | 0.0304 | 98.0 | 55 |
| XiangShan-pr-1323__wAESyiS | patch_submitted | 1316.7 | 5.2 | 0.0151 | 96.9 | 39 |
| XiangShan-pr-1395__gEApaUt | patch_submitted | 171.5 | 2.1 | 0.0050 | 89.6 | 12 |
| XiangShan-pr-1401__5BMjK4z | patch_submitted | 1134.5 | 3.2 | 0.0176 | 95.5 | 20 |
| XiangShan-pr-1602__LiroN57 | patch_submitted | 2580.2 | 6.4 | 0.0328 | 97.4 | 42 |
| XiangShan-pr-1679__GFMbRu3 | patch_submitted | 1725.3 | 5.8 | 0.0208 | 97.4 | 45 |
| XiangShan-pr-1694__WEVpFVc | patch_submitted | 1813.2 | 5.1 | 0.0278 | 96.6 | 36 |
| XiangShan-pr-1793__GLKx284 | patch_submitted | 979.2 | 4.2 | 0.0119 | 96.4 | 36 |
| XiangShan-pr-1820__tr9uADL | patch_submitted | 540.8 | 3.1 | 0.0091 | 94.3 | 19 |
| XiangShan-pr-1907__vFg4Guq | patch_submitted | 877.9 | 3.4 | 0.0160 | 94.8 | 22 |
| XiangShan-pr-1931__azJ5WsW | patch_submitted | 363.7 | 1.7 | 0.0084 | 90.3 | 12 |
| XiangShan-pr-2095__AZX4w8R | patch_submitted | 268.4 | 1.9 | 0.0068 | 91.7 | 10 |
| XiangShan-pr-2195__i6Medoe | patch_submitted | 724.1 | 4.1 | 0.0098 | 94.9 | 25 |
| XiangShan-pr-2246__Xyd3bg5 | patch_submitted | 452.0 | 3.0 | 0.0061 | 94.9 | 23 |
| XiangShan-pr-2351__24sVqyj | patch_submitted | 4960.6 | 9.7 | 0.0364 | 98.4 | 68 |
| XiangShan-pr-2483__ggtKVYi | patch_submitted | 78.2 | 1.2 | 0.0033 | 78.2 | 4 |
| XiangShan-pr-2513__yjH3832 | patch_submitted | 808.5 | 4.8 | 0.0104 | 95.3 | 23 |
| XiangShan-pr-2781__vAJPwrN | patch_submitted | 569.3 | 4.1 | 0.0079 | 94.9 | 27 |
| XiangShan-pr-281__69Cgenv | patch_submitted | 88.3 | 1.0 | 0.0056 | 75.9 | 5 |
| XiangShan-pr-2845__AnhwusF | patch_submitted | 619.6 | 3.0 | 0.0087 | 94.8 | 26 |
| XiangShan-pr-2997__NH2pUqb | patch_submitted | 2024.6 | 5.4 | 0.0235 | 98.2 | 45 |
| XiangShan-pr-3182__GhXv3vv | patch_submitted | 1249.1 | 6.3 | 0.0126 | 97.1 | 44 |
| XiangShan-pr-3307__ZF7uLCW | patch_submitted | 900.3 | 3.4 | 0.0169 | 96.3 | 24 |
| XiangShan-pr-3329__fckiDLS | patch_submitted | 314.8 | 2.2 | 0.0070 | 90.8 | 14 |
| XiangShan-pr-3555__85ZTTKX | patch_submitted | 958.5 | 3.3 | 0.0161 | 93.9 | 24 |
| XiangShan-pr-3636__8F5WLus | patch_submitted | 2365.9 | 6.2 | 0.0253 | 97.6 | 51 |
| XiangShan-pr-3717__wnUYigZ | patch_submitted | 561.2 | 2.3 | 0.0128 | 95.1 | 15 |
| XiangShan-pr-3753__KmoZxLc | patch_submitted | 1377.8 | 6.1 | 0.0179 | 96.7 | 28 |
| XiangShan-pr-3859__RJHtmh8 | patch_submitted | 6055.7 | 12.1 | 0.0395 | 98.6 | 90 |
| XiangShan-pr-3867__yw5Mg6M | patch_submitted | 233.0 | 2.1 | 0.0064 | 90.0 | 13 |
| XiangShan-pr-3907__SNB2vFs | patch_submitted | 122.1 | 0.9 | 0.0030 | 87.2 | 7 |
| XiangShan-pr-3955__j4cYGFx | patch_submitted | 1053.8 | 4.7 | 0.0131 | 96.6 | 33 |
| XiangShan-pr-39__99DKL68 | patch_submitted | 734.3 | 2.8 | 0.0132 | 96.1 | 18 |
| XiangShan-pr-4110__VCfru4p | patch_submitted | 849.9 | 4.5 | 0.0140 | 95.8 | 39 |
| XiangShan-pr-4166__a8rMcEa | patch_submitted | 2104.9 | 7.5 | 0.0241 | 97.3 | 52 |
| XiangShan-pr-4179__snHp8YR | patch_submitted | 701.3 | 4.2 | 0.0117 | 93.3 | 22 |
| XiangShan-pr-4337__PxFrtuX | patch_submitted | 922.0 | 3.9 | 0.0130 | 96.7 | 26 |
| XiangShan-pr-4426__RZmzzfC | patch_submitted | 1035.7 | 2.9 | 0.0173 | 93.3 | 18 |
| XiangShan-pr-4442__SWDx4TS | patch_submitted | 1231.4 | 4.1 | 0.0162 | 96.0 | 31 |
| XiangShan-pr-4533__Yptk34L | patch_submitted | 226.4 | 1.3 | 0.0066 | 88.9 | 8 |
| XiangShan-pr-4750__NDBa3s5 | patch_submitted | 856.9 | 4.1 | 0.0118 | 95.3 | 31 |
| XiangShan-pr-4764__DtCDr4r | patch_submitted | 696.6 | 3.3 | 0.0090 | 94.5 | 32 |
| XiangShan-pr-4943__iaMPLWV | patch_submitted | 1293.8 | 9.1 | 0.0141 | 96.9 | 65 |
| XiangShan-pr-4959__TpVoCkX | patch_submitted | 626.0 | 3.4 | 0.0100 | 94.8 | 27 |
| XiangShan-pr-4968__RsMwJdk | patch_submitted | 1063.2 | 4.3 | 0.0136 | 94.8 | 28 |
| XiangShan-pr-5080__dvt9eu4 | patch_submitted | 51.9 | 0.4 | 0.0129 | 59.5 | 4 |
| XiangShan-pr-5182__fGirYGT | patch_submitted | 1252.1 | 4.6 | 0.0189 | 95.6 | 29 |
| XiangShan-pr-5189__MnQbKbs | patch_submitted | 744.9 | 3.0 | 0.0089 | 96.3 | 27 |
| XiangShan-pr-5496__tAXmmrp | patch_submitted | 1165.9 | 6.7 | 0.0127 | 96.8 | 48 |
| XiangShan-pr-5593__mUGEymL | patch_submitted | 376.8 | 3.5 | 0.0073 | 93.9 | 17 |

