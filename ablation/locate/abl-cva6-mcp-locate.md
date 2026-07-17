# Cva6 MCP+Locate Analysis

## 总体结果

```yaml
baseline:
  resolved: 28/35 (80%)
mcp_alone:
  resolved: 31/35 (89%)
MCP+Locate:
  resolved: 24/35 (69%)
```

## MCP+Locate vs Baseline

| 指标 | Baseline | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 28/35 (80%) | 24/35 (69%) |
| 净变化 | | -4 |
### 新解决
  ✅ pr-2279 (interface)
  ✅ pr-2989 (spec)
### 丢失
  ❌ pr-2017 (logic)
  ❌ pr-2282 (logic)
  ❌ pr-2468 (logic)
  ❌ pr-2916 (interface)
  ❌ pr-2944 (logic)
  ❌ pr-3168 (logic)
## MCP+Locate vs MCP alone

| 指标 | MCP alone | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 31/35 (89%) | 24/35 (69%) |
| 净变化 | | -7 |

### 相对 MCP 新解决
  无

### 相对 MCP 丢失
  ❌ pr-2017: logic
  ❌ pr-2282: logic
  ❌ pr-2420: config_integ
  ❌ pr-2468: logic
  ❌ pr-2916: interface
  ❌ pr-2944: logic
  ❌ pr-3168: logic
## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +1 | -1 | +0 |
| logic | +0 | -5 | -5 |
| spec | +1 | -0 | +1 |

## 未解决 Case

```json
[
  {"pr": 2170, "test": "N/A", "type": "config_integ", "desc": "N/A"},  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 2944, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 3042, "test": "N/A", "type": "config_integ", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 2
  logic: 1
  spec: 1
```
