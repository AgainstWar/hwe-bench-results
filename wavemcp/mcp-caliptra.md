# Caliptra MCP + WAVES Analysis

## Overall Results

```yaml
opencode:
  agent: OpenCode
  model: DeepSeek V4 Flash
  mcp: WAVES + waves-debug skill
  resolved: 12
  total: 16
  pct: 75%
  infra_errors: 0
```

## MCP vs Baseline (No MCP)

| Metric | Baseline | MCP |
|---|---|---|
| Resolved | 13/16 (81%) | 12/16 (75%) |
| Net Change | | -1 |
| Infra Errors | 0 | 0 |

### MCP Newly Solved
  None

### MCP Lost
  ❌ pr-633: logic

## Bug Type Impact (MCP Changes)

| Bug Type | +MCP Solved | -MCP Lost | Net |
|----------|:-:|:-:|:-:|
| logic | +0 | -1 | -1 |

## Unresolved Cases

```json
[
  {
    "pr": 70,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 633,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 725,
    "test": "need_check",
    "type": "logic",
    "desc": "N/A"
  },
  {
    "pr": 1033,
    "test": "need_check",
    "type": "sw_hw_config",
    "desc": "N/A"
  }
]
```

## Bug Type Breakdown (Unresolved)

```yaml
  logic: 3
  sw_hw_config: 1
```

## Comparison with Official GPT-5.4

| Category | Count | PRs |
|---|---|---|
| Both Resolved | 12 | 134, 195, 252, 298, 506, 594, 747, 757, 786, 963, 1073, 1089 |
| Official Only | 4 | 70, 633, 725, 1033 |
| MCP Only | 0 | None |
| Neither | 0 | None |

## Conclusion

MCP + WAVES slight regression (-1) on Caliptra, but narrowing vs old MCP runs. Zero infrastructure errors.
