# Caliptra MCP+Locate Analysis

## 总体结果

```yaml
baseline:
  resolved: 13/16 (81%)
mcp_alone:
  resolved: 12/16 (75%)
MCP+Locate:
  resolved: 8/16 (50%)
```

## MCP+Locate vs Baseline

| 指标 | Baseline | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 13/16 (81%) | 8/16 (50%) |
| 净变化 | | -5 |
### 新解决
  ✅ pr-725 (logic)
### 丢失
  ❌ pr-298 (logic)
  ❌ pr-633 (logic)
  ❌ pr-757 (timing_sync)
  ❌ pr-786 (logic)
  ❌ pr-1073 (logic)
  ❌ pr-1089 (logic)
## MCP+Locate vs MCP alone

| 指标 | MCP alone | MCP+Locate |
|------|:--------:|:-------:|
| 解决 | 12/16 (75%) | 8/16 (50%) |
| 净变化 | | -4 |

### 相对 MCP 新解决
  ✅ pr-725: logic
### 相对 MCP 丢失
  ❌ pr-298: logic
  ❌ pr-757: timing_sync
  ❌ pr-786: logic
  ❌ pr-1073: logic
  ❌ pr-1089: logic
## Bug Type 影响（vs Baseline）

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| logic | +1 | -5 | -4 |
| timing_sync | +0 | -1 | -1 |

## 未解决 Case

```json
[
  {"pr": 757, "test": "N/A", "type": "timing_sync", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  timing_sync: 1
```
