# Ibex Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 27
  total: 35
  pct: 77%
  infra_errors: 0

skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skills: locate + repair
  resolved: 21
  total: 35
  pct: 60%
  infra_errors: 0
```

## Skills vs Baseline

| 指标 | Baseline | Skills |
|------|:--------:|:------:|
| 解决 | 27/35 (77%) | 21/35 (60%) |
| 净变化 | | -6 |
| 基础设施错误 | 0 | 0 |

### 新解决
  ✅ pr-974: timing_sync
  ✅ pr-1141: interface

### 丢失
  ❌ pr-83: logic
  ❌ pr-293: interface
  ❌ pr-332: spec
  ❌ pr-882: logic
  ❌ pr-1469: spec
  ❌ pr-1584: spec
  ❌ pr-1816: spec
  ❌ pr-2232: interface

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +1 | -2 | -1 |
| logic | +0 | -2 | -2 |
| spec | +0 | -4 | -4 |
| timing_sync | +1 | -0 | +1 |

## 未解决 Case

```json
[
  {"pr": 83, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 155, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 293, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 332, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 475, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 882, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1469, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 1816, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 2232, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  interface: 4
  logic: 4
  spec: 5
```

## 结论

Skills 在该项目上有轻微退步。 基础设施错误为 0。
