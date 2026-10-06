# XiangShan Repair V2 Analysis

## 总体结果

```yaml
repair_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (hdl-minimal-repair, no MCP)
  resolved: 26
  total: 54
  resolved_rate: 48.1%
  file_level_precision: 98.18%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V2 |
|------|:-----------:|:---------:|
| Resolved Rate | 32/53 (60.4%) | 26/54 (48.1%) |
| File-Level Precision | 93.64% | 98.18% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 1/1 |
| pr-739 | 100.0% | 1/1 |
| pr-1242 | 100.0% | 6/6 |
| pr-1323 | 100.0% | 1/1 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 100.0% | 5/5 |
| pr-1602 | 100.0% | 18/18 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 1/1 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 50.0% | 1/2 |
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
| pr-3636 | 100.0% | 3/3 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 100.0% | 6/6 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 100.0% | 1/1 |
| pr-4166 | 100.0% | 4/4 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4750 | 100.0% | 2/2 |
| pr-4764 | 100.0% | 1/1 |
| pr-4943 | 100.0% | 8/8 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 90.0% | 9/10 |
| pr-5080 | 100.0% | 1/1 |
| pr-5182 | 100.0% | 1/1 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 98.2%
- **Average (per-task)**: 98.9%

## 未解决 Case

| PR |
|----|
| pr-655 |
| pr-1242 |
| pr-1323 |
| pr-1395 |
| pr-1401 |
| pr-1694 |
| pr-1907 |
| pr-1931 |
| pr-2195 |
| pr-2246 |
| pr-2997 |
| pr-3307 |
| pr-3329 |
| pr-3636 |
| pr-3859 |
| pr-3907 |
| pr-3955 |
| pr-4110 |
| pr-4166 |
| pr-4426 |
| pr-4442 |
| pr-4533 |
| pr-4750 |
| pr-4764 |
| pr-4943 |
| pr-5189 |
| pr-5496 |
| pr-5593 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 2821.2
  completion_k: 14.7
  cache_hit_pct: 97.5
  tool_calls: 49.6
  mcp_calls: 0.0
  repair_skill_calls: 1.0
  ordinary_calls: 48.6
  cost_usd: 0.035370
  tasks: 54
  resolved: 26
  unresolved: 28
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| XiangShan-pr-39__Q2MupR7 | patch_submitted | 1711.7 | 26.5 | 0.0381 | 94.0 | 43 | 0 | 1 | 42 |
| XiangShan-pr-281__bcnkyc5 | patch_submitted | 2118.1 | 4.4 | 0.0474 | 94.7 | 49 | 0 | 1 | 48 |
| XiangShan-pr-655__NErDHed | patch_submitted | 7878.3 | 9.1 | 0.0767 | 98.4 | 77 | 0 | 1 | 76 |
| XiangShan-pr-739__ZiWkHCC | patch_submitted | 1470.3 | 5.1 | 0.0220 | 96.9 | 45 | 0 | 1 | 44 |
| XiangShan-pr-1242__xRtMWG8 | patch_submitted | 7491.8 | 11.7 | 0.0709 | 98.6 | 92 | 0 | 1 | 91 |
| XiangShan-pr-1323__g6WnqYQ | patch_submitted | 2722.3 | 7.3 | 0.0344 | 97.7 | 68 | 0 | 1 | 67 |
| XiangShan-pr-1395__EEdXwo8 | patch_submitted | 900.6 | 3.6 | 0.0179 | 94.0 | 30 | 0 | 1 | 29 |
| XiangShan-pr-1401__X5bJKxD | patch_submitted | 2453.5 | 5.8 | 0.0357 | 96.7 | 51 | 0 | 1 | 50 |
| XiangShan-pr-1602__5WT4k42 | patch_submitted | 16505.5 | 19.4 | 0.1147 | 99.0 | 133 | 0 | 1 | 132 |
| XiangShan-pr-1679__vmVAybf | patch_submitted | 727.5 | 15.2 | 0.0216 | 90.3 | 26 | 0 | 1 | 25 |
| XiangShan-pr-1694__UtL2p2D | patch_submitted | 2609.6 | 6.6 | 0.0318 | 97.8 | 57 | 0 | 1 | 56 |
| XiangShan-pr-1793__cSfMrN8 | patch_submitted | 930.0 | 22.3 | 0.0222 | 95.6 | 31 | 0 | 1 | 30 |
| XiangShan-pr-1820__geWhnUq | patch_submitted | 1445.3 | 37.6 | 0.0312 | 98.0 | 44 | 0 | 1 | 43 |
| XiangShan-pr-1907__FDexrHR | patch_submitted | 1752.9 | 4.7 | 0.0292 | 95.2 | 35 | 0 | 1 | 34 |
| XiangShan-pr-1931__cSvsVYQ | patch_submitted | 1990.2 | 4.9 | 0.0334 | 95.3 | 40 | 0 | 1 | 39 |
| XiangShan-pr-2095__3YGRbPD | patch_submitted | 1992.3 | 21.9 | 0.0252 | 97.9 | 59 | 0 | 1 | 58 |
| XiangShan-pr-2195__6Ye2ufV | patch_submitted | 1555.9 | 4.7 | 0.0259 | 96.9 | 40 | 0 | 1 | 39 |
| XiangShan-pr-2246__9YU9Nrz | patch_submitted | 6106.1 | 11.6 | 0.0538 | 98.4 | 96 | 0 | 1 | 95 |
| XiangShan-pr-2351__Ya7RsBS | patch_submitted | 12261.2 | 78.3 | 0.1003 | 99.1 | 102 | 0 | 1 | 101 |
| XiangShan-pr-2483__xPBbw5h | patch_submitted | 370.1 | 7.4 | 0.0085 | 94.6 | 22 | 0 | 1 | 21 |
| XiangShan-pr-2513__ohzpt3i | patch_submitted | 477.8 | 11.5 | 0.0118 | 95.1 | 20 | 0 | 1 | 19 |
| XiangShan-pr-2781__u6yYZ6o | patch_submitted | 6045.1 | 52.6 | 0.0595 | 98.9 | 99 | 0 | 1 | 98 |
| XiangShan-pr-2845__kBXoaK2 | patch_submitted | 1249.9 | 4.0 | 0.0190 | 95.5 | 39 | 0 | 1 | 38 |
| XiangShan-pr-2997__T9DbKmZ | patch_submitted | 2359.5 | 5.2 | 0.0350 | 96.3 | 52 | 0 | 1 | 51 |
| XiangShan-pr-3182__KnTchFg | patch_submitted | 2339.4 | 30.8 | 0.0361 | 96.9 | 40 | 0 | 1 | 39 |
| XiangShan-pr-3307__qqRv4Pp | patch_submitted | 1292.6 | 4.8 | 0.0207 | 95.6 | 35 | 0 | 1 | 34 |
| XiangShan-pr-3329__Yj9H8Vm | patch_submitted | 1859.0 | 5.3 | 0.0318 | 96.7 | 41 | 0 | 1 | 40 |
| XiangShan-pr-3555__MxQEuXQ | patch_submitted | 1030.8 | 3.5 | 0.0181 | 94.3 | 35 | 0 | 1 | 34 |
| XiangShan-pr-3636__5jT58zw | patch_submitted | 1937.4 | 6.1 | 0.0297 | 95.7 | 44 | 0 | 1 | 43 |
| XiangShan-pr-3717__DyFdFNC | patch_submitted | 1510.2 | 27.9 | 0.0283 | 96.8 | 29 | 0 | 1 | 28 |
| XiangShan-pr-3753__8Rc9ya9 | patch_submitted | 4802.8 | 76.4 | 0.0693 | 98.7 | 58 | 0 | 1 | 57 |
| XiangShan-pr-3859__Nwu4QCL | patch_submitted | 3726.0 | 12.3 | 0.0417 | 97.7 | 87 | 0 | 1 | 86 |
| XiangShan-pr-3867__V3VHDZF | patch_submitted | 3167.2 | 31.3 | 0.0406 | 97.4 | 45 | 0 | 1 | 44 |
| XiangShan-pr-3907__k5hBsLP | patch_submitted | 453.6 | 2.4 | 0.0085 | 94.0 | 22 | 0 | 1 | 21 |
| XiangShan-pr-3955__qxw3wPB | patch_submitted | 1853.6 | 6.3 | 0.0321 | 96.4 | 50 | 0 | 1 | 49 |
| XiangShan-pr-4110__vYyH6kF | patch_submitted | 2605.4 | 5.1 | 0.0339 | 96.4 | 50 | 0 | 1 | 49 |
| XiangShan-pr-4166__nqD7vjQ | patch_submitted | 4203.9 | 8.8 | 0.0426 | 97.5 | 68 | 0 | 1 | 67 |
| XiangShan-pr-4179__hHHX4F2 | patch_submitted | 2386.4 | 4.7 | 0.0312 | 96.1 | 42 | 0 | 1 | 41 |
| XiangShan-pr-4337__3oEP7on | patch_submitted | 2769.7 | 28.6 | 0.0340 | 97.9 | 56 | 0 | 1 | 55 |
| XiangShan-pr-4426__rm8FBgW | patch_submitted | 2518.4 | 5.1 | 0.0395 | 95.1 | 38 | 0 | 1 | 37 |
| XiangShan-pr-4442__KbU9B3r | patch_submitted | 1158.0 | 3.3 | 0.0218 | 94.9 | 30 | 0 | 1 | 29 |
| XiangShan-pr-4533__qMKzjZv | patch_submitted | 1613.0 | 6.6 | 0.0268 | 97.3 | 44 | 0 | 1 | 43 |
| XiangShan-pr-4750__dtCHbd6 | patch_submitted | 3907.9 | 9.3 | 0.0457 | 97.7 | 63 | 0 | 1 | 62 |
| XiangShan-pr-4764__cjtjxGe | patch_submitted | 1129.2 | 3.2 | 0.0178 | 95.4 | 31 | 0 | 1 | 30 |
| XiangShan-pr-4943__ovRGQwM | patch_submitted | 3543.2 | 9.7 | 0.0458 | 96.4 | 64 | 0 | 1 | 63 |
| XiangShan-pr-4959__6ATgM6S | patch_submitted | 1515.5 | 28.1 | 0.0286 | 96.8 | 34 | 0 | 1 | 33 |
| XiangShan-pr-4968__WGu7Hnj | patch_submitted | 5045.5 | 36.0 | 0.0492 | 98.3 | 62 | 0 | 1 | 61 |
| XiangShan-pr-5080__sfn4MDR | patch_submitted | 486.3 | 2.9 | 0.0189 | 94.2 | 22 | 0 | 1 | 21 |
| XiangShan-pr-5182__eZnyXe7 | patch_submitted | 2017.7 | 4.5 | 0.0238 | 96.7 | 38 | 0 | 1 | 37 |
| XiangShan-pr-5189__VtGkezw | patch_submitted | 3021.9 | 6.2 | 0.0375 | 97.1 | 55 | 0 | 1 | 54 |
| XiangShan-pr-5496__9uvoMch | patch_submitted | 1116.7 | 4.8 | 0.0183 | 96.4 | 41 | 0 | 1 | 40 |
| XiangShan-pr-5593__FtqkZod | patch_submitted | 1079.7 | 3.4 | 0.0201 | 95.9 | 28 | 0 | 1 | 27 |
| XiangShan-pr-5687__tnCntnb | patch_submitted | 1866.6 | 30.1 | 0.0330 | 96.6 | 38 | 0 | 1 | 37 |
| XiangShan-pr-5700__v42gH9M | patch_submitted | 1260.9 | 4.5 | 0.0187 | 96.4 | 38 | 0 | 1 | 37 |

