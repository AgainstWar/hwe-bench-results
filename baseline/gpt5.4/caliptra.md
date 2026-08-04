# Caliptra Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 16
  total: 16
  pct: 100
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 16
  total: 16
  pct: 100
  infra_errors: 0
```

## 未解决 Case

无。全部 16 个 case 均被 OpenCode 修复，与官方持平。

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 16
    prs: [全部]
  official_only:
    count: 0
    prs: []
  opencode_only:
    count: 0
    prs: []
  neither:
    count: 0
    prs: []
```

## 结论

Caliptra 所有 16 个 case 全部修复（100%），与官方结果完全一致。
## File-Level Precision

- **Overall**: 59.0%

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 16
  status: unresolved=16
  prompt_k: 2170.0
  completion_k: 6.8
  cache_hit_pct: 94.5
  tool_calls: 58.2
  cost_usd: 1.102473
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| caliptra-rtl-pr-1033__JZHhi66 | resolved | 6279.5 | 13.4 | 2.7814 | 96.3 | 92 |
| caliptra-rtl-pr-1073__yho8TMN | resolved | 2765.2 | 9.7 | 1.2893 | 95.4 | 64 |
| caliptra-rtl-pr-1089__NHut5DY | resolved | 1346.2 | 6.1 | 0.7684 | 93.2 | 42 |
| caliptra-rtl-pr-134__vFag4vP | resolved | 1395.2 | 5.3 | 0.7544 | 92.3 | 61 |
| caliptra-rtl-pr-195__CjbdQjw | resolved | 1323.1 | 4.3 | 0.7449 | 92.3 | 44 |
| caliptra-rtl-pr-252__uvA8F9Y | resolved | 3272.8 | 8.6 | 1.5613 | 94.8 | 68 |
| caliptra-rtl-pr-298__z998Ava | resolved | 724.3 | 3.7 | 0.4511 | 94.0 | 42 |
| caliptra-rtl-pr-506__BEHYAVJ | resolved | 1843.7 | 6.9 | 1.0692 | 94.1 | 70 |
| caliptra-rtl-pr-594__sVT7brW | resolved | 773.5 | 6.9 | 0.5850 | 93.7 | 41 |
| caliptra-rtl-pr-633__U3gHrC7 | resolved | 2164.3 | 8.0 | 1.3075 | 90.8 | 67 |
| caliptra-rtl-pr-70__7GrLSeo | resolved | 6633.3 | 10.7 | 2.8875 | 95.2 | 97 |
| caliptra-rtl-pr-725__t4bLwYj | resolved | 1205.5 | 4.5 | 0.6701 | 93.5 | 40 |
| caliptra-rtl-pr-747__Q2Hkphr | resolved | 649.8 | 5.2 | 0.4587 | 93.8 | 45 |
| caliptra-rtl-pr-757__BuBQt4y | resolved | 1410.8 | 6.6 | 0.8120 | 94.4 | 49 |
| caliptra-rtl-pr-786__hFCD7Cn | resolved | 2177.1 | 6.0 | 1.0598 | 94.5 | 65 |
| caliptra-rtl-pr-963__8J6zZCS | resolved | 755.4 | 3.2 | 0.4387 | 93.3 | 44 |

