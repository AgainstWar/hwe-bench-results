# Rocket-Chip Analysis (DeepSeek V4 Flash)

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: DeepSeek V3.2
  resolved: 16
  total: 32
  pct: 50
  infra_errors: 0

opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  resolved: 8
  total: 32
  pct: 25
  infra_errors: 0
```

## 未解决 Case

```json[
  {
    "pr": 1093,
    "test": "bus_error_unit_rv32_elaboration",
    "type": "sw_hw_interact",
    "desc": "N/A"
  },
  {
    "pr": 1176,
    "test": "tl_mmio_port_internal_wiring",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1493,
    "test": "async_pbus_bootrom_access",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 1656,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1761,
    "test": "csr-tvec-uninitialized-alignment",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 177,
    "test": "lrsc_mshr_secondary_dirty",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1878,
    "test": "misa_x_bit",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 2018,
    "test": "N/A",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 2036,
    "test": "mret_not_misdetected_as_dret",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2167,
    "test": "jtag_async_reset",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 2213,
    "test": "debug_apb_gap_behavior",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 2368,
    "test": "asyncvalidsync-mixed-reset-elaboration",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 2543,
    "test": "heterogeneous_hartid_elaboration",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 2621,
    "test": "N/A",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 3004,
    "test": "frontend_progress_quiesce",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 3256,
    "test": "aes64ks1i_decode",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 3526,
    "test": "N/A",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 3600,
    "test": "need_check",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 3624,
    "test": "hypervisor_tinst_warl",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 3651,
    "test": "N/A",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 387,
    "test": "async_queue_half_reset",
    "type": "timing_sync",
    "desc": "N/A"
  },
  {
    "pr": 404,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 485,
    "test": "diplomatic_ahb_elaboration",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 745,
    "test": "rocc_example_elaboration",
    "type": "config_integ",
    "desc": "N/A"
  }
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  config_integ: 4
  interface: 4
  logic: 6
  need_classification: 3
  spec: 3
  sw_hw_interact: 1
  timing_sync: 3
```

## 对比官方

```yaml
bug_type_breakdown:
  config_integ: 4
  interface: 5
  logic: 7
  spec: 3
  sw_hw_interact: 1
  timing_sync: 4
```

## 结论

DeepSeek V4 Flash (OpenCode) 在 rocket-chip 上 8/32 (25%)。0 基础设施错误。
