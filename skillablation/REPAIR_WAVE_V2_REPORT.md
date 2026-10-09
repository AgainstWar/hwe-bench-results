# DeepSeek V4 Flash Repair+Wave V2 Report

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode |
| 模型 | DeepSeek V4 Flash (`opencode-go/deepseek-v4-flash`) |
| Provider | OpenCode Go |
| Skill | repair + wave (`SKILLS_ENABLED=true`, `SKILLS_INCLUDE=repair,wave`) |
| MCP | WAVES (`WAVES_ENABLED=true`) |
| 运行方式 | Harbor Framework, Docker 容器化 |
| 并行度 | Verilog 项目 4 并发, Chisel 项目 2 并发 |
| 重试次数 | 2 次 (k=1, r=2) |
| reasoning_effort | medium |
| 基础设施错误 | 0 |

---

## 总体结果

| Repo | Resolved | Rate | File-Level Precision | 空 Patch |
|------|:--------:|:----:|:--------------------:|:--------:|
| ibex | 34/35 | 97.1% | 97.52% | 0 |
| cva6 | 35/35 | 100.0% | 96.55% | 0 |
| caliptra | 15/16 | 93.8% | 100.00% | 0 |
| rocketchip | 11/32 | 34.4% | 86.90% | 0 |
| xiangshan | 30/54 | 55.6% | 100.00% | 0 |
| **Total** | **125/172** | **72.7%** | — | **0** |

说明：
- 全部 172 条已完成轨迹中 MCP 调用为 0（`wave` skill 被加载但 WAVES MCP 工具未被调用）。

---

## 各项目结果

### Ibex (lowRISC/ibex) — 34/35 (97.1%)

未解决（1）：1229

### CVA6 (openhwgroup/cva6) — 35/35 (100.0%)

无未解决用例。

### Caliptra (chipsalliance/caliptra-rtl) — 15/16 (93.8%)

未解决（1）：594

### RocketChip (chipsalliance/rocket-chip) — 11/32 (34.4%)

未解决（21）：177, 387, 404, 745, 1093, 1176, 1493, 1761, 1878, 2018, 2036, 2167, 2213, 2368, 2543, 2621, 3004, 3065, 3256, 3624, 3651

### XiangShan (OpenXiangShan/XiangShan) — 30/54 (55.6%)

未解决（24）：655, 1242, 1323, 1395, 1401, 1694, 1907, 2195, 2246, 2351, 3307, 3329, 3867, 4166, 4426, 4442, 4533, 4750, 4764, 4943, 5189, 5496, 5593, 5687

---

## 指标统计

- **Resolved Rate**：agent patch 使测试 FAIL→PASS 的任务比例
- **File-Level Precision**：agent 修改的文件中出现在 ground-truth patch 中的比例 = |agent_files ∩ ground_truth_files| / |agent_files|

| Repo | Resolved Rate | Overall Precision | Average (per-case) Precision |
|------|:------------:|:-----------------:|:----------------------------:|
| ibex | 97.1% | 97.52% | 96.43% |
| cva6 | 100.0% | 96.55% | 99.20% |
| caliptra | 93.8% | 100.00% | 100.00% |
| rocketchip | 34.4% | 86.90% | 96.88% |
| xiangshan | 55.6% | 100.00% | 100.00% |

---

## Token 消耗统计

| Repo | Tasks | Prompt(K) | Comp(K) | Cache% | Calls | MCP | Repair Skill | Wave Skill | Ordinary | Cost($) | Own-price($) |
|------|-------|-----------|---------|--------|-------|-----|--------------|------------|----------|---------|--------------|
| ibex | 35 | 3635.0 | 13.1 | 98.0 | 55.4 | 0.0 | 1.4 | 0.3 | 53.7 | 0.039030 | 0.995846 |
| cva6 | 35 | 2105.7 | 6.2 | 96.8 | 45.0 | 0.0 | 1.3 | 0.0 | 43.7 | 0.026048 | 0.575370 |
| caliptra | 16 | 2506.4 | 6.2 | 97.0 | 45.9 | 0.0 | 1.4 | 0.1 | 44.4 | 0.030740 | 0.683548 |
| rocketchip | 32 | 1765.6 | 5.9 | 96.6 | 45.3 | 0.0 | 1.2 | 0.0 | 44.2 | 0.024926 | 0.483191 |
| xiangshan | 54 | 2684.4 | 9.0 | 96.6 | 47.1 | 0.0 | 1.2 | 0.0 | 45.9 | 0.034987 | 0.734687 |

注：
- 上表除 `Tasks` 外均为**每任务均值**。
- 全实验 API 总成本 **$5.4564**，own-price 估算总成本 **$121.065**。

---

## Skill / MCP 使用情况

| Repo | repair skill | wave skill | MCP | Ordinary |
|------|:------------:|:----------:|:---:|:--------:|
| ibex | 48 | 12 | 0 | 1878 |
| cva6 | 45 | 0 | 0 | 1530 |
| caliptra | 22 | 2 | 0 | 710 |
| rocketchip | 38 | 0 | 0 | 1413 |
| xiangshan | 67 | 1 | 0 | 2477 |
| **合计** | **220** | **15** | **0** | **8008** |

- `repair` skill 每个任务调用约 1.2–1.4 次；`wave` skill 仅少量调用（合计 15 次）。
- **WAVES MCP 一次都未被调用**（`waves_wave_*` = 0），尽管 `WAVES_ENABLED=true` 且 `wave` skill 已被加载。

---

## 与 Baseline V2 对比

| Repo | Baseline V2 | Repair+Wave V2 | 变化 |
|------|:-----------:|:--------------:|:----:|
| ibex | 35/35 (100.0%) | 34/35 (97.1%) | -2.9 |
| cva6 | 35/35 (100.0%) | 35/35 (100.0%) | 0.0 |
| caliptra | 15/16 (93.8%) | 15/16 (93.8%) | 0.0 |
| rocketchip | 20/32 (62.5%) | 11/32 (34.4%) | -28.1 |
| xiangshan | 32/53 (60.4%) | 30/54 (55.6%) | -4.8 |
| **Total** | **137/171 (80.1%)** | **125/172 (72.7%)** | **-7.4** |

| Repo | Baseline V2 Precision | Repair+Wave V2 Precision |
|------|:---------------------:|:------------------------:|
| ibex | 98.15% | 97.52% |
| cva6 | 94.83% | 96.55% |
| caliptra | 93.33% | 100.00% |
| rocketchip | 94.52% | 86.90% |
| xiangshan | 93.64% | 100.00% |

---

## 核心发现

1. **WAVES MCP 未被调用**：172 条轨迹中 `waves_wave_*` 为 0；`wave` skill 虽被加载（15 次），但 agent 从未真正查询波形。

2. **总体低于 Baseline V2**：125/172 (72.7%) vs 137/171 (80.1%)，差 7.4 个百分点。

3. **退步主要在 Chisel**：rocketchip -28.1、xiangshan -4.8；Verilog 三库（ibex/cva6/caliptra）基本与基线持平。

4. **精度很高**：caliptra 与 xiangshan 均 100.00%，rocketchip 86.90% 最低。

5. **数据完整**：本实验无空 patch（172 条轨迹均有非空 patch）。

---

## 数据来源与口径

- 原始包：`results-repair-wave-v2.tar.gz`（含 `jobs/hwe-repair-wave-v2-*` 与 `results/hwe-repair-wave-v2-*`）
- `resolved/unresolved/empty_patch/error`：`results/hwe-repair-wave-v2-<repo>/eval/final_report.json`
- File-Level Precision：`results-archive/analysis/compute_precision.py`
- Token / Calls：`results-archive/analysis/token_report.py`（`result.json` + `agent/trajectory.json`）
- Skill 分类：`repair` skill = `hdl-minimal-repair` + `repair`；`wave` skill = `wave` + `waves-debug`；MCP = `waves_wave_*`；其余为 Ordinary
- 本报告未修改 `results-archive/analysis/`；旧版报告保持原样。
