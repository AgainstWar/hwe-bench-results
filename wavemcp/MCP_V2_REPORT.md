# DeepSeek V4 Flash MCP V2 Report

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode |
| 模型 | DeepSeek V4 Flash (`opencode-go/deepseek-v4-flash`) |
| Provider | OpenCode Go |
| MCP | WAVES (`WAVES_ENABLED=true`) |
| Skills | 未启用 |
| 运行方式 | Harbor Framework, Docker 容器化 |
| 并行度 | Verilog 项目 4 并发, Chisel 项目 2 并发 |
| 重试次数 | 2 次 (k=1, r=2) |
| reasoning_effort | medium |
| 基础设施错误 | 0 |

---

## 总体结果

| Repo | Resolved | Rate | File-Level Precision | 未完成 | 空 Patch |
|------|:--------:|:----:|:--------------------:|:------:|:--------:|
| ibex | 31/35 | 88.6% | 90.10% | 0 | 0 |
| cva6 | 34/35 | 97.1% | 88.54% | 0 | 0 |
| caliptra | 14/14 | 100.0% | 96.15% | 2 | 0 |
| rocketchip | 20/32 | 62.5% | 84.27% | 0 | 0 |
| xiangshan | 25/53 | 47.2% | 96.23% | 0 | 1 (pr-4750) |
| **Total** | **124/169** | **73.4%** | — | **2** | **1** |

说明：
- caliptra 数据集 16 例，其中 `pr-70`、`pr-786` 未产出 verifier 结果（未完成），最终进入评估 14 例。
- xiangshan `pr-4750` 为空 patch，被 `verify_bridge` 排除。
- 若按全量数据集 172 例计，总体为 124/172 (72.1%)。
- 全部 170 条已完成轨迹中 `skill` 调用为 0。

---

## 各项目结果

### Ibex (lowRISC/ibex) — 31/35 (88.6%)

未解决（4）：104, 276, 1229, 1865

### CVA6 (openhwgroup/cva6) — 34/35 (97.1%)

未解决（1）：2170

### Caliptra (chipsalliance/caliptra-rtl) — 14/14 (100.0%)

未完成（2）：`pr-70`, `pr-786`（agent 已运行，MCP 已注册，但无 `result.json` / verifier 输出，未计入）

### RocketChip (chipsalliance/rocket-chip) — 20/32 (62.5%)

未解决（12）：177, 387, 1493, 1761, 2018, 2036, 2167, 2621, 3256, 3526, 3624, 3651

### XiangShan (OpenXiangShan/XiangShan) — 25/53 (47.2%)

未解决（28）：655, 1242, 1323, 1401, 1694, 1907, 2195, 2246, 3307, 3753, 3907, 4166, 4179, 4337, 4426, 4442, 4533, 4764, 4943, 4959, 4968, 5080, 5182, 5189, 5496, 5593, 5687, 5700

---

## 指标统计

- **Resolved Rate**：agent patch 使测试 FAIL→PASS 的任务比例
- **File-Level Precision**：agent 修改的文件中出现在 ground-truth patch 中的比例 = |agent_files ∩ ground_truth_files| / |agent_files|

| Repo | Resolved Rate | Overall Precision | Average (per-case) Precision |
|------|:------------:|:-----------------:|:----------------------------:|
| ibex | 88.6% | 90.10% | 93.03% |
| cva6 | 97.1% | 88.54% | 92.38% |
| caliptra | 100.0% | 96.15% | 96.43% |
| rocketchip | 62.5% | 84.27% | 93.36% |
| xiangshan | 47.2% | 96.23% | 97.17% |

---

## Token 消耗统计

| Repo | Tasks | Prompt(K) | Comp(K) | Cache% | Calls | MCP | Other Skill | Ordinary | Cost($) | Own-price($) |
|------|-------|-----------|---------|--------|-------|-----|-------------|----------|---------|--------------|
| ibex | 35 | 10749.4 | 61.4 | 99.1 | 96.5 | 0.03 | 0.0 | 96.4 | 0.083391 | 2.969838 |
| cva6 | 35 | 4196.5 | 26.1 | 98.5 | 59.3 | 0.0 | 0.0 | 59.3 | 0.037451 | 1.161739 |
| caliptra | 14 | 4240.2 | 40.2 | 97.9 | 62.3 | 0.0 | 0.0 | 62.3 | 0.049825 | 1.189132 |
| rocketchip | 32 | 3630.0 | 24.3 | 96.4 | 59.6 | 0.0 | 0.0 | 59.6 | 0.046343 | 1.006849 |
| xiangshan | 53 | 3335.6 | 33.0 | 97.4 | 47.7 | 0.0 | 0.0 | 47.7 | 0.042657 | 0.936871 |

注：
- 上表除 `Tasks` 外均为**每任务均值**。
- 全实验 API 总成本 **$8.7135**，own-price 估算总成本 **$244.063**。
- caliptra 仅统计已完成的 14 例。

---

## MCP 使用情况

170 条已完成轨迹的工具调用统计：

| Repo | `waves_wave_*`（MCP） | `skill`（Skill） | Ordinary |
|------|:---------------------:|:----------------:|:--------:|
| ibex | 1 | 0 | 3375 |
| cva6 | 0 | 0 | 2076 |
| caliptra | 0 | 0 | 872 |
| rocketchip | 0 | 0 | 1907 |
| xiangshan | 0 | 0 | 2576 |
| **合计** | **1** | **0** | **10806** |

唯一一次 MCP 调用是 `waves_wave_get_info`（ibex）。其余主要工具为 `bash`、`read`、`edit`、`grep`，另有 `webfetch` 与 `websearch` 被频繁使用。也就是说，仅开启 `WAVES_ENABLED=true` 时，agent 基本不会主动使用 WAVES MCP。

---

## 与 Baseline V2 对比

| Repo | Baseline V2 | MCP V2 | 变化 |
|------|:-----------:|:------:|:----:|
| ibex | 35/35 (100.0%) | 31/35 (88.6%) | -11.4 |
| cva6 | 35/35 (100.0%) | 34/35 (97.1%) | -2.9 |
| caliptra | 15/16 (93.8%) | 14/14 (100.0%) | +6.2 |
| rocketchip | 20/32 (62.5%) | 20/32 (62.5%) | 0.0 |
| xiangshan | 32/53 (60.4%) | 25/53 (47.2%) | -13.2 |
| **Total** | **137/171 (80.1%)** | **124/169 (73.4%)** | **-6.7** |

注：两次运行的 caliptra 分母不同（baseline 16，MCP 14，差在 `pr-70`/`pr-786` 未完成），比较以 per-repo 行为准。

| Repo | Baseline V2 Precision | MCP V2 Precision |
|------|:---------------------:|:----------------:|
| ibex | 98.15% | 90.10% |
| cva6 | 94.83% | 88.54% |
| caliptra | 93.33% | 96.15% |
| rocketchip | 94.52% | 84.27% |
| xiangshan | 93.64% | 96.23% |

---

## 核心发现

1. **MCP 几乎未被调用**：170 条轨迹中仅 1 次 `waves_wave_*`，且没有 skill 调用。仅设置 `WAVES_ENABLED=true` 并没有让 agent 使用 WAVES。

2. **总体低于 Baseline V2**：124/169 (73.4%) vs 137/171 (80.1%)。下降主要来自 ibex（-4）与 xiangshan（-7）。

3. **Chisel 项目仍是最弱环节**：rocketchip 62.5%、xiangshan 47.2%，两库合计贡献 40/45 个未解决。

4. **精度表现分化**：caliptra 96.15%、xiangshan 96.23% 较高，但 rocketchip 84.27%、cva6 88.54% 偏低。

5. **数据完整性问题**：caliptra `pr-70`、`pr-786` 未完成，xiangshan `pr-4750` 空 patch；评估前需注意分母差异。

---

## 数据来源与口径

- 原始包：`results-mcp-v2.tar.gz`（含 `jobs/hwe-mcp-v2-*` 与 `results/hwe-mcp-v2-*`）
- `resolved/unresolved/empty_patch/error`：`results/hwe-mcp-v2-<repo>/eval/final_report.json`
- File-Level Precision：`results-archive/analysis/compute_precision.py`
- Token / Calls：`results-archive/analysis/token_report.py`（`result.json` + `agent/trajectory.json`）
- MCP / Skill 分类：`waves_wave_*` 计为 MCP，`skill` 计为 Skill，其余为 Ordinary
- 未完成判定：trial 目录缺 `result.json` 且 `verifier/` 为空
- 本报告未修改 `results-archive/analysis/`；旧版报告（`MCP_BASELINE_REPORT.md`、`mcp-<repo>.md`）保持原样。
