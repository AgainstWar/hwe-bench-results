# Ibex Analysis (DeepSeek V4 Flash)

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: DeepSeek V3.2
  resolved: 21
  total: 35
  pct: 60
  infra_errors: 0

opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 27
  total: 35
  pct: 77
  infra_errors: 0
```

## 未解决 Case

```json
[
  {"pr": 104,  "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1141, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1229, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1513, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 155,  "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 475,  "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 907,  "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 974,  "test": "unknown",  "type": "logic",         "desc": "unknown"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  logic: 8
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 18
    prs: [1135, 122, 1383, 157, 166, 167, 176, 1780, 222, 2232, 244, 282, 377, 45, 48, 54, 83, 882]
  official_only:
    count: 3
    prs: [1141, 475, 907]
  opencode_only:
    count: 9
    prs: [1469, 1584, 1735, 1816, 1865, 276, 293, 332, 465]
  neither:
    count: 5
    prs: [104, 1229, 1513, 155, 974]
```

## 结论

DeepSeek V4 Flash (OpenCode) 在 ibex 上 27/35 (77%)，高于官方 V3.2 (Codex) 的 60%。OpenCode agent 在 Verilog 项目上表现优于 Codex，模型升级也带来了 17% 的提升。0 基础设施错误。
