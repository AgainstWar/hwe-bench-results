# XiangShan Repair V3 Analysis

## 总体结果

```yaml
repair_v3:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (revised, hdl-minimal-repair)
  resolved: 31
  total: 53
  resolved_rate: 58.5%
  file_level_precision: 99.01%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V3 |
|------|:-----------:|:---------:|
| Resolved Rate | 32/53 (60.4%) | 31/53 (58.5%) |
| File-Level Precision | 93.64% | 99.01% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 2/2 |
| pr-739 | 100.0% | 1/1 |
| pr-1242 | 100.0% | 1/1 |
| pr-1323 | 100.0% | 1/1 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 100.0% | 5/5 |
| pr-1602 | 100.0% | 18/18 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 3/3 |
| pr-1793 | 100.0% | 3/3 |
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
| pr-4166 | 100.0% | 2/2 |
| pr-4179 | 100.0% | 2/2 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 100.0% | 1/1 |
| pr-4764 | 0.0% | 0/1 |
| pr-4943 | 100.0% | 6/6 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 9/9 |
| pr-5080 | 100.0% | 1/1 |
| pr-5182 | 100.0% | 1/1 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 99.0%
- **Average (per-task)**: 98.1%

## 未解决 Case

| PR |
|----|
| pr-655 |
| pr-1242 |
| pr-1323 |
| pr-1694 |
| pr-1907 |
| pr-2195 |
| pr-2246 |
| pr-3307 |
| pr-3867 |
| pr-4110 |
| pr-4166 |
| pr-4179 |
| pr-4426 |
| pr-4442 |
| pr-4533 |
| pr-4764 |
| pr-4943 |
| pr-5182 |
| pr-5189 |
| pr-5496 |
| pr-5593 |
| pr-5687 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 2359.0
  completion_k: 14.0
  cache_hit_pct: 0.0
  tool_calls: 45.7
  mcp_calls: 0.0
  repair_skill_calls: 1.6
  ordinary_calls: 44.1
  cost_usd: 0.035388
  tasks: 53
  resolved: 31
  unresolved: 22
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| XiangShan-pr-39__RArbaix | patch_submitted | 229.6 | 10.6 | 0.0103 | 90.3 | 13 | 0 | 2 | 11 |
| XiangShan-pr-281__ytXXQaf | patch_submitted | 174.2 | 1.3 | 0.0044 | 92.3 | 13 | 0 | 1 | 12 |
| XiangShan-pr-655__YXu79mM | patch_submitted | 6822.8 | 7.8 | 0.0753 | 97.6 | 76 | 0 | 1 | 75 |
| XiangShan-pr-739__MH5gZek | patch_submitted | 2452.4 | 7.1 | 0.0302 | 97.0 | 60 | 0 | 1 | 59 |
| XiangShan-pr-1242__U9AuNVb | patch_submitted | 4464.9 | 34.1 | 0.0466 | 98.2 | 72 | 0 | 1 | 71 |
| XiangShan-pr-1323__LaNuf7K | patch_submitted | 2244.0 | 19.6 | 0.0311 | 96.4 | 54 | 0 | 2 | 52 |
| XiangShan-pr-1395__rBZeMXg | patch_submitted | 975.4 | 5.2 | 0.0217 | 92.7 | 36 | 0 | 2 | 34 |
| XiangShan-pr-1401__Fs4VMY4 | patch_submitted | 5399.0 | 9.9 | 0.0519 | 97.6 | 76 | 0 | 2 | 74 |
| XiangShan-pr-1602__5DCoHFB | patch_submitted | 5871.3 | 51.7 | 0.0680 | 97.8 | 87 | 0 | 1 | 86 |
| XiangShan-pr-1679__RwJwneJ | patch_submitted | 1013.6 | 3.1 | 0.0368 | 84.5 | 32 | 0 | 2 | 30 |
| XiangShan-pr-1694__qC266mc | patch_submitted | 1121.7 | 3.5 | 0.0394 | 85.5 | 28 | 0 | 2 | 26 |
| XiangShan-pr-1793__gyvCbqs | patch_submitted | 3805.0 | 25.4 | 0.0620 | 94.8 | 61 | 0 | 2 | 59 |
| XiangShan-pr-1820__zCPrrtQ | patch_submitted | 536.6 | 2.3 | 0.0129 | 93.0 | 27 | 0 | 1 | 26 |
| XiangShan-pr-1907__RAU9RAy | patch_submitted | 8103.0 | 31.1 | 0.0674 | 98.3 | 100 | 0 | 1 | 99 |
| XiangShan-pr-1931__jfTu3wq | patch_submitted | 1833.2 | 8.5 | 0.0347 | 94.2 | 46 | 0 | 2 | 44 |
| XiangShan-pr-2095__ffzz8Yt | patch_submitted | 281.5 | 2.4 | 0.0104 | 85.9 | 19 | 0 | 2 | 17 |
| XiangShan-pr-2195__Jnwu2Hy | patch_submitted | 725.3 | 11.9 | 0.0156 | 94.2 | 31 | 0 | 1 | 30 |
| XiangShan-pr-2246__27KYE7W | patch_submitted | 4988.1 | 9.8 | 0.0537 | 97.8 | 84 | 0 | 1 | 83 |
| XiangShan-pr-2351__ckKdSVg | patch_submitted | 3550.1 | 7.1 | 0.0393 | 97.4 | 61 | 0 | 1 | 60 |
| XiangShan-pr-2483__GVmhJu7 | patch_submitted | 943.8 | 8.6 | 0.0206 | 92.5 | 42 | 0 | 2 | 40 |
| XiangShan-pr-2513__s2gmqGf | patch_submitted | 374.9 | 4.3 | 0.0118 | 88.4 | 16 | 0 | 1 | 15 |
| XiangShan-pr-2781__uGg9Vh5 | patch_submitted | 4276.4 | 27.8 | 0.0430 | 98.1 | 85 | 0 | 1 | 84 |
| XiangShan-pr-2845__PxFMdTd | patch_submitted | 930.8 | 15.4 | 0.0191 | 94.9 | 26 | 0 | 1 | 25 |
| XiangShan-pr-2997__DWaKRUX | patch_submitted | 6270.1 | 45.9 | 0.0805 | 96.7 | 60 | 0 | 2 | 58 |
| XiangShan-pr-3182__3ar4vM7 | patch_submitted | 1212.3 | 18.5 | 0.0222 | 95.8 | 39 | 0 | 2 | 37 |
| XiangShan-pr-3307__4KbcLe4 | patch_submitted | 1589.4 | 4.0 | 0.0242 | 95.6 | 35 | 0 | 2 | 33 |
| XiangShan-pr-3329__BGL9nX5 | patch_submitted | 1317.3 | 3.1 | 0.0347 | 88.3 | 35 | 0 | 2 | 33 |
| XiangShan-pr-3555__bcvXcuJ | patch_submitted | 1338.8 | 5.3 | 0.0307 | 90.0 | 38 | 0 | 1 | 37 |
| XiangShan-pr-3636__qBzUd8M | patch_submitted | 1649.2 | 5.4 | 0.0279 | 94.3 | 42 | 0 | 2 | 40 |
| XiangShan-pr-3717__ku5EJqY | patch_submitted | 815.6 | 2.4 | 0.0181 | 92.5 | 27 | 0 | 2 | 25 |
| XiangShan-pr-3753__bvCY5vd | patch_submitted | 2417.9 | 11.5 | 0.0473 | 93.4 | 50 | 0 | 2 | 48 |
| XiangShan-pr-3859__fDGuHLb | patch_submitted | 6503.4 | 10.8 | 0.0587 | 97.9 | 84 | 0 | 1 | 83 |
| XiangShan-pr-3867__brCorkS | patch_submitted | 2011.0 | 4.9 | 0.0305 | 95.9 | 45 | 0 | 2 | 43 |
| XiangShan-pr-3907__DM8Y6P5 | patch_submitted | 257.2 | 2.2 | 0.0052 | 95.3 | 20 | 0 | 1 | 19 |
| XiangShan-pr-3955__pibaBKR | patch_submitted | 1949.7 | 11.6 | 0.0367 | 94.4 | 51 | 0 | 2 | 49 |
| XiangShan-pr-4110__Puppwqr | patch_submitted | 2397.4 | 16.9 | 0.0382 | 94.8 | 46 | 0 | 2 | 44 |
| XiangShan-pr-4166__fge8vxT | patch_submitted | 4953.9 | 34.1 | 0.0493 | 98.1 | 74 | 0 | 2 | 72 |
| XiangShan-pr-4179__YV4g92C | patch_submitted | 1898.2 | 26.4 | 0.0370 | 94.7 | 40 | 0 | 2 | 38 |
| XiangShan-pr-4337__fPTeU2k | patch_submitted | 1000.5 | 4.4 | 0.0277 | 89.9 | 41 | 0 | 2 | 39 |
| XiangShan-pr-4426__5kyfCa7 | patch_submitted | 1265.9 | 3.1 | 0.0216 | 95.5 | 29 | 0 | 2 | 27 |
| XiangShan-pr-4442__KZUQgNV | patch_submitted | 1370.8 | 3.3 | 0.0245 | 94.5 | 31 | 0 | 2 | 29 |
| XiangShan-pr-4533__CxcAUWs | patch_submitted | 469.8 | 9.0 | 0.0209 | 85.9 | 22 | 0 | 2 | 20 |
| XiangShan-pr-4750__uKjhV47 | patch_submitted | 2320.4 | 21.8 | 0.0505 | 93.3 | 47 | 0 | 1 | 46 |
| XiangShan-pr-4764__QSPVDRQ | patch_submitted | 686.6 | 9.1 | 0.0140 | 93.8 | 25 | 0 | 2 | 23 |
| XiangShan-pr-4943__Jq38NH8 | patch_submitted | 10762.7 | 70.1 | 0.1479 | 95.4 | 125 | 0 | 2 | 123 |
| XiangShan-pr-4959__k9DMA2Z | patch_submitted | 455.1 | 2.8 | 0.0109 | 93.9 | 23 | 0 | 2 | 21 |
| XiangShan-pr-4968__kueq6YR | patch_submitted | 2437.3 | 6.8 | 0.0390 | 94.2 | 54 | 0 | 2 | 52 |
| XiangShan-pr-5080__6G3Viys | patch_submitted | 2255.9 | 51.1 | 0.0638 | 92.1 | 48 | 0 | 1 | 47 |
| XiangShan-pr-5182__ZbqcheB | patch_submitted | 1457.1 | 12.7 | 0.0279 | 93.2 | 33 | 0 | 1 | 32 |
| XiangShan-pr-5189__SpyTCDX | patch_submitted | 1536.9 | 4.4 | 0.0312 | 94.8 | 43 | 0 | 2 | 41 |
| XiangShan-pr-5496__ZYTMkVs | patch_submitted | 1250.0 | 5.1 | 0.0225 | 95.5 | 49 | 0 | 2 | 47 |
| XiangShan-pr-5593__8c8Pqcm | patch_submitted | 408.5 | 15.7 | 0.0165 | 90.4 | 17 | 0 | 2 | 15 |
| XiangShan-pr-5687__2BL4mFt | patch_submitted | 780.3 | 2.6 | 0.0166 | 93.1 | 23 | 0 | 2 | 21 |
| XiangShan-pr-5700__gyh8NnV | patch_submitted | 1227.2 | 25.1 | 0.0281 | 94.8 | 27 | 0 | 2 | 25 |

