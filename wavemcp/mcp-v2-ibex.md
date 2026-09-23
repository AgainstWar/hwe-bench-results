# Ibex MCP V2 Analysis

## 总体结果

```yaml
mcp_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES (WAVES_ENABLED=true, no skills)
  resolved: 31
  total: 35
  resolved_rate: 88.6%
  file_level_precision: 90.10%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | MCP V2 |
|------|:-----------:|:------:|
| Resolved Rate | 35/35 (100.0%) | 31/35 (88.6%) |
| File-Level Precision | 98.15% | 90.10% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
| pr-104 | 100.0% | 8/8 |
| pr-122 | 100.0% | 1/1 |
| pr-155 | 75.0% | 3/4 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 50.0% | 1/2 |
| pr-293 | 100.0% | 2/2 |
| pr-332 | 100.0% | 3/3 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 1/1 |
| pr-475 | 100.0% | 1/1 |
| pr-882 | 66.7% | 2/3 |
| pr-907 | 100.0% | 2/2 |
| pr-974 | 100.0% | 2/2 |
| pr-1135 | 100.0% | 2/2 |
| pr-1141 | 100.0% | 3/3 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 100.0% | 8/8 |
| pr-1513 | 100.0% | 11/11 |
| pr-1584 | 100.0% | 11/11 |
| pr-1735 | 14.3% | 1/7 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 1/1 |
| pr-2232 | 100.0% | 12/12 |

## File-Level Precision

- **Overall**: 90.1%
- **Average (per-task)**: 93.0%

## 未解决 Case

| PR |
|----|
| pr-104 |
| pr-276 |
| pr-1229 |
| pr-1865 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 10749.4
  completion_k: 61.4
  cache_hit_pct: 99.1
  tool_calls: 96.5
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 96.4
  cost_usd: 0.083391
  tasks: 35
  resolved: 31
  unresolved: 4
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------------|----------|
| ibex-pr-45__5RZcKmQ | resolved | 177.8 | 2.4 | 0.0034 | 94.7 | 13 | 0 | 0 | 13 |
| ibex-pr-48__M39KS9N | resolved | 993.8 | 20.5 | 0.0175 | 98.5 | 38 | 0 | 0 | 38 |
| ibex-pr-54__HjhcrBP | resolved | 869.6 | 21.1 | 0.0223 | 94.5 | 22 | 0 | 0 | 22 |
| ibex-pr-83__gMb8ptX | resolved | 2225.2 | 33.5 | 0.0330 | 98.1 | 70 | 0 | 0 | 70 |
| ibex-pr-104__MYAP3vz | unresolved | 31006.2 | 105.4 | 0.1818 | 99.4 | 205 | 0 | 0 | 205 |
| ibex-pr-122__fWZynHV | resolved | 12770.8 | 93.8 | 0.1093 | 99.2 | 135 | 0 | 0 | 135 |
| ibex-pr-155__MKALoaa | resolved | 42707.9 | 197.3 | 0.2816 | 99.4 | 224 | 0 | 0 | 224 |
| ibex-pr-157__fZeZpq6 | resolved | 6398.1 | 62.3 | 0.0667 | 98.9 | 100 | 0 | 0 | 100 |
| ibex-pr-166__pTeeHuR | resolved | 266.0 | 4.0 | 0.0052 | 94.8 | 17 | 0 | 0 | 17 |
| ibex-pr-167__tYVHzVF | resolved | 1492.6 | 18.0 | 0.0229 | 96.5 | 30 | 0 | 0 | 30 |
| ibex-pr-176__vjR5eV9 | resolved | 627.7 | 13.7 | 0.0125 | 97.4 | 36 | 0 | 0 | 36 |
| ibex-pr-222__a8kdLmQ | resolved | 16877.0 | 97.0 | 0.1304 | 99.1 | 141 | 0 | 0 | 141 |
| ibex-pr-244__CSmFSTJ | resolved | 14374.3 | 107.2 | 0.1273 | 99.1 | 118 | 0 | 0 | 118 |
| ibex-pr-276__k32FwTU | unresolved | 15191.8 | 186.1 | 0.1732 | 99.3 | 103 | 0 | 0 | 103 |
| ibex-pr-282__zvyTa6i | resolved | 12270.9 | 97.0 | 0.1103 | 99.2 | 136 | 0 | 0 | 136 |
| ibex-pr-293__pxipYHS | resolved | 20711.9 | 126.4 | 0.1574 | 99.4 | 148 | 0 | 0 | 148 |
| ibex-pr-332__WSqNJ7r | resolved | 8288.2 | 73.0 | 0.0795 | 99.1 | 104 | 0 | 0 | 104 |
| ibex-pr-377__3ZWxfu6 | resolved | 9352.3 | 87.3 | 0.0914 | 99.2 | 107 | 0 | 0 | 107 |
| ibex-pr-465__SDV9gyW | resolved | 1023.3 | 11.7 | 0.0160 | 96.1 | 33 | 0 | 0 | 33 |
| ibex-pr-475__rW3CiWF | resolved | 954.3 | 11.2 | 0.0177 | 94.2 | 26 | 0 | 0 | 26 |
| ibex-pr-882__ZVhem3E | resolved | 7801.6 | 78.7 | 0.0840 | 98.8 | 91 | 0 | 0 | 91 |
| ibex-pr-907__aU3dNau | resolved | 2386.5 | 28.3 | 0.0320 | 97.8 | 43 | 0 | 0 | 43 |
| ibex-pr-974__wv3PYRX | resolved | 5588.4 | 49.2 | 0.0579 | 98.6 | 75 | 0 | 0 | 75 |
| ibex-pr-1135__67MTcaQ | resolved | 5747.2 | 64.7 | 0.0676 | 98.6 | 65 | 0 | 0 | 65 |
| ibex-pr-1141__qXoZnbR | resolved | 5890.6 | 29.7 | 0.0471 | 98.7 | 99 | 0 | 0 | 99 |
| ibex-pr-1229__RsdKCR7 | unresolved | 3360.3 | 21.7 | 0.0335 | 97.9 | 66 | 0 | 0 | 66 |
| ibex-pr-1383__nTVkysB | resolved | 1141.5 | 9.7 | 0.0183 | 94.6 | 29 | 0 | 0 | 29 |
| ibex-pr-1469__Q4wdGoH | resolved | 8667.3 | 34.9 | 0.0643 | 98.6 | 96 | 0 | 0 | 96 |
| ibex-pr-1513__ZAbCAzf | resolved | 5277.4 | 16.6 | 0.0411 | 98.0 | 64 | 0 | 0 | 64 |
| ibex-pr-1584__BtqeKdH | resolved | 13484.7 | 46.0 | 0.0862 | 99.1 | 147 | 0 | 0 | 147 |
| ibex-pr-1735__DSCw8i8 | resolved | 52543.8 | 134.7 | 0.3174 | 99.0 | 297 | 1 | 0 | 296 |
| ibex-pr-1780__2fc5KXX | resolved | 1789.6 | 20.9 | 0.0239 | 97.7 | 42 | 0 | 0 | 42 |
| ibex-pr-1816__yq8QAqm | resolved | 56596.1 | 155.3 | 0.2947 | 99.6 | 322 | 0 | 0 | 322 |
| ibex-pr-1865__27q3iG3 | unresolved | 3653.0 | 67.7 | 0.0576 | 98.9 | 60 | 0 | 0 | 60 |
| ibex-pr-2232__5ENuy6e | resolved | 3720.2 | 21.0 | 0.0338 | 98.2 | 74 | 0 | 0 | 74 |

