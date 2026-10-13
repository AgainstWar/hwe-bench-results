# DeepSeek V4 Flash Repair V3 Report

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode |
| 模型 | DeepSeek V4 Flash (`opencode-go/deepseek-v4-flash`) |
| Provider | OpenCode Go |
| Skill | repair（改版，`SKILLS_ENABLED=true`, `SKILLS_INCLUDE=repair`） |
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
| ibex | 35/35 | 100.0% | 100.00% | 0 |
| cva6 | 35/35 | 100.0% | 100.00% | 0 |
| caliptra | 16/16 | 100.0% | 91.67% | 0 |
| rocketchip | 25/32 | 78.1% | 92.42% | 0 |
| xiangshan | 31/53 | 58.5% | 99.01% | 0 |
| **Total** | **142/171** | **83.0%** | — | **0** |

说明：
- 全部 171 条已完成轨迹中 MCP 调用为 0；repair skill 合计调用 247 次。
- 29 个未解决用例中，28 个为补丁未通过测试，仅 `xiangshan pr-5496` 为超时（构建 1794s，超过 1800s 上限）。

---

## 各项目结果

### Ibex (lowRISC/ibex) — 35/35 (100.0%)

无未解决用例。

### CVA6 (openhwgroup/cva6) — 35/35 (100.0%)

无未解决用例。

### Caliptra (chipsalliance/caliptra-rtl) — 16/16 (100.0%)

无未解决用例。

### RocketChip (chipsalliance/rocket-chip) — 25/32 (78.1%)

未解决（7）：387, 1493, 1761, 2036, 2167, 3256, 3624

### XiangShan (OpenXiangShan/XiangShan) — 31/53 (58.5%)

未解决（22）：655, 1242, 1323, 1694, 1907, 2195, 2246, 3307, 3867, 4110, 4166, 4179, 4426, 4442, 4533, 4764, 4943, 5182, 5189, 5496, 5593, 5687

（其中 `pr-5496` 为超时失败，其余为补丁未通过。）

---

## 指标统计

- **Resolved Rate**：agent patch 使测试 FAIL→PASS 的任务比例
- **File-Level Precision**：agent 修改的文件中出现在 ground-truth patch 中的比例 = |agent_files ∩ ground_truth_files| / |agent_files|

| Repo | Resolved Rate | Overall Precision | Average (per-case) Precision |
|------|:------------:|:-----------------:|:----------------------------:|
| ibex | 100.0% | 100.00% | 100.00% |
| cva6 | 100.0% | 100.00% | 100.00% |
| caliptra | 100.0% | 91.67% | 97.50% |
| rocketchip | 78.1% | 92.42% | 94.40% |
| xiangshan | 58.5% | 99.01% | 98.11% |

---

## Token 消耗统计

| Repo | Tasks | Prompt(K) | Comp(K) | Cache% | Calls | MCP | Repair Skill | Ordinary | Cost($) | Own-price($) |
|------|-------|-----------|---------|--------|-------|-----|--------------|----------|---------|--------------|
| ibex | 35 | 2312.9 | 11.4 | 96.7 | 44.5 | 0.0 | 1.2 | 43.3 | 0.030075 | 0.637003 |
| cva6 | 35 | 2651.9 | 11.9 | 97.2 | 48.7 | 0.0 | 1.5 | 47.2 | 0.029591 | 0.729055 |
| caliptra | 16 | 5548.0 | 36.3 | 98.4 | 58.2 | 0.0 | 1.5 | 56.7 | 0.054203 | 1.537882 |
| rocketchip | 32 | 3512.1 | 15.3 | 97.8 | 56.6 | 0.0 | 1.3 | 55.3 | 0.036150 | 0.965108 |
| xiangshan | 53 | 2359.0 | 14.0 | 95.7 | 45.7 | 0.0 | 1.7 | 44.0 | 0.035388 | 0.652373 |

注：
- 上表除 `Tasks` 外均为**每任务均值**。
- 全实验 API 总成本 **$6.0233**，own-price 估算总成本 **$138.530**。

---

## 与 Baseline V2 对比

| Repo | Baseline V2 | Repair V3 | 变化 |
|------|:-----------:|:---------:|:----:|
| ibex | 35/35 (100.0%) | 35/35 (100.0%) | 0.0 |
| cva6 | 35/35 (100.0%) | 35/35 (100.0%) | 0.0 |
| caliptra | 15/16 (93.8%) | 16/16 (100.0%) | +6.2 |
| rocketchip | 20/32 (62.5%) | 25/32 (78.1%) | +15.6 |
| xiangshan | 32/53 (60.4%) | 31/53 (58.5%) | -1.9 |
| **Total** | **137/171 (80.1%)** | **142/171 (83.0%)** | **+2.9** |

| Repo | Baseline V2 Precision | Repair V3 Precision |
|------|:---------------------:|:-------------------:|
| ibex | 98.15% | 100.00% |
| cva6 | 94.83% | 100.00% |
| caliptra | 93.33% | 91.67% |
| rocketchip | 94.52% | 92.42% |
| xiangshan | 93.64% | 99.01% |

---

## 核心发现

1. **改版 repair skill 是目前最好的一轮**：142/171 (83.0%)，高于 Baseline V2 (80.1%)，比 repair V2（71.8%）高约 11.2 个百分点。

2. **Verilog 三库全满**：ibex、cva6、caliptra 均 100%；caliptra 相比基线提升（15/16 → 16/16）。

3. **rocketchip 大幅改善**：25/32 (78.1%)，比基线高 15.6 个百分点，也远好于 repair V2 的 15/31。

4. **xiangshan 略降**：31/53 (58.5%) vs 基线 32/53 (60.4%)，是本轮唯一低于基线的项目。

5. **精度普遍很高**：ibex/cva6 100%、xiangshan 99.01%；caliptra 91.67% 最低。

6. **仅 1 个基础设施失败**：`xiangshan pr-5496` 构建耗时 1794s，超过 1800s 上限而超时；其余 28 个未解决均为补丁未通过。

7. **MCP 为 0**：repair skill 合计调用 247 次（约 1.44/任务），未使用 WAVES MCP。

---

## 数据来源与口径

- 原始包：`results-repair-v3.tar.gz`（含 `jobs/hwe-repair-v3-*` 与 `results/hwe-repair-v3-*`）
- `resolved/unresolved/empty_patch/error`：`results/hwe-repair-v3-<repo>/eval/final_report.json`
- File-Level Precision：`results-archive/analysis/compute_precision.py`
- Token / Calls：`results-archive/analysis/token_report.py`（`result.json` + `agent/trajectory.json`）
- Skill 分类：`repair` skill = `hdl-minimal-repair` + `repair`；MCP = `waves_wave_*`；其余为 Ordinary
- 评估容器通过 `--global_env` 注入 `HTTP_PROXY/HTTPS_PROXY` 以完成测试期联网步骤
- 本报告未修改 `results-archive/analysis/`；旧版报告保持原样。
