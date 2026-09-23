# RocketChip MCP V2 Analysis

## 总体结果

```yaml
mcp_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES (WAVES_ENABLED=true, no skills)
  resolved: 20
  total: 32
  resolved_rate: 62.5%
  file_level_precision: 84.27%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | MCP V2 |
|------|:-----------:|:------:|
| Resolved Rate | 20/32 (62.5%) | 20/32 (62.5%) |
| File-Level Precision | 94.52% | 84.27% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/11 |
| pr-387 | 100.0% | 3/3 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 100.0% | 11/11 |
| pr-542 | 100.0% | 1/1 |
| pr-576 | 100.0% | 1/1 |
| pr-745 | 100.0% | 5/5 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 87.5% | 7/8 |
| pr-1656 | 100.0% | 13/13 |
| pr-1761 | 100.0% | 2/2 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 2/2 |
| pr-2213 | 100.0% | 2/2 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 100.0% | 1/1 |
| pr-2621 | 100.0% | 2/2 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 50.0% | 1/2 |
| pr-2994 | 50.0% | 1/2 |
| pr-3004 | 100.0% | 2/2 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 100.0% | 1/1 |
| pr-3600 | 100.0% | 3/3 |
| pr-3624 | 100.0% | 3/3 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 84.3%
- **Average (per-task)**: 93.4%

## 未解决 Case

| PR |
|----|
| pr-177 |
| pr-387 |
| pr-1493 |
| pr-1761 |
| pr-2018 |
| pr-2036 |
| pr-2167 |
| pr-2621 |
| pr-3256 |
| pr-3526 |
| pr-3624 |
| pr-3651 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 3630.0
  completion_k: 24.3
  cache_hit_pct: 96.4
  tool_calls: 59.6
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 59.6
  cost_usd: 0.046343
  tasks: 32
  resolved: 20
  unresolved: 12
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------------|----------|
| rocket-chip-pr-177__3vodP9h | unresolved | 7007.2 | 30.9 | 0.0787 | 96.9 | 95 | 0 | 0 | 95 |
| rocket-chip-pr-387__PrK97Vx | unresolved | 14565.0 | 106.1 | 0.1889 | 96.4 | 133 | 0 | 0 | 133 |
| rocket-chip-pr-404__ZVNqor5 | resolved | 1057.4 | 9.2 | 0.0318 | 87.2 | 37 | 0 | 0 | 37 |
| rocket-chip-pr-485__QFxn5nT | resolved | 10143.5 | 32.2 | 0.0821 | 98.0 | 108 | 0 | 0 | 108 |
| rocket-chip-pr-542__Xfm3q2R | resolved | 112.3 | 5.2 | 0.0067 | 80.7 | 11 | 0 | 0 | 11 |
| rocket-chip-pr-576__ycKFDzP | resolved | 825.5 | 4.8 | 0.0202 | 91.0 | 27 | 0 | 0 | 27 |
| rocket-chip-pr-745__yGxJ6Sv | resolved | 6406.8 | 34.4 | 0.0693 | 97.2 | 102 | 0 | 0 | 102 |
| rocket-chip-pr-1069__scHwf9h | resolved | 2867.9 | 20.2 | 0.0281 | 98.3 | 78 | 0 | 0 | 78 |
| rocket-chip-pr-1093__kLZiq3C | resolved | 2646.6 | 15.8 | 0.0401 | 95.6 | 68 | 0 | 0 | 68 |
| rocket-chip-pr-1176__nBbYYBB | resolved | 140.8 | 1.0 | 0.0055 | 86.5 | 9 | 0 | 0 | 9 |
| rocket-chip-pr-1330__DrCZC8u | resolved | 5909.1 | 59.3 | 0.0819 | 96.8 | 93 | 0 | 0 | 93 |
| rocket-chip-pr-1493__sWMvgpF | unresolved | 2817.0 | 16.6 | 0.0396 | 95.0 | 63 | 0 | 0 | 63 |
| rocket-chip-pr-1656__ZqcZkUc | resolved | 1894.7 | 10.2 | 0.0360 | 93.8 | 58 | 0 | 0 | 58 |
| rocket-chip-pr-1761__YTrozea | unresolved | 523.8 | 1.9 | 0.0132 | 91.1 | 21 | 0 | 0 | 21 |
| rocket-chip-pr-1878__LV8pH4Y | resolved | 1593.9 | 11.6 | 0.0274 | 93.8 | 39 | 0 | 0 | 39 |
| rocket-chip-pr-2018__3KzfRNB | unresolved | 4339.6 | 31.3 | 0.0524 | 97.2 | 96 | 0 | 0 | 96 |
| rocket-chip-pr-2036__ETSQMfS | unresolved | 100.8 | 0.9 | 0.0039 | 84.1 | 8 | 0 | 0 | 8 |
| rocket-chip-pr-2167__4hFtmTc | unresolved | 5140.9 | 36.6 | 0.0783 | 94.6 | 84 | 0 | 0 | 84 |
| rocket-chip-pr-2213__tvftFdV | resolved | 934.7 | 5.2 | 0.0238 | 90.1 | 37 | 0 | 0 | 37 |
| rocket-chip-pr-2368__JqVadHB | resolved | 12087.9 | 59.9 | 0.0895 | 99.0 | 133 | 0 | 0 | 133 |
| rocket-chip-pr-2543__bKFgoho | resolved | 8430.2 | 55.1 | 0.0743 | 98.7 | 89 | 0 | 0 | 89 |
| rocket-chip-pr-2621__Qpi3wWY | unresolved | 1835.7 | 39.9 | 0.0378 | 97.0 | 50 | 0 | 0 | 50 |
| rocket-chip-pr-2984__DgVkHb9 | resolved | 521.7 | 9.0 | 0.0106 | 95.3 | 25 | 0 | 0 | 25 |
| rocket-chip-pr-2988__DKHgvb2 | resolved | 3085.4 | 36.9 | 0.0433 | 97.4 | 73 | 0 | 0 | 73 |
| rocket-chip-pr-2994__CAZViYY | resolved | 2803.3 | 26.9 | 0.0369 | 97.0 | 66 | 0 | 0 | 66 |
| rocket-chip-pr-3004__gn5cka7 | resolved | 6033.0 | 16.1 | 0.0775 | 94.4 | 59 | 0 | 0 | 59 |
| rocket-chip-pr-3065__C6eoMpj | resolved | 4245.4 | 35.0 | 0.0414 | 98.8 | 74 | 0 | 0 | 74 |
| rocket-chip-pr-3256__GV3QZrp | unresolved | 736.1 | 10.1 | 0.0167 | 92.2 | 21 | 0 | 0 | 21 |
| rocket-chip-pr-3526__Q6QLABz | unresolved | 1040.0 | 19.8 | 0.0275 | 91.8 | 21 | 0 | 0 | 21 |
| rocket-chip-pr-3600__7ftEyeu | resolved | 1895.5 | 12.1 | 0.0276 | 95.0 | 47 | 0 | 0 | 47 |
| rocket-chip-pr-3624__xh45QwN | unresolved | 3652.4 | 21.0 | 0.0620 | 92.9 | 61 | 0 | 0 | 61 |
| rocket-chip-pr-3651__Tus4BmT | unresolved | 766.1 | 2.9 | 0.0300 | 81.9 | 21 | 0 | 0 | 21 |

