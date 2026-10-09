# Ibex Repair+Wave V2 Analysis

## 总体结果

```yaml
repair_wave_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair + wave (hdl-minimal-repair / wave)
  mcp: WAVES (WAVES_ENABLED=true)
  resolved: 34
  total: 35
  resolved_rate: 97.1%
  file_level_precision: 97.52%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair+Wave V2 |
|------|:-----------:|:--------------:|
| Resolved Rate | 35/35 (100.0%) | 34/35 (97.1%) |
| File-Level Precision | 98.15% | 97.52% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 7/7 |
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
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 2/2 |
| pr-282 | 100.0% | 2/2 |
| pr-293 | 100.0% | 2/2 |
| pr-332 | 100.0% | 3/3 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 83.3% | 5/6 |
| pr-475 | 100.0% | 1/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 2/2 |
| pr-974 | 100.0% | 3/3 |
| pr-1135 | 100.0% | 2/2 |
| pr-1141 | 100.0% | 3/3 |
| pr-1229 | 0.0% | 0/1 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 100.0% | 8/8 |
| pr-1513 | 100.0% | 11/11 |
| pr-1584 | 91.7% | 11/12 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 13/13 |
| pr-2232 | 100.0% | 11/11 |

## File-Level Precision

- **Overall**: 97.5%
- **Average (per-task)**: 96.4%

## 未解决 Case

| PR |
|----|
| pr-1229 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 3635.0
  completion_k: 13.1
  cache_hit_pct: 98.0
  tool_calls: 55.4
  mcp_calls: 0.0
  repair_skill_calls: 1.4
  wave_skill_calls: 0.3
  ordinary_calls: 53.7
  cost_usd: 0.039030
  tasks: 35
  resolved: 34
  unresolved: 1
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Wave Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|------------|----------|
| ibex-pr-45__2x9jkPU | resolved | 1574.6 | 4.3 | 0.0245 | 95.9 | 44 | 0 | 2 | 0 | 42 |
| ibex-pr-48__F7UsarT | resolved | 429.0 | 4.3 | 0.0133 | 94.3 | 23 | 0 | 2 | 0 | 21 |
| ibex-pr-54__72DCG77 | resolved | 689.0 | 4.5 | 0.0146 | 94.4 | 25 | 0 | 2 | 0 | 23 |
| ibex-pr-83__S3TBxdV | resolved | 974.2 | 5.3 | 0.0159 | 96.5 | 33 | 0 | 2 | 0 | 31 |
| ibex-pr-104__Fwb2Kg6 | resolved | 7582.0 | 11.0 | 0.0643 | 98.4 | 86 | 0 | 1 | 0 | 85 |
| ibex-pr-122__UiUTVep | resolved | 4132.0 | 10.3 | 0.0549 | 98.0 | 56 | 0 | 1 | 2 | 53 |
| ibex-pr-155__bdzRK63 | resolved | 9338.3 | 23.3 | 0.0812 | 98.9 | 107 | 0 | 2 | 1 | 104 |
| ibex-pr-157__gDFFxLK | resolved | 2953.3 | 12.0 | 0.0388 | 97.6 | 58 | 0 | 1 | 2 | 55 |
| ibex-pr-166__NKUNkpD | resolved | 1103.9 | 4.1 | 0.0198 | 94.9 | 29 | 0 | 1 | 0 | 28 |
| ibex-pr-167__guKqV9U | resolved | 4916.9 | 13.4 | 0.0565 | 98.3 | 83 | 0 | 1 | 0 | 82 |
| ibex-pr-176__9zRgzxN | resolved | 379.3 | 2.4 | 0.0082 | 93.2 | 25 | 0 | 2 | 0 | 23 |
| ibex-pr-222__4rpCPbu | resolved | 1115.7 | 4.0 | 0.0185 | 95.9 | 32 | 0 | 1 | 0 | 31 |
| ibex-pr-244__A5XMsdm | resolved | 36272.6 | 124.7 | 0.2440 | 99.2 | 205 | 0 | 0 | 1 | 204 |
| ibex-pr-276__yCMVfgq | resolved | 956.6 | 3.5 | 0.0183 | 93.5 | 27 | 0 | 1 | 0 | 26 |
| ibex-pr-282__XcdyNG3 | resolved | 2384.8 | 12.1 | 0.0368 | 97.5 | 55 | 0 | 2 | 1 | 52 |
| ibex-pr-293__9uiYSTk | resolved | 4165.7 | 38.8 | 0.0568 | 97.3 | 84 | 0 | 1 | 2 | 81 |
| ibex-pr-332__XSzyjnF | resolved | 2102.6 | 7.1 | 0.0331 | 97.7 | 48 | 0 | 1 | 0 | 47 |
| ibex-pr-377__HQvVoMq | resolved | 2805.5 | 48.5 | 0.0488 | 97.3 | 54 | 0 | 1 | 0 | 53 |
| ibex-pr-465__JrcKzxQ | resolved | 3881.5 | 8.6 | 0.0381 | 97.4 | 70 | 0 | 2 | 0 | 68 |
| ibex-pr-475__KjaAUXz | resolved | 597.3 | 2.3 | 0.0118 | 92.9 | 25 | 0 | 2 | 0 | 23 |
| ibex-pr-882__efHzibt | resolved | 2884.7 | 8.4 | 0.0452 | 97.1 | 48 | 0 | 1 | 1 | 46 |
| ibex-pr-907__okUqXU9 | resolved | 1388.6 | 4.8 | 0.0235 | 96.4 | 37 | 0 | 2 | 0 | 35 |
| ibex-pr-974__QhFYcF2 | resolved | 2297.1 | 5.6 | 0.0244 | 97.3 | 42 | 0 | 2 | 0 | 40 |
| ibex-pr-1135__YgJfgZR | resolved | 2194.5 | 8.2 | 0.0353 | 96.7 | 50 | 0 | 2 | 0 | 48 |
| ibex-pr-1141__iX7K7CR | resolved | 7728.9 | 11.1 | 0.0689 | 98.6 | 88 | 0 | 2 | 0 | 86 |
| ibex-pr-1229__b4LsM5V | unresolved | 1262.0 | 17.0 | 0.0242 | 94.8 | 39 | 0 | 1 | 0 | 38 |
| ibex-pr-1383__3k29ksb | resolved | 533.7 | 3.2 | 0.0118 | 94.6 | 27 | 0 | 0 | 0 | 27 |
| ibex-pr-1469__UezahDg | resolved | 3322.4 | 8.4 | 0.0373 | 97.6 | 79 | 0 | 1 | 0 | 78 |
| ibex-pr-1513__NJxgG9L | resolved | 2633.6 | 7.0 | 0.0311 | 97.3 | 72 | 0 | 0 | 2 | 70 |
| ibex-pr-1584__NcDT2tG | resolved | 3724.4 | 12.0 | 0.0406 | 97.9 | 63 | 0 | 2 | 0 | 61 |
| ibex-pr-1735__RxmSHRE | resolved | 2262.8 | 5.1 | 0.0256 | 96.8 | 42 | 0 | 2 | 0 | 40 |
| ibex-pr-1780__KgLBaam | resolved | 3417.6 | 9.2 | 0.0365 | 98.0 | 57 | 0 | 1 | 0 | 56 |
| ibex-pr-1816__zPpe8x6 | resolved | 1719.6 | 6.0 | 0.0217 | 97.0 | 46 | 0 | 2 | 0 | 44 |
| ibex-pr-1865__G4vQhve | resolved | 2715.3 | 5.0 | 0.0275 | 97.5 | 50 | 0 | 1 | 0 | 49 |
| ibex-pr-2232__SCWRWJA | resolved | 783.6 | 2.9 | 0.0142 | 93.8 | 29 | 0 | 1 | 0 | 28 |

