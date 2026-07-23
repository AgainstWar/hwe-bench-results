# CVA6 MCP + All Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  resolved: 28/35 (80%)
mcp_alone:
  resolved: 31/35 (89%)
mcp_all:
  resolved: 27/35 (77%)
```

## MCP + All vs Baseline

| 指标 | Baseline | MCP + All |
|------|:--------:|:---------:|
| 解决 | 28/35 (80%) | 27/35 (77%) |
| 净变化 | | -1 |

### 新解决
  ✅ pr-2279: interface
  ✅ pr-2420: config_integ
  ✅ pr-2989: spec

### 丢失
  ❌ pr-2032: logic
  ❌ pr-2282: logic
  ❌ pr-2916: interface
  ❌ pr-3226: logic

## MCP + All vs MCP alone

| 指标 | MCP alone | MCP + All |
|------|:--------:|:----------:|
| 解决 | 31/35 (89%) | 27/35 (77%) |
| 净变化 | | -4 |

### 相对 MCP 新解决
  无

### 相对 MCP 丢失
  ❌ pr-2032: logic
  ❌ pr-2282: logic
  ❌ pr-2916: interface
  ❌ pr-3226: logic

## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +1 | -0 | +1 |
| interface | +1 | -1 | +0 |
| logic | +0 | -3 | -3 |
| spec | +1 | -0 | +1 |

## 未解决 Case

```json
[
  {"pr": 2032, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 2844, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  logic: 1
  spec: 2
```
