# CVA6 Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 34
  total: 35
  pct: 97
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 33
  total: 35
  pct: 94
  infra_errors: 0
```

## 未解决 Case

```json
[
  {"pr": 2170, "test": "unknown",  "type": "config_integ",  "desc": "WB cache 在 32-bit CVA6 构建中对齐错误, 64-bit AXI 总线宽度不匹配"},
  {"pr": 3042, "test": "unknown",  "type": "config_integ",  "desc": "AXI 参数宏无法从配置文件覆盖, 可能使用不一致的总线设置构建"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  config_integ: 2
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 33
    prs: [list]
  official_only:
    count: 1
    prs: [2170]
  opencode_only:
    count: 0
    prs: []
  neither:
    count: 1
    prs: [3042]
```

## 结论

CVA6 仅 2 个 case 未解决。官方能解而 OpenCode 没解的是 pr-2170（Config/Integ, AXI 总线宽度适配）。pr-3042 双方都没解。整体差距极小（97% vs 94%），Verilog 项目不受影响。
