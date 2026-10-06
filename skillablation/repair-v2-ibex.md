# Ibex Repair V2 Analysis

## 总体结果

```yaml
repair_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair (hdl-minimal-repair, no MCP)
  resolved: 31
  total: 34
  resolved_rate: 91.2%
  file_level_precision: 96.43%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair V2 |
|------|:-----------:|:---------:|
| Resolved Rate | 35/35 (100.0%) | 31/34 (91.2%) |
| File-Level Precision | 98.15% | 96.43% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
| pr-104 | 100.0% | 8/8 |
| pr-122 | 100.0% | 1/1 |
| pr-155 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-282 | 100.0% | 2/2 |
| pr-293 | 100.0% | 2/2 |
| pr-332 | 100.0% | 2/2 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 4/4 |
| pr-475 | 100.0% | 1/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 2/2 |
| pr-974 | 100.0% | 3/3 |
| pr-1135 | 100.0% | 2/2 |
| pr-1141 | 100.0% | 2/2 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 100.0% | 8/8 |
| pr-1513 | 81.8% | 9/11 |
| pr-1584 | 100.0% | 4/4 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 2/2 |
| pr-2232 | 100.0% | 11/11 |

## File-Level Precision

- **Overall**: 96.4%
- **Average (per-task)**: 98.0%

## 未解决 Case

| PR |
|----|
| pr-104 |
| pr-1229 |
| pr-1865 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 12610.1
  completion_k: 85.1
  cache_hit_pct: 99.2
  tool_calls: 98.7
  mcp_calls: 0.0
  repair_skill_calls: 1.0
  ordinary_calls: 97.7
  cost_usd: 0.104186
  tasks: 34
  resolved: 31
  unresolved: 3
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|----------|
| ibex-pr-45__egYtCzx | resolved | 657.0 | 9.6 | 0.0121 | 95.5 | 27 | 0 | 1 | 26 |
| ibex-pr-48__57NMPkD | resolved | 1775.2 | 40.1 | 0.0356 | 97.6 | 38 | 0 | 1 | 37 |
| ibex-pr-54__nAjqhJV | resolved | 903.6 | 25.7 | 0.0244 | 95.3 | 25 | 0 | 1 | 24 |
| ibex-pr-83__7S5KH58 | resolved | 2565.9 | 32.6 | 0.0329 | 98.5 | 61 | 0 | 1 | 60 |
| ibex-pr-104__8BYGjyQ | unresolved | 32365.6 | 133.1 | 0.2104 | 99.3 | 171 | 0 | 1 | 170 |
| ibex-pr-122__Cvd8mz2 | resolved | 9674.7 | 97.7 | 0.1008 | 99.1 | 99 | 0 | 1 | 98 |
| ibex-pr-155__C828wya | resolved | 19009.3 | 160.9 | 0.1698 | 99.4 | 136 | 0 | 1 | 135 |
| ibex-pr-157__GtZgMCu | resolved | 2305.5 | 41.1 | 0.0395 | 97.7 | 45 | 0 | 1 | 44 |
| ibex-pr-166__psQTSeV | resolved | 854.2 | 11.3 | 0.0145 | 95.9 | 33 | 0 | 1 | 32 |
| ibex-pr-167__T4p3hfh | resolved | 7925.7 | 62.8 | 0.0735 | 99.0 | 103 | 0 | 1 | 102 |
| ibex-pr-176__KtHAJRZ | resolved | 1294.2 | 31.6 | 0.0277 | 97.5 | 38 | 0 | 1 | 37 |
| ibex-pr-222__awvAnTQ | resolved | 1482.8 | 18.4 | 0.0204 | 97.7 | 50 | 0 | 1 | 49 |
| ibex-pr-244__DBq3KQV | resolved | 38377.9 | 187.1 | 0.2576 | 99.5 | 201 | 0 | 1 | 200 |
| ibex-pr-276__fLDQh6F | unresolved | 953.8 | 86.0 | 0.0615 | 95.0 | 26 | 0 | 1 | 25 |
| ibex-pr-282__8KgYXGt | resolved | 7029.7 | 105.0 | 0.0971 | 98.7 | 76 | 0 | 1 | 75 |
| ibex-pr-293__HL2KsS2 | resolved | 9770.6 | 102.0 | 0.1026 | 99.2 | 109 | 0 | 1 | 108 |
| ibex-pr-332__DkZCbPD | resolved | 25033.7 | 157.3 | 0.1905 | 99.4 | 136 | 0 | 1 | 135 |
| ibex-pr-377__9vgUtCj | resolved | 8423.5 | 100.1 | 0.0993 | 98.9 | 95 | 0 | 1 | 94 |
| ibex-pr-465__8oznrLV | resolved | 46991.4 | 207.8 | 0.2959 | 99.6 | 259 | 0 | 1 | 258 |
| ibex-pr-475__pBLn5ag | resolved | 3802.4 | 41.2 | 0.0474 | 98.0 | 59 | 0 | 1 | 58 |
| ibex-pr-882__4FYKCen | resolved | 14103.5 | 103.4 | 0.1225 | 99.1 | 98 | 0 | 1 | 97 |
| ibex-pr-907__Mf8by45 | resolved | 24244.8 | 151.5 | 0.1820 | 99.5 | 153 | 0 | 1 | 152 |
| ibex-pr-974__z8kM2QV | resolved | 4662.1 | 31.6 | 0.0432 | 98.5 | 72 | 0 | 1 | 71 |
| ibex-pr-1135__V8E5NjQ | resolved | 6821.9 | 87.7 | 0.0844 | 98.9 | 73 | 0 | 1 | 72 |
| ibex-pr-1141__oCZmQt6 | resolved | 40959.4 | 256.1 | 0.3025 | 99.6 | 172 | 0 | 1 | 171 |
| ibex-pr-1229__9bksu3L | unresolved | 11609.6 | 66.3 | 0.0894 | 99.1 | 117 | 0 | 1 | 116 |
| ibex-pr-1383__vZKNro5 | resolved | 4316.0 | 39.4 | 0.0480 | 98.2 | 68 | 0 | 1 | 67 |
| ibex-pr-1469__PXx9xZb | resolved | 33101.5 | 153.6 | 0.2157 | 99.5 | 193 | 0 | 1 | 192 |
| ibex-pr-1513__aEUhiGX | resolved | 23570.3 | 87.8 | 0.1771 | 98.4 | 162 | 0 | 1 | 161 |
| ibex-pr-1584__e5cQYC3 | resolved | 21113.2 | 89.1 | 0.1386 | 99.3 | 148 | 0 | 1 | 147 |
| ibex-pr-1735__G9uqkGa | resolved | 21227.8 | 121.3 | 0.1608 | 99.2 | 162 | 0 | 1 | 161 |
| ibex-pr-1780__dXrUFej | resolved | 1891.9 | 21.7 | 0.0264 | 97.2 | 42 | 0 | 1 | 41 |
| ibex-pr-1816__hw4tvTx | resolved | 2916.9 | 30.0 | 0.0363 | 97.8 | 49 | 0 | 1 | 48 |
| ibex-pr-1865__SagNVzS | unresolved | 3690.8 | 60.6 | 0.0563 | 98.4 | 72 | 0 | 1 | 71 |
| ibex-pr-2232__9PhV9mK | resolved | 5927.4 | 27.6 | 0.0498 | 98.2 | 85 | 0 | 1 | 84 |

