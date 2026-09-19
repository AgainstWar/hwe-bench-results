# RocketChip Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 23
  total: 32
  resolved_rate: 71.9%
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 8
  total: 32
  resolved_rate: 25.0%
  file_level_precision: 69.8%
  infra_errors: 0
```

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-177 | 0.0% | 0/1 |
| pr-387 | 100.0% | 1/1 |
| pr-404 | 100.0% | 1/1 |
| pr-485 | 80.0% | 8/10 |
| pr-542 | 100.0% | 1/1 |
| pr-745 | 100.0% | 1/1 |
| pr-1069 | 100.0% | 2/2 |
| pr-1093 | 100.0% | 1/1 |
| pr-1176 | 100.0% | 1/1 |
| pr-1330 | 100.0% | 1/1 |
| pr-1493 | 100.0% | 1/1 |
| pr-1656 | 100.0% | 4/4 |
| pr-1761 | 100.0% | 1/1 |
| pr-1878 | 100.0% | 1/1 |
| pr-2018 | 100.0% | 1/1 |
| pr-2036 | 100.0% | 1/1 |
| pr-2167 | 100.0% | 1/1 |
| pr-2213 | 0.0% | 0/1 |
| pr-2368 | 100.0% | 1/1 |
| pr-2543 | 100.0% | 1/1 |
| pr-2621 | 100.0% | 3/3 |
| pr-2984 | 100.0% | 1/1 |
| pr-2988 | 50.0% | 1/2 |
| pr-2994 | 6.7% | 1/15 |
| pr-3004 | 100.0% | 2/2 |
| pr-3065 | 100.0% | 1/1 |
| pr-3256 | 100.0% | 1/1 |
| pr-3526 | 100.0% | 1/1 |
| pr-3624 | 100.0% | 3/3 |
| pr-3651 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 69.8%
- **Average (per-task)**: 87.9%

## 未解决 Case

```json
[
  {
    "pr": 177,
    "test": "lrsc_mshr_secondary_dirty",
    "type": "logic",
    "desc": "LR/SC 一致性状态更新错误, store-conditional 成功标志丢失"
  },
  {
    "pr": 387,
    "test": "async_queue_half_reset",
    "type": "timing_sync",
    "desc": "异步跨时钟域复位未完全清除 FIFO 状态, ready/valid 不安全"
  },
  {
    "pr": 485,
    "test": "diplomatic_ahb_elaboration",
    "type": "interface",
    "desc": "AHB 适配器在 diplomacy 桥接中导致错误的总线接口行为"
  },
  {
    "pr": 576,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 745,
    "test": "rocc_example_elaboration",
    "type": "config_integ",
    "desc": "Tile 交叉开关集成问题, 需要仲裁减少引脚并修复多 RoCC 配置"
  },
  {
    "pr": 1069,
    "test": "csr-decodewidth-multiport",
    "type": "logic",
    "desc": "CSR 非法指令解码只处理单条指令, 多发射解码检查错误"
  },
  {
    "pr": 1093,
    "test": "bus_error_unit_rv32_elaboration",
    "type": "sw_hw_interact",
    "desc": "总线/ECC 错误路径缺少本地中断生成, 故障未上报软件"
  },
  {
    "pr": 1176,
    "test": "tl_mmio_port_internal_wiring",
    "type": "interface",
    "desc": "TL MMIO 端口在 diplomacy 连接中接线错误"
  },
  {
    "pr": 1493,
    "test": "async_pbus_bootrom_access",
    "type": "config_integ",
    "desc": "外设时钟域拆分需要将控制外设移到独立时钟/复位集成路径"
  },
  {
    "pr": 1761,
    "test": "csr-tvec-uninitialized-alignment",
    "type": "logic",
    "desc": "tvec 位清零在错误阶段执行, 首次写入前残留过期值"
  },
  {
    "pr": 1878,
    "test": "misa_x_bit",
    "type": "spec",
    "desc": "misa.X 未为 CEASE 指令设置, 违反 ISA 特性报告规范"
  },
  {
    "pr": 2018,
    "test": "unknown",
    "type": "interface",
    "desc": "TLToAHB 用户位未在事务 FSM 中保留, 地址和元数据不同步"
  },
  {
    "pr": 2036,
    "test": "mret_not_misdetected_as_dret",
    "type": "logic",
    "desc": "DRET 有效性检查了错误流水线阶段的 CSR 地址"
  },
  {
    "pr": 2167,
    "test": "jtag_async_reset",
    "type": "timing_sync",
    "desc": "JTAG TDO 需要异步复位行为以匹配 jtag_reset 信号"
  },
  {
    "pr": 2213,
    "test": "debug_apb_gap_behavior",
    "type": "interface",
    "desc": "Debug APB 未定义地址访问别名到有效寄存器而非返回错误"
  },
  {
    "pr": 2368,
    "test": "asyncvalidsync-mixed-reset-elaboration",
    "type": "config_integ",
    "desc": "AsyncValidSync 模块样式集成问题, 功能无变化"
  },
  {
    "pr": 2543,
    "test": "heterogeneous_hartid_elaboration",
    "type": "logic",
    "desc": "HartID/复位向量宽度计算使用了错误的 Chisel 兼容模式宽度逻辑"
  },
  {
    "pr": 2621,
    "test": "unknown",
    "type": "config_integ",
    "desc": "L1 TLB 可配置 set/way 的 sectored-LRU 宽度错误"
  },
  {
    "pr": 3004,
    "test": "frontend_progress_quiesce",
    "type": "timing_sync",
    "desc": "Hypervisor 推测 ITLB 重填冲击 DCache, 阻塞旧加载的进度"
  },
  {
    "pr": 3256,
    "test": "aes64ks1i_decode",
    "type": "logic",
    "desc": "AES64KS1I 解码将操作数当作 rs2 而非立即数"
  },
  {
    "pr": 3526,
    "test": "unknown",
    "type": "logic",
    "desc": "S2 PTE 缓存命中逻辑更新了错误的 r_pte 条件"
  },
  {
    "pr": 3600,
    "test": "N/A",
    "type": "unknown",
    "desc": "N/A"
  },
  {
    "pr": 3624,
    "test": "hypervisor_tinst_warl",
    "type": "spec",
    "desc": "Hypervisor 客户页故障处理未按要求驱动 mtinst/htinst"
  },
  {
    "pr": 3651,
    "test": "unknown",
    "type": "spec",
    "desc": "PTW GPA 位验证基于 PTE 有效性而非叶子节点性, 错误分类非叶子条目"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 4
  interface: 4
  logic: 7
  spec: 3
  sw_hw_interact: 1
  timing_sync: 3
  unknown: 2
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1310.0
  completion_k: 5.1
  cache_hit_pct: 93.7
  tool_calls: 51.0
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 51.0
  cost_usd: 0.995443
  own_price_cost_usd: 1.688024
  tasks: 32
  resolved: 8
  unresolved: 24
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| rocket-chip-pr-1069 | unresolved | 358.9 | 4.0 | 0.3206 | 87.2 | 31 | 0 | 0 | 31 |
| rocket-chip-pr-1093 | unresolved | 2835.8 | 9.2 | 2.1777 | 94.9 | 88 | 0 | 0 | 88 |
| rocket-chip-pr-1176 | unresolved | 372.8 | 3.3 | 0.2904 | 87.1 | 43 | 0 | 0 | 43 |
| rocket-chip-pr-1330 | resolved | 676.5 | 5.0 | 0.6211 | 92.6 | 58 | 0 | 0 | 58 |
| rocket-chip-pr-1493 | unresolved | 891.4 | 3.5 | 0.5848 | 91.0 | 45 | 0 | 0 | 45 |
| rocket-chip-pr-1656 | resolved | 686.8 | 4.3 | 0.9324 | 90.4 | 40 | 0 | 0 | 40 |
| rocket-chip-pr-1761 | unresolved | 386.3 | 2.4 | 0.3794 | 86.7 | 21 | 0 | 0 | 21 |
| rocket-chip-pr-177 | unresolved | 507.7 | 3.5 | 0.3539 | 90.9 | 31 | 0 | 0 | 31 |
| rocket-chip-pr-1878 | unresolved | 821.8 | 3.5 | 0.5039 | 92.1 | 45 | 0 | 0 | 45 |
| rocket-chip-pr-2018 | unresolved | 542.6 | 2.6 | 0.4581 | 86.9 | 25 | 0 | 0 | 25 |
| rocket-chip-pr-2036 | unresolved | 298.2 | 1.8 | 0.2369 | 82.7 | 20 | 0 | 0 | 20 |
| rocket-chip-pr-2167 | unresolved | 416.8 | 2.3 | 0.3217 | 83.9 | 22 | 0 | 0 | 22 |
| rocket-chip-pr-2213 | unresolved | 1216.9 | 4.6 | 1.1478 | 92.3 | 56 | 0 | 0 | 56 |
| rocket-chip-pr-2368 | unresolved | 4383.4 | 11.6 | 2.3134 | 96.9 | 120 | 0 | 0 | 120 |
| rocket-chip-pr-2543 | unresolved | 2137.8 | 5.7 | 1.2277 | 94.8 | 82 | 0 | 0 | 82 |
| rocket-chip-pr-2621 | unresolved | 1284.6 | 7.7 | 1.8724 | 93.3 | 76 | 0 | 0 | 76 |
| rocket-chip-pr-2984 | resolved | 995.5 | 4.3 | 0.6543 | 87.8 | 50 | 0 | 0 | 50 |
| rocket-chip-pr-2988 | resolved | 1093.3 | 6.0 | 0.8300 | 89.5 | 51 | 0 | 0 | 51 |
| rocket-chip-pr-2994 | resolved | 2074.6 | 7.7 | 1.0664 | 95.4 | 82 | 0 | 0 | 82 |
| rocket-chip-pr-3004 | unresolved | 1131.6 | 4.6 | 0.7981 | 92.6 | 43 | 0 | 0 | 43 |
| rocket-chip-pr-3065 | resolved | 1282.9 | 5.2 | 0.9504 | 91.8 | 56 | 0 | 0 | 56 |
| rocket-chip-pr-3256 | unresolved | 853.8 | 3.4 | 0.7214 | 85.4 | 39 | 0 | 0 | 39 |
| rocket-chip-pr-3526 | unresolved | 402.2 | 2.6 | 0.5156 | 91.8 | 28 | 0 | 0 | 28 |
| rocket-chip-pr-3600 | unresolved | 526.7 | 3.2 | 0.6945 | 91.1 | 33 | 0 | 0 | 33 |
| rocket-chip-pr-3624 | unresolved | 6234.6 | 10.1 | 2.7817 | 96.5 | 108 | 0 | 0 | 108 |
| rocket-chip-pr-3651 | unresolved | 547.6 | 2.9 | 0.4451 | 91.9 | 35 | 0 | 0 | 35 |
| rocket-chip-pr-387 | unresolved | 537.8 | 4.4 | 1.0332 | 89.1 | 39 | 0 | 0 | 39 |
| rocket-chip-pr-404 | resolved | 413.4 | 2.6 | 0.3321 | 91.5 | 33 | 0 | 0 | 33 |
| rocket-chip-pr-485 | unresolved | 6527.3 | 20.3 | 5.3930 | 96.5 | 121 | 0 | 0 | 121 |
| rocket-chip-pr-542 | resolved | 302.4 | 2.7 | 0.2715 | 89.7 | 28 | 0 | 0 | 28 |
| rocket-chip-pr-576 | unresolved | 730.8 | 3.0 | 1.3186 | 92.3 | 44 | 0 | 0 | 44 |
| rocket-chip-pr-745 | unresolved | 447.1 | 3.6 | 0.3059 | 92.3 | 39 | 0 | 0 | 39 |
