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
| caliptra | 15/16 | 93.8% | 92.86% | 0 | 0 |
| rocketchip | 20/32 | 62.5% | 84.27% | 0 | 0 |
| xiangshan | 35/53 | 66.0% | 95.24% | 0 | 1 (pr-4750) |
| **Total** | **135/171** | **78.9%** | — | **0** | **1** |

说明：
- xiangshan `pr-4750` 为空 patch，被 `verify_bridge` 排除。
- caliptra 首次运行时 `pr-70`/`pr-786` 因 WAVES 安装阶段的网络问题未完成，已单独重跑并合并（`pr-786` resolved，`pr-70` 仍 unresolved）。
- xiangshan 的 28 个未解决用例额外重跑一次并合并，新增解决 10 个（含评估抖动，见文末说明）。
- 全部 171 条已完成轨迹中 `skill` 调用为 0。

---

## 各项目结果

### Ibex (lowRISC/ibex) — 31/35 (88.6%)

未解决（4）：104, 276, 1229, 1865

### CVA6 (openhwgroup/cva6) — 34/35 (97.1%)

未解决（1）：2170

### Caliptra (chipsalliance/caliptra-rtl) — 15/16 (93.8%)

未解决（1）：70

### RocketChip (chipsalliance/rocket-chip) — 20/32 (62.5%)

未解决（12）：177, 387, 1493, 1761, 2018, 2036, 2167, 2621, 3256, 3526, 3624, 3651

### XiangShan (OpenXiangShan/XiangShan) — 35/53 (66.0%)

未解决（18）：655, 1242, 1323, 1401, 1694, 1907, 2195, 2246, 3307, 4166, 4426, 4442, 4533, 4943, 5182, 5189, 5496, 5687

---

## 指标统计

- **Resolved Rate**：agent patch 使测试 FAIL→PASS 的任务比例
- **File-Level Precision**：agent 修改的文件中出现在 ground-truth patch 中的比例 = |agent_files ∩ ground_truth_files| / |agent_files|

| Repo | Resolved Rate | Overall Precision | Average (per-case) Precision |
|------|:------------:|:-----------------:|:----------------------------:|
| ibex | 88.6% | 90.10% | 93.03% |
| cva6 | 97.1% | 88.54% | 92.38% |
| caliptra | 93.8% | 92.86% | 90.62% |
| rocketchip | 62.5% | 84.27% | 93.36% |
| xiangshan | 66.0% | 95.24% | 96.23% |

---

## Token 消耗统计

| Repo | Tasks | Prompt(K) | Comp(K) | Cache% | Calls | MCP | Other Skill | Ordinary | Cost($) | Own-price($) |
|------|-------|-----------|---------|--------|-------|-----|-------------|----------|---------|--------------|
| ibex | 35 | 10749.4 | 61.4 | 99.1 | 96.5 | 0.03 | 0.0 | 96.4 | 0.083391 | 2.969838 |
| cva6 | 35 | 4196.5 | 26.1 | 98.5 | 59.3 | 0.0 | 0.0 | 59.3 | 0.037451 | 1.161739 |
| caliptra | 16 | 8040.8 | 56.0 | 98.2 | 78.1 | 0.0 | 0.0 | 78.1 | 0.078789 | 2.232623 |
| rocketchip | 32 | 3630.0 | 24.3 | 96.4 | 59.6 | 0.0 | 0.0 | 59.6 | 0.046343 | 1.006849 |
| xiangshan | 53 | 2876.7 | 30.2 | 96.2 | 45.0 | 0.0 | 0.0 | 45.0 | 0.043177 | 0.809884 |

注：
- 上表除 `Tasks` 外均为**每任务均值**。
- 全实验 API 总成本 **$9.3047**，own-price 估算总成本 **$256.280**。

---

## MCP 使用情况

171 条已完成轨迹的工具调用统计：

| Repo | `waves_wave_*`（MCP） | `skill`（Skill） | Ordinary |
|------|:---------------------:|:----------------:|:--------:|
| ibex | 1 | 0 | 3375 |
| cva6 | 0 | 0 | 2076 |
| caliptra | 0 | 0 | 1249 |
| rocketchip | 0 | 0 | 1907 |
| xiangshan | 0 | 0 | 2432 |
| **合计** | **1** | **0** | **11039** |

唯一一次 MCP 调用是 `waves_wave_get_info`（ibex）。其余主要工具为 `bash`、`read`、`edit`、`grep`，另有 `webfetch` 与 `websearch` 被频繁使用。也就是说，仅开启 `WAVES_ENABLED=true` 时，agent 基本不会主动使用 WAVES MCP。

---

## 与 Baseline V2 对比

| Repo | Baseline V2 | MCP V2 | 变化 |
|------|:-----------:|:------:|:----:|
| ibex | 35/35 (100.0%) | 31/35 (88.6%) | -11.4 |
| cva6 | 35/35 (100.0%) | 34/35 (97.1%) | -2.9 |
| caliptra | 15/16 (93.8%) | 15/16 (93.8%) | 0.0 |
| rocketchip | 20/32 (62.5%) | 20/32 (62.5%) | 0.0 |
| xiangshan | 32/53 (60.4%) | 35/53 (66.0%) | +5.7 |
| **Total** | **137/171 (80.1%)** | **135/171 (78.9%)** | **-1.2** |

| Repo | Baseline V2 Precision | MCP V2 Precision |
|------|:---------------------:|:----------------:|
| ibex | 98.15% | 90.10% |
| cva6 | 94.83% | 88.54% |
| caliptra | 93.33% | 92.86% |
| rocketchip | 94.52% | 84.27% |
| xiangshan | 93.64% | 95.24% |

---

## 核心发现

1. **MCP 几乎未被调用**：171 条轨迹中仅 1 次 `waves_wave_*`，且没有 skill 调用。仅设置 `WAVES_ENABLED=true` 并没有让 agent 使用 WAVES。

2. **总体与 Baseline V2 接近**：135/171 (78.9%) vs 137/171 (80.1%)，仅差 1.2 个百分点。差异集中在 ibex（-4）与 xiangshan（+3）。

3. **Chisel 项目**：rocketchip 62.5%、xiangshan 66.0%，仍是主要失分点。

4. **精度表现分化**：xiangshan 95.24%、caliptra 92.86% 较高，但 rocketchip 84.27%、cva6 88.54% 偏低。

5. **数据完整性**：caliptra `pr-70`/`pr-786` 与 xiangshan 28 个未解决用例均已补跑合并；xiangshan `pr-4750` 为空 patch。

6. **评估存在抖动**：xiangshan 的 28 个未解决用例独立重跑评估时解决 7 个，合并后全量重算解决 10 个（3753、3907、4764、5593 由未解决变解决，5182 反向），同一份 patch 结果不一致，提示仿真/评估存在不稳定性。本报告采用全量重算后的结果。

---

## 数据来源与口径

- 原始包：`results-mcp-v2.tar.gz`（含 `jobs/hwe-mcp-v2-*` 与 `results/hwe-mcp-v2-*`）
- `resolved/unresolved/empty_patch/error`：`results/hwe-mcp-v2-<repo>/eval/final_report.json`
- File-Level Precision：`results-archive/analysis/compute_precision.py`
- Token / Calls：`results-archive/analysis/token_report.py`（`result.json` + `agent/trajectory.json`）
- MCP / Skill 分类：`waves_wave_*` 计为 MCP，`skill` 计为 Skill，其余为 Ordinary
- WAVES 安装：`git clone` 经 `ghproxy.net` 镜像、`pip install` 经 `pypi.tuna.tsinghua.edu.cn` 镜像
- 补跑记录：`hwe-mcp-v2-caliptra-retry`（caliptra pr-70/pr-786）、`hwe-mcp-v2-xiangshan-retry`（xiangshan 28 例），均随包归档
- 未完成判定：trial 目录缺 `result.json` 且 `verifier/` 为空
- 本报告未修改 `results-archive/analysis/`；旧版报告（`MCP_BASELINE_REPORT.md`、`mcp-<repo>.md`）保持原样。
