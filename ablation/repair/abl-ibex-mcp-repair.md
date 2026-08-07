# Ibex MCP+REPAIR Analysis

## 总体结果

```yaml
mcp+repair:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 23
  total: 35
  resolved_rate: 65.7%
  file_level_precision: 85.7%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | MCP+REPAIR |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 23/35 (65.7%) |
| File-Level Precision | 79.2% | 85.7% |

### 新解决
  pr-475, pr-974, pr-1141

### 丢失
  pr-176, pr-293, pr-332, pr-882, pr-1135, pr-1469, pr-1584

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
| pr-104 | 100.0% | 3/3 |
| pr-122 | 100.0% | 1/1 |
| pr-155 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 1/1 |
| pr-475 | 100.0% | 1/1 |
| pr-882 | 100.0% | 1/1 |
| pr-907 | 100.0% | 1/1 |
| pr-974 | 100.0% | 2/2 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 100.0% | 1/1 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1513 | 50.0% | 2/4 |
| pr-1584 | 100.0% | 2/2 |
| pr-1735 | 0.0% | 0/1 |
| pr-1780 | 33.3% | 1/3 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 1/1 |
| pr-2232 | 100.0% | 2/2 |

## File-Level Precision

- **Overall**: 85.7%
- **Average (per-task)**: 91.4%

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
    "pr": 155,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 176,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 293,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 332,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 882,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 907,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1135,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 1229,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1469,
    "test": "N/A",
    "type": "unknown",
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
    "type": "spec",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 2
  logic: 3
  spec: 2
  unknown: 4
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1213.9
  completion_k: 4.6
  cache_hit_pct: 96.5
  tool_calls: 29.3
  mcp_calls: 0.0
  skill_calls: 0.9
  ordinary_calls: 28.5
  cost_usd: 0.016126
  own_price_cost_usd: 0.332772
  tasks: 35
  resolved: 23
  unresolved: 12
  error: 1
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| ibex-pr-104 | unresolved | 3061.6 | 8.6 | 0.0249 | 97.5 | 50 | 0 | 1 | 49 |
| ibex-pr-1135 | unresolved | 928.9 | 3.4 | 0.0145 | 96.7 | 28 | 0 | 1 | 27 |
| ibex-pr-1141 | resolved | 3489.3 | 8.9 | 0.0311 | 98.1 | 58 | 0 | 1 | 57 |
| ibex-pr-122 | resolved | 2132.5 | 5.6 | 0.0257 | 97.7 | 41 | 0 | 1 | 40 |
| ibex-pr-1229 | unresolved | 707.6 | 3.7 | 0.0124 | 93.0 | 24 | 0 | 1 | 23 |
| ibex-pr-1383 | resolved | 1096.4 | 5.5 | 0.0136 | 96.3 | 35 | 0 | 1 | 34 |
| ibex-pr-1469 | unresolved | 107.8 | 0.5 | 0.0183 | 41.2 | 7 | 0 | 1 | 6 |
| ibex-pr-1513 | unresolved | 3161.8 | 8.1 | 0.0274 | 97.3 | 53 | 0 | 1 | 52 |
| ibex-pr-155 | unresolved | 1359.0 | 6.4 | 0.0207 | 95.9 | 32 | 0 | 1 | 31 |
| ibex-pr-157 | resolved | 796.7 | 4.6 | 0.0133 | 95.4 | 26 | 0 | 1 | 25 |
| ibex-pr-1584 | unresolved | 1474.3 | 5.5 | 0.0181 | 96.4 | 54 | 0 | 0 | 54 |
| ibex-pr-166 | resolved | 263.9 | 4.3 | 0.0057 | 91.2 | 12 | 0 | 1 | 11 |
| ibex-pr-167 | resolved | 1344.2 | 4.7 | 0.0160 | 97.3 | 38 | 0 | 0 | 38 |
| ibex-pr-1735 | resolved | 4436.6 | 9.1 | 0.0335 | 98.4 | 74 | 0 | 1 | 73 |
| ibex-pr-176 | error | 0.0 | 0.0 | 0.0000 | 0.0 | 0 | 0 | 0 | 0 |
| ibex-pr-1780 | resolved | 899.2 | 5.7 | 0.0114 | 95.5 | 33 | 0 | 1 | 32 |
| ibex-pr-1816 | resolved | 1039.2 | 5.1 | 0.0135 | 96.8 | 40 | 0 | 0 | 40 |
| ibex-pr-1865 | resolved | 977.0 | 4.1 | 0.0160 | 95.5 | 27 | 0 | 1 | 26 |
| ibex-pr-222 | resolved | 614.2 | 3.8 | 0.0093 | 95.0 | 28 | 0 | 1 | 27 |
| ibex-pr-2232 | resolved | 1065.8 | 5.9 | 0.0147 | 95.3 | 38 | 0 | 1 | 37 |
| ibex-pr-244 | resolved | 2029.6 | 5.3 | 0.0210 | 96.8 | 38 | 0 | 1 | 37 |
| ibex-pr-276 | resolved | 2638.4 | 8.5 | 0.0312 | 98.0 | 44 | 0 | 1 | 43 |
| ibex-pr-282 | resolved | 679.2 | 3.4 | 0.0130 | 95.5 | 17 | 0 | 1 | 16 |
| ibex-pr-293 | unresolved | 72.1 | 0.5 | 0.0132 | 61.6 | 5 | 0 | 1 | 4 |
| ibex-pr-332 | unresolved | 192.1 | 0.7 | 0.0200 | 86.9 | 8 | 0 | 1 | 7 |
| ibex-pr-377 | resolved | 788.8 | 4.8 | 0.0124 | 95.6 | 21 | 0 | 1 | 20 |
| ibex-pr-45 | resolved | 132.0 | 1.6 | 0.0052 | 81.5 | 8 | 0 | 1 | 7 |
| ibex-pr-465 | resolved | 613.5 | 3.0 | 0.0091 | 93.7 | 20 | 0 | 1 | 19 |
| ibex-pr-475 | resolved | 583.0 | 4.0 | 0.0082 | 94.9 | 24 | 0 | 1 | 23 |
| ibex-pr-48 | resolved | 134.1 | 1.9 | 0.0044 | 85.2 | 8 | 0 | 1 | 7 |
| ibex-pr-54 | resolved | 353.1 | 2.9 | 0.0065 | 94.3 | 23 | 0 | 1 | 22 |
| ibex-pr-83 | resolved | 382.1 | 4.0 | 0.0064 | 93.9 | 20 | 0 | 0 | 20 |
| ibex-pr-882 | unresolved | 1881.6 | 4.1 | 0.0264 | 97.0 | 29 | 0 | 1 | 28 |
| ibex-pr-907 | unresolved | 735.1 | 2.7 | 0.0194 | 92.3 | 17 | 0 | 1 | 16 |
| ibex-pr-974 | resolved | 2315.5 | 8.8 | 0.0282 | 97.4 | 46 | 0 | 1 | 45 |
