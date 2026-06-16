# XiangShan Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 40
  total: 54
  pct: 74
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 27
  total: 54
  pct: 50
  infra_errors: 0
```

## 未解决 Case

```json
[
  {"pr": 281,  "test": "freelist_availability",                        "type": "logic",         "desc": "Dispatch1 ready/valid 处理优化不当, 队列部分满时握手延迟"},
  {"pr": 655,  "test": "loadpipe_data_port_conflict",                   "type": "logic",         "desc": "DCache 写优先级相对于读错误, 仲裁逻辑需重新排序"},
  {"pr": 1242, "test": "statusarray_store_set_wakeup",                  "type": "logic",         "desc": "Memory/MDP 使用 sqIdx 而非 robIdx, 跟踪错误条目"},
  {"pr": 1323, "test": "csr_mask_behavior",                            "type": "spec",          "desc": "CSR 写入 satp.ppn 和 xstatus.xs 需要掩码/只读处理"},
  {"pr": 1395, "test": "memblock_atomic_exception_hold",               "type": "logic",         "desc": "Atomic exception valid 在重定向后未正确恢复"},
  {"pr": 1401, "test": "loadunit_refill_replay",                       "type": "timing_sync",   "desc": "加载重填延迟过长(LQ 标志更新路径过于保守)"},
  {"pr": 1602, "test": "wb2ctrl_load_writeback_delay",                 "type": "timing_sync",   "desc": "LSU/L1 时序修复以满足流水线和内存时序约束"},
  {"pr": 1694, "test": "loadunit_replay_from_fetch",                   "type": "logic",         "desc": "从取指重放未正确更新加载队列"},
  {"pr": 1907, "test": "ctrlblock_redirect_vset",                      "type": "logic",         "desc": "向量控制块 vset 路径指令/控制处理错误"},
  {"pr": 1931, "test": "ftq_skip_empty_redirected_entry",              "type": "logic",         "desc": "FTQ 行为回归, 需要回退以恢复正确的取指跟踪"},
  {"pr": 2195, "test": "memblock_io_compile",                          "type": "timing_sync",   "desc": "MemBlock IO 优化以保持内存块接口正常"},
  {"pr": 2246, "test": "fpga_platform_private_l2_db_gating",           "type": "config_integ",  "desc": "L2DB 在 FPGAPlatform 下启用/配置错误"},
  {"pr": 2483, "test": "hperf_counter_selection_logic",                "type": "logic",         "desc": "HPM 选择逻辑错误(含笔误), 性能计数器选择错误"},
  {"pr": 2513, "test": "fusiondecoder_same_src_guard",                 "type": "logic",         "desc": "FusionDecoder 在 inst2.rs1 == rs2 时错误融合指令"},
  {"pr": 2997, "test": "frontend_fallthrough_address_regression",      "type": "logic",         "desc": "低功耗 FTB 处理中 fallThroughAddr 计算错误"},
  {"pr": 3636, "test": "s3_fallthrough_target",                        "type": "logic",         "desc": "BPU S3 目标选择在 fallThroughErr 断言时错误"},
  {"pr": 3717, "test": "csrpermit_vstimecmp_exii",                    "type": "spec",          "desc": "stimecmp/vstimecmp 读写权限/条件判断错误"},
  {"pr": 3753, "test": "interrupt_filter_aia_topi_priority_matrix",    "type": "spec",          "desc": "AIA 中断过滤优先级/ID 处理错误"},
  {"pr": 3859, "test": "rvc_fs_off_illegal",                          "type": "spec",          "desc": "压缩浮点指令在 fs 关闭时未标记为非法"},
  {"pr": 3867, "test": "dispatch_single_step_redirect_reuse",          "type": "logic",         "desc": "单步异常处理可能错误提交下一条指令"},
  {"pr": 3907, "test": "dret_event_virtual_mode",                      "type": "spec",          "desc": "dret 更新特权状态错误(虚拟化相关位)"},
  {"pr": 4110, "test": "dcache_cmo_source_capacity",                   "type": "sw_hw_config",  "desc": "DCache TileLink 客户端参数配置错误"},
  {"pr": 4179, "test": "interrupt_filter_priority_regression",         "type": "spec",          "desc": "外部中断优先级比较在优先级 > 255 时错误"},
  {"pr": 4337, "test": "dcache_lrsc_block_duration",                   "type": "logic",         "desc": "LR 阻塞使用了错误的 lrsc_count 条件"},
  {"pr": 4943, "test": "frontend_tl_user_fields_contract",             "type": "sw_hw_config",  "desc": "TileLink 用户字段接线错误"},
  {"pr": 4968, "test": "tage_reset_compatibility",                     "type": "timing_sync",   "desc": "BPU SRAM 在复位完成前被读取, 产生 x 态"},
  {"pr": 5496, "test": "kunminghuv2minimalconfig_verilog",             "type": "sw_hw_config",  "desc": "MinimalConfig 缺少 fullAddressBits"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  logic: 14
  spec: 6
  timing_sync: 3
  sw_hw_config: 3
  config_integ: 1
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: 23
    prs: [39, 739, 1679, 1793, 1820, 2095, 2351, 2781, 2845, 3182, 3307, 3329, 3555, 3955, 4166, 4442, 4533, 4959, 5080, 5182, 5189, 5593, 5687]
  official_only:
    count: 17
    prs: [281, 655, 1323, 1694, 1907, 1931, 2195, 2246, 2483, 2513, 2997, 3859, 3867, 3907, 4337, 4968, 5496]
  opencode_only:
    count: 4
    prs: [4426, 4750, 4764, 5700]
  neither:
    count: 10
    prs: [1242, 1395, 1401, 1602, 3636, 3717, 3753, 4110, 4179, 4943]
```

## 结论

所有 27 个失败均为 patch 质量问题，基础设施错误 = 0。主要 bug 类型为 logic（52%）和 Spec（22%）。官方能解而 OpenCode 不能解的 17 个 case 中，logic 类占多数，反映了当前模型在 Chisel 硬件逻辑修复上的能力退化。Verilog 项目（Ibex、CVA6、Caliptra）不受此影响，OpenCode 达到 91-100% 的修复率。
