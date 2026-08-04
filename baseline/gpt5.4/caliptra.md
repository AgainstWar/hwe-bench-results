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

## Token 统计（token_report.py）

```yaml
token_statistics:
  tasks: 16
  status: resolved=16
  prompt_k: 2170.0
  completion_k: 6.8
  cache_hit_pct: 94.5
  tool_calls: 58.2
  cost_usd: 1.102473
```

## File-Level Precision

- **Overall**: 59.0%
