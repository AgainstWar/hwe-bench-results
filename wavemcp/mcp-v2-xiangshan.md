# XiangShan MCP V2 Analysis

## 总体结果

```yaml
mcp_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES (WAVES_ENABLED=true, no skills)
  resolved: 25
  total: 53
  resolved_rate: 47.2%
  file_level_precision: 96.23%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | MCP V2 |
|------|:-----------:|:------:|
| Resolved Rate | 32/53 (60.4%) | 25/53 (47.2%) |
| File-Level Precision | 93.64% | 96.23% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 1/1 |
| pr-739 | 100.0% | 1/1 |
| pr-1242 | 100.0% | 6/6 |
| pr-1323 | 50.0% | 1/2 |
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
| pr-4166 | 100.0% | 4/4 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/3 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 8/8 |
| pr-5080 | 100.0% | 1/1 |
| pr-5182 | 100.0% | 1/1 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 96.2%
- **Average (per-task)**: 97.2%

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
| pr-3753 |
| pr-3907 |
| pr-4166 |
| pr-4179 |
| pr-4337 |
| pr-4426 |
| pr-4442 |
| pr-4533 |
| pr-4764 |
| pr-4943 |
| pr-4959 |
| pr-4968 |
| pr-5080 |
| pr-5182 |
| pr-5189 |
| pr-5496 |
| pr-5593 |
| pr-5687 |
| pr-5700 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 3335.6
  completion_k: 33.0
  cache_hit_pct: 97.4
  tool_calls: 47.7
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 47.7
  cost_usd: 0.042657
  tasks: 53
  resolved: 25
  unresolved: 28
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------------|----------|
| XiangShan-pr-39__FoCZyXD | patch_submitted | 278.7 | 11.5 | 0.0110 | 92.1 | 16 | 0 | 0 | 16 |
| XiangShan-pr-281__VQe6jFQ | patch_submitted | 234.2 | 6.5 | 0.0062 | 95.2 | 16 | 0 | 0 | 16 |
| XiangShan-pr-655__TtAtaX8 | patch_submitted | 8245.4 | 81.6 | 0.0888 | 98.8 | 80 | 0 | 0 | 80 |
| XiangShan-pr-739__XCgAbVt | patch_submitted | 5251.6 | 65.8 | 0.0830 | 96.4 | 70 | 0 | 0 | 70 |
| XiangShan-pr-1242__qw8K7Zb | patch_submitted | 12679.8 | 80.2 | 0.1032 | 99.1 | 128 | 0 | 0 | 128 |
| XiangShan-pr-1323__ywxF8Un | patch_submitted | 2233.7 | 22.6 | 0.0298 | 97.1 | 37 | 0 | 0 | 37 |
| XiangShan-pr-1395__SqguHAw | patch_submitted | 2032.4 | 16.4 | 0.0268 | 96.4 | 37 | 0 | 0 | 37 |
| XiangShan-pr-1401__DKivnYy | patch_submitted | 15472.4 | 88.1 | 0.1231 | 99.0 | 100 | 0 | 0 | 100 |
| XiangShan-pr-1602__mGE7haE | patch_submitted | 7713.0 | 51.0 | 0.0722 | 98.4 | 82 | 0 | 0 | 82 |
| XiangShan-pr-1679__DoLwwTF | patch_submitted | 3202.0 | 33.1 | 0.0411 | 97.5 | 56 | 0 | 0 | 56 |
| XiangShan-pr-1694__Wb5MKG8 | patch_submitted | 2519.5 | 24.3 | 0.0312 | 97.6 | 54 | 0 | 0 | 54 |
| XiangShan-pr-1793__3hQQ2KL | patch_submitted | 1625.0 | 24.5 | 0.0283 | 96.3 | 37 | 0 | 0 | 37 |
| XiangShan-pr-1820__tDKFADg | patch_submitted | 522.8 | 13.3 | 0.0162 | 91.4 | 25 | 0 | 0 | 25 |
| XiangShan-pr-1907__DfkSteh | patch_submitted | 1441.8 | 26.1 | 0.0305 | 95.0 | 31 | 0 | 0 | 31 |
| XiangShan-pr-1931__b7KFTvX | patch_submitted | 8323.5 | 92.9 | 0.1052 | 98.0 | 67 | 0 | 0 | 67 |
| XiangShan-pr-2095__iM686Pr | patch_submitted | 795.2 | 13.8 | 0.0162 | 95.3 | 26 | 0 | 0 | 26 |
| XiangShan-pr-2195__bqnNYwY | patch_submitted | 1055.5 | 13.0 | 0.0174 | 95.9 | 30 | 0 | 0 | 30 |
| XiangShan-pr-2246__7hYqWR6 | patch_submitted | 2081.9 | 15.5 | 0.0260 | 96.6 | 49 | 0 | 0 | 49 |
| XiangShan-pr-2351__kcR93kv | patch_submitted | 6910.1 | 49.9 | 0.0753 | 97.6 | 60 | 0 | 0 | 60 |
| XiangShan-pr-2483__XpDfj4q | patch_submitted | 174.3 | 4.2 | 0.0051 | 92.1 | 16 | 0 | 0 | 16 |
| XiangShan-pr-2513__LgEza9Q | patch_submitted | 854.2 | 17.0 | 0.0170 | 96.6 | 27 | 0 | 0 | 27 |
| XiangShan-pr-2781__jZz8RFL | patch_submitted | 1612.2 | 27.1 | 0.0267 | 97.6 | 45 | 0 | 0 | 45 |
| XiangShan-pr-2845__bJTqddU | patch_submitted | 524.0 | 7.0 | 0.0097 | 94.8 | 28 | 0 | 0 | 28 |
| XiangShan-pr-2997__imt53ox | patch_submitted | 2096.2 | 33.1 | 0.0363 | 96.7 | 40 | 0 | 0 | 40 |
| XiangShan-pr-3182__cofiUAk | patch_submitted | 2078.6 | 18.2 | 0.0332 | 94.7 | 47 | 0 | 0 | 47 |
| XiangShan-pr-3307__88zLzYx | patch_submitted | 1820.6 | 23.6 | 0.0407 | 92.1 | 28 | 0 | 0 | 28 |
| XiangShan-pr-3329__J5ViyZb | patch_submitted | 1386.9 | 20.9 | 0.0255 | 95.7 | 39 | 0 | 0 | 39 |
| XiangShan-pr-3555__iewrCJP | patch_submitted | 588.3 | 15.8 | 0.0178 | 92.4 | 20 | 0 | 0 | 20 |
| XiangShan-pr-3636__H7Qpbaq | patch_submitted | 3280.4 | 38.0 | 0.0446 | 97.5 | 43 | 0 | 0 | 43 |
| XiangShan-pr-3717__3eSyFuB | patch_submitted | 2627.2 | 52.6 | 0.0648 | 93.4 | 38 | 0 | 0 | 38 |
| XiangShan-pr-3753__7KmfQfn | patch_submitted | 7010.9 | 103.8 | 0.1181 | 96.6 | 63 | 0 | 0 | 63 |
| XiangShan-pr-3859__uTrsCEY | patch_submitted | 8871.9 | 37.7 | 0.0730 | 98.2 | 85 | 0 | 0 | 85 |
| XiangShan-pr-3867__ZRXARdy | patch_submitted | 3237.6 | 35.0 | 0.0457 | 96.8 | 47 | 0 | 0 | 47 |
| XiangShan-pr-3907__TvjcQqd | patch_submitted | 151.7 | 3.0 | 0.0043 | 90.8 | 11 | 0 | 0 | 11 |
| XiangShan-pr-3955__HKXJfWh | patch_submitted | 1186.4 | 25.1 | 0.0258 | 95.9 | 36 | 0 | 0 | 36 |
| XiangShan-pr-4110__7Xebze3 | patch_submitted | 2849.0 | 20.4 | 0.0375 | 96.0 | 41 | 0 | 0 | 41 |
| XiangShan-pr-4166__jYfVBay | patch_submitted | 2707.0 | 21.6 | 0.0435 | 94.4 | 53 | 0 | 0 | 53 |
| XiangShan-pr-4179__qEpCtGP | patch_submitted | 1633.3 | 19.7 | 0.0261 | 96.1 | 39 | 0 | 0 | 39 |
| XiangShan-pr-4337__uKRCAR4 | patch_submitted | 2216.8 | 42.9 | 0.0397 | 97.8 | 41 | 0 | 0 | 41 |
| XiangShan-pr-4426__Exr3hek | patch_submitted | 1790.4 | 30.5 | 0.0354 | 95.5 | 27 | 0 | 0 | 27 |
| XiangShan-pr-4442__r5Y9WZ4 | patch_submitted | 2116.1 | 31.9 | 0.0439 | 94.1 | 33 | 0 | 0 | 33 |
| XiangShan-pr-4533__z63Ws6y | patch_submitted | 459.2 | 19.9 | 0.0185 | 92.3 | 16 | 0 | 0 | 16 |
| XiangShan-pr-4750__5Pk5YVm | patch_submitted | 2183.2 | 39.6 | 0.0431 | 96.0 | 46 | 0 | 0 | 46 |
| XiangShan-pr-4764__dc3NEh2 | patch_submitted | 1285.5 | 13.0 | 0.0222 | 94.5 | 36 | 0 | 0 | 36 |
| XiangShan-pr-4943__8eJ9qEb | patch_submitted | 11474.1 | 52.6 | 0.0857 | 98.8 | 125 | 0 | 0 | 125 |
| XiangShan-pr-4959__7tVMDAc | patch_submitted | 1484.7 | 33.3 | 0.0333 | 95.9 | 34 | 0 | 0 | 34 |
| XiangShan-pr-4968__3qSWRyy | patch_submitted | 11561.4 | 46.6 | 0.0930 | 98.2 | 122 | 0 | 0 | 122 |
| XiangShan-pr-5080__qJfQmQ3 | patch_submitted | 822.7 | 21.9 | 0.0220 | 94.7 | 26 | 0 | 0 | 26 |
| XiangShan-pr-5182__u3t7a8y | patch_submitted | 1713.0 | 18.4 | 0.0251 | 96.4 | 37 | 0 | 0 | 37 |
| XiangShan-pr-5189__5d2tXsy | patch_submitted | 7948.3 | 48.5 | 0.0768 | 98.0 | 100 | 0 | 0 | 100 |
| XiangShan-pr-5496__GHgACb2 | patch_submitted | 2649.3 | 25.9 | 0.0312 | 98.0 | 80 | 0 | 0 | 80 |
| XiangShan-pr-5593__mXsABoj | patch_submitted | 1200.1 | 31.9 | 0.0342 | 93.5 | 27 | 0 | 0 | 27 |
| XiangShan-pr-5687__MpjVrV7 | patch_submitted | 1491.3 | 29.9 | 0.0291 | 97.0 | 39 | 0 | 0 | 39 |
| XiangShan-pr-5700__uMRchaW | patch_submitted | 2417.0 | 39.5 | 0.0433 | 96.5 | 40 | 0 | 0 | 40 |

