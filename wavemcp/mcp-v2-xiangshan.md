# XiangShan MCP V2 Analysis

## 总体结果

```yaml
mcp_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES (WAVES_ENABLED=true, no skills)
  resolved: 35
  total: 53
  resolved_rate: 66.0%
  file_level_precision: 95.24%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | MCP V2 |
|------|:-----------:|:------:|
| Resolved Rate | 32/53 (60.4%) | 35/53 (66.0%) |
| File-Level Precision | 93.64% | 95.24% |

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
| pr-1401 | 100.0% | 5/5 |
| pr-1602 | 100.0% | 19/19 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 1/1 |
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
| pr-3636 | 100.0% | 3/3 |
| pr-3717 | 100.0% | 1/1 |
| pr-3753 | 100.0% | 1/1 |
| pr-3859 | 100.0% | 5/5 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 100.0% | 1/1 |
| pr-4166 | 60.0% | 3/5 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/1 |
| pr-4943 | 100.0% | 8/8 |
| pr-4959 | 100.0% | 2/2 |
| pr-4968 | 90.0% | 9/10 |
| pr-5080 | 100.0% | 1/1 |
| pr-5182 | 50.0% | 1/2 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 95.2%
- **Average (per-task)**: 96.2%

## 未解决 Case

| PR |
|----|
| pr-655 |
| pr-1242 |
| pr-1323 |
| pr-1401 |
| pr-1694 |
| pr-1907 |
| pr-2195 |
| pr-2246 |
| pr-3307 |
| pr-4166 |
| pr-4426 |
| pr-4442 |
| pr-4533 |
| pr-4943 |
| pr-5182 |
| pr-5189 |
| pr-5496 |
| pr-5687 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 2876.7
  completion_k: 30.2
  cache_hit_pct: 96.2
  tool_calls: 45.0
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 45.0
  cost_usd: 0.043177
  tasks: 53
  resolved: 35
  unresolved: 18
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------------|----------|
| XiangShan-pr-39__FoCZyXD | patch_submitted | 278.7 | 11.5 | 0.0110 | 92.1 | 16 | 0 | 0 | 16 |
| XiangShan-pr-281__VQe6jFQ | patch_submitted | 234.2 | 6.5 | 0.0062 | 95.2 | 16 | 0 | 0 | 16 |
| XiangShan-pr-655__6FRo57S | patch_submitted | 3147.6 | 46.6 | 0.0486 | 97.6 | 48 | 0 | 0 | 48 |
| XiangShan-pr-739__XCgAbVt | patch_submitted | 5251.6 | 65.8 | 0.0830 | 96.4 | 70 | 0 | 0 | 70 |
| XiangShan-pr-1242__NvAVPk8 | patch_submitted | 1277.4 | 21.5 | 0.0314 | 92.2 | 41 | 0 | 0 | 41 |
| XiangShan-pr-1323__p3zaVep | patch_submitted | 2616.2 | 18.8 | 0.0406 | 94.4 | 58 | 0 | 0 | 58 |
| XiangShan-pr-1395__SqguHAw | patch_submitted | 2032.4 | 16.4 | 0.0268 | 96.4 | 37 | 0 | 0 | 37 |
| XiangShan-pr-1401__smVejZ7 | patch_submitted | 9318.4 | 39.8 | 0.0898 | 97.3 | 98 | 0 | 0 | 98 |
| XiangShan-pr-1602__mGE7haE | patch_submitted | 7713.0 | 51.0 | 0.0722 | 98.4 | 82 | 0 | 0 | 82 |
| XiangShan-pr-1679__DoLwwTF | patch_submitted | 3202.0 | 33.1 | 0.0411 | 97.5 | 56 | 0 | 0 | 56 |
| XiangShan-pr-1694__BdcAnGJ | patch_submitted | 790.7 | 20.6 | 0.0204 | 95.2 | 23 | 0 | 0 | 23 |
| XiangShan-pr-1793__3hQQ2KL | patch_submitted | 1625.0 | 24.5 | 0.0283 | 96.3 | 37 | 0 | 0 | 37 |
| XiangShan-pr-1820__tDKFADg | patch_submitted | 522.8 | 13.3 | 0.0162 | 91.4 | 25 | 0 | 0 | 25 |
| XiangShan-pr-1907__uSvvH6Q | patch_submitted | 1378.5 | 27.8 | 0.0382 | 91.4 | 30 | 0 | 0 | 30 |
| XiangShan-pr-1931__b7KFTvX | patch_submitted | 8323.5 | 92.9 | 0.1052 | 98.0 | 67 | 0 | 0 | 67 |
| XiangShan-pr-2095__iM686Pr | patch_submitted | 795.2 | 13.8 | 0.0162 | 95.3 | 26 | 0 | 0 | 26 |
| XiangShan-pr-2195__WbZaQYi | patch_submitted | 1055.4 | 10.8 | 0.0154 | 96.3 | 38 | 0 | 0 | 38 |
| XiangShan-pr-2246__cQ6D2Tk | patch_submitted | 3451.1 | 17.5 | 0.0410 | 96.0 | 68 | 0 | 0 | 68 |
| XiangShan-pr-2351__kcR93kv | patch_submitted | 6910.1 | 49.9 | 0.0753 | 97.6 | 60 | 0 | 0 | 60 |
| XiangShan-pr-2483__XpDfj4q | patch_submitted | 174.3 | 4.2 | 0.0051 | 92.1 | 16 | 0 | 0 | 16 |
| XiangShan-pr-2513__LgEza9Q | patch_submitted | 854.2 | 17.0 | 0.0170 | 96.6 | 27 | 0 | 0 | 27 |
| XiangShan-pr-2781__jZz8RFL | patch_submitted | 1612.2 | 27.1 | 0.0267 | 97.6 | 45 | 0 | 0 | 45 |
| XiangShan-pr-2845__bJTqddU | patch_submitted | 524.0 | 7.0 | 0.0097 | 94.8 | 28 | 0 | 0 | 28 |
| XiangShan-pr-2997__imt53ox | patch_submitted | 2096.2 | 33.1 | 0.0363 | 96.7 | 40 | 0 | 0 | 40 |
| XiangShan-pr-3182__cofiUAk | patch_submitted | 2078.6 | 18.2 | 0.0332 | 94.7 | 47 | 0 | 0 | 47 |
| XiangShan-pr-3307__Q7To7UH | patch_submitted | 2602.1 | 27.1 | 0.0450 | 94.6 | 49 | 0 | 0 | 49 |
| XiangShan-pr-3329__J5ViyZb | patch_submitted | 1386.9 | 20.9 | 0.0255 | 95.7 | 39 | 0 | 0 | 39 |
| XiangShan-pr-3555__iewrCJP | patch_submitted | 588.3 | 15.8 | 0.0178 | 92.4 | 20 | 0 | 0 | 20 |
| XiangShan-pr-3636__H7Qpbaq | patch_submitted | 3280.4 | 38.0 | 0.0446 | 97.5 | 43 | 0 | 0 | 43 |
| XiangShan-pr-3717__3eSyFuB | patch_submitted | 2627.2 | 52.6 | 0.0648 | 93.4 | 38 | 0 | 0 | 38 |
| XiangShan-pr-3753__KEjrd6K | patch_submitted | 1857.2 | 39.6 | 0.0411 | 95.7 | 27 | 0 | 0 | 27 |
| XiangShan-pr-3859__uTrsCEY | patch_submitted | 8871.9 | 37.7 | 0.0730 | 98.2 | 85 | 0 | 0 | 85 |
| XiangShan-pr-3867__ZRXARdy | patch_submitted | 3237.6 | 35.0 | 0.0457 | 96.8 | 47 | 0 | 0 | 47 |
| XiangShan-pr-3907__yBwdCst | patch_submitted | 143.0 | 1.9 | 0.0053 | 82.8 | 11 | 0 | 0 | 11 |
| XiangShan-pr-3955__HKXJfWh | patch_submitted | 1186.4 | 25.1 | 0.0258 | 95.9 | 36 | 0 | 0 | 36 |
| XiangShan-pr-4110__7Xebze3 | patch_submitted | 2849.0 | 20.4 | 0.0375 | 96.0 | 41 | 0 | 0 | 41 |
| XiangShan-pr-4166__yRCkiSU | patch_submitted | 4453.1 | 36.3 | 0.0634 | 95.8 | 65 | 0 | 0 | 65 |
| XiangShan-pr-4179__NgM67hX | patch_submitted | 2098.7 | 26.2 | 0.0447 | 92.7 | 41 | 0 | 0 | 41 |
| XiangShan-pr-4337__CnzdwsZ | patch_submitted | 2705.6 | 47.9 | 0.0465 | 97.6 | 46 | 0 | 0 | 46 |
| XiangShan-pr-4426__vb8QaP5 | patch_submitted | 1738.6 | 31.1 | 0.0535 | 88.4 | 26 | 0 | 0 | 26 |
| XiangShan-pr-4442__AMHMwVL | patch_submitted | 1798.1 | 33.5 | 0.0361 | 96.0 | 25 | 0 | 0 | 25 |
| XiangShan-pr-4533__XXAG6WR | patch_submitted | 703.1 | 28.2 | 0.0332 | 86.3 | 19 | 0 | 0 | 19 |
| XiangShan-pr-4750__5Pk5YVm | patch_submitted | 2183.2 | 39.6 | 0.0431 | 96.0 | 46 | 0 | 0 | 46 |
| XiangShan-pr-4764__DRayCqY | patch_submitted | 876.9 | 9.2 | 0.0185 | 92.0 | 35 | 0 | 0 | 35 |
| XiangShan-pr-4943__RHFjZvz | patch_submitted | 5302.7 | 22.3 | 0.0559 | 96.6 | 80 | 0 | 0 | 80 |
| XiangShan-pr-4959__nnnWQ4f | patch_submitted | 2204.1 | 25.6 | 0.0407 | 94.2 | 46 | 0 | 0 | 46 |
| XiangShan-pr-4968__qYDHs7J | patch_submitted | 4639.2 | 20.6 | 0.0589 | 95.5 | 82 | 0 | 0 | 82 |
| XiangShan-pr-5080__QwgFw5i | patch_submitted | 8119.5 | 78.9 | 0.1299 | 95.4 | 87 | 0 | 0 | 87 |
| XiangShan-pr-5182__mWvwBMx | patch_submitted | 2284.9 | 21.5 | 0.0395 | 94.2 | 41 | 0 | 0 | 41 |
| XiangShan-pr-5189__UtpYUpq | patch_submitted | 10036.3 | 70.1 | 0.1055 | 97.7 | 92 | 0 | 0 | 92 |
| XiangShan-pr-5496__nmJ8ccQ | patch_submitted | 5394.5 | 56.1 | 0.0991 | 94.0 | 70 | 0 | 0 | 70 |
| XiangShan-pr-5593__pZfWzRW | patch_submitted | 1587.9 | 22.6 | 0.0392 | 91.2 | 29 | 0 | 0 | 29 |
| XiangShan-pr-5687__r6jFihU | patch_submitted | 1918.4 | 29.7 | 0.0315 | 97.2 | 38 | 0 | 0 | 38 |
| XiangShan-pr-5700__iGNrwpr | patch_submitted | 1403.8 | 26.5 | 0.0312 | 94.6 | 29 | 0 | 0 | 29 |

