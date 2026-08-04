# RocketChip Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 23
  total: 32
  pct: 72
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 8
  total: 30
  pct: 27
  infra_errors: 0
```

## 未解决 Case

```json
[
  {"pr": 177,  "test": "lrsc_mshr_secondary_dirty",              "type": "logic",         "desc": "LR/SC 一致性状态更新错误, store-conditional 成功标志丢失"},
  {"pr": 387,  "test": "async_queue_half_reset",                 "type": "timing_sync",   "desc": "异步跨时钟域复位未完全清除 FIFO 状态, ready/valid 不安全"},
  {"pr": 485,  "test": "diplomatic_ahb_elaboration",             "type": "interface",     "desc": "AHB 适配器在 diplomacy 桥接中导致错误的总线接口行为"},
  {"pr": 745,  "test": "rocc_example_elaboration",               "type": "config_integ",  "desc": "Tile 交叉开关集成问题, 需要仲裁减少引脚并修复多 RoCC 配置"},
  {"pr": 1069, "test": "csr-decodewidth-multiport",              "type": "logic",         "desc": "CSR 非法指令解码只处理单条指令, 多发射解码检查错误"},
  {"pr": 1093, "test": "bus_error_unit_rv32_elaboration",        "type": "sw_hw_interact", "desc": "总线/ECC 错误路径缺少本地中断生成, 故障未上报软件"},
  {"pr": 1176, "test": "tl_mmio_port_internal_wiring",           "type": "interface",     "desc": "TL MMIO 端口在 diplomacy 连接中接线错误"},
  {"pr": 1493, "test": "async_pbus_bootrom_access",              "type": "config_integ",  "desc": "外设时钟域拆分需要将控制外设移到独立时钟/复位集成路径"},
  {"pr": 1761, "test": "csr-tvec-uninitialized-alignment",       "type": "logic",         "desc": "tvec 位清零在错误阶段执行, 首次写入前残留过期值"},
  {"pr": 1878, "test": "misa_x_bit",                             "type": "spec",          "desc": "misa.X 未为 CEASE 指令设置, 违反 ISA 特性报告规范"},
  {"pr": 2018, "test": "unknown",                                "type": "interface",     "desc": "TLToAHB 用户位未在事务 FSM 中保留, 地址和元数据不同步"},
  {"pr": 2036, "test": "mret_not_misdetected_as_dret",           "type": "logic",         "desc": "DRET 有效性检查了错误流水线阶段的 CSR 地址"},
  {"pr": 2167, "test": "jtag_async_reset",                       "type": "timing_sync",   "desc": "JTAG TDO 需要异步复位行为以匹配 jtag_reset 信号"},
  {"pr": 2213, "test": "debug_apb_gap_behavior",                 "type": "interface",     "desc": "Debug APB 未定义地址访问别名到有效寄存器而非返回错误"},
  {"pr": 2368, "test": "asyncvalidsync-mixed-reset-elaboration",  "type": "config_integ",  "desc": "AsyncValidSync 模块样式集成问题, 功能无变化"},
  {"pr": 2543, "test": "heterogeneous_hartid_elaboration",       "type": "logic",         "desc": "HartID/复位向量宽度计算使用了错误的 Chisel 兼容模式宽度逻辑"},
  {"pr": 2621, "test": "unknown",                                "type": "config_integ",  "desc": "L1 TLB 可配置 set/way 的 sectored-LRU 宽度错误"},
  {"pr": 3004, "test": "frontend_progress_quiesce",              "type": "timing_sync",   "desc": "Hypervisor 推测 ITLB 重填冲击 DCache, 阻塞旧加载的进度"},
  {"pr": 3256, "test": "aes64ks1i_decode",                       "type": "logic",         "desc": "AES64KS1I 解码将操作数当作 rs2 而非立即数"},
  {"pr": 3526, "test": "unknown",                                "type": "logic",         "desc": "S2 PTE 缓存命中逻辑更新了错误的 r_pte 条件"},
  {"pr": 3624, "test": "hypervisor_tinst_warl",                  "type": "spec",          "desc": "Hypervisor 客户页故障处理未按要求驱动 mtinst/htinst"},
  {"pr": 3651, "test": "unknown",                                "type": "spec",          "desc": "PTW GPA 位验证基于 PTE 有效性而非叶子节点性, 错误分类非叶子条目"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  logic: 7
  interface: 4
  timing_sync: 3
  config_integ: 4
  spec: 3
  sw_hw_interact: 1
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 8
    prs: [404, 542, 1330, 1656, 2984, 2988, 2994, 3065]
  official_only:
    count: 15
    prs: [177, 387, 745, 1069, 1176, 1761, 1878, 2018, 2036, 2167, 2213, 2543, 3526, 3624, 3600]
  opencode_only:
    count: 0
    prs: []
  neither:
    count: 8
    prs: [485, 1093, 1493, 2368, 2621, 3004, 3256, 3651]
```

## 结论

RocketChip 的 22 个未解决 case 全为 patch 质量问题, 基础设施错误 = 0。主要 bug 类型为 logic（7个）和 interface/config_integ（各 4 个）。OpenCode 在 RocketChip 上仅 27% 的修复率, 远低于官方的 72%, 差距比 XiangShan（50% vs 74%）更明显。值得注意的是 RocketChip 上 OpenCode 没有反超官方的 case（opencode_only = 0）。
## File-Level Precision

- **Overall**: 69.8%

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 32
  status: unresolved=32
  prompt_k: 1310.0
  completion_k: 5.1
  cache_hit_pct: 93.7
  tool_calls: 51.0
  cost_usd: 0.995443
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| rocket-chip-pr-1069__WRxrVkZ | unresolved | 358.9 | 4.0 | 0.3206 | 87.2 | 31 |
| rocket-chip-pr-1093__heq3fgv | unresolved | 2835.8 | 9.2 | 2.1777 | 94.9 | 88 |
| rocket-chip-pr-1176__tENFqsb | unresolved | 372.8 | 3.3 | 0.2904 | 87.1 | 43 |
| rocket-chip-pr-1330__AkLgTrK | resolved | 676.5 | 5.0 | 0.6211 | 92.6 | 58 |
| rocket-chip-pr-1493__Bwnc4X3 | unresolved | 891.4 | 3.5 | 0.5848 | 91.0 | 45 |
| rocket-chip-pr-1656__mW2tUGV | resolved | 686.8 | 4.3 | 0.9324 | 90.4 | 40 |
| rocket-chip-pr-1761__JepeedN | unresolved | 386.3 | 2.4 | 0.3794 | 86.7 | 21 |
| rocket-chip-pr-177__swWZW7e | unresolved | 507.7 | 3.5 | 0.3539 | 90.9 | 31 |
| rocket-chip-pr-1878__BPaEk62 | unresolved | 821.8 | 3.5 | 0.5039 | 92.1 | 45 |
| rocket-chip-pr-2018__f45KrKP | unresolved | 542.6 | 2.6 | 0.4581 | 86.9 | 25 |
| rocket-chip-pr-2036__VLpqKQW | unresolved | 298.2 | 1.8 | 0.2369 | 82.7 | 20 |
| rocket-chip-pr-2167__tPqbrMy | unresolved | 416.8 | 2.3 | 0.3217 | 83.9 | 22 |
| rocket-chip-pr-2213__fZxUH68 | unresolved | 1216.9 | 4.6 | 1.1478 | 92.3 | 56 |
| rocket-chip-pr-2368__PB77Z3o | unresolved | 4383.4 | 11.6 | 2.3134 | 96.9 | 120 |
| rocket-chip-pr-2543__sQki4yJ | unresolved | 2137.8 | 5.7 | 1.2277 | 94.8 | 82 |
| rocket-chip-pr-2621__PMCsAuJ | unresolved | 1284.6 | 7.7 | 1.8724 | 93.3 | 76 |
| rocket-chip-pr-2984__aYgMyQ6 | resolved | 995.5 | 4.3 | 0.6543 | 87.8 | 50 |
| rocket-chip-pr-2988__iDMhyE7 | resolved | 1093.3 | 6.0 | 0.8300 | 89.5 | 51 |
| rocket-chip-pr-2994__zw2HzbN | resolved | 2074.6 | 7.7 | 1.0664 | 95.4 | 82 |
| rocket-chip-pr-3004__HyWvnn4 | unresolved | 1131.6 | 4.6 | 0.7981 | 92.6 | 43 |
| rocket-chip-pr-3065__UXqSWyV | resolved | 1282.9 | 5.2 | 0.9504 | 91.8 | 56 |
| rocket-chip-pr-3256__N7JeJsi | unresolved | 853.8 | 3.4 | 0.7214 | 85.4 | 39 |
| rocket-chip-pr-3526__XfRsxr2 | unresolved | 402.2 | 2.6 | 0.5156 | 91.8 | 28 |
| rocket-chip-pr-3600__JY3w8TD | unresolved | 526.7 | 3.2 | 0.6945 | 91.1 | 33 |
| rocket-chip-pr-3624__kmpYNGz | unresolved | 6234.6 | 10.1 | 2.7817 | 96.5 | 108 |
| rocket-chip-pr-3651__7XKh9Fn | unresolved | 547.6 | 2.9 | 0.4451 | 91.9 | 35 |
| rocket-chip-pr-387__dm7KTXc | unresolved | 537.8 | 4.4 | 1.0332 | 89.1 | 39 |
| rocket-chip-pr-404__XKiEMq6 | resolved | 413.4 | 2.6 | 0.3321 | 91.5 | 33 |
| rocket-chip-pr-485__FUFcjzL | unresolved | 6527.3 | 20.3 | 5.3930 | 96.5 | 121 |
| rocket-chip-pr-542__QpY3CNg | resolved | 302.4 | 2.7 | 0.2715 | 89.7 | 28 |
| rocket-chip-pr-576__XsrfE2D | unresolved | 730.8 | 3.0 | 1.3186 | 92.3 | 44 |
| rocket-chip-pr-745__v7iQGSc | unresolved | 447.1 | 3.6 | 0.3059 | 92.3 | 39 |

