# RocketChip Repair+Wave V2 Analysis

## 总体结果

```yaml
repair_wave_v2:
  agent: OpenCode
  model: DeepSeek V4 Flash
  skill: repair + wave (hdl-minimal-repair / wave)
  mcp: WAVES (WAVES_ENABLED=true)
  resolved: 11
  total: 32
  resolved_rate: 34.4%
  file_level_precision: 86.90%
  infra_errors: 0
```

## 指标对比（V2 系列）

| 指标 | Baseline V2 | Repair+Wave V2 |
|------|:-----------:|:--------------:|
| Resolved Rate | 20/32 (62.5%) | 11/32 (34.4%) |
| File-Level Precision | 94.52% | 86.90% |

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/11 |
| pr-387 | 100.0% | 2/2 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 100.0% | 11/11 |
| pr-542 | 100.0% | 1/1 |
| pr-576 | 100.0% | 1/1 |
| pr-745 | 100.0% | 2/2 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 8/8 |
| pr-1656 | 100.0% | 13/13 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 2/2 |
| pr-2213 | 100.0% | 2/2 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 100.0% | 1/1 |
| pr-2621 | 100.0% | 4/4 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 100.0% | 1/1 |
| pr-2994 | 100.0% | 1/1 |
| pr-3004 | 100.0% | 2/2 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 100.0% | 1/1 |
| pr-3600 | 100.0% | 3/3 |
| pr-3624 | 100.0% | 3/3 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 86.9%
- **Average (per-task)**: 96.9%

## 未解决 Case

| PR |
|----|
| pr-177 |
| pr-387 |
| pr-404 |
| pr-745 |
| pr-1093 |
| pr-1176 |
| pr-1493 |
| pr-1761 |
| pr-1878 |
| pr-2018 |
| pr-2036 |
| pr-2167 |
| pr-2213 |
| pr-2368 |
| pr-2543 |
| pr-2621 |
| pr-3004 |
| pr-3065 |
| pr-3256 |
| pr-3624 |
| pr-3651 |

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1765.6
  completion_k: 5.9
  cache_hit_pct: 96.6
  tool_calls: 45.3
  mcp_calls: 0.0
  repair_skill_calls: 1.2
  wave_skill_calls: 0.0
  ordinary_calls: 44.2
  cost_usd: 0.024926
  tasks: 32
  resolved: 11
  unresolved: 21
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Repair Skill | Wave Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|-----|--------------|------------|----------|
| rocket-chip-pr-177__w2JLdXt | unresolved | 909.5 | 5.9 | 0.0202 | 92.8 | 36 | 0 | 1 | 0 | 35 |
| rocket-chip-pr-387__F9sEJ8k | unresolved | 1096.6 | 5.5 | 0.0232 | 94.5 | 41 | 0 | 0 | 0 | 41 |
| rocket-chip-pr-404__uZ9etWa | unresolved | 577.1 | 3.6 | 0.0111 | 95.9 | 29 | 0 | 1 | 0 | 28 |
| rocket-chip-pr-485__yyx7h42 | resolved | 5429.3 | 9.6 | 0.0448 | 98.4 | 92 | 0 | 1 | 0 | 91 |
| rocket-chip-pr-542__vCtQxQs | resolved | 5006.8 | 29.6 | 0.0614 | 96.6 | 84 | 0 | 2 | 0 | 82 |
| rocket-chip-pr-576__LoJFce8 | resolved | 802.7 | 2.7 | 0.0180 | 93.3 | 27 | 0 | 1 | 0 | 26 |
| rocket-chip-pr-745__M5JZ7fC | unresolved | 3322.8 | 8.7 | 0.0397 | 97.6 | 76 | 0 | 1 | 0 | 75 |
| rocket-chip-pr-1069__ByjmEaM | resolved | 2299.8 | 7.7 | 0.0269 | 97.3 | 56 | 0 | 2 | 0 | 54 |
| rocket-chip-pr-1093__iajPz9r | unresolved | 1731.1 | 6.2 | 0.0240 | 97.3 | 65 | 0 | 0 | 0 | 65 |
| rocket-chip-pr-1176__paVeaMf | unresolved | 1007.9 | 4.3 | 0.0185 | 95.7 | 35 | 0 | 2 | 0 | 33 |
| rocket-chip-pr-1330__At9QYfy | resolved | 2196.4 | 10.8 | 0.0395 | 97.5 | 60 | 0 | 1 | 0 | 59 |
| rocket-chip-pr-1493__usFy2wg | unresolved | 5449.8 | 10.1 | 0.0538 | 98.0 | 77 | 0 | 1 | 0 | 76 |
| rocket-chip-pr-1656__ojLRrmM | resolved | 3441.4 | 7.7 | 0.0462 | 97.0 | 73 | 0 | 0 | 0 | 73 |
| rocket-chip-pr-1761__fWV4qyH | unresolved | 490.8 | 2.5 | 0.0122 | 94.2 | 24 | 0 | 2 | 0 | 22 |
| rocket-chip-pr-1878__WTh9Wo7 | unresolved | 618.1 | 2.9 | 0.0124 | 94.1 | 30 | 0 | 1 | 0 | 29 |
| rocket-chip-pr-2018__gQoVwJE | unresolved | 961.7 | 3.7 | 0.0172 | 94.5 | 33 | 0 | 1 | 0 | 32 |
| rocket-chip-pr-2036__HBBNXHp | unresolved | 748.5 | 2.8 | 0.0160 | 92.9 | 27 | 0 | 1 | 0 | 26 |
| rocket-chip-pr-2167__JCPzAdp | unresolved | 1434.9 | 5.5 | 0.0212 | 96.4 | 50 | 0 | 2 | 0 | 48 |
| rocket-chip-pr-2213__UbJbhQS | unresolved | 2515.1 | 7.5 | 0.0315 | 97.6 | 67 | 0 | 2 | 0 | 65 |
| rocket-chip-pr-2368__paaWt78 | unresolved | 568.9 | 3.0 | 0.0119 | 93.5 | 27 | 0 | 0 | 0 | 27 |
| rocket-chip-pr-2543__ZZ3wt4Q | unresolved | 600.7 | 2.6 | 0.0115 | 94.2 | 28 | 0 | 2 | 0 | 26 |
| rocket-chip-pr-2621__vd3Yw6M | unresolved | 1465.5 | 5.8 | 0.0277 | 95.1 | 49 | 0 | 2 | 0 | 47 |
| rocket-chip-pr-2984__6bmV5aE | resolved | 1493.5 | 3.8 | 0.0218 | 96.3 | 38 | 0 | 1 | 0 | 37 |
| rocket-chip-pr-2988__ETCDgLF | resolved | 218.9 | 1.5 | 0.0057 | 90.0 | 15 | 0 | 1 | 0 | 14 |
| rocket-chip-pr-2994__wEXE72g | resolved | 1684.4 | 4.2 | 0.0224 | 96.4 | 45 | 0 | 1 | 0 | 44 |
| rocket-chip-pr-3004__VQrppsC | unresolved | 1277.1 | 3.9 | 0.0206 | 93.9 | 33 | 0 | 2 | 0 | 31 |
| rocket-chip-pr-3065__TySE4i6 | unresolved | 1123.4 | 3.7 | 0.0172 | 95.8 | 31 | 0 | 1 | 0 | 30 |
| rocket-chip-pr-3256__uzjcwmN | unresolved | 2272.7 | 4.2 | 0.0271 | 96.6 | 43 | 0 | 1 | 0 | 42 |
| rocket-chip-pr-3526__3q4SGrq | resolved | 635.1 | 2.7 | 0.0165 | 91.8 | 20 | 0 | 1 | 0 | 19 |
| rocket-chip-pr-3600__Mj8SENF | resolved | 1413.5 | 2.9 | 0.0225 | 95.3 | 33 | 0 | 1 | 0 | 32 |
| rocket-chip-pr-3624__pQQfCRh | unresolved | 1142.2 | 7.5 | 0.0213 | 96.5 | 56 | 0 | 1 | 0 | 55 |
| rocket-chip-pr-3651__SPLXuCz | unresolved | 2562.3 | 5.6 | 0.0333 | 97.6 | 51 | 0 | 2 | 0 | 49 |

