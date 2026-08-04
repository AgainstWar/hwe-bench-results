# Ibex Ablation - REPAIR

## 总体结果

```yaml
baseline (no skill):
  resolved: 27
  total: 35
  pct: 77%

repair:
  resolved: 25
  total: 35
  pct: 71%
```

## REPAIR vs Baseline

| 指标 | Baseline | REPAIR |
|------|:--------:|:--------------:|
| 解决 | 27/35 (77%) | 25/35 (71%) |
| 净变化 | | -2 |

### 新解决
  ✅ pr-475: spec
  ✅ pr-1141: interface

### 丢失
  ❌ pr-54: logic
  ❌ pr-332: spec
  ❌ pr-882: logic
  ❌ pr-1135: config_integ

## Bug Type 影响

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +0 | -1 | -1 |
| interface | +1 | -0 | +1 |
| logic | +0 | -2 | -2 |
| spec | +1 | -1 | +0 |

## 未解决 Case

```json
[
  {"pr": 54, "test": "N/A", "type": "logic", "desc": "N/A"},
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 332, "test": "N/A", "type": "spec", "desc": "N/A"},
  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 974, "test": "N/A", "type": "timing_sync", "desc": "N/A"},
  {"pr": 1135, "test": "N/A", "type": "config_integ", "desc": "N/A"},
  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},
  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  interface: 2
  logic: 2
  spec: 2
  timing_sync: 1
```

## File-Level Precision

- **Overall**: 93.6%
- **Average (per-task)**: 96.5%

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
| pr-104 | 100.0% | 5/5 |
| pr-122 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 1/1 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 100.0% | 1/1 |
| pr-465 | 100.0% | 1/1 |
| pr-475 | 100.0% | 1/1 |
| pr-907 | 100.0% | 1/1 |
| pr-974 | 100.0% | 1/1 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 100.0% | 1/1 |
| pr-1229 | 50.0% | 1/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 83.3% | 5/6 |
| pr-1513 | 50.0% | 1/2 |
| pr-1584 | 100.0% | 2/2 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 100.0% | 1/1 |
| pr-1816 | 100.0% | 1/1 |
| pr-1865 | 100.0% | 2/2 |
| pr-2232 | 100.0% | 2/2 |


## Token 统计（token_report.py）

### 平均指标



### 逐 Task 明细

注：此配置使用 combined tarball，token 数据为所有 repo 混合统计，无法拆分为 per-task 明细。

