# Ibex MCP + WAVES Analysis

## Overall Results

```yaml
opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES + waves-debug skill
  resolved: 24
  total: 35
  pct: 69%
  infra_errors: 0
```

## MCP vs Baseline (No MCP)

| Metric | Baseline | MCP |
|---|---|---|
| Resolved | 27/35 (77%) | 24/35 (69%) |
| Net Change | | -3 |
| Infra Errors | 0 | 0 |

### MCP Newly Solved
  ✅ pr-974: timing_sync
  ✅ pr-1141: interface

### MCP Lost
  ❌ pr-293: interface
  ❌ pr-1135: config_integ
  ❌ pr-1469: spec
  ❌ pr-1816: spec
  ❌ pr-1865: interface

## Bug Type Impact (MCP Changes)

| Bug Type | +MCP Solved | -MCP Lost | Net |
|----------|:-:|:-:|:-:|
| config_integ | +0 | -1 | -1 |
| interface | +1 | -2 | -1 |
| spec | +0 | -2 | -2 |
| timing_sync | +1 | -0 | +1 |

## Unresolved Cases

```json[
  {
    "pr": 104,
    "test": "unknown",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 155,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 293,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 475,
    "test": "need_check",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 907,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1135,
    "test": "need_check",
    "type": "config_integ",
    "desc": "N/A"
  },
  {
    "pr": 1229,
    "test": "need_check",
    "type": "interface",
    "desc": "N/A"
  },
  {
    "pr": 1469,
    "test": "need_check",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 1513,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1816,
    "test": "need_check",
    "type": "spec",
    "desc": "N/A"
  },
  {
    "pr": 1865,
    "test": "unknown",
    "type": "interface",
    "desc": "N/A"
  }
]
```

## Bug Type Breakdown (Unresolved)

```yaml
  config_integ: 1
  interface: 3
  logic: 2
  need_classification: 1
  spec: 4
```

## Comparison with Official GPT-5.4

| Category | Count | PRs |
|---|---|---|
| Both Resolved | 22 | 45, 48, 54, 83, 122, 157, 166, 167, 176, 222, 244, 282, 332, 377, 465, 882, 974, 1141, 1383, 1584, 1735, 2232 |
| Official Only | 10 | 155, 293, 475, 907, 1135, 1229, 1469, 1513, 1816, 1865 |
| MCP Only | 2 | 276, 1780 |
| Neither | 1 | 104 |

## Conclusion

MCP + WAVES slight regression (-3) on Ibex, but narrowing vs old MCP runs. Zero infrastructure errors.
