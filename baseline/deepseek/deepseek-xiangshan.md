# XiangShan Analysis (DeepSeek V4 Flash)

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: DeepSeek V3.2
  resolved: 25
  total: 54
  pct: 46
  infra_errors: 0

opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 51
  pct: 24
  infra_errors: 0
```

注：总数为 51 而非 54，3 个 PR（5080/5189/5593）agent 未产出 patch（empty_patch）。

## 未解决 Case

```json
[
  {"pr": 1242, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1323, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 1395, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1401, "test": "unknown",  "type": "timing_sync",   "desc": "unknown"},
  {"pr": 1602, "test": "unknown",  "type": "timing_sync",   "desc": "unknown"},
  {"pr": 1679, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1694, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1793, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1820, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 1907, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2095, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2195, "test": "unknown",  "type": "timing_sync",   "desc": "unknown"},
  {"pr": 2246, "test": "unknown",  "type": "config_integ",  "desc": "unknown"},
  {"pr": 2351, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2513, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2781, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 2997, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 3307, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 3329, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 3555, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 3636, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 3717, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 3753, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 3859, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 3907, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 3955, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 4110, "test": "unknown",  "type": "sw_hw_config",  "desc": "unknown"},
  {"pr": 4166, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 4179, "test": "unknown",  "type": "spec",          "desc": "unknown"},
  {"pr": 4426, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 4442, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 4533, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 4750, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 4968, "test": "unknown",  "type": "timing_sync",   "desc": "unknown"},
  {"pr": 5182, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 5496, "test": "unknown",  "type": "sw_hw_config",  "desc": "unknown"},
  {"pr": 5687, "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 655,  "test": "unknown",  "type": "logic",         "desc": "unknown"},
  {"pr": 739,  "test": "unknown",  "type": "logic",         "desc": "unknown"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  logic: 22
  timing_sync: 5
  spec: 6
  config_integ: 1
  sw_hw_config: 2
  interface: 1
  unknown: 2
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 10
    prs: [39, 281, 2845, 3182, 3867, 4337, 4764, 4959, 5700, 4943]
  official_only:
    count: 15
    prs: [1679, 1694, 2095, 2513, 2997, 3307, 3555, 3717, 3955, 4442, 5496, 5687, 739, 5080, 5593]
  opencode_only:
    count: 2
    prs: [1931, 2483]
  neither:
    count: 26
    prs: [655, 1242, 1323, 1395, 1401, 1602, 1793, 1820, 1907, 2195, 2246, 2351, 2781, 3329, 3636, 3753, 3859, 3907, 4110, 4166, 4179, 4426, 4533, 4750, 4968, 5182]
```

## 结论

DeepSeek V4 Flash (OpenCode) 在 xiangshan 上 12/51 (24%)，低于官方 V3.2 (Codex) 的 46%。3 个 PR 未产出 patch（empty_patch）。与 rocketchip 一样，Chisel 项目构建体系过重导致 agent 无法获取仿真反馈。0 基础设施错误。
