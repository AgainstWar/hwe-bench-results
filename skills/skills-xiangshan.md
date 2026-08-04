# XiangShan SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 16
  total: 54
  resolved_rate: 29.6%
  file_level_precision: 71.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 12/54 (22.2%) | 16/54 (29.6%) |
| File-Level Precision | 89.7% | 71.7% |


## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-1242 | 0.0% | 0/1 |
| pr-1323 | 50.0% | 1/2 |
| pr-1401 | 33.3% | 1/3 |
| pr-1602 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 0.0% | 0/1 |
| pr-2095 | 0.0% | 0/1 |
| pr-2195 | 50.0% | 1/2 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 0.0% | 0/1 |
| pr-2483 | 100.0% | 1/1 |
| pr-2513 | 100.0% | 1/1 |
| pr-2781 | 100.0% | 1/1 |
| pr-2845 | 0.0% | 0/1 |
| pr-2997 | 100.0% | 1/1 |
| pr-3182 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3329 | 0.0% | 0/1 |
| pr-3555 | 100.0% | 1/1 |
| pr-3636 | 66.7% | 2/3 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 100.0% | 5/5 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 100.0% | 1/1 |
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4426 | 100.0% | 1/1 |
| pr-4533 | 0.0% | 0/1 |
| pr-4750 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 2/2 |
| pr-5182 | 50.0% | 1/2 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 0.0% | 0/1 |
| pr-5700 | 100.0% | 1/1 |

## 未解决 Case

```json
[
  {"pr": 1242, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1323, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 1401, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1602, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1679, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1694, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1907, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 1931, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2095, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2195, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 2246, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2351, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2513, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 2781, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 2845, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 3307, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3329, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 3636, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3753, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 3867, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3907, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4110, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 4166, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4179, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 4442, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4533, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 4750, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 4943, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5496, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"},  {"pr": 5687, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 5700, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 8
  logic: 10
  spec: 4
  sw_hw_config: 3
  timing_sync: 5
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=54
  prompt_k: 992.9
  completion_k: 4.3
  cache_hit_pct: 95.4
  tool_calls: 25.9
  cost_usd: 0.015380
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| XiangShan-pr-1242__5KzT2Ph | patch_submitted | 1190.5 | 5.1 | 0.0199 | 95.6 | 33 |
| XiangShan-pr-1323__oiRAGL5 | patch_submitted | 1422.2 | 6.3 | 0.0158 | 96.7 | 55 |
| XiangShan-pr-1395__N5hYs3a | patch_submitted | 225.0 | 2.7 | 0.0085 | 87.8 | 13 |
| XiangShan-pr-1401__oxAmQL9 | patch_submitted | 4866.3 | 10.7 | 0.0398 | 98.6 | 77 |
| XiangShan-pr-1602__TEoYSut | patch_submitted | 2605.7 | 6.6 | 0.0350 | 96.7 | 40 |
| XiangShan-pr-1679__RL7P7td | patch_submitted | 1088.8 | 4.5 | 0.0205 | 96.0 | 26 |
| XiangShan-pr-1694__kjQS9xk | patch_submitted | 885.2 | 4.2 | 0.0171 | 93.8 | 17 |
| XiangShan-pr-1793__X453Qri | patch_submitted | 197.6 | 3.0 | 0.0051 | 88.2 | 14 |
| XiangShan-pr-1820__Kzaz825 | patch_submitted | 1018.7 | 6.1 | 0.0145 | 94.9 | 28 |
| XiangShan-pr-1907__RedhWz9 | patch_submitted | 370.3 | 2.6 | 0.0083 | 92.9 | 16 |
| XiangShan-pr-1931__22swoon | patch_submitted | 591.4 | 3.1 | 0.0144 | 91.0 | 17 |
| XiangShan-pr-2095__NC95pcR | patch_submitted | 143.6 | 2.4 | 0.0058 | 84.8 | 7 |
| XiangShan-pr-2195__LLAwGmJ | patch_submitted | 950.6 | 3.9 | 0.0112 | 95.4 | 27 |
| XiangShan-pr-2246__tdA7hgj | patch_submitted | 889.8 | 3.3 | 0.0096 | 95.7 | 29 |
| XiangShan-pr-2351__5vzZkK9 | patch_submitted | 942.0 | 4.0 | 0.0259 | 92.1 | 17 |
| XiangShan-pr-2483__aLPSBhz | patch_submitted | 286.4 | 2.7 | 0.0054 | 92.6 | 12 |
| XiangShan-pr-2513__vPYGoiG | patch_submitted | 1035.4 | 5.1 | 0.0122 | 95.7 | 25 |
| XiangShan-pr-2781__kr3ytdi | patch_submitted | 337.6 | 1.9 | 0.0093 | 88.3 | 13 |
| XiangShan-pr-281__tnfXjnk | patch_submitted | 98.2 | 1.0 | 0.0033 | 86.1 | 7 |
| XiangShan-pr-2845__Ro3A2Tc | patch_submitted | 191.6 | 2.7 | 0.0055 | 87.2 | 9 |
| XiangShan-pr-2997__6CyjBY5 | patch_submitted | 1166.0 | 4.2 | 0.0192 | 95.8 | 31 |
| XiangShan-pr-3182__KcvfGDU | patch_submitted | 1091.7 | 6.2 | 0.0209 | 91.0 | 33 |
| XiangShan-pr-3307__hceGmfZ | patch_submitted | 516.0 | 2.9 | 0.0101 | 95.6 | 24 |
| XiangShan-pr-3329__RpnYCdd | patch_submitted | 1163.6 | 4.7 | 0.0154 | 96.4 | 31 |
| XiangShan-pr-3555__h3YrmDH | patch_submitted | 1055.1 | 3.5 | 0.0164 | 94.7 | 27 |
| XiangShan-pr-3636__GH2aC7G | patch_submitted | 2186.1 | 5.7 | 0.0250 | 97.4 | 42 |
| XiangShan-pr-3717__5a7dBcP | patch_submitted | 223.5 | 2.1 | 0.0066 | 87.7 | 9 |
| XiangShan-pr-3753__HgaJMsE | patch_submitted | 620.3 | 4.7 | 0.0159 | 90.8 | 14 |
| XiangShan-pr-3859__cVcBqGV | patch_submitted | 3060.3 | 7.5 | 0.0285 | 97.2 | 50 |
| XiangShan-pr-3867__FnvQcx5 | patch_submitted | 1953.9 | 6.5 | 0.0213 | 97.2 | 38 |
| XiangShan-pr-3907__4XJuDuK | patch_submitted | 442.5 | 2.9 | 0.0070 | 92.7 | 20 |
| XiangShan-pr-3955__cZV8Cmy | patch_submitted | 877.9 | 5.9 | 0.0129 | 95.3 | 30 |
| XiangShan-pr-39__ec9ALAz | patch_submitted | 380.9 | 2.0 | 0.0115 | 90.2 | 12 |
| XiangShan-pr-4110__gPf2dDM | patch_submitted | 913.1 | 4.1 | 0.0135 | 96.2 | 38 |
| XiangShan-pr-4166__XKnsrYq | patch_submitted | 2652.6 | 8.0 | 0.0272 | 97.7 | 57 |
| XiangShan-pr-4179__4x2pDPV | patch_submitted | 1107.9 | 4.3 | 0.0118 | 96.5 | 31 |
| XiangShan-pr-4337__jti8Rg3 | patch_submitted | 274.4 | 3.1 | 0.0088 | 87.9 | 13 |
| XiangShan-pr-4426__X26LQ9S | patch_submitted | 457.2 | 3.7 | 0.0123 | 91.4 | 16 |
| XiangShan-pr-4442__B8Zpoir | patch_submitted | 323.6 | 3.0 | 0.0107 | 84.5 | 13 |
| XiangShan-pr-4533__fLeXj7Q | patch_submitted | 448.9 | 3.3 | 0.0132 | 92.4 | 14 |
| XiangShan-pr-4750__cFFA9op | patch_submitted | 2240.2 | 4.9 | 0.0298 | 96.5 | 34 |
| XiangShan-pr-4764__i5YkFms | patch_submitted | 716.3 | 4.5 | 0.0106 | 93.7 | 28 |
| XiangShan-pr-4943__jpSdy3F | patch_submitted | 843.8 | 5.6 | 0.0127 | 94.0 | 38 |
| XiangShan-pr-4959__xVFqiov | patch_submitted | 1099.9 | 6.4 | 0.0164 | 95.3 | 36 |
| XiangShan-pr-4968__DSyqiEF | patch_submitted | 2340.0 | 7.2 | 0.0277 | 96.5 | 39 |
| XiangShan-pr-5080__nVvQBcv | patch_submitted | 150.4 | 0.7 | 0.0197 | 81.5 | 7 |
| XiangShan-pr-5182__QJZk2SS | patch_submitted | 906.6 | 5.1 | 0.0140 | 94.2 | 31 |
| XiangShan-pr-5189__Zi8XyaP | patch_submitted | 1244.4 | 6.0 | 0.0228 | 95.6 | 41 |
| XiangShan-pr-5496__DyZfePT | patch_submitted | 236.6 | 2.5 | 0.0049 | 91.5 | 15 |
| XiangShan-pr-5593__fWesgkS | patch_submitted | 361.3 | 2.7 | 0.0086 | 91.0 | 14 |

