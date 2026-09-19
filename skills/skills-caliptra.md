# Caliptra SKILLS Analysis

## 总体结果

```yaml
skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 11
  total: 16
  resolved_rate: 68.8%
  file_level_precision: 76.2%
  infra_errors: 0
```

## 指标对比

| 指标 | Baseline | SKILLS |
|------|:--------:|:-------------:|
| Resolved Rate | 13/16 (81.2%) | 11/16 (68.8%) |
| File-Level Precision | 90.0% | 76.2% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-134 | 75.0% | 3/4 |
| pr-252 | 100.0% | 1/1 |
| pr-298 | 100.0% | 1/1 |
| pr-506 | 50.0% | 1/2 |
| pr-594 | 100.0% | 1/1 |
| pr-633 | 100.0% | 1/1 |
| pr-725 | 100.0% | 1/1 |
| pr-747 | 100.0% | 1/1 |
| pr-757 | 100.0% | 1/1 |
| pr-786 | 100.0% | 1/1 |
| pr-963 | 100.0% | 1/1 |
| pr-1033 | 50.0% | 1/2 |
| pr-1073 | 33.3% | 1/3 |
| pr-1089 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 76.2%
- **Average (per-task)**: 86.3%

## 未解决 Case

```json
[
  {
    "pr": 70,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 195,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 725,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 757,
    "test": "N/A",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1033,
    "test": "N/A",
    "type": "sw_hw_config",
    "desc": "N/A"
  }
]
```

## Bug 类型分布

```yaml
  logic: 1
  sw_hw_config: 1
  timing_sync: 1
  unknown: 2
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 781.7
  completion_k: 3.9
  cache_hit_pct: 94.0
  tool_calls: 22.4
  mcp_calls: 0.0
  other_skill_calls: 1.2
  ordinary_calls: 21.1
  cost_usd: 0.014015
  own_price_cost_usd: 0.215316
  tasks: 16
  resolved: 11
  unresolved: 5
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| caliptra-rtl-pr-1033 | unresolved | 1272.6 | 4.5 | 0.0236 | 92.5 | 26 | 0 | 1 | 25 |
| caliptra-rtl-pr-1073 | resolved | 1701.1 | 8.2 | 0.0183 | 97.0 | 39 | 0 | 2 | 37 |
| caliptra-rtl-pr-1089 | resolved | 1529.4 | 5.5 | 0.0185 | 96.5 | 35 | 0 | 2 | 33 |
| caliptra-rtl-pr-134 | resolved | 481.8 | 4.8 | 0.0093 | 92.4 | 31 | 0 | 0 | 31 |
| caliptra-rtl-pr-195 | unresolved | 144.7 | 2.0 | 0.0070 | 79.2 | 8 | 0 | 1 | 7 |
| caliptra-rtl-pr-252 | resolved | 191.9 | 1.4 | 0.0075 | 85.2 | 8 | 0 | 0 | 8 |
| caliptra-rtl-pr-298 | resolved | 763.9 | 5.2 | 0.0176 | 92.6 | 25 | 0 | 3 | 22 |
| caliptra-rtl-pr-506 | resolved | 1605.6 | 4.3 | 0.0211 | 94.3 | 29 | 0 | 2 | 27 |
| caliptra-rtl-pr-594 | resolved | 473.6 | 3.8 | 0.0094 | 93.5 | 17 | 0 | 2 | 15 |
| caliptra-rtl-pr-633 | resolved | 1278.1 | 5.5 | 0.0154 | 96.6 | 43 | 0 | 1 | 42 |
| caliptra-rtl-pr-70 | unresolved | 1194.8 | 4.7 | 0.0320 | 94.2 | 34 | 0 | 1 | 33 |
| caliptra-rtl-pr-725 | unresolved | 542.4 | 2.7 | 0.0111 | 90.6 | 15 | 0 | 1 | 14 |
| caliptra-rtl-pr-747 | resolved | 127.9 | 1.4 | 0.0054 | 82.2 | 6 | 0 | 1 | 5 |
| caliptra-rtl-pr-757 | unresolved | 608.4 | 3.2 | 0.0129 | 96.4 | 21 | 0 | 1 | 20 |
| caliptra-rtl-pr-786 | resolved | 441.5 | 2.6 | 0.0111 | 89.5 | 13 | 0 | 1 | 12 |
| caliptra-rtl-pr-963 | resolved | 149.4 | 1.9 | 0.0042 | 87.6 | 8 | 0 | 1 | 7 |
