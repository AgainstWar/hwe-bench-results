# DeepSeek V4 Flash Repair V2 Report

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode |
| 模型 | DeepSeek V4 Flash (`opencode-go/deepseek-v4-flash`) |
| Provider | OpenCode Go |
| Skill | repair (`SKILLS_ENABLED=true`, `SKILLS_INCLUDE=repair`) |
| MCP | 未启用 |
| 运行方式 | Harbor Framework, Docker 容器化 |
| 并行度 | Verilog 项目 4 并发, Chisel 项目 2 并发 |
| 重试次数 | 2 次 (k=1, r=2) |
| reasoning_effort | medium |
| 基础设施错误 | 0 |

---

## 总体结果

| Repo | Resolved | Rate | File-Level Precision | 空 Patch |
|------|:--------:|:----:|:--------------------:|:--------:|
| ibex | 31/34 | 91.2% | 96.43% | 1 (pr-276) |
| cva6 | 35/35 | 100.0% | 89.90% | 0 |
| caliptra | 15/16 | 93.8% | 93.33% | 0 |
| rocketchip | 15/31 | 48.4% | 84.52% | 1 (pr-1176) |
| xiangshan | 26/54 | 48.1% | 98.18% | 0 |
| **Total** | **122/170** | **71.8%** | — | **2** |

说明：
- `ibex pr-276`、`rocketchip pr-1176` 为空 patch，被 `verify_bridge` 排除。
- 全部 170 条已完成轨迹中 MCP 调用为 0；`repair` skill 每个任务调用 1 次。

---

## 各项目结果

### Ibex (lowRISC/ibex) — 31/34 (91.2%)

未解决（3）：104, 1229, 1865

### CVA6 (openhwgroup/cva6) — 35/35 (100.0%)

无未解决用例。

### Caliptra (chipsalliance/caliptra-rtl) — 15/16 (93.8%)

未解决（1）：70

### RocketChip (chipsalliance/rocket-chip) — 15/31 (48.4%)

未解决（16）：177, 387, 745, 1093, 1493, 1761, 1878, 2018, 2036, 2167, 2213, 2543, 3004, 3256, 3624, 3651

### XiangShan (OpenXiangShan/XiangShan) — 26/54 (48.1%)

未解决（28）：655, 1242, 1323, 1395, 1401, 1694, 1907, 1931, 2195, 2246, 2997, 3307, 3329, 3636, 3859, 3907, 3955, 4110, 4166, 4426, 4442, 4533, 4750, 4764, 4943, 5189, 5496, 5593

---

## 指标统计

- **Resolved Rate**：agent patch 使测试 FAIL→PASS 的任务比例
- **File-Level Precision**：agent 修改的文件中出现在 ground-truth patch 中的比例 = |agent_files ∩ ground_truth_files| / |agent_files|

| Repo | Resolved Rate | Overall Precision | Average (per-case) Precision |
|------|:------------:|:-----------------:|:----------------------------:|
| ibex | 91.2% | 96.43% | 97.99% |
| cva6 | 100.0% | 89.90% | 96.82% |
| caliptra | 93.8% | 93.33% | 90.62% |
| rocketchip | 48.4% | 84.52% | 94.76% |
| xiangshan | 48.1% | 98.18% | 98.89% |

---

## Token 消耗统计

| Repo | Tasks | Prompt(K) | Comp(K) | Cache% | Calls | MCP | Repair Skill | Ordinary | Cost($) | Own-price($) |
|------|-------|-----------|---------|--------|-------|-----|--------------|----------|---------|--------------|
| ibex | 35 | 12610.1 | 85.1 | 99.2 | 98.7 | 0.0 | 1.0 | 97.7 | 0.104186 | 3.498370 |
| cva6 | 35 | 6153.8 | 45.0 | 98.7 | 82.0 | 0.0 | 1.0 | 81.0 | 0.057152 | 1.711074 |
| caliptra | 16 | 6357.9 | 73.1 | 98.7 | 70.2 | 0.0 | 1.0 | 69.2 | 0.075368 | 1.797069 |
| rocketchip | 32 | 4488.9 | 24.5 | 98.4 | 70.1 | 0.0 | 1.0 | 69.1 | 0.044339 | 1.238909 |
| xiangshan | 54 | 2821.2 | 14.7 | 97.5 | 49.6 | 0.0 | 1.0 | 48.6 | 0.035370 | 0.777887 |

注：
- 上表除 `Tasks` 外均为**每任务均值**。
- 全实验 API 总成本 **$10.1815**，own-price 估算总成本 **$292.735**。
- `Tasks` 为 Harbor trial 数；其中 `ibex pr-276`、`rocketchip pr-1176` 为空 patch，未进入 resolved 统计。

---

## Skill 使用情况

| Repo | `repair`（hdl-minimal-repair） | MCP | Ordinary |
|------|:------------------------------:|:---:|:--------:|
| ibex | 35 | 0 | 3418 |
| cva6 | 35 | 0 | 2834 |
| caliptra | 16 | 0 | 1108 |
| rocketchip | 31 | 0 | 2143 |
| xiangshan | 54 | 0 | 2624 |
| **合计** | **171** | **0** | **12127** |

`repair` skill 在几乎每个任务中被调用一次（加载一次即按指引进行修复）。

---

## 与 Baseline V2 对比

| Repo | Baseline V2 | Repair V2 | 变化 |
|------|:-----------:|:---------:|:----:|
| ibex | 35/35 (100.0%) | 31/34 (91.2%) | -8.8 |
| cva6 | 35/35 (100.0%) | 35/35 (100.0%) | 0.0 |
| caliptra | 15/16 (93.8%) | 15/16 (93.8%) | 0.0 |
| rocketchip | 20/32 (62.5%) | 15/31 (48.4%) | -14.1 |
| xiangshan | 32/53 (60.4%) | 26/54 (48.1%) | -12.3 |
| **Total** | **137/171 (80.1%)** | **122/170 (71.8%)** | **-8.3** |

| Repo | Baseline V2 Precision | Repair V2 Precision |
|------|:---------------------:|:-------------------:|
| ibex | 98.15% | 96.43% |
| cva6 | 94.83% | 89.90% |
| caliptra | 93.33% | 93.33% |
| rocketchip | 94.52% | 84.52% |
| xiangshan | 93.64% | 98.18% |

---

## 核心发现

1. **repair skill 被稳定调用**：基本每个任务调用 1 次 `hdl-minimal-repair`（合计 171 次），MCP 为 0。

2. **总体低于 Baseline V2**：122/170 (71.8%) vs 137/171 (80.1%)，差 8.3 个百分点。

3. **退步集中在 Chisel 两库**：rocketchip（-14.1）与 xiangshan（-12.3）；Verilog 侧 cva6、caliptra 与基线持平，ibex 略降。

4. **精度表现分化**：xiangshan 98.18% 最高、ibex 96.43% 次之；rocketchip 84.52% 最低。

5. **数据完整性**：`ibex pr-276`、`rocketchip pr-1176` 为空 patch；其余用例均有非空 patch。

---

## 数据来源与口径

- 原始包：`results-repair-v2.tar.gz`（含 `jobs/hwe-repair-v2-*` 与 `results/hwe-repair-v2-*`）
- `resolved/unresolved/empty_patch/error`：`results/hwe-repair-v2-<repo>/eval/final_report.json`
- File-Level Precision：`results-archive/analysis/compute_precision.py`
- Token / Calls：`results-archive/analysis/token_report.py`（`result.json` + `agent/trajectory.json`）
- Skill 分类：`function_name == "skill"` 且 `arguments.name == "hdl-minimal-repair"` 计为 repair skill；MCP 恒为 0，其余为 Ordinary
- 本报告未修改 `results-archive/analysis/`；旧版报告保持原样。
