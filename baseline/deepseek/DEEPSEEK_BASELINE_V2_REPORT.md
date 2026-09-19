# DeepSeek V4 Flash Baseline V2 Report

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode |
| 模型 | DeepSeek V4 Flash (`deepseek-v4-flash`) |
| Provider | **OpenCode Go** (`opencode-go/deepseek-v4-flash`) |
| 运行方式 | Harbor Framework, Docker 容器化 |
| 并行度 | Verilog 项目 4 并发, Chisel 项目 2 并发 |
| 重试次数 | 2 次 (k=1, r=2) |
| reasoning_effort | medium |
| Skills / MCP | 均未启用（纯基线） |
| 基础设施错误 | 0 |

---

## 总体结果

| Repo | Resolved | Rate | 空 Patch | 基础设施错误 |
|------|:--------:|:----:|:--------:|:------------:|
| ibex | 35/35 | 100.0% | 0 | 0 |
| cva6 | 35/35 | 100.0% | 0 | 0 |
| caliptra | 15/16 | 93.8% | 0 | 0 |
| rocketchip | 20/32 | 62.5% | 0 | 0 |
| xiangshan | 32/53 | 60.4% | 1 (pr-4750) | 0 |
| **Total** | **137/171** | **80.1%** | **1** | **0** |

说明：
- xiangshan 数据集 54 例，其中 `pr-4750` agent 未产出 patch（`empty_patch`），被 `verify_bridge` 排除，最终进入评估 53 例。
- 若把该空 patch 计为未解决（分母取全量 172），总体为 **137/172 (79.7%)**。
- 全部 172 条轨迹中 `skill` / `waves_*` 调用数为 **0**，确认基线纯度。

---

## 各项目结果

### Ibex (lowRISC/ibex) — 35/35 (100%)

| 指标 | 数值 |
|------|------|
| 总用例 | 35 |
| 解决 | 35 (100%) |
| 未解决 | 0 |
| 空 Patch | 0 |
| File-Level Precision | 98.15% |

无未解决用例。

### CVA6 (openhwgroup/cva6) — 35/35 (100%)

| 指标 | 数值 |
|------|------|
| 总用例 | 35 |
| 解决 | 35 (100%) |
| 未解决 | 0 |
| 空 Patch | 0 |
| File-Level Precision | 94.83% |

无未解决用例。

### Caliptra (chipsalliance/caliptra-rtl) — 15/16 (93.8%)

| 指标 | 数值 |
|------|------|
| 总用例 | 16 |
| 解决 | 15 (93.8%) |
| 未解决 | 1 |
| 空 Patch | 0 |
| File-Level Precision | 93.33% |

未解决：`pr-70`

### RocketChip (chipsalliance/rocket-chip) — 20/32 (62.5%)

| 指标 | 数值 |
|------|------|
| 总用例 | 32 |
| 解决 | 20 (62.5%) |
| 未解决 | 12 |
| 空 Patch | 0 |
| File-Level Precision | 94.52% |

未解决（12）：177, 387, 1093, 1493, 1761, 2018, 2036, 2167, 3256, 3526, 3624, 3651

### XiangShan (OpenXiangShan/XiangShan) — 32/53 (60.4%)

| 指标 | 数值 |
|------|------|
| 总用例 | 54（其中 pr-4750 为空 patch，未进入评估） |
| 解决 | 32 (60.4%) |
| 未解决 | 21 |
| 空 Patch | 1 (pr-4750) |
| File-Level Precision | 93.64% |

未解决（21）：655, 1242, 1323, 1401, 1694, 1907, 2195, 2246, 3307, 3753, 3907, 4166, 4179, 4426, 4442, 4533, 4943, 5182, 5189, 5496, 5593

---

## 指标统计

本报告使用论文的两个互补指标：
- **Resolved Rate**：agent patch 使测试 FAIL→PASS 的任务比例
- **File-Level Precision**：agent 修改的文件中出现在 ground-truth patch 中的比例 = |agent_files ∩ ground_truth_files| / |agent_files|

| Repo | Resolved Rate | Overall Precision | Average (per-case) Precision |
|------|:------------:|:-----------------:|:----------------------------:|
| ibex | 100.0% | 98.15% | 98.10% |
| cva6 | 100.0% | 94.83% | 97.49% |
| caliptra | 93.8% | 93.33% | 87.50% |
| rocketchip | 62.5% | 94.52% | 94.40% |
| xiangshan | 60.4% | 93.64% | 96.08% |

---

## Token 消耗统计

| Repo | Tasks | Prompt(K) | Comp(K) | Cache% | Calls | MCP | Other Skill | Ordinary | Cost($) | Own-price($) |
|------|-------|-----------|---------|--------|-------|-----|-------------|----------|---------|--------------|
| ibex | 35 | 4577.9 | 31.1 | 98.0 | 59.7 | 0.0 | 0.0 | 59.7 | 0.046445 | 1.270251 |
| cva6 | 35 | 2728.6 | 12.5 | 97.4 | 39.2 | 0.0 | 0.0 | 39.2 | 0.027226 | 0.750474 |
| caliptra | 16 | 4405.4 | 24.7 | 96.6 | 50.4 | 0.0 | 0.0 | 50.4 | 0.052622 | 1.216629 |
| rocketchip | 32 | 4551.8 | 35.4 | 98.2 | 64.7 | 0.0 | 0.0 | 64.7 | 0.047065 | 1.267960 |
| xiangshan | 54 | 3351.9 | 28.2 | 96.6 | 47.6 | 0.0 | 0.0 | 47.6 | 0.043863 | 0.936051 |

注：
- 上表除 `Tasks` 外均为**每任务均值**。
- 全实验 API 总成本 **$7.2952**，own-price 估算总成本 **$181.313**。
- xiangshan 的 token 统计覆盖 54 条轨迹（含空 patch 的 pr-4750），评估实例为 53。
- `MCP` 与 `Other Skill` 均为 0，符合纯基线设置。

---

## 核心发现

1. **总体 137/171 (80.1%)**：Verilog 三库 ibex 100%、cva6 100%、caliptra 93.8%，已接近饱和。

2. **Chisel 项目是主要失分点**：rocketchip 62.5%、xiangshan 60.4%；全部 34 个未解决用例中有 33 个来自 Chisel 两库。

3. **精度普遍很高**：Overall File-Level Precision 为 93.3–98.2%，说明即使未通过验证，agent 的修改也基本落在正确文件上。

4. **零基础设施错误**：仅 1 个空 patch（xiangshan pr-4750），其余未解决均为 patch 质量或验证问题。

5. **基线纯度成立**：172 条轨迹中无任何 skill 或 MCP 调用，可作为干净的对照基线。

---

## 数据来源与口径

- 原始包：`results-baseline-v2.tar.gz`（含 `jobs/hwe-baseline-v2-*` 与 `results/hwe-baseline-v2-*`）
- `resolved/unresolved/empty_patch/error`：`results/hwe-baseline-v2-<repo>/eval/final_report.json`
- File-Level Precision：`results-archive/analysis/compute_precision.py`（patches.jsonl × dataset modified_files）
- Token / Calls：`results-archive/analysis/token_report.py`（`jobs/` 下 `result.json` + `agent/trajectory.json`）
- 空 patch 判定：`results/hwe-baseline-v2-xiangshan/patches/collection_summary.json` 中 `has_patch=false, error=empty_patch`
- 本报告中 `analysis/` 目录未做任何修改。
