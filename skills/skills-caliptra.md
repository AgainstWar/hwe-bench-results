# Caliptra Skills (locate + repair) Analysis

## 总体结果

```yaml
baseline:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 13
  total: 16
  pct: 81%
  infra_errors: 0

skills:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skills: locate + repair
  resolved: 11
  total: 16
  pct: 69%
  infra_errors: 0
```

## Skills vs Baseline

| 指标 | Baseline | Skills |
|------|:--------:|:------:|
| 解决 | 13/16 (81%) | 11/16 (69%) |
| 净变化 | | -2 |
| 基础设施错误 | 0 | 0 |

### 新解决
  无

### 丢失
  ❌ pr-195: logic
  ❌ pr-757: timing_sync

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| logic | +0 | -1 | -1 |
| timing_sync | +0 | -1 | -1 |

## 未解决 Case

```json
[
  {"pr": 725, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 757, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 1033, "test": "N/A", "type": "sw_hw_config", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  logic: 1
  sw_hw_config: 1
  timing_sync: 1
```

## 结论

Skills 在该项目上有轻微退步。 基础设施错误为 0。
