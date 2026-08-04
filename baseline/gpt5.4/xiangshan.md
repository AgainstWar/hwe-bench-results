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
## File-Level Precision

- **Overall**: 81.1%

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  tasks: 54
  status: patch_submitted=54
  prompt_k: 1431.6
  completion_k: 4.2
  cache_hit_pct: 94.5
  tool_calls: 47.3
  cost_usd: 0.727621
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| XiangShan-pr-1242__LiATbEc | patch_submitted | 1032.7 | 3.1 | 0.6285 | 94.9 | 41 |
| XiangShan-pr-1323__uwKyVtn | patch_submitted | 1799.1 | 3.5 | 0.8218 | 94.0 | 49 |
| XiangShan-pr-1395__Hfq5oeh | patch_submitted | 1176.4 | 3.9 | 0.7157 | 94.8 | 56 |
| XiangShan-pr-1401__eA7kskA | patch_submitted | 2715.2 | 5.9 | 1.3220 | 95.3 | 65 |
| XiangShan-pr-1602__gNr2eMZ | patch_submitted | 1574.2 | 4.2 | 1.2027 | 91.2 | 49 |
| XiangShan-pr-1679__CEhUduX | patch_submitted | 540.5 | 2.0 | 0.3575 | 88.9 | 30 |
| XiangShan-pr-1694__JZjpdwQ | patch_submitted | 2354.9 | 4.5 | 1.0854 | 95.1 | 62 |
| XiangShan-pr-1793__2iwkJD3 | patch_submitted | 556.7 | 2.3 | 0.3659 | 88.8 | 29 |
| XiangShan-pr-1820__gM8LgmJ | patch_submitted | 629.6 | 2.5 | 0.4082 | 90.5 | 41 |
| XiangShan-pr-1907__7iYzwnu | patch_submitted | 400.7 | 1.8 | 0.2961 | 87.4 | 23 |
| XiangShan-pr-1931__8kkHwMG | patch_submitted | 988.1 | 2.7 | 0.5823 | 91.7 | 34 |
| XiangShan-pr-2095__C9LTdDK | patch_submitted | 309.2 | 1.5 | 0.2357 | 84.3 | 23 |
| XiangShan-pr-2195__Dp5jK6b | patch_submitted | 2318.9 | 5.2 | 1.0184 | 94.9 | 57 |
| XiangShan-pr-2246__YiG7skh | patch_submitted | 1330.4 | 4.2 | 0.6352 | 94.8 | 55 |
| XiangShan-pr-2351__GC7Pom6 | patch_submitted | 1985.4 | 5.7 | 1.0509 | 94.6 | 61 |
| XiangShan-pr-2483__WyjmBnL | patch_submitted | 253.6 | 2.4 | 0.2081 | 88.8 | 21 |
| XiangShan-pr-2513__rDP8ypX | patch_submitted | 1108.2 | 4.9 | 0.6493 | 92.9 | 43 |
| XiangShan-pr-2781__XQaQtCx | patch_submitted | 1499.0 | 4.7 | 0.6915 | 95.7 | 61 |
| XiangShan-pr-281__xiXJ3U4 | patch_submitted | 258.0 | 1.5 | 0.2298 | 82.8 | 23 |
| XiangShan-pr-2845__D9gxndN | patch_submitted | 367.9 | 2.0 | 0.2263 | 90.3 | 24 |
| XiangShan-pr-2997__jHJDkwy | patch_submitted | 1225.8 | 3.9 | 0.6627 | 94.9 | 58 |
| XiangShan-pr-3182__sQKRo8z | patch_submitted | 988.1 | 4.2 | 0.5713 | 93.3 | 49 |
| XiangShan-pr-3307__sP6BTCe | patch_submitted | 942.8 | 2.8 | 0.4860 | 93.9 | 41 |
| XiangShan-pr-3329__j35qhvP | patch_submitted | 596.9 | 2.7 | 0.3789 | 91.3 | 31 |
| XiangShan-pr-3555__ibZWzRm | patch_submitted | 701.7 | 2.0 | 0.3944 | 91.1 | 26 |
| XiangShan-pr-3636__TNaDH4a | patch_submitted | 888.5 | 3.6 | 0.5009 | 92.7 | 44 |
| XiangShan-pr-3717__ZXZMECB | patch_submitted | 3226.4 | 13.4 | 1.5300 | 96.8 | 79 |
| XiangShan-pr-3753__gNCwwB2 | patch_submitted | 6057.5 | 16.4 | 2.5756 | 97.0 | 90 |
| XiangShan-pr-3859__iGNzW93 | patch_submitted | 4352.4 | 8.0 | 1.7464 | 96.5 | 97 |
| XiangShan-pr-3867__Jf7CsBv | patch_submitted | 1040.9 | 3.2 | 0.6159 | 93.1 | 41 |
| XiangShan-pr-3907__b8Vdbcz | patch_submitted | 559.6 | 2.9 | 0.3456 | 91.8 | 42 |
| XiangShan-pr-3955__uEYYLdP | patch_submitted | 674.0 | 2.8 | 0.3941 | 92.3 | 34 |
| XiangShan-pr-39__BUrE2ZT | patch_submitted | 477.5 | 2.3 | 0.2988 | 91.5 | 24 |
| XiangShan-pr-4110__nZNBgze | patch_submitted | 918.9 | 3.3 | 0.4844 | 93.9 | 47 |
| XiangShan-pr-4166__ws9bPQD | patch_submitted | 2137.1 | 4.4 | 0.9265 | 95.6 | 56 |
| XiangShan-pr-4179__ZmsBiYA | patch_submitted | 2076.2 | 10.1 | 1.0240 | 95.4 | 64 |
| XiangShan-pr-4337__U9XJ3jT | patch_submitted | 978.4 | 3.3 | 0.6278 | 93.3 | 44 |
| XiangShan-pr-4426__3QrvAgF | patch_submitted | 974.9 | 2.6 | 0.5027 | 93.1 | 30 |
| XiangShan-pr-4442__iKVXr7b | patch_submitted | 936.3 | 2.7 | 0.4865 | 94.2 | 30 |
| XiangShan-pr-4533__tiXCu3X | patch_submitted | 1753.1 | 5.1 | 0.8063 | 95.4 | 55 |
| XiangShan-pr-4750__4gcy4w9 | patch_submitted | 2190.7 | 5.4 | 1.0859 | 95.7 | 54 |
| XiangShan-pr-4764__4xnosxy | patch_submitted | 643.7 | 3.0 | 0.4212 | 90.8 | 41 |
| XiangShan-pr-4943__5NekvXc | patch_submitted | 3675.6 | 8.3 | 1.5628 | 95.6 | 122 |
| XiangShan-pr-4959__ACyNJDc | patch_submitted | 667.9 | 2.6 | 0.4586 | 91.4 | 30 |
| XiangShan-pr-4968__KYxhQsq | patch_submitted | 1689.8 | 4.9 | 0.8348 | 94.6 | 62 |
| XiangShan-pr-5080__Mv8rM4L | patch_submitted | 754.4 | 2.6 | 0.4352 | 92.7 | 35 |
| XiangShan-pr-5182__AU6P9Dx | patch_submitted | 835.0 | 2.7 | 0.4738 | 92.2 | 32 |
| XiangShan-pr-5189__MmYj3UZ | patch_submitted | 1584.2 | 3.6 | 0.7587 | 94.5 | 47 |
| XiangShan-pr-5496__zuf4n68 | patch_submitted | 2727.3 | 4.4 | 1.2241 | 94.4 | 59 |
| XiangShan-pr-5593__McG5Lit | patch_submitted | 1027.6 | 3.0 | 0.5219 | 94.1 | 38 |

