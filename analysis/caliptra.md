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
