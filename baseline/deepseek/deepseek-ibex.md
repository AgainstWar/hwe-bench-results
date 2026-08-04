# Ibex Baseline (DeepSeek V4 Flash) Analysis

## Overall Results

```yaml
config: baseline
repo: ibex
agent: OpenCode
model: DeepSeek V4 Flash
resolved: 27
total: 35
resolved_rate: 77%
file_level_precision: 79.2%
infra_errors: 0
```

## Token Statistics (token_report.py)

### Average Metrics

```yaml
token_statistics:
  tasks: 35
  status: resolved=27 unresolved=8
  prompt_k: 856.3
  completion_k: 17.7
  cache_hit_pct: 97.0
  tool_calls: 23.2
  cost_usd: 0.000000
  own_price_cost_usd: 0.250615
```

### Per-Task Detail

| Trial | Status | Prompt(K) | Comp(K) | Cost($) | Cache% | Calls |
|-------|--------|-----------|---------|---------|--------|-------|
| ibex-pr-104__vCDUADU | unresolved | 1488.0 | 12.5 | 0.0000 | 96.8 | 37 |
| ibex-pr-1135__BbERkks | resolved | 598.0 | 24.4 | 0.0000 | 93.7 | 16 |
| ibex-pr-1141__QFRNfNm | unresolved | 1313.9 | 20.6 | 0.0000 | 97.2 | 38 |
| ibex-pr-1229__gis7PTv | unresolved | 459.2 | 8.5 | 0.0000 | 94.2 | 22 |
| ibex-pr-122__SmhAKws | resolved | 556.1 | 13.0 | 0.0000 | 96.4 | 21 |
| ibex-pr-1383__Yy8gXQ8 | resolved | 209.8 | 4.9 | 0.0000 | 96.1 | 15 |
| ibex-pr-1469__HkuFviA | resolved | 2640.4 | 19.9 | 0.0000 | 97.2 | 41 |
| ibex-pr-1513__AKNhkke | unresolved | 2376.8 | 16.5 | 0.0000 | 97.2 | 55 |
| ibex-pr-155__nmbQQW2 | unresolved | 1512.0 | 45.5 | 0.0000 | 97.4 | 44 |
| ibex-pr-157__RGMgmo5 | resolved | 212.3 | 11.5 | 0.0000 | 94.1 | 10 |
| ibex-pr-1584__5iQmvsR | resolved | 4969.1 | 41.4 | 0.0000 | 98.4 | 64 |
| ibex-pr-166__GgJid4B | resolved | 63.8 | 4.2 | 0.0000 | 89.9 | 4 |
| ibex-pr-167__Fk2tPWZ | resolved | 2889.3 | 21.7 | 0.0000 | 98.3 | 67 |
| ibex-pr-1735__9hF3V3y | resolved | 299.8 | 13.1 | 0.0000 | 95.7 | 15 |
| ibex-pr-176__xPx8NYP | resolved | 62.5 | 1.7 | 0.0000 | 94.5 | 5 |
| ibex-pr-1780__UupAdMJ | resolved | 352.0 | 8.4 | 0.0000 | 97.0 | 21 |
| ibex-pr-1816__gbE9bb6 | resolved | 857.7 | 33.2 | 0.0000 | 96.8 | 34 |
| ibex-pr-1865__2yiAWvp | resolved | 198.8 | 9.3 | 0.0000 | 94.7 | 13 |
| ibex-pr-222__KcXE6wN | resolved | 246.7 | 9.2 | 0.0000 | 94.7 | 15 |
| ibex-pr-2232__rrKG6zo | resolved | 495.8 | 9.6 | 0.0000 | 95.4 | 24 |
| ibex-pr-244__M24mLst | resolved | 712.5 | 29.3 | 0.0000 | 96.1 | 23 |
| ibex-pr-276__SANhEYm | resolved | 1625.2 | 56.4 | 0.0000 | 97.7 | 29 |
| ibex-pr-282__vHWgFwo | resolved | 308.1 | 13.9 | 0.0000 | 95.1 | 18 |
| ibex-pr-293__UTaQbm6 | resolved | 186.3 | 9.7 | 0.0000 | 96.1 | 13 |
| ibex-pr-332__iuMTLAy | resolved | 1554.1 | 55.8 | 0.0000 | 97.6 | 24 |
| ibex-pr-377__RswQaRr | resolved | 1187.5 | 20.6 | 0.0000 | 97.4 | 31 |
| ibex-pr-45__GawhjKW | resolved | 143.8 | 3.9 | 0.0000 | 93.8 | 11 |
| ibex-pr-465__6zkhz37 | resolved | 59.3 | 1.5 | 0.0000 | 90.7 | 4 |
| ibex-pr-475__pm3p7H8 | unresolved | 241.0 | 7.3 | 0.0000 | 91.6 | 13 |
| ibex-pr-48__ecoqMeK | resolved | 58.0 | 3.1 | 0.0000 | 92.1 | 4 |
| ibex-pr-54__kyZqNkw | resolved | 60.7 | 4.4 | 0.0000 | 87.3 | 8 |
| ibex-pr-83__Sda7d4Y | resolved | 290.0 | 4.2 | 0.0000 | 96.0 | 17 |
| ibex-pr-882__SBGsmor | resolved | 801.6 | 36.2 | 0.0000 | 95.8 | 19 |
| ibex-pr-907__sTj7XPM | unresolved | 592.2 | 33.3 | 0.0000 | 96.2 | 20 |
| ibex-pr-974__xKrUbPn | unresolved | 347.2 | 9.5 | 0.0000 | 94.8 | 17 |

## Unresolved Cases

```json
[
  {"pr": 104, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 155, "test": "N/A", "type": "logic", "desc": "N/A"},  {"pr": 475, "test": "N/A", "type": "spec", "desc": "N/A"},  {"pr": 907, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 974, "test": "N/A", "type": "timing_sync", "desc": "N/A"},  {"pr": 1141, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1229, "test": "N/A", "type": "interface", "desc": "N/A"},  {"pr": 1513, "test": "N/A", "type": "logic", "desc": "N/A"}
]
```

## Bug Type Distribution

```yaml
  interface: 3
  logic: 2
  spec: 2
  timing_sync: 1
```

## File-Level Precision

- **Overall**: 79.2%
