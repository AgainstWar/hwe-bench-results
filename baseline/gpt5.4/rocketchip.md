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
