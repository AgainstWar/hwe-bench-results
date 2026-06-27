# RocketChip MCP + WAVES Analysis

## Overall Results

```yaml
opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES + waves-debug skill
  resolved: 12
  total: 32
  pct: 38%
  infra_errors: 0
```

## MCP vs Baseline (No MCP)

| Metric | Baseline | MCP |
|---|---|---|
| Resolved | 8/32 (25%) | 12/32 (38%) |
| Net Change | | +4 |
| Infra Errors | 0 | 0 |

### MCP Newly Solved
  ✅ pr-404: unknown
  ✅ pr-1093: sw_hw_interact
  ✅ pr-1176: interface
  ✅ pr-1878: spec
  ✅ pr-2213: interface

### MCP Lost
  ❌ pr-3065: unknown

## Bug Type Impact (MCP Changes)

| Bug Type | +MCP Solved | -MCP Lost | Net |
|----------|:-:|:-:|:-:|
| interface | +2 | -0 | +2 |
| spec | +1 | -0 | +1 |
| sw_hw_interact | +1 | -0 | +1 |
| unknown | +1 | -1 | +0 |

## Unresolved Cases

```json[
  {
    "pr": 177,
    "test": "lrsc_mshr_secondary_dirty",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 387,
    "test": "async_queue_half_reset",
    "type": "timing_sync",
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
    "pr": 2018,
    "test": "unknown",
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
    "test": "unknown",
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
    "pr": 3065,
    "test": "need_check",
    "type": "interface",
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
    "test": "unknown",
    "type": "logic",
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
    "test": "unknown",
    "type": "spec",
    "desc": "N/A"
  }
]
```

## Bug Type Breakdown (Unresolved)

```yaml
  config_integ: 4
  interface: 2
  logic: 6
  need_classification: 2
  spec: 2
  timing_sync: 3
```

## Comparison with Official GPT-5.4

| Category | Count | PRs |
|---|---|---|
| Both Resolved | 10 | 404, 542, 1069, 1176, 1330, 1878, 2213, 2984, 2988, 2994 |
| Official Only | 13 | 177, 387, 745, 1656, 1761, 2018, 2036, 2167, 2543, 3065, 3526, 3600, 3624 |
| MCP Only | 2 | 576, 1093 |
| Neither | 7 | 485, 1493, 2368, 2621, 3004, 3256, 3651 |

## Conclusion

MCP + WAVES positive net gain of +4 on RocketChip. Zero infrastructure errors.
