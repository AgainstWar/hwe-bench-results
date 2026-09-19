# XiangShan Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: 40
  total: 54
  resolved_rate: 74.1%
  infra_errors: 0

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: 27
  total: 54
  resolved_rate: 50.0%
  file_level_precision: 81.1%
  infra_errors: 0
```

## Task 级 File-Level Precision

| PR | Precision | 匹配文件/修改文件 |
|----|:---------:|:-----------------:|
| pr-39 | 100.0% | 1/1 |
| pr-281 | 100.0% | 1/1 |
| pr-655 | 100.0% | 1/1 |
| pr-739 | 50.0% | 1/2 |
| pr-1242 | 50.0% | 1/2 |
| pr-1323 | 100.0% | 1/1 |
| pr-1395 | 100.0% | 1/1 |
| pr-1401 | 75.0% | 3/4 |
| pr-1602 | 100.0% | 1/1 |
| pr-1679 | 100.0% | 1/1 |
| pr-1694 | 0.0% | 0/1 |
| pr-1793 | 100.0% | 1/1 |
| pr-1820 | 100.0% | 1/1 |
| pr-1907 | 100.0% | 1/1 |
| pr-1931 | 100.0% | 1/1 |
| pr-2095 | 100.0% | 1/1 |
| pr-2195 | 100.0% | 1/1 |
| pr-2246 | 100.0% | 1/1 |
| pr-2351 | 100.0% | 2/2 |
| pr-2483 | 100.0% | 1/1 |
| pr-2513 | 50.0% | 1/2 |
| pr-2781 | 100.0% | 1/1 |
| pr-2845 | 100.0% | 1/1 |
| pr-2997 | 100.0% | 1/1 |
| pr-3182 | 100.0% | 1/1 |
| pr-3307 | 100.0% | 1/1 |
| pr-3329 | 100.0% | 1/1 |
| pr-3555 | 100.0% | 1/1 |
| pr-3636 | 66.7% | 2/3 |
| pr-3717 | 50.0% | 1/2 |
| pr-3753 | 50.0% | 1/2 |
| pr-3859 | 62.5% | 5/8 |
| pr-3867 | 100.0% | 1/1 |
| pr-3907 | 100.0% | 1/1 |
| pr-3955 | 100.0% | 1/1 |
| pr-4110 | 50.0% | 1/2 |
| pr-4166 | 66.7% | 2/3 |
| pr-4179 | 66.7% | 2/3 |
| pr-4337 | 100.0% | 1/1 |
| pr-4426 | 100.0% | 1/1 |
| pr-4442 | 100.0% | 1/1 |
| pr-4533 | 50.0% | 1/2 |
| pr-4750 | 100.0% | 2/2 |
| pr-4764 | 0.0% | 0/2 |
| pr-4943 | 100.0% | 7/7 |
| pr-4959 | 100.0% | 1/1 |
| pr-4968 | 100.0% | 5/5 |
| pr-5080 | 100.0% | 1/1 |
| pr-5182 | 100.0% | 1/1 |
| pr-5189 | 100.0% | 1/1 |
| pr-5496 | 100.0% | 1/1 |
| pr-5593 | 100.0% | 1/1 |
| pr-5687 | 100.0% | 1/1 |
| pr-5700 | 100.0% | 1/1 |

## File-Level Precision

- **Overall**: 81.1%
- **Average (per-task)**: 86.8%

## 未解决 Case

```json
[
  {
    "pr": 281,
    "test": "freelist_availability",
    "type": "logic",
    "desc": "Dispatch1 ready/valid 处理优化不当, 队列部分满时握手延迟"
  },
  {
    "pr": 655,
    "test": "loadpipe_data_port_conflict",
    "type": "logic",
    "desc": "DCache 写优先级相对于读错误, 仲裁逻辑需重新排序"
  },
  {
    "pr": 1242,
    "test": "statusarray_store_set_wakeup",
    "type": "logic",
    "desc": "Memory/MDP 使用 sqIdx 而非 robIdx, 跟踪错误条目"
  },
  {
    "pr": 1323,
    "test": "csr_mask_behavior",
    "type": "spec",
    "desc": "CSR 写入 satp.ppn 和 xstatus.xs 需要掩码/只读处理"
  },
  {
    "pr": 1395,
    "test": "memblock_atomic_exception_hold",
    "type": "logic",
    "desc": "Atomic exception valid 在重定向后未正确恢复"
  },
  {
    "pr": 1401,
    "test": "loadunit_refill_replay",
    "type": "timing_sync",
    "desc": "加载重填延迟过长(LQ 标志更新路径过于保守)"
  },
  {
    "pr": 1602,
    "test": "wb2ctrl_load_writeback_delay",
    "type": "timing_sync",
    "desc": "LSU/L1 时序修复以满足流水线和内存时序约束"
  },
  {
    "pr": 1694,
    "test": "loadunit_replay_from_fetch",
    "type": "logic",
    "desc": "从取指重放未正确更新加载队列"
  },
  {
    "pr": 1907,
    "test": "ctrlblock_redirect_vset",
    "type": "logic",
    "desc": "向量控制块 vset 路径指令/控制处理错误"
  },
  {
    "pr": 1931,
    "test": "ftq_skip_empty_redirected_entry",
    "type": "logic",
    "desc": "FTQ 行为回归, 需要回退以恢复正确的取指跟踪"
  },
  {
    "pr": 2195,
    "test": "memblock_io_compile",
    "type": "timing_sync",
    "desc": "MemBlock IO 优化以保持内存块接口正常"
  },
  {
    "pr": 2246,
    "test": "fpga_platform_private_l2_db_gating",
    "type": "config_integ",
    "desc": "L2DB 在 FPGAPlatform 下启用/配置错误"
  },
  {
    "pr": 2483,
    "test": "hperf_counter_selection_logic",
    "type": "logic",
    "desc": "HPM 选择逻辑错误(含笔误), 性能计数器选择错误"
  },
  {
    "pr": 2513,
    "test": "fusiondecoder_same_src_guard",
    "type": "logic",
    "desc": "FusionDecoder 在 inst2.rs1 == rs2 时错误融合指令"
  },
  {
    "pr": 2997,
    "test": "frontend_fallthrough_address_regression",
    "type": "logic",
    "desc": "低功耗 FTB 处理中 fallThroughAddr 计算错误"
  },
  {
    "pr": 3636,
    "test": "s3_fallthrough_target",
    "type": "logic",
    "desc": "BPU S3 目标选择在 fallThroughErr 断言时错误"
  },
  {
    "pr": 3717,
    "test": "csrpermit_vstimecmp_exii",
    "type": "spec",
    "desc": "stimecmp/vstimecmp 读写权限/条件判断错误"
  },
  {
    "pr": 3753,
    "test": "interrupt_filter_aia_topi_priority_matrix",
    "type": "spec",
    "desc": "AIA 中断过滤优先级/ID 处理错误"
  },
  {
    "pr": 3859,
    "test": "rvc_fs_off_illegal",
    "type": "spec",
    "desc": "压缩浮点指令在 fs 关闭时未标记为非法"
  },
  {
    "pr": 3867,
    "test": "dispatch_single_step_redirect_reuse",
    "type": "logic",
    "desc": "单步异常处理可能错误提交下一条指令"
  },
  {
    "pr": 3907,
    "test": "dret_event_virtual_mode",
    "type": "spec",
    "desc": "dret 更新特权状态错误(虚拟化相关位)"
  },
  {
    "pr": 4110,
    "test": "dcache_cmo_source_capacity",
    "type": "sw_hw_config",
    "desc": "DCache TileLink 客户端参数配置错误"
  },
  {
    "pr": 4179,
    "test": "interrupt_filter_priority_regression",
    "type": "spec",
    "desc": "外部中断优先级比较在优先级 > 255 时错误"
  },
  {
    "pr": 4337,
    "test": "dcache_lrsc_block_duration",
    "type": "logic",
    "desc": "LR 阻塞使用了错误的 lrsc_count 条件"
  },
  {
    "pr": 4943,
    "test": "frontend_tl_user_fields_contract",
    "type": "sw_hw_config",
    "desc": "TileLink 用户字段接线错误"
  },
  {
    "pr": 4968,
    "test": "tage_reset_compatibility",
    "type": "timing_sync",
    "desc": "BPU SRAM 在复位完成前被读取, 产生 x 态"
  },
  {
    "pr": 5496,
    "test": "kunminghuv2minimalconfig_verilog",
    "type": "sw_hw_config",
    "desc": "MinimalConfig 缺少 fullAddressBits"
  }
]
```

## Bug 类型分布

```yaml
  config_integ: 1
  logic: 13
  spec: 6
  sw_hw_config: 3
  timing_sync: 4
```

## Token 统计（token_report.py）

### 平均指标

```yaml
token_statistics:
  prompt_k: 1431.6
  completion_k: 4.2
  cache_hit_pct: 94.5
  tool_calls: 47.3
  mcp_calls: 0.0
  other_skill_calls: 0.0
  ordinary_calls: 47.3
  cost_usd: 0.727621
  own_price_cost_usd: 1.831318
  tasks: 54
  resolved: 27
  unresolved: 27
  error: 0
  no_patch: 0
```

### 逐 Task 明细

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls | MCP | Other Skill | Ordinary |
|-------|--------|-----------|---------|---------|--------|-------|------|-------------|----------|
| XiangShan-pr-1242 | unresolved | 1032.7 | 3.1 | 0.6285 | 94.9 | 41 | 0 | 0 | 41 |
| XiangShan-pr-1323 | unresolved | 1799.1 | 3.5 | 0.8218 | 94.0 | 49 | 0 | 0 | 49 |
| XiangShan-pr-1395 | unresolved | 1176.4 | 3.9 | 0.7157 | 94.8 | 56 | 0 | 0 | 56 |
| XiangShan-pr-1401 | unresolved | 2715.2 | 5.9 | 1.3220 | 95.3 | 65 | 0 | 0 | 65 |
| XiangShan-pr-1602 | unresolved | 1574.2 | 4.2 | 1.2027 | 91.2 | 49 | 0 | 0 | 49 |
| XiangShan-pr-1679 | resolved | 540.5 | 2.0 | 0.3575 | 88.9 | 30 | 0 | 0 | 30 |
| XiangShan-pr-1694 | unresolved | 2354.9 | 4.5 | 1.0854 | 95.1 | 62 | 0 | 0 | 62 |
| XiangShan-pr-1793 | resolved | 556.7 | 2.3 | 0.3659 | 88.8 | 29 | 0 | 0 | 29 |
| XiangShan-pr-1820 | resolved | 629.6 | 2.5 | 0.4082 | 90.5 | 41 | 0 | 0 | 41 |
| XiangShan-pr-1907 | unresolved | 400.7 | 1.8 | 0.2961 | 87.4 | 23 | 0 | 0 | 23 |
| XiangShan-pr-1931 | unresolved | 988.1 | 2.7 | 0.5823 | 91.7 | 34 | 0 | 0 | 34 |
| XiangShan-pr-2095 | resolved | 309.2 | 1.5 | 0.2357 | 84.3 | 23 | 0 | 0 | 23 |
| XiangShan-pr-2195 | unresolved | 2318.9 | 5.2 | 1.0184 | 94.9 | 57 | 0 | 0 | 57 |
| XiangShan-pr-2246 | unresolved | 1330.4 | 4.2 | 0.6352 | 94.8 | 55 | 0 | 0 | 55 |
| XiangShan-pr-2351 | resolved | 1985.4 | 5.7 | 1.0509 | 94.6 | 61 | 0 | 0 | 61 |
| XiangShan-pr-2483 | unresolved | 253.6 | 2.4 | 0.2081 | 88.8 | 21 | 0 | 0 | 21 |
| XiangShan-pr-2513 | unresolved | 1108.2 | 4.9 | 0.6493 | 92.9 | 43 | 0 | 0 | 43 |
| XiangShan-pr-2781 | resolved | 1499.0 | 4.7 | 0.6915 | 95.7 | 61 | 0 | 0 | 61 |
| XiangShan-pr-281 | unresolved | 258.0 | 1.5 | 0.2298 | 82.8 | 23 | 0 | 0 | 23 |
| XiangShan-pr-2845 | resolved | 367.9 | 2.0 | 0.2263 | 90.3 | 24 | 0 | 0 | 24 |
| XiangShan-pr-2997 | unresolved | 1225.8 | 3.9 | 0.6627 | 94.9 | 58 | 0 | 0 | 58 |
| XiangShan-pr-3182 | resolved | 988.1 | 4.2 | 0.5713 | 93.3 | 49 | 0 | 0 | 49 |
| XiangShan-pr-3307 | resolved | 942.8 | 2.8 | 0.4860 | 93.9 | 41 | 0 | 0 | 41 |
| XiangShan-pr-3329 | resolved | 596.9 | 2.7 | 0.3789 | 91.3 | 31 | 0 | 0 | 31 |
| XiangShan-pr-3555 | resolved | 701.7 | 2.0 | 0.3944 | 91.1 | 26 | 0 | 0 | 26 |
| XiangShan-pr-3636 | unresolved | 888.5 | 3.6 | 0.5009 | 92.7 | 44 | 0 | 0 | 44 |
| XiangShan-pr-3717 | unresolved | 3226.4 | 13.4 | 1.5300 | 96.8 | 79 | 0 | 0 | 79 |
| XiangShan-pr-3753 | unresolved | 6057.5 | 16.4 | 2.5756 | 97.0 | 90 | 0 | 0 | 90 |
| XiangShan-pr-3859 | unresolved | 4352.4 | 8.0 | 1.7464 | 96.5 | 97 | 0 | 0 | 97 |
| XiangShan-pr-3867 | unresolved | 1040.9 | 3.2 | 0.6159 | 93.1 | 41 | 0 | 0 | 41 |
| XiangShan-pr-39 | resolved | 477.5 | 2.3 | 0.2988 | 91.5 | 24 | 0 | 0 | 24 |
| XiangShan-pr-3907 | unresolved | 559.6 | 2.9 | 0.3456 | 91.8 | 42 | 0 | 0 | 42 |
| XiangShan-pr-3955 | resolved | 674.0 | 2.8 | 0.3941 | 92.3 | 34 | 0 | 0 | 34 |
| XiangShan-pr-4110 | unresolved | 918.9 | 3.3 | 0.4844 | 93.9 | 47 | 0 | 0 | 47 |
| XiangShan-pr-4166 | resolved | 2137.1 | 4.4 | 0.9265 | 95.6 | 56 | 0 | 0 | 56 |
| XiangShan-pr-4179 | unresolved | 2076.2 | 10.1 | 1.0240 | 95.4 | 64 | 0 | 0 | 64 |
| XiangShan-pr-4337 | unresolved | 978.4 | 3.3 | 0.6278 | 93.3 | 44 | 0 | 0 | 44 |
| XiangShan-pr-4426 | resolved | 974.9 | 2.6 | 0.5027 | 93.1 | 30 | 0 | 0 | 30 |
| XiangShan-pr-4442 | resolved | 936.3 | 2.7 | 0.4865 | 94.2 | 30 | 0 | 0 | 30 |
| XiangShan-pr-4533 | resolved | 1753.1 | 5.1 | 0.8063 | 95.4 | 55 | 0 | 0 | 55 |
| XiangShan-pr-4750 | resolved | 2190.7 | 5.4 | 1.0859 | 95.7 | 54 | 0 | 0 | 54 |
| XiangShan-pr-4764 | resolved | 643.7 | 3.0 | 0.4212 | 90.8 | 41 | 0 | 0 | 41 |
| XiangShan-pr-4943 | unresolved | 3675.6 | 8.3 | 1.5628 | 95.6 | 122 | 0 | 0 | 122 |
| XiangShan-pr-4959 | resolved | 667.9 | 2.6 | 0.4586 | 91.4 | 30 | 0 | 0 | 30 |
| XiangShan-pr-4968 | unresolved | 1689.8 | 4.9 | 0.8348 | 94.6 | 62 | 0 | 0 | 62 |
| XiangShan-pr-5080 | resolved | 754.4 | 2.6 | 0.4352 | 92.7 | 35 | 0 | 0 | 35 |
| XiangShan-pr-5182 | resolved | 835.0 | 2.7 | 0.4738 | 92.2 | 32 | 0 | 0 | 32 |
| XiangShan-pr-5189 | resolved | 1584.2 | 3.6 | 0.7587 | 94.5 | 47 | 0 | 0 | 47 |
| XiangShan-pr-5496 | unresolved | 2727.3 | 4.4 | 1.2241 | 94.4 | 59 | 0 | 0 | 59 |
| XiangShan-pr-5593 | resolved | 1027.6 | 3.0 | 0.5219 | 94.1 | 38 | 0 | 0 | 38 |
| XiangShan-pr-5687 | resolved | 1667.6 | 4.5 | 0.8947 | 94.3 | 52 | 0 | 0 | 52 |
| XiangShan-pr-5700 | resolved | 1377.5 | 2.9 | 0.6917 | 93.6 | 36 | 0 | 0 | 36 |
| XiangShan-pr-655 | unresolved | 1856.6 | 4.2 | 0.8933 | 95.3 | 55 | 0 | 0 | 55 |
| XiangShan-pr-739 | resolved | 1904.8 | 5.4 | 0.9450 | 95.2 | 64 | 0 | 0 | 64 |
