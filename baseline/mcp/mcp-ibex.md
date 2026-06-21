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
  ✅ pr-974: unknown (unknown)
  ✅ pr-1141: unknown (unknown)

### MCP Lost
  ❌ pr-293: unknown (unknown)
  ❌ pr-1135: unknown (unknown)
  ❌ pr-1469: unknown (unknown)
  ❌ pr-1816: unknown (unknown)
  ❌ pr-1865: unknown (interface)

## Bug Type Impact (MCP Changes)

| Bug Type | +MCP Solved | -MCP Lost | Net |
|----------|:-:|:-:|:-:|
| interface | +0 | -1 | -1 |
| unknown | +2 | -4 | -2 |

## Unresolved Cases

```json
[
  {"pr": 104, "test": "unknown", "type": "spec", "desc": "unknown"},  {"pr": 155, "test": "need_check", "type": "need_classification", "desc": "unknown"},  {"pr": 293, "test": "need_check", "type": "need_classification", "desc": "unknown"},  {"pr": 475, "test": "need_check", "type": "need_classification", "desc": "unknown"},  {"pr": 907, "test": "need_check", "type": "need_classification", "desc": "unknown"},  {"pr": 1135, "test": "need_check", "type": "need_classification", "desc": "unknown"},  {"pr": 1229, "test": "need_check", "type": "need_classification", "desc": "unknown"},  {"pr": 1469, "test": "need_check", "type": "need_classification", "desc": "unknown"},  {"pr": 1513, "test": "need_check", "type": "need_classification", "desc": "unknown"},  {"pr": 1816, "test": "need_check", "type": "need_classification", "desc": "unknown"},  {"pr": 1865, "test": "unknown", "type": "interface", "desc": "unknown"}
]
```

## Bug Type Breakdown (Unresolved)

```yaml
  interface: 1
  need_classification: 9
  spec: 1
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
