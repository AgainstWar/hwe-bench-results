# Ibex Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 32
  total: 35
  resolved_rate: 91.4%
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 32
  total: 35
  resolved_rate: 91.4%
  file_level_precision: 88.3%
  infra_errors: 0
```

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-45 | 100.0% | 1/1 |
| pr-48 | 100.0% | 1/1 |
| pr-54 | 100.0% | 1/1 |
| pr-83 | 100.0% | 1/1 |
| pr-104 | 85.7% | 6/7 |
| pr-122 | 100.0% | 1/1 |
| pr-155 | 100.0% | 1/1 |
| pr-157 | 100.0% | 1/1 |
| pr-166 | 100.0% | 1/1 |
| pr-167 | 100.0% | 1/1 |
| pr-176 | 100.0% | 1/1 |
| pr-222 | 100.0% | 1/1 |
| pr-244 | 100.0% | 3/3 |
| pr-276 | 100.0% | 1/1 |
| pr-282 | 100.0% | 1/1 |
| pr-293 | 100.0% | 1/1 |
| pr-332 | 100.0% | 1/1 |
| pr-377 | 50.0% | 1/2 |
| pr-465 | 80.0% | 4/5 |
| pr-475 | 100.0% | 1/1 |
| pr-882 | 100.0% | 2/2 |
| pr-907 | 100.0% | 2/2 |
| pr-974 | 100.0% | 3/3 |
| pr-1135 | 100.0% | 1/1 |
| pr-1141 | 75.0% | 3/4 |
| pr-1229 | 100.0% | 2/2 |
| pr-1383 | 100.0% | 1/1 |
| pr-1469 | 100.0% | 1/1 |
| pr-1513 | 60.0% | 3/5 |
| pr-1584 | 100.0% | 4/4 |
| pr-1735 | 100.0% | 1/1 |
| pr-1780 | 33.3% | 1/3 |
| pr-1816 | 50.0% | 1/2 |
| pr-1865 | 100.0% | 1/1 |
| pr-2232 | 100.0% | 12/12 |

## File-Level Precision

- **Overall**: 88.3%
- **Average (per-task)**: 92.4%

## 未解决 Case

```json
[
  {
    "pr": 104,
    "test": "unknown",
    "type": "spec",
    "desc": "Trap 处理不符合 RISC-V 特权规范, 异常/中断及相关 CSR 需重做"
  },
  {
    "pr": 276,
    "test": "unknown",
    "type": "timing_sync",
    "desc": "加载存储单元存在通过外部请求/响应信号的时序环路"
  },
  {
    "pr": 1865,
    "test": "unknown",
    "type": "interface",
    "desc": "core_busy_o 状态信号为单比特, 可能被毛刺拉低, 需改为多比特保护编码"
  }
]
```

## Bug 类型分布

```yaml
  interface: 1
  spec: 1
  timing_sync: 1
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1879.5
  completion_k: 6.3
  cache_hit_pct: 95.6
  tool_calls: 59.3
  mcp_calls: 0.0
  skill_calls: 0.0
  ordinary_calls: 59.3
  cost_usd: 0.942087
  own_price_cost_usd: 2.412784
  tasks: 35
  resolved: 32
  unresolved: 3
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|-------|----------|
| ibex-pr-104 | unresolved | 5577.0 | 16.3 | 2.2281 | 97.1 | 111 | 0 | 0 | 111 |
| ibex-pr-1135 | resolved | 1044.9 | 2.9 | 0.5562 | 94.6 | 41 | 0 | 0 | 41 |
| ibex-pr-1141 | resolved | 3990.0 | 11.6 | 1.7397 | 96.6 | 91 | 0 | 0 | 91 |
| ibex-pr-122 | resolved | 1165.9 | 5.6 | 0.6669 | 94.8 | 42 | 0 | 0 | 42 |
| ibex-pr-1229 | resolved | 965.1 | 3.6 | 0.5277 | 93.0 | 44 | 0 | 0 | 44 |
| ibex-pr-1383 | resolved | 2063.3 | 8.5 | 0.9490 | 95.9 | 66 | 0 | 0 | 66 |
| ibex-pr-1469 | resolved | 1814.1 | 4.2 | 0.9373 | 94.9 | 61 | 0 | 0 | 61 |
| ibex-pr-1513 | resolved | 2166.9 | 6.6 | 0.9945 | 96.1 | 65 | 0 | 0 | 65 |
| ibex-pr-155 | resolved | 4883.0 | 12.1 | 2.0773 | 96.7 | 96 | 0 | 0 | 96 |
| ibex-pr-157 | resolved | 417.0 | 3.0 | 0.3556 | 90.2 | 40 | 0 | 0 | 40 |
| ibex-pr-1584 | resolved | 4716.3 | 10.9 | 2.0509 | 96.6 | 110 | 0 | 0 | 110 |
| ibex-pr-166 | resolved | 635.2 | 4.4 | 0.3889 | 94.3 | 46 | 0 | 0 | 46 |
| ibex-pr-167 | resolved | 696.8 | 3.7 | 0.4501 | 90.3 | 50 | 0 | 0 | 50 |
| ibex-pr-1735 | resolved | 3975.7 | 5.1 | 1.6282 | 96.0 | 65 | 0 | 0 | 65 |
| ibex-pr-176 | resolved | 621.6 | 5.3 | 0.3937 | 94.1 | 43 | 0 | 0 | 43 |
| ibex-pr-1780 | resolved | 3180.8 | 7.4 | 1.4280 | 96.5 | 85 | 0 | 0 | 85 |
| ibex-pr-1816 | resolved | 2189.6 | 7.3 | 1.1553 | 95.9 | 70 | 0 | 0 | 70 |
| ibex-pr-1865 | unresolved | 862.9 | 3.7 | 0.6641 | 93.2 | 44 | 0 | 0 | 44 |
| ibex-pr-222 | resolved | 559.1 | 3.1 | 0.3916 | 91.5 | 40 | 0 | 0 | 40 |
| ibex-pr-2232 | resolved | 3523.3 | 9.1 | 1.5208 | 95.6 | 91 | 0 | 0 | 91 |
| ibex-pr-244 | resolved | 2444.8 | 6.5 | 1.1000 | 96.4 | 78 | 0 | 0 | 78 |
| ibex-pr-276 | unresolved | 1142.5 | 5.1 | 0.9773 | 91.9 | 42 | 0 | 0 | 42 |
| ibex-pr-282 | resolved | 806.3 | 4.1 | 0.5327 | 93.3 | 49 | 0 | 0 | 49 |
| ibex-pr-293 | resolved | 1819.1 | 9.3 | 1.2209 | 95.5 | 50 | 0 | 0 | 50 |
| ibex-pr-332 | resolved | 1145.9 | 6.4 | 1.0447 | 92.7 | 34 | 0 | 0 | 34 |
| ibex-pr-377 | resolved | 1572.3 | 6.4 | 0.9099 | 94.4 | 48 | 0 | 0 | 48 |
| ibex-pr-45 | resolved | 512.4 | 2.8 | 0.2881 | 93.4 | 38 | 0 | 0 | 38 |
| ibex-pr-465 | resolved | 3042.4 | 10.5 | 1.3425 | 96.8 | 86 | 0 | 0 | 86 |
| ibex-pr-475 | resolved | 765.0 | 3.3 | 0.4394 | 92.4 | 50 | 0 | 0 | 50 |
| ibex-pr-48 | resolved | 536.6 | 4.8 | 0.3958 | 93.2 | 35 | 0 | 0 | 35 |
| ibex-pr-54 | resolved | 420.4 | 3.5 | 0.2967 | 92.1 | 26 | 0 | 0 | 26 |
| ibex-pr-83 | resolved | 519.2 | 3.7 | 0.3517 | 90.3 | 44 | 0 | 0 | 44 |
| ibex-pr-882 | resolved | 3911.0 | 12.1 | 1.7370 | 97.4 | 87 | 0 | 0 | 87 |
| ibex-pr-907 | resolved | 759.6 | 3.7 | 0.5082 | 93.0 | 43 | 0 | 0 | 43 |
| ibex-pr-974 | resolved | 1336.5 | 5.5 | 0.7242 | 94.1 | 65 | 0 | 0 | 65 |
