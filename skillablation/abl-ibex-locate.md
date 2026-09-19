# Ibex Ablation - LOCATE

## 总体结果

```yaml
locate:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 7
  total: 35
  resolved_rate: 20.0%
  file_level_precision: 76.5%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | LOCATE |
|------|:--------:|:-------------:|
| Resolved Rate | 27/35 (77.1%) | 7/35 (20.0%) |
| File-Level Precision | 79.2% | 76.5% |

### 新解决
  无

### 丢失
  pr-45, pr-48, pr-83, pr-157, pr-167, pr-176, pr-222, pr-276, pr-282, pr-293, pr-332, pr-377, pr-465, pr-882, pr-1135, pr-1469, pr-1584, pr-1780, pr-1865, pr-2232

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-54 | 100.0% | 1/1 |
| pr-83 | 0.0% | 0/1 |
| pr-104 | 80.0% | 4/5 |
| pr-122 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-882 | 0.0% | 0/1 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1735 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 76.5%
- **Average (per-task)**: 77.5%

## 未解决 Case

```json
[
  {
    "pr": 45,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 48,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 83,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 104,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 155,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 157,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 167,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 176,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 222,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 276,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 282,
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
    "pr": 332,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 377,
    "test": "N/A",
    "type": "unknown",
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
    "type": "logic",
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
    "type": "unknown",
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
    "type": "unknown",
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
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1584,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1780,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 1865,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 2232,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  interface: 2
  logic: 2
  spec: 1
  unknown: 23
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 521.0
  completion_k: 3.7
  cache_hit_pct: 92.6
  tool_calls: 18.9
  mcp_calls: 0.0
  other_skill_calls: 1.0
  ordinary_calls: 17.9
  cost_usd: 0.011150
  own_price_cost_usd: 0.144746
  tasks: 35
  resolved: 7
  unresolved: 28
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| ibex-pr-104 | unresolved | 2566.6 | 13.7 | 0.0206 | 97.8 | 61 | 0 | 1 | 60 |
| ibex-pr-1135 | unresolved | 283.5 | 3.5 | 0.0112 | 86.5 | 10 | 0 | 1 | 9 |
| ibex-pr-1141 | unresolved | 543.2 | 4.7 | 0.0105 | 92.9 | 24 | 0 | 1 | 23 |
| ibex-pr-122 | resolved | 1091.2 | 4.9 | 0.0182 | 96.1 | 27 | 0 | 1 | 26 |
| ibex-pr-1229 | unresolved | 623.8 | 3.1 | 0.0148 | 89.8 | 25 | 0 | 1 | 24 |
| ibex-pr-1383 | resolved | 396.4 | 3.6 | 0.0073 | 93.6 | 18 | 0 | 1 | 17 |
| ibex-pr-1469 | unresolved | 389.6 | 2.8 | 0.0122 | 85.9 | 16 | 0 | 1 | 15 |
| ibex-pr-1513 | unresolved | 621.5 | 3.5 | 0.0136 | 88.3 | 22 | 0 | 1 | 21 |
| ibex-pr-155 | unresolved | 626.6 | 4.5 | 0.0176 | 94.9 | 31 | 0 | 1 | 30 |
| ibex-pr-157 | unresolved | 167.0 | 2.6 | 0.0061 | 85.5 | 10 | 0 | 1 | 9 |
| ibex-pr-1584 | unresolved | 403.3 | 4.3 | 0.0079 | 91.2 | 26 | 0 | 1 | 25 |
| ibex-pr-166 | resolved | 378.8 | 2.5 | 0.0067 | 91.7 | 15 | 0 | 1 | 14 |
| ibex-pr-167 | unresolved | 653.3 | 3.2 | 0.0138 | 92.9 | 18 | 0 | 1 | 17 |
| ibex-pr-1735 | resolved | 1474.3 | 6.8 | 0.0185 | 95.8 | 37 | 0 | 1 | 36 |
| ibex-pr-176 | unresolved | 63.3 | 1.6 | 0.0043 | 61.4 | 3 | 0 | 1 | 2 |
| ibex-pr-1780 | unresolved | 214.0 | 2.3 | 0.0128 | 74.7 | 8 | 0 | 1 | 7 |
| ibex-pr-1816 | resolved | 1489.4 | 7.0 | 0.0169 | 97.1 | 45 | 0 | 1 | 44 |
| ibex-pr-1865 | unresolved | 324.6 | 4.4 | 0.0080 | 91.1 | 17 | 0 | 1 | 16 |
| ibex-pr-222 | unresolved | 352.8 | 3.3 | 0.0092 | 91.6 | 20 | 0 | 1 | 19 |
| ibex-pr-2232 | unresolved | 242.8 | 3.1 | 0.0077 | 86.2 | 18 | 0 | 1 | 17 |
| ibex-pr-244 | resolved | 1176.2 | 4.1 | 0.0179 | 94.8 | 24 | 0 | 1 | 23 |
| ibex-pr-276 | unresolved | 132.9 | 2.0 | 0.0080 | 81.8 | 6 | 0 | 1 | 5 |
| ibex-pr-282 | unresolved | 81.3 | 1.5 | 0.0047 | 75.5 | 4 | 0 | 1 | 3 |
| ibex-pr-293 | unresolved | 810.7 | 3.9 | 0.0154 | 97.1 | 20 | 0 | 1 | 19 |
| ibex-pr-332 | unresolved | 263.8 | 2.3 | 0.0159 | 88.5 | 10 | 0 | 1 | 9 |
| ibex-pr-377 | unresolved | 115.2 | 2.0 | 0.0062 | 75.8 | 6 | 0 | 1 | 5 |
| ibex-pr-45 | unresolved | 70.9 | 1.6 | 0.0043 | 67.0 | 4 | 0 | 1 | 3 |
| ibex-pr-465 | unresolved | 227.0 | 2.4 | 0.0098 | 75.0 | 12 | 0 | 1 | 11 |
| ibex-pr-475 | unresolved | 155.5 | 4.2 | 0.0064 | 82.5 | 10 | 0 | 1 | 9 |
| ibex-pr-48 | unresolved | 153.8 | 2.5 | 0.0061 | 82.7 | 9 | 0 | 1 | 8 |
| ibex-pr-54 | resolved | 238.9 | 2.8 | 0.0061 | 87.9 | 13 | 0 | 1 | 12 |
| ibex-pr-83 | unresolved | 463.2 | 3.9 | 0.0098 | 93.5 | 24 | 0 | 1 | 23 |
| ibex-pr-882 | unresolved | 313.2 | 2.9 | 0.0111 | 86.9 | 12 | 0 | 1 | 11 |
| ibex-pr-907 | unresolved | 403.3 | 3.7 | 0.0171 | 90.9 | 17 | 0 | 1 | 16 |
| ibex-pr-974 | unresolved | 721.2 | 4.9 | 0.0135 | 93.2 | 40 | 0 | 1 | 39 |
