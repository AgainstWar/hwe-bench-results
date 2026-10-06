# RocketChip Repair V2 Analysis

## 总体结果

```yaml
repair_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (hdl-minimal-repair, no MCP)
  resolved: 15
  total: 31
  resolved_rate: 48.4%
  file_level_precision: 84.52%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V2 |
|------|:-----------:|:---------:|
| Resolved Rate | 20/32 (62.5%) | 15/31 (48.4%) |
| File-Level Precision | 94.52% | 84.52% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/11 |
| pr-387 | 100.0% | 15/15 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 100.0% | 8/8 |
| pr-542 | 100.0% | 1/1 |
| pr-576 | 100.0% | 1/1 |
| pr-745 | 100.0% | 2/2 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 87.5% | 7/8 |
| pr-1656 | 100.0% | 4/4 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 100.0% | 2/2 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 100.0% | 1/1 |
| pr-2621 | 100.0% | 4/4 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 50.0% | 1/2 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 100.0% | 2/2 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 100.0% | 1/1 |
| pr-3600 | 100.0% | 3/3 |
| pr-3624 | 100.0% | 3/3 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 84.5%
- **Average (per-task)**: 94.8%

## 未解决 Case

| PR |
|----|
| pr-177 |
| pr-387 |
| pr-745 |
| pr-1093 |
| pr-1493 |
| pr-1761 |
| pr-1878 |
| pr-2018 |
| pr-2036 |
| pr-2167 |
| pr-2213 |
| pr-2543 |
| pr-3004 |
| pr-3256 |
| pr-3624 |
| pr-3651 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 4488.9
  completion_k: 24.5
  cache_hit_pct: 98.4
  tool_calls: 70.1
  mcp_calls: 0.0
  repair_skill_calls: 1.0
  ordinary_calls: 67.0
  cost_usd: 0.044339
  tasks: 31
  resolved: 15
  unresolved: 16
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| rocket-chip-pr-177__JVkeA3i | unresolved | 2370.4 | 7.0 | 0.0268 | 97.8 | 53 | 0 | 1 | 52 |
| rocket-chip-pr-387__brvCSk8 | unresolved | 2834.4 | 5.7 | 0.0351 | 97.1 | 53 | 0 | 1 | 52 |
| rocket-chip-pr-404__Xh37rCM | resolved | 1041.6 | 3.4 | 0.0148 | 96.2 | 37 | 0 | 1 | 36 |
| rocket-chip-pr-485__VJWYKXs | resolved | 21320.2 | 128.4 | 0.1644 | 99.3 | 172 | 0 | 1 | 171 |
| rocket-chip-pr-542__5YfW4ZM | resolved | 6588.8 | 51.0 | 0.0624 | 98.8 | 102 | 0 | 1 | 101 |
| rocket-chip-pr-576__2v8RnSU | resolved | 2710.0 | 43.4 | 0.0462 | 97.0 | 45 | 0 | 1 | 44 |
| rocket-chip-pr-745__mdvX2UH | unresolved | 8966.0 | 14.5 | 0.0779 | 98.7 | 99 | 0 | 1 | 98 |
| rocket-chip-pr-1069__NbW58qC | resolved | 10902.1 | 61.3 | 0.0827 | 99.2 | 143 | 0 | 1 | 142 |
| rocket-chip-pr-1093__J9sWPWg | unresolved | 8056.9 | 10.1 | 0.0722 | 98.3 | 87 | 0 | 1 | 86 |
| rocket-chip-pr-1176__7ykoUXR | error | 0.0 | 0.0 | 0.0000 | 0.0 | - | 0 | 0 | 0 |
| rocket-chip-pr-1330__Utmpjzj | resolved | 928.7 | 26.7 | 0.0211 | 98.3 | 34 | 0 | 1 | 33 |
| rocket-chip-pr-1493__dYC37PP | unresolved | 2814.2 | 6.8 | 0.0344 | 97.3 | 65 | 0 | 1 | 64 |
| rocket-chip-pr-1656__Fe8X6nL | resolved | 3505.5 | 37.8 | 0.0521 | 96.3 | 77 | 0 | 1 | 76 |
| rocket-chip-pr-1761__qRTEfBC | unresolved | 3385.3 | 7.5 | 0.0385 | 98.0 | 58 | 0 | 1 | 57 |
| rocket-chip-pr-1878__ArtdMwu | unresolved | 1949.7 | 22.2 | 0.0257 | 97.7 | 55 | 0 | 1 | 54 |
| rocket-chip-pr-2018__n86CaUC | unresolved | 2062.1 | 7.0 | 0.0283 | 97.1 | 69 | 0 | 1 | 68 |
| rocket-chip-pr-2036__8TN9tTn | unresolved | 305.6 | 2.4 | 0.0085 | 90.8 | 19 | 0 | 1 | 18 |
| rocket-chip-pr-2167__gc8HcKw | unresolved | 13670.6 | 74.1 | 0.1023 | 99.2 | 147 | 0 | 1 | 146 |
| rocket-chip-pr-2213__XGLSZz8 | unresolved | 2745.2 | 7.2 | 0.0330 | 97.4 | 60 | 0 | 1 | 59 |
| rocket-chip-pr-2368__SdTCJRB | resolved | 9436.4 | 63.5 | 0.0795 | 99.1 | 117 | 0 | 1 | 116 |
| rocket-chip-pr-2543__xyLAehX | unresolved | 889.7 | 3.9 | 0.0149 | 95.4 | 39 | 0 | 1 | 38 |
| rocket-chip-pr-2621__ASj7VgH | resolved | 970.4 | 4.9 | 0.0181 | 94.5 | 39 | 0 | 1 | 38 |
| rocket-chip-pr-2984__JREzYSP | resolved | 708.2 | 12.9 | 0.0140 | 96.0 | 29 | 0 | 1 | 28 |
| rocket-chip-pr-2988__zs5D834 | resolved | 1541.7 | 17.1 | 0.0201 | 97.7 | 50 | 0 | 1 | 49 |
| rocket-chip-pr-2994__o9KFBrB | resolved | 8169.9 | 77.2 | 0.0846 | 98.9 | 114 | 0 | 1 | 113 |
| rocket-chip-pr-3004__zjg8UQ8 | unresolved | 1748.7 | 4.2 | 0.0238 | 95.7 | 39 | 0 | 1 | 38 |
| rocket-chip-pr-3065__jKCkFAp | resolved | 11004.1 | 49.0 | 0.0781 | 99.0 | 120 | 0 | 1 | 119 |
| rocket-chip-pr-3256__GMobUFH | unresolved | 3031.1 | 5.4 | 0.0370 | 97.3 | 50 | 0 | 1 | 49 |
| rocket-chip-pr-3526__ErvL2Nu | resolved | 1555.7 | 5.6 | 0.0210 | 96.9 | 46 | 0 | 1 | 45 |
| rocket-chip-pr-3600__FqGASry | resolved | 3200.4 | 9.0 | 0.0398 | 97.0 | 49 | 0 | 1 | 48 |
| rocket-chip-pr-3624__NuHTZAP | unresolved | 4098.3 | 9.4 | 0.0381 | 98.2 | 70 | 0 | 1 | 69 |
| rocket-chip-pr-3651__5XZ27Q2 | unresolved | 1133.7 | 4.0 | 0.0233 | 95.2 | 37 | 0 | 1 | 36 |

