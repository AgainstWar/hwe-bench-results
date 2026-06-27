# XiangShan MCP + WAVES Analysis

## Overall Results

```yaml
opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES + waves-debug skill
  resolved: 18
  total: 54
  pct: 33%
  infra_errors: 0
```

## MCP vs Baseline (No MCP)

| Metric | Baseline | MCP |
|---|---|---|
| Resolved | 12/54 (22%) | 18/54 (33%) |
| Net Change | | +6 |
| Infra Errors | 0 | 0 |

### MCP Newly Solved
  ✅ pr-739: unknown
  ✅ pr-1679: unknown
  ✅ pr-1820: unknown
  ✅ pr-2351: unknown
  ✅ pr-2513: logic
  ✅ pr-2781: unknown
  ✅ pr-2997: logic
  ✅ pr-3555: unknown
  ✅ pr-3717: spec
  ✅ pr-5182: unknown

### MCP Lost
  ❌ pr-2483: logic
  ❌ pr-3867: logic
  ❌ pr-4943: sw_hw_config
  ❌ pr-5700: unknown

## Bug Type Impact (MCP Changes)

| Bug Type | +MCP Solved | -MCP Lost | Net |
|----------|:-:|:-:|:-:|
| logic | +2 | -2 | +0 |
| spec | +1 | -0 | +1 |
| sw_hw_config | +0 | -1 | -1 |
| unknown | +7 | -1 | +6 |

## Unresolved Cases

```json[
  {
    "pr": 655,
    "test": "loadpipe_data_port_conflict",
    "type": "logic",
    "desc": "N/A"
  },
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
    "pr": 2483,
    "test": "hperf_counter_selection_logic",
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
    "pr": 3636,
    "test": "s3_fallthrough_target",
    "type": "logic",
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
    "pr": 3867,
    "test": "dispatch_single_step_redirect_reuse",
    "type": "logic",
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
    "pr": 4943,
    "test": "frontend_tl_user_fields_contract",
    "type": "sw_hw_config",
    "desc": "N/A"
  },
  {
    "pr": 4968,
    "test": "tage_reset_compatibility",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 5189,
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
    "pr": 5593,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 5687,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 5700,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  }
]
```

## Bug Type Breakdown (Unresolved)

```yaml
  config_integ: 1
  logic: 8
  need_classification: 14
  spec: 5
  sw_hw_config: 3
  timing_sync: 4
```

## Comparison with Official GPT-5.4

| Category | Count | PRs |
|---|---|---|
| Both Resolved | 16 | 39, 281, 739, 1679, 1820, 1931, 2351, 2513, 2781, 2845, 2997, 3182, 3555, 4337, 4959, 5182 |
| Official Only | 24 | 655, 1323, 1694, 1793, 1907, 2095, 2195, 2246, 2483, 3307, 3329, 3859, 3867, 3907, 3955, 4166, 4442, 4533, 4968, 5080, 5189, 5496, 5593, 5687 |
| MCP Only | 2 | 3717, 4764 |
| Neither | 12 | 1242, 1395, 1401, 1602, 3636, 3753, 4110, 4179, 4426, 4750, 4943, 5700 |

## Conclusion

MCP + WAVES positive net gain of +6 on XiangShan. Zero infrastructure errors.
