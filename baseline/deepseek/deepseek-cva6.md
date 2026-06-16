# CVA6 Analysis (DeepSeek V4 Flash)

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: DeepSeek V3.2
  resolved: 24
  total: 34
  pct: 71
  infra_errors: 0

opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 28
  total: 34
  pct: 82
  infra_errors: 0
```

## 未解决 Case

```json
[
  {"pr": 2279, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2420, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2802, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2844, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2989, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 3042, "test": "unknown",  "type": "logic",         "desc": "unknown"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  logic: 6
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 22
    prs: [1482, 2017, 2032, 2282, 2330, 2374, 2375, 2468, 2469, 2549, 2589, 2685, 2711, 2728, 2916, 2945, 3059, 3137, 3171, 3191, 3204, 3226]
  official_only:
    count: 2
    prs: [2420, 2989]
  opencode_only:
    count: 6
    prs: [2053, 2123, 2603, 2658, 2833, 2938]
  neither:
    count: 4
    prs: [2279, 2802, 2844, 3042]
```

## 结论

DeepSeek V4 Flash (OpenCode) 在 cva6 上 28/34 (82%)，高于官方 V3.2 (Codex) 的 71%。表现优于官方 V3.2，0 基础设施错误。
