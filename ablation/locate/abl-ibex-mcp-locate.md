# Ibex MCP+LOCATE Analysis

## 总体结果

```yaml
mcp+locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 19
  total: 35
  resolved_rate: 54.3%
  file_level_precision: 80.5%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 19/35 (54.3%) |
| File-Level Precision | 79.2% | 80.5% |

### 新解决
  pr-155, pr-1229

### 丢失
  pr-222, pr-293, pr-377, pr-465, pr-882, pr-1135, pr-1469, pr-1584, pr-1735, pr-1865

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 2/2 |
| pr-104 | 100.0% | 3/3 |
| pr-122 | 100.0% | 1/1 |
| pr-155 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 0.0% | 0/1 |
| pr-974 | 0.0% | 0/1 |
| pr-1141 | 50.0% | 1/2 |
| pr-1229 | 100.0% | 2/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 100.0% | 2/2 |
| pr-1513 | 40.0% | 2/5 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 33.3% | 1/3 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 1/1 |
| pr-2232 | 100.0% | 2/2 |

## File-Level Precision

- **Overall**: 80.5%
- **Average (per-task)**: 86.5%

## 未解决 Case

```json
[
  {
    "pr": 104,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 222,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 293,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 377,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 465,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 475,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 882,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 907,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 974,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1135,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1141,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1469,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 1513,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1584,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1735,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1865,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  interface: 3
  logic: 3
  spec: 2
  timing_sync: 1
  unknown: 7
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1255.7
  completion_k: 5.1
  cache_hit_pct: 96.3
  tool_calls: 29.5
  mcp_calls: 0.0
  other_skill_calls: 0.9
  ordinary_calls: 28.5
  cost_usd: 0.016165
  own_price_cost_usd: 0.344695
  tasks: 35
  resolved: 19
  unresolved: 16
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| ibex-pr-104 | unresolved | 2405.8 | 8.5 | 0.0201 | 97.5 | 57 | 0 | 1 | 56 |
| ibex-pr-1135 | unresolved | 79.5 | 2.4 | 0.0043 | 70.7 | 6 | 0 | 1 | 5 |
| ibex-pr-1141 | unresolved | 2973.2 | 7.3 | 0.0253 | 98.1 | 59 | 0 | 1 | 58 |
| ibex-pr-122 | resolved | 1542.3 | 4.9 | 0.0194 | 96.9 | 34 | 0 | 1 | 33 |
| ibex-pr-1229 | resolved | 1606.8 | 5.2 | 0.0173 | 95.9 | 53 | 0 | 1 | 52 |
| ibex-pr-1383 | resolved | 811.0 | 3.4 | 0.0130 | 93.9 | 21 | 0 | 1 | 20 |
| ibex-pr-1469 | unresolved | 1165.4 | 4.3 | 0.0192 | 93.8 | 27 | 0 | 1 | 26 |
| ibex-pr-1513 | unresolved | 5200.7 | 11.5 | 0.0330 | 98.3 | 75 | 0 | 1 | 74 |
| ibex-pr-155 | resolved | 2056.1 | 6.9 | 0.0324 | 97.2 | 37 | 0 | 1 | 36 |
| ibex-pr-157 | resolved | 385.3 | 2.5 | 0.0095 | 92.1 | 14 | 0 | 1 | 13 |
| ibex-pr-1584 | unresolved | 925.7 | 4.7 | 0.0217 | 93.2 | 31 | 0 | 1 | 30 |
| ibex-pr-166 | resolved | 188.4 | 4.0 | 0.0057 | 86.3 | 8 | 0 | 1 | 7 |
| ibex-pr-167 | resolved | 314.9 | 2.7 | 0.0068 | 90.8 | 12 | 0 | 1 | 11 |
| ibex-pr-1735 | unresolved | 2337.7 | 7.3 | 0.0243 | 96.2 | 42 | 0 | 1 | 41 |
| ibex-pr-176 | resolved | 209.8 | 2.3 | 0.0051 | 88.5 | 10 | 0 | 1 | 9 |
| ibex-pr-1780 | resolved | 1415.2 | 6.3 | 0.0185 | 96.2 | 37 | 0 | 1 | 36 |
| ibex-pr-1816 | resolved | 2438.6 | 7.4 | 0.0240 | 98.2 | 56 | 0 | 1 | 55 |
| ibex-pr-1865 | unresolved | 1798.7 | 6.2 | 0.0218 | 96.9 | 45 | 0 | 1 | 44 |
| ibex-pr-222 | unresolved | 436.3 | 3.8 | 0.0118 | 91.5 | 23 | 0 | 1 | 22 |
| ibex-pr-2232 | resolved | 1434.8 | 7.3 | 0.0192 | 95.5 | 41 | 0 | 1 | 40 |
| ibex-pr-244 | resolved | 1157.7 | 3.7 | 0.0183 | 95.3 | 25 | 0 | 1 | 24 |
| ibex-pr-276 | resolved | 1481.6 | 5.4 | 0.0239 | 96.7 | 32 | 0 | 1 | 31 |
| ibex-pr-282 | resolved | 392.1 | 3.9 | 0.0080 | 92.1 | 14 | 0 | 1 | 13 |
| ibex-pr-293 | unresolved | 5309.1 | 20.7 | 0.0426 | 98.7 | 72 | 0 | 1 | 71 |
| ibex-pr-332 | resolved | 1848.7 | 4.7 | 0.0253 | 97.7 | 28 | 0 | 1 | 27 |
| ibex-pr-377 | unresolved | 785.8 | 4.8 | 0.0126 | 95.0 | 30 | 0 | 1 | 29 |
| ibex-pr-45 | resolved | 399.4 | 2.5 | 0.0067 | 92.9 | 17 | 0 | 1 | 16 |
| ibex-pr-465 | unresolved | 106.2 | 2.5 | 0.0047 | 76.4 | 10 | 0 | 1 | 9 |
| ibex-pr-475 | unresolved | 341.9 | 3.2 | 0.0089 | 86.9 | 15 | 0 | 1 | 14 |
| ibex-pr-48 | resolved | 234.5 | 2.3 | 0.0043 | 92.3 | 14 | 0 | 0 | 14 |
| ibex-pr-54 | resolved | 616.8 | 4.3 | 0.0087 | 96.0 | 30 | 0 | 0 | 30 |
| ibex-pr-83 | resolved | 232.0 | 2.5 | 0.0048 | 91.8 | 15 | 0 | 0 | 15 |
| ibex-pr-882 | unresolved | 536.7 | 3.4 | 0.0201 | 87.8 | 12 | 0 | 1 | 11 |
| ibex-pr-907 | unresolved | 108.5 | 2.5 | 0.0097 | 70.6 | 6 | 0 | 1 | 5 |
| ibex-pr-974 | unresolved | 673.5 | 4.6 | 0.0144 | 93.5 | 23 | 0 | 1 | 22 |
