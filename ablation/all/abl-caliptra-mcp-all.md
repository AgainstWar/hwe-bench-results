# Caliptra MCP + All Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  resolved: 13/16 (81%)
mcp_alone:
  resolved: 12/16 (75%)
mcp_all:
  resolved: 8/16 (50%)
```

## MCP + All vs Baseline

| 指标 | Baseline | MCP + All |
|------|:--------:|:---------:|
| 解决 | 13/16 (81%) | 8/16 (50%) |
| 净变化 | | -5 |

### 新解决
  无

### 丢失
  ❌ pr-298: logic
  ❌ pr-506: interface
  ❌ pr-594: logic
  ❌ pr-1073: logic
  ❌ pr-1089: logic

## MCP + All vs MCP alone

| 指标 | MCP alone | MCP + All |
|------|:--------:|:----------:|
| 解决 | 12/16 (75%) | 8/16 (50%) |
| 净变化 | | -4 |

### 相对 MCP 新解决
  ✅ pr-633: logic

### 相对 MCP 丢失
  ❌ pr-298: logic
  ❌ pr-506: interface
  ❌ pr-594: logic
  ❌ pr-1073: logic
  ❌ pr-1089: logic

## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +0 | -1 | -1 |
| logic | +0 | -4 | -4 |

## 未解决 Case

```json
[
  {"pr": 70, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 506, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 1
  logic: 1
```
