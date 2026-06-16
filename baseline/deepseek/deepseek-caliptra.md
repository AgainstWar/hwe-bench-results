# Caliptra-Rtl Analysis (DeepSeek V4 Flash)

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: DeepSeek V3.2
  resolved: 13
  total: 16
  pct: 81
  infra_errors: 0

opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 13
  total: 16
  pct: 81
  infra_errors: 0
```

## 未解决 Case

```json
[
  {"pr": 1033, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 70, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 725, "test": "need_check", "type": "need_classification", "desc": "unknown"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  need_classification: 3
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 11
    prs: [1073, 1089, 252, 298, 506, 594, 633, 747, 757, 786, 963]
  official_only:
    count: 2
    prs: [70, 725]
  opencode_only:
    count: 2
    prs: [134, 195]
  neither:
    count: 1
    prs: [1033]
```

## 结论

DeepSeek V4 Flash (OpenCode) 在 caliptra-rtl 上 13/16 (81%)。0 基础设施错误。
