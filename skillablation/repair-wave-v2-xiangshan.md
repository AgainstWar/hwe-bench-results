# XiangShan Repair+Wave V2 Analysis

## 总体结果

```yaml
repair_wave_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair + wave (hdl-minimal-repair / wave)
  mcp: WAVES (WAVES_ENABLED=true)
  resolved: 30
  total: 54
  resolved_rate: 55.6%
  file_level_precision: 100.00%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair+Wave V2 |
|------|:-----------:|:--------------:|
| Resolved Rate | 32/53 (60.4%) | 30/54 (55.6%) |
| File-Level Precision | 93.64% | 100.00% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 7/7 |
| pr-739 | 100.0% | 1/1 |
| pr-1242 | 100.0% | 6/6 |
| pr-1323 | 100.0% | 2/2 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 100.0% | 5/5 |
| pr-1602 | 100.0% | 18/18 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 100.0% | 1/1 |
| pr-1793 | 100.0% | 4/4 |
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
| pr-4750 | 100.0% | 2/2 |
| pr-4764 | 100.0% | 1/1 |
| pr-4943 | 100.0% | 8/8 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 3/3 |
| pr-5080 | 100.0% | 1/1 |
| pr-5182 | 100.0% | 1/1 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 100.0%
- **Average (per-task)**: 100.0%

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
| pr-2195 |
| pr-2246 |
| pr-2351 |
| pr-3307 |
| pr-3329 |
| pr-3867 |
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
| pr-5687 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 2684.4
  completion_k: 9.0
  cache_hit_pct: 96.6
  tool_calls: 47.1
  mcp_calls: 0.0
  repair_skill_calls: 1.2
  wave_skill_calls: 0.0
  ordinary_calls: 45.9
  cost_usd: 0.034987
  tasks: 54
  resolved: 30
  unresolved: 24
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Wave Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|------------|----------|
| XiangShan-pr-39__ntWdWzu | patch_submitted | 2881.8 | 5.8 | 0.0434 | 97.0 | 51 | 0 | 1 | 0 | 50 |
| XiangShan-pr-281__FkZ8UGo | patch_submitted | 693.6 | 3.6 | 0.0130 | 95.6 | 31 | 0 | 2 | 0 | 29 |
| XiangShan-pr-655__CmcGXF9 | patch_submitted | 2838.8 | 6.7 | 0.0443 | 97.9 | 55 | 0 | 0 | 0 | 55 |
| XiangShan-pr-739__ERHTM8K | patch_submitted | 775.7 | 3.0 | 0.0175 | 95.0 | 25 | 0 | 1 | 0 | 24 |
| XiangShan-pr-1242__6x8ngt9 | patch_submitted | 5766.4 | 10.0 | 0.0541 | 98.4 | 81 | 0 | 1 | 0 | 80 |
| XiangShan-pr-1323__Avy5wRc | patch_submitted | 2819.9 | 6.5 | 0.0338 | 97.2 | 59 | 0 | 2 | 0 | 57 |
| XiangShan-pr-1395__6tAxhNr | patch_submitted | 1501.1 | 3.8 | 0.0245 | 95.2 | 42 | 0 | 2 | 1 | 39 |
| XiangShan-pr-1401__tJUbrKS | patch_submitted | 3545.4 | 6.3 | 0.0444 | 96.7 | 57 | 0 | 2 | 0 | 55 |
| XiangShan-pr-1602__NU8dGhH | patch_submitted | 38310.0 | 110.4 | 0.3180 | 97.6 | 254 | 0 | 1 | 0 | 253 |
| XiangShan-pr-1679__WviSHE2 | patch_submitted | 367.8 | 2.0 | 0.0141 | 89.4 | 20 | 0 | 0 | 0 | 20 |
| XiangShan-pr-1694__vPi4VnT | patch_submitted | 1490.2 | 4.0 | 0.0301 | 95.6 | 40 | 0 | 2 | 0 | 38 |
| XiangShan-pr-1793__JtdQ7EY | patch_submitted | 3878.9 | 7.1 | 0.0456 | 97.6 | 53 | 0 | 1 | 0 | 52 |
| XiangShan-pr-1820__E9iwAXi | patch_submitted | 844.6 | 4.4 | 0.0167 | 95.4 | 35 | 0 | 1 | 0 | 34 |
| XiangShan-pr-1907__ZoTnLXp | patch_submitted | 3708.3 | 5.8 | 0.0478 | 97.2 | 51 | 0 | 2 | 0 | 49 |
| XiangShan-pr-1931__ff2pJDU | patch_submitted | 1475.0 | 12.9 | 0.0350 | 91.8 | 39 | 0 | 1 | 0 | 38 |
| XiangShan-pr-2095__J2QtNYD | patch_submitted | 256.9 | 2.4 | 0.0082 | 91.4 | 18 | 0 | 2 | 0 | 16 |
| XiangShan-pr-2195__nshoMMz | patch_submitted | 1908.5 | 6.8 | 0.0230 | 97.8 | 59 | 0 | 1 | 0 | 58 |
| XiangShan-pr-2246__drBFdPU | patch_submitted | 3225.9 | 9.6 | 0.0349 | 97.7 | 72 | 0 | 1 | 0 | 71 |
| XiangShan-pr-2351__MBZekk3 | patch_submitted | 4813.8 | 6.4 | 0.0533 | 96.8 | 50 | 0 | 1 | 0 | 49 |
| XiangShan-pr-2483__8JPmcHj | patch_submitted | 417.3 | 2.9 | 0.0115 | 92.7 | 17 | 0 | 1 | 0 | 16 |
| XiangShan-pr-2513__vLvJUvy | patch_submitted | 677.4 | 2.5 | 0.0139 | 93.1 | 25 | 0 | 2 | 0 | 23 |
| XiangShan-pr-2781__PYthT7M | patch_submitted | 1276.6 | 5.5 | 0.0234 | 96.8 | 51 | 0 | 1 | 0 | 50 |
| XiangShan-pr-2845__d6wqLZU | patch_submitted | 2494.3 | 5.4 | 0.0278 | 97.5 | 58 | 0 | 2 | 0 | 56 |
| XiangShan-pr-2997__f7cBiF6 | patch_submitted | 844.7 | 3.6 | 0.0188 | 93.9 | 37 | 0 | 1 | 0 | 36 |
| XiangShan-pr-3182__Yi6N6Xf | patch_submitted | 2164.1 | 4.5 | 0.0266 | 96.4 | 48 | 0 | 1 | 0 | 47 |
| XiangShan-pr-3307__6HDSNZg | patch_submitted | 2026.4 | 4.8 | 0.0279 | 96.8 | 44 | 0 | 1 | 0 | 43 |
| XiangShan-pr-3329__EHw4YAw | patch_submitted | 1383.6 | 25.4 | 0.0302 | 94.7 | 38 | 0 | 1 | 0 | 37 |
| XiangShan-pr-3555__nKwLkYB | patch_submitted | 673.8 | 2.8 | 0.0141 | 92.5 | 25 | 0 | 1 | 0 | 24 |
| XiangShan-pr-3636__bNznqvg | patch_submitted | 3515.3 | 6.8 | 0.0378 | 97.9 | 52 | 0 | 2 | 0 | 50 |
| XiangShan-pr-3717__gTPYgC6 | patch_submitted | 2860.1 | 19.9 | 0.0395 | 96.7 | 51 | 0 | 1 | 0 | 50 |
| XiangShan-pr-3753__zmLrkqe | patch_submitted | 1622.4 | 6.0 | 0.0293 | 95.6 | 35 | 0 | 1 | 0 | 34 |
| XiangShan-pr-3859__YUq3ESo | patch_submitted | 3034.1 | 9.4 | 0.0368 | 96.9 | 64 | 0 | 2 | 0 | 62 |
| XiangShan-pr-3867__mNPkBur | patch_submitted | 1269.2 | 4.0 | 0.0212 | 95.3 | 34 | 0 | 1 | 0 | 33 |
| XiangShan-pr-3907__gSsgXwR | patch_submitted | 537.3 | 3.0 | 0.0091 | 95.1 | 32 | 0 | 2 | 0 | 30 |
| XiangShan-pr-3955__EKtqMzJ | patch_submitted | 1105.1 | 3.9 | 0.0213 | 95.4 | 33 | 0 | 2 | 0 | 31 |
| XiangShan-pr-4110__TjXekWx | patch_submitted | 1291.4 | 3.8 | 0.0211 | 95.4 | 37 | 0 | 2 | 0 | 35 |
| XiangShan-pr-4166__5z8M7Wg | patch_submitted | 2433.8 | 6.4 | 0.0329 | 95.9 | 55 | 0 | 0 | 0 | 55 |
| XiangShan-pr-4179__M9zhU7Y | patch_submitted | 3089.0 | 8.7 | 0.0664 | 90.5 | 34 | 0 | 1 | 0 | 33 |
| XiangShan-pr-4337__8sQqHK7 | patch_submitted | 916.3 | 3.4 | 0.0191 | 93.8 | 29 | 0 | 1 | 0 | 28 |
| XiangShan-pr-4426__Utx5qDc | patch_submitted | 1113.4 | 4.2 | 0.0193 | 95.5 | 39 | 0 | 2 | 0 | 37 |
| XiangShan-pr-4442__KCv4dYU | patch_submitted | 1403.2 | 3.9 | 0.0222 | 95.9 | 36 | 0 | 1 | 0 | 35 |
| XiangShan-pr-4533__gqJJhsw | patch_submitted | 995.2 | 3.3 | 0.0199 | 95.5 | 29 | 0 | 1 | 0 | 28 |
| XiangShan-pr-4750__h3fA4ik | patch_submitted | 4195.7 | 7.9 | 0.0445 | 97.4 | 51 | 0 | 1 | 0 | 50 |
| XiangShan-pr-4764__VTHy7YR | patch_submitted | 1327.3 | 3.7 | 0.0214 | 95.2 | 41 | 0 | 0 | 0 | 41 |
| XiangShan-pr-4943__Pv2Eg6n | patch_submitted | 2543.4 | 5.6 | 0.0260 | 97.2 | 63 | 0 | 0 | 0 | 63 |
| XiangShan-pr-4959__HZvBrLQ | patch_submitted | 1000.6 | 24.1 | 0.0334 | 89.1 | 32 | 0 | 1 | 0 | 31 |
| XiangShan-pr-4968__9Q9QbfX | patch_submitted | 2914.0 | 39.7 | 0.0531 | 95.4 | 52 | 0 | 1 | 0 | 51 |
| XiangShan-pr-5080__bipiDHk | patch_submitted | 1348.8 | 12.4 | 0.0432 | 92.0 | 37 | 0 | 1 | 0 | 36 |
| XiangShan-pr-5182__h5WMoeb | patch_submitted | 2473.9 | 4.3 | 0.0277 | 96.8 | 42 | 0 | 1 | 0 | 41 |
| XiangShan-pr-5189__TH3Z2Mc | patch_submitted | 2764.3 | 6.4 | 0.0346 | 97.4 | 48 | 0 | 1 | 0 | 47 |
| XiangShan-pr-5496__nHwF4Sz | patch_submitted | 3500.4 | 7.5 | 0.0392 | 97.8 | 72 | 0 | 2 | 0 | 70 |
| XiangShan-pr-5593__nYAkGb3 | patch_submitted | 1243.4 | 4.4 | 0.0213 | 96.1 | 34 | 0 | 1 | 0 | 33 |
| XiangShan-pr-5687__nWZQDJe | patch_submitted | 1635.0 | 4.9 | 0.0262 | 96.6 | 43 | 0 | 2 | 0 | 41 |
| XiangShan-pr-5700__YX8ZvDP | patch_submitted | 1763.6 | 4.0 | 0.0267 | 95.3 | 35 | 0 | 2 | 0 | 33 |

