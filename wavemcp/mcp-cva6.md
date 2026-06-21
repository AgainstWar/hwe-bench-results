# CVA6 MCP + WAVES Analysis

## Overall Results

```yaml
opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES + waves-debug skill
  resolved: 31
  total: 35
  pct: 89%
  infra_errors: 0
```

## MCP vs Baseline (No MCP)

| Metric | Baseline | MCP |
|---|---|---|
| Resolved | 28/35 (80%) | 31/35 (89%) |
| Net Change | | +3 |
| Infra Errors | 0 | 0 |

### MCP Newly Solved
  ✅ pr-2279: interface
  ✅ pr-2420: config_integ
  ✅ pr-2989: spec

### MCP Lost
  None

## Bug Type Impact (MCP Changes)

| Bug Type | +MCP Solved | -MCP Lost | Net |
|----------|:-:|:-:|:-:|
| config_integ | +1 | -0 | +1 |
| interface | +1 | -0 | +1 |
| spec | +1 | -0 | +1 |

## Unresolved Cases

```json
[
  {"pr": 2170, "test": "unknown", "type": "config_integ", "desc": "unknown"},
  {"pr": 2802, "test": "need_check", "type": "spec", "desc": "unknown"},
  {"pr": 2844, "test": "need_check", "type": "spec", "desc": "unknown"},
  {"pr": 3042, "test": "unknown", "type": "config_integ", "desc": "unknown"}
]
```

## Bug Type Breakdown (Unresolved)

```yaml
  config_integ: 2
  spec: 2
```

## Comparison with Official GPT-5.4

| Category | Count | PRs |
|---|---|---|
| Both Resolved | 31 | 1482, 2017, 2032, 2248, 2279, 2282, 2330, 2374, 2375, 2420, 2468, 2469, 2476, 2549, 2589, 2685, 2711, 2728, 2916, 2944, 2945, 2989, 3059, 3107, 3137, 3168, 3171, 3191, 3204, 3226, 3231 |
| Official Only | 3 | 2170, 2802, 2844 |
| MCP Only | 0 | None |
| Neither | 1 | 3042 |

## Conclusion

MCP + WAVES positive net gain of +3 on CVA6. Zero infrastructure errors.
