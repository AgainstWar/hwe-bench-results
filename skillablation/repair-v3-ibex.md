# Ibex Repair V3 Analysis

## 总体结果

```yaml
repair_v3:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (revised, hdl-minimal-repair)
  resolved: 35
  total: 35
  resolved_rate: 100.0%
  file_level_precision: 100.00%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V3 |
|------|:-----------:|:---------:|
| Resolved Rate | 35/35 (100.0%) | 35/35 (100.0%) |
| File-Level Precision | 98.15% | 100.00% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
| pr-104 | 100.0% | 10/10 |
| pr-122 | 100.0% | 1/1 |
| pr-155 | 100.0% | 6/6 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 3/3 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 2/2 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 3/3 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 5/5 |
| pr-475 | 100.0% | 1/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 2/2 |
| pr-974 | 100.0% | 3/3 |
| pr-1135 | 100.0% | 2/2 |
| pr-1141 | 100.0% | 3/3 |
| pr-1229 | 100.0% | 2/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 100.0% | 8/8 |
| pr-1513 | 100.0% | 11/11 |
| pr-1584 | 100.0% | 11/11 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 13/13 |
| pr-2232 | 100.0% | 11/11 |

## File-Level Precision

- **Overall**: 100.0%
- **Average (per-task)**: 100.0%

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 2312.9
  completion_k: 11.4
  cache_hit_pct: 0.0
  tool_calls: 44.5
  mcp_calls: 0.0
  repair_skill_calls: 1.2
  ordinary_calls: 43.3
  cost_usd: 0.030075
  tasks: 35
  resolved: 35
  unresolved: 0
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| ibex-pr-45__oan8Vvm | resolved | 451.4 | 3.5 | 0.0100 | 93.9 | 21 | 0 | 1 | 20 |
| ibex-pr-48__QbgTpwe | resolved | 430.1 | 3.9 | 0.0092 | 95.7 | 25 | 0 | 1 | 24 |
| ibex-pr-54__fG2F57z | resolved | 344.8 | 2.9 | 0.0094 | 91.5 | 16 | 0 | 1 | 15 |
| ibex-pr-83__tAnrRaf | resolved | 13340.8 | 119.6 | 0.1618 | 98.0 | 103 | 0 | 1 | 102 |
| ibex-pr-104__iKpeJR3 | resolved | 1293.4 | 11.3 | 0.0212 | 94.8 | 43 | 0 | 1 | 42 |
| ibex-pr-122__9VEDNnR | resolved | 2211.3 | 8.5 | 0.0310 | 97.5 | 51 | 0 | 1 | 50 |
| ibex-pr-155__yMscX7o | resolved | 11906.5 | 47.8 | 0.1036 | 98.2 | 116 | 0 | 2 | 114 |
| ibex-pr-157__sNopFjU | resolved | 1869.5 | 4.8 | 0.0393 | 91.7 | 36 | 0 | 1 | 35 |
| ibex-pr-166__kHYhRFD | resolved | 5062.3 | 16.5 | 0.0552 | 96.7 | 77 | 0 | 1 | 76 |
| ibex-pr-167__fHckYrN | resolved | 871.4 | 3.1 | 0.0144 | 95.1 | 30 | 0 | 1 | 29 |
| ibex-pr-176__DnZct3t | resolved | 116.2 | 1.0 | 0.0046 | 82.4 | 9 | 0 | 2 | 7 |
| ibex-pr-222__vcHC5EK | resolved | 1259.6 | 4.5 | 0.0185 | 96.3 | 35 | 0 | 1 | 34 |
| ibex-pr-244__rh6maim | resolved | 2018.1 | 5.2 | 0.0230 | 97.4 | 43 | 0 | 1 | 42 |
| ibex-pr-276__q2FS2Q5 | resolved | 427.7 | 1.8 | 0.0101 | 92.3 | 21 | 0 | 1 | 20 |
| ibex-pr-282__Noktho9 | resolved | 1357.4 | 8.6 | 0.0214 | 96.1 | 34 | 0 | 1 | 33 |
| ibex-pr-293__kC4eE4x | resolved | 1122.5 | 9.5 | 0.0190 | 97.2 | 46 | 0 | 2 | 44 |
| ibex-pr-332__TDEv5zC | resolved | 1862.1 | 6.8 | 0.0284 | 97.2 | 40 | 0 | 2 | 38 |
| ibex-pr-377__PiMtCCP | resolved | 1608.7 | 3.7 | 0.0199 | 97.0 | 41 | 0 | 1 | 40 |
| ibex-pr-465__6kVkRoJ | resolved | 991.6 | 5.7 | 0.0151 | 96.0 | 50 | 0 | 1 | 49 |
| ibex-pr-475__sJzc4VF | resolved | 1334.9 | 6.4 | 0.0286 | 90.3 | 32 | 0 | 2 | 30 |
| ibex-pr-882__oqDsTmv | resolved | 1503.5 | 12.6 | 0.0329 | 92.4 | 31 | 0 | 1 | 30 |
| ibex-pr-907__KZJKWc5 | resolved | 1494.3 | 4.4 | 0.0212 | 95.9 | 33 | 0 | 1 | 32 |
| ibex-pr-974__PQ2EpQR | resolved | 1032.6 | 4.7 | 0.0164 | 96.1 | 40 | 0 | 1 | 39 |
| ibex-pr-1135__sDb9kcm | resolved | 2076.7 | 5.0 | 0.0272 | 97.0 | 46 | 0 | 1 | 45 |
| ibex-pr-1141__odzYL9Q | resolved | 1928.8 | 3.0 | 0.0265 | 95.4 | 32 | 0 | 1 | 31 |
| ibex-pr-1229__VCCBnNe | resolved | 3329.4 | 31.3 | 0.0407 | 97.6 | 74 | 0 | 1 | 73 |
| ibex-pr-1383__zG4spza | resolved | 1733.5 | 11.0 | 0.0303 | 95.3 | 60 | 0 | 1 | 59 |
| ibex-pr-1469__RwrN432 | resolved | 3406.9 | 7.2 | 0.0377 | 97.4 | 66 | 0 | 2 | 64 |
| ibex-pr-1513__8EA7gfv | resolved | 1386.0 | 2.8 | 0.0212 | 94.8 | 33 | 0 | 1 | 32 |
| ibex-pr-1584__mHJLYSi | resolved | 5458.7 | 15.9 | 0.0610 | 96.1 | 67 | 0 | 1 | 66 |
| ibex-pr-1735__TA8rFb5 | resolved | 1310.8 | 5.0 | 0.0169 | 96.7 | 42 | 0 | 1 | 41 |
| ibex-pr-1780__5pLtPLV | resolved | 841.6 | 3.6 | 0.0138 | 96.0 | 30 | 0 | 1 | 29 |
| ibex-pr-1816__wne6hFJ | resolved | 780.1 | 3.3 | 0.0130 | 95.4 | 27 | 0 | 1 | 26 |
| ibex-pr-1865__ftJmVJe | resolved | 3883.6 | 10.4 | 0.0355 | 98.2 | 75 | 0 | 1 | 74 |
| ibex-pr-2232__PrvBTV3 | resolved | 906.6 | 2.5 | 0.0147 | 94.0 | 32 | 0 | 1 | 31 |

