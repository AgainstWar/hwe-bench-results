# RocketChip Analysis (DeepSeek V4 Flash)

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: DeepSeek V3.2
  resolved: 16
  total: 32
  pct: 50
  infra_errors: 0

opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 32
  pct: 25
  infra_errors: 0
```

## 未解决 Case

```json
[
  {"pr": 1093, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1176, "test": "unknown",  "type": "interface",     "desc": "unknown"},
  {"pr": 1493, "test": "unknown",  "type": "config_integ",  "desc": "unknown"},
  {"pr": 1656, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1761, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 177,  "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1878, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 2018, "test": "unknown",  "type": "interface",     "desc": "unknown"},
  {"pr": 2036, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2167, "test": "unknown",  "type": "timing_sync",   "desc": "unknown"},
  {"pr": 2213, "test": "unknown",  "type": "interface",     "desc": "unknown"},
  {"pr": 2368, "test": "unknown",  "type": "config_integ",  "desc": "unknown"},
  {"pr": 2543, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2621, "test": "unknown",  "type": "config_integ",  "desc": "unknown"},
  {"pr": 3004, "test": "unknown",  "type": "timing_sync",   "desc": "unknown"},
  {"pr": 3256, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 3526, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 3600, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 3624, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 3651, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 387,  "test": "unknown",  "type": "timing_sync",   "desc": "unknown"},
  {"pr": 404,  "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 485,  "test": "unknown",  "type": "interface",     "desc": "unknown"},
  {"pr": 745,  "test": "unknown",  "type": "config_integ",  "desc": "unknown"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  logic: 9
  interface: 4
  timing_sync: 3
  spec: 4
  config_integ: 4
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 7
    prs: [542, 576, 1330, 2984, 2988, 2994, 3065]
  official_only:
    count: 9
    prs: [177, 404, 1093, 1176, 1878, 2018, 2036, 2213, 3256]
  opencode_only:
    count: 1
    prs: [1656]
  neither:
    count: 15
    prs: [387, 485, 745, 1493, 1761, 2167, 2368, 2543, 2621, 3004, 3526, 3600, 3624, 3651]
```

## 结论

DeepSeek V4 Flash (OpenCode) 在 rocketchip 上 8/32 (25%)，低于官方 V3.2 (Codex) 的 50%。Chisel 项目构建体系过重，agent run 期间无法获取仿真反馈，修复以静态分析为主。0 基础设施错误。
