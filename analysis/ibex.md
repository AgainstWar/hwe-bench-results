# Ibex Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 32
  total: 35
  pct: 91
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 32
  total: 35
  pct: 91
  infra_errors: 0
```

## 未解决 Case

```json
[
  {"pr": 104,  "test": "unknown",  "type": "spec",         "desc": "Trap 处理不符合 RISC-V 特权规范, 异常/中断及相关 CSR 需重做"},
  {"pr": 276,  "test": "unknown",  "type": "timing_sync",  "desc": "加载存储单元存在通过外部请求/响应信号的时序环路"},
  {"pr": 1865, "test": "unknown",  "type": "interface",    "desc": "core_busy_o 状态信号为单比特, 可能被毛刺拉低, 需改为多比特保护编码"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  spec: 1
  timing_sync: 1
  interface: 1
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 31
    prs: [list]
  official_only:
    count: 1
    prs: [1865]
  opencode_only:
    count: 0
    prs: []
  neither:
    count: 2
    prs: [104, 276]
```

## 结论

Ibex 仅 3 个 case 未解决，其中 2 个官方也没解（pr-104 和 pr-276），1 个官方能解而 OpenCode 没解（pr-1865, interface 类型）。整体修复率持平（91%），Verilog 项目不受模型退化影响。
