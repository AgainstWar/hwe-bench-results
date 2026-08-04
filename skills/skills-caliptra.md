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

## 未解决 Case

```json
[
  {"pr": 725, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 757, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1033, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 1
  sw_hw_config: 1
  timing_sync: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 16
  status: unresolved=16
  prompt_k: 781.7
  completion_k: 3.9
  cache_hit_pct: 94.0
  tool_calls: 22.4
  cost_usd: 0.014015
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| caliptra-rtl-pr-1033__X8tvfeX | unresolved | 1272.6 | 4.5 | 0.0236 | 92.5 | 26 |
| caliptra-rtl-pr-1073__62vV6tf | resolved | 1701.1 | 8.2 | 0.0183 | 97.0 | 39 |
| caliptra-rtl-pr-1089__UHjdojN | resolved | 1529.4 | 5.5 | 0.0185 | 96.5 | 35 |
| caliptra-rtl-pr-134__d8HmhCv | resolved | 481.8 | 4.8 | 0.0093 | 92.4 | 31 |
| caliptra-rtl-pr-195__dU5mvsW | unresolved | 144.7 | 2.0 | 0.0070 | 79.2 | 8 |
| caliptra-rtl-pr-252__shKuWcQ | resolved | 191.9 | 1.4 | 0.0075 | 85.2 | 8 |
| caliptra-rtl-pr-298__6EJeS72 | resolved | 763.9 | 5.2 | 0.0176 | 92.6 | 25 |
| caliptra-rtl-pr-506__ozeNJW8 | resolved | 1605.6 | 4.3 | 0.0211 | 94.3 | 29 |
| caliptra-rtl-pr-594__VK6Gzkr | resolved | 473.6 | 3.8 | 0.0094 | 93.5 | 17 |
| caliptra-rtl-pr-633__BYKU4qo | resolved | 1278.1 | 5.5 | 0.0154 | 96.6 | 43 |
| caliptra-rtl-pr-70__rjhpQta | unresolved | 1194.8 | 4.7 | 0.0320 | 94.2 | 34 |
| caliptra-rtl-pr-725__zFZtNa2 | unresolved | 542.4 | 2.7 | 0.0111 | 90.6 | 15 |
| caliptra-rtl-pr-747__iW5BNPt | resolved | 127.9 | 1.4 | 0.0054 | 82.2 | 6 |
| caliptra-rtl-pr-757__np4CKfq | unresolved | 608.4 | 3.2 | 0.0129 | 96.4 | 21 |
| caliptra-rtl-pr-786__fBajr6i | resolved | 441.5 | 2.6 | 0.0111 | 89.5 | 13 |
| caliptra-rtl-pr-963__x8Cq5Xi | resolved | 149.4 | 1.9 | 0.0042 | 87.6 | 8 |

