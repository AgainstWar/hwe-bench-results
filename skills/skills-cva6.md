# CVA6 Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 28
  total: 35
  pct: 80%
  infra_errors: 0

skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skills: locate + repair
  resolved: 25
  total: 35
  pct: 71%
  infra_errors: 0
```

## Skills vs Baseline

| 指标 | Baseline | Skills |
|------|:--------:|:------:|
| 解决 | 28/35 (80%) | 25/35 (71%) |
| 净变化 | | -3 |
| 基础设施错误 | 0 | 0 |

### 新解决
  ✅ pr-2279: interface
  ✅ pr-2989: spec

### 丢失
  ❌ pr-2374: spec
  ❌ pr-2549: logic
  ❌ pr-2711: spec
  ❌ pr-2916: interface
  ❌ pr-3168: logic

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| interface | +1 | -1 | +0 |
| logic | +0 | -2 | -2 |
| spec | +1 | -2 | -1 |

## 未解决 Case

```json
[
  {"pr": 2170, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 2420, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 2711, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 2802, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 2916, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 3042, "test": "N/A", "type": "interface", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 3
  spec: 2
```

## 结论

Skills 在该项目上有轻微退步。 基础设施错误为 0。
