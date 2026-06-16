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

```json
[
  {"pr": 1242, "test": "statusarray_store_set_wakeup", "type": "logic", "desc": "unknown"},
  {"pr": 1323, "test": "csr_mask_behavior", "type": "spec", "desc": "unknown"},
  {"pr": 1395, "test": "memblock_atomic_exception_hold", "type": "logic", "desc": "unknown"},
  {"pr": 1401, "test": "loadunit_refill_replay", "type": "timing_sync", "desc": "unknown"},
  {"pr": 1602, "test": "wb2ctrl_load_writeback_delay", "type": "timing_sync", "desc": "unknown"},
  {"pr": 1679, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 1694, "test": "loadunit_replay_from_fetch", "type": "logic", "desc": "unknown"},
  {"pr": 1793, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 1820, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 1907, "test": "ctrlblock_redirect_vset", "type": "logic", "desc": "unknown"},
  {"pr": 2095, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 2195, "test": "memblock_io_compile", "type": "timing_sync", "desc": "unknown"},
  {"pr": 2246, "test": "fpga_platform_private_l2_db_gating", "type": "config_integ", "desc": "unknown"},
  {"pr": 2351, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 2513, "test": "fusiondecoder_same_src_guard", "type": "logic", "desc": "unknown"},
  {"pr": 2781, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 2997, "test": "frontend_fallthrough_address_regression", "type": "logic", "desc": "unknown"},
  {"pr": 3307, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 3329, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 3555, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 3636, "test": "s3_fallthrough_target", "type": "logic", "desc": "unknown"},
  {"pr": 3717, "test": "csrpermit_vstimecmp_exii", "type": "spec", "desc": "unknown"},
  {"pr": 3753, "test": "interrupt_filter_aia_topi_priority_matrix", "type": "spec", "desc": "unknown"},
  {"pr": 3859, "test": "rvc_fs_off_illegal", "type": "spec", "desc": "unknown"},
  {"pr": 3907, "test": "dret_event_virtual_mode", "type": "spec", "desc": "unknown"},
  {"pr": 3955, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 4110, "test": "dcache_cmo_source_capacity", "type": "sw_hw_config", "desc": "unknown"},
  {"pr": 4166, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 4179, "test": "interrupt_filter_priority_regression", "type": "spec", "desc": "unknown"},
  {"pr": 4426, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 4442, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 4533, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 4750, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 4968, "test": "tage_reset_compatibility", "type": "timing_sync", "desc": "unknown"},
  {"pr": 5182, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 5496, "test": "kunminghuv2minimalconfig_verilog", "type": "sw_hw_config", "desc": "unknown"},
  {"pr": 5687, "test": "need_check", "type": "need_classification", "desc": "unknown"},
  {"pr": 655, "test": "loadpipe_data_port_conflict", "type": "logic", "desc": "unknown"},
  {"pr": 739, "test": "need_check", "type": "need_classification", "desc": "unknown"}
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
comparison_with_official:
  both_resolved:
    count: 10
    prs: [1931, 2483, 281, 2845, 3182, 3867, 39, 4337, 4764, 4959]
  official_only:
    count: 15
    prs: [1679, 1694, 2095, 2513, 2997, 3307, 3555, 3717, 3955, 4442, 5080, 5496, 5593, 5687, 739]
  opencode_only:
    count: 2
    prs: [4943, 5700]
  neither:
    count: 26
    prs: [1242, 1323, 1395, 1401, 1602, 1793, 1820, 1907, 2195, 2246, 2351, 2781, 3329, 3636, 3753, 3859, 3907, 4110, 4166, 4179, 4426, 4533, 4750, 4968, 5182, 655]
```

## 结论

DeepSeek V4 Flash (OpenCode) 在 XiangShan 上 12/51 (24%)。0 基础设施错误。
