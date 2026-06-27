# Xiangshan Analysis (DeepSeek V4 Flash)

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: DeepSeek V3.2
  resolved: 25
  total: 54
  pct: 46
  infra_errors: 0

opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 12
  total: 51
  pct: 24
  infra_errors: 0
```

## 未解决 Case

```json[
  {
    "pr": 1242,
    "test": "statusarray_store_set_wakeup",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1323,
    "test": "csr_mask_behavior",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 1395,
    "test": "memblock_atomic_exception_hold",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1401,
    "test": "loadunit_refill_replay",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1602,
    "test": "wb2ctrl_load_writeback_delay",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1679,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1694,
    "test": "loadunit_replay_from_fetch",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1793,
    "test": "need_check",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 1820,
    "test": "need_check",
    "type": "sw_hw_config",
    "desc": "N/A"
  },
  {
    "pr": 1907,
    "test": "ctrlblock_redirect_vset",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2095,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2195,
    "test": "memblock_io_compile",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 2246,
    "test": "fpga_platform_private_l2_db_gating",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2351,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 2513,
    "test": "fusiondecoder_same_src_guard",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2781,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 2997,
    "test": "frontend_fallthrough_address_regression",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 3307,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 3329,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 3555,
    "test": "need_check",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 3636,
    "test": "s3_fallthrough_target",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 3717,
    "test": "csrpermit_vstimecmp_exii",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 3753,
    "test": "interrupt_filter_aia_topi_priority_matrix",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 3859,
    "test": "rvc_fs_off_illegal",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 3907,
    "test": "dret_event_virtual_mode",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 3955,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 4110,
    "test": "dcache_cmo_source_capacity",
    "type": "sw_hw_config",
    "desc": "N/A"
  },
  {
    "pr": 4166,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 4179,
    "test": "interrupt_filter_priority_regression",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 4426,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 4442,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 4533,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 4750,
    "test": "need_check",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 4968,
    "test": "tage_reset_compatibility",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 5182,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 5496,
    "test": "kunminghuv2minimalconfig_verilog",
    "type": "sw_hw_config",
    "desc": "N/A"
  },
  {
    "pr": 5687,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 655,
    "test": "loadpipe_data_port_conflict",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 739,
    "test": "need_check",
    "type": "timing_sync",
    "desc": "N/A"
  }
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  config_integ: 1
  logic: 8
  need_classification: 18
  spec: 6
  sw_hw_config: 2
  timing_sync: 4
```

## 对比官方

```yaml
bug_type_breakdown:
  config_integ: 1
  interface: 10
  logic: 11
  spec: 7
  sw_hw_config: 3
  timing_sync: 7
```

## 结论

DeepSeek V4 Flash (OpenCode) 在 XiangShan 上 12/51 (24%)。0 基础设施错误。
