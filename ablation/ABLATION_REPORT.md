# MCP + Skill Ablation Report

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode v1.17.4 |
| 模型 | DeepSeek V4 Flash (opencode-go) |
| MCP | WAVES (VCD/FST waveform analysis) |
| Skill locate | Fault localization workflow |
| Skill repair | Minimal patch repair workflow |
| 并行度 | Verilog 4 并发, Chisel 2 并发 |
| 重试次数 | 2 次 (k=1, r=2) |
| 基础设施错误 | 0 |

---
## 全量对比

注：Baseline 为无 MCP、无 Skill 的纯净 DeepSeek V4 Flash 基线。MCP alone 为仅启用 WAVES MCP 的配置。

| Repo | Baseline | MCP alone | MCP+Locate | MCP+Repair |
|------|:-------:|:---------:|:----------:|:----------:|
| ibex | 27/35 (77%) | 24/35 (69%) | 19/35 (54%) | 23/35 (66%) |
| cva6 | 28/35 (80%) | 31/35 (89%) | 24/35 (69%) | 30/35 (86%) |
| caliptra | 13/16 (81%) | 12/16 (75%) | 8/16 (50%) | 11/16 (69%) |
| rocketchip | 8/32 (25%) | 12/32 (38%) | 7/32 (22%) | 12/32 (38%) |
| xiangshan | 12/54 (22%) | 18/54 (33%) | 8/54 (15%) | 23/54 (43%) |
| **Total** | **88/172 (51%)** | **97/172 (56%)** | **66/172 (38%)** | **99/172 (58%)** |

---
## MCP + Locate

Locate skill 指导 agent 进行故障定位。以下为该配置的测试结果。

| Repo | Baseline | MCP+Locate | Δ vs Base | Δ vs MCP |
|------|:-------:|:----------:|:---------:|:--------:|
| ibex | 27/35 (77%) | 19/35 (54%) | -8 | -5 |
| cva6 | 28/35 (80%) | 24/35 (69%) | -4 | -7 |
| caliptra | 13/16 (81%) | 8/16 (50%) | -5 | -4 |
| rocketchip | 8/32 (25%) | 7/32 (22%) | -1 | -5 |
| xiangshan | 12/54 (22%) | 8/54 (15%) | -4 | -10 |

### MCP + Locate 各项目详情

#### Ibex（ibex）
19/35（54%）| vs Baseline: -8 | vs MCP alone: -5

vs Baseline 新解决: [155, 1229]
vs Baseline 丢失: [222, 293, 377, 465, 882, 1135, 1469, 1584, 1735, 1865]

#### CVA6（cva6）
24/35（69%）| vs Baseline: -4 | vs MCP alone: -7

vs Baseline 新解决: [2279, 2989]
vs Baseline 丢失: [2017, 2282, 2468, 2916, 2944, 3168]

#### Caliptra（caliptra）
8/16（50%）| vs Baseline: -5 | vs MCP alone: -4

vs Baseline 新解决: [725]
vs Baseline 丢失: [298, 633, 757, 786, 1073, 1089]

#### RocketChip（rocketchip）
7/32（22%）| vs Baseline: -1 | vs MCP alone: -5

vs Baseline 新解决: [485, 1878, 3600]
vs Baseline 丢失: [576, 1330, 2984, 3065]

#### XiangShan（xiangshan）
8/54（15%）| vs Baseline: -4 | vs MCP alone: -10

vs Baseline 新解决: [1679, 2513, 3717, 5080]
vs Baseline 丢失: [39, 2483, 2845, 3182, 3867, 4337, 4943, 4959]

---
## MCP + Repair

Repair skill 指导 agent 进行最小化补丁修复。以下为该配置的测试结果。

| Repo | Baseline | MCP+Repair | Δ vs Base | Δ vs MCP |
|------|:-------:|:----------:|:---------:|:--------:|
| ibex | 27/35 (77%) | 23/35 (66%) | -4 | -1 |
| cva6 | 28/35 (80%) | 30/35 (86%) | +2 | -1 |
| caliptra | 13/16 (81%) | 11/16 (69%) | -2 | -1 |
| rocketchip | 8/32 (25%) | 12/32 (38%) | +4 | +0 |
| xiangshan | 12/54 (22%) | 23/54 (43%) | +11 | +5 |

### MCP + Repair 各项目详情

#### Ibex（ibex）
23/35（66%）| vs Baseline: -4 | vs MCP alone: -1

vs Baseline 新解决: [475, 974, 1141]
vs Baseline 丢失: [176, 293, 332, 882, 1135, 1469, 1584]

#### CVA6（cva6）
30/35（86%）| vs Baseline: +2 | vs MCP alone: -1

vs Baseline 新解决: [2279, 2420, 2989]
vs Baseline 丢失: [2032]

#### Caliptra（caliptra）
11/16（69%）| vs Baseline: -2 | vs MCP alone: -1

vs Baseline 丢失: [594, 633]

#### RocketChip（rocketchip）
12/32（38%）| vs Baseline: +4 | vs MCP alone: +0

vs Baseline 新解决: [177, 404, 1878, 2213, 2368, 2621]
vs Baseline 丢失: [576, 1069]

#### XiangShan（xiangshan）
23/54（43%）| vs Baseline: +11 | vs MCP alone: +5

vs Baseline 新解决: [739, 1323, 1679, 1820, 2095, 2513, 2997, 3329, 3555, 3717, 3859, 3955, 4968, 5080, 5593]
vs Baseline 丢失: [1931, 2483, 4943, 5700]

---

---
## MCP + All (locate + repair)
MCP + All 同时启用 WAVES MCP、locate skill 和 repair skill。
| Repo | Baseline | MCP alone | MCP + All | Δ Base | Δ MCP ||------|:-------:|:---------:|:--------:|:------:|:-----:|| ibex | 27/35 (77%) | 24/35 (69%) | 23/35 (66%) | -4 | -1 || cva6 | 28/35 (80%) | 31/35 (89%) | 27/35 (77%) | -1 | -4 || caliptra | 13/16 (81%) | 12/16 (75%) | 8/16 (50%) | -5 | -4 || rocketchip | 8/32 (25%) | 12/32 (38%) | 6/32 (19%) | -2 | -6 || xiangshan | 12/54 (22%) | 18/54 (33%) | 25/54 (46%) | +13 | +7 || **Total** | **88/172 (51%)** | **97/172 (56%)** | **89/172 (52%)** | **+1** | **-8** |
共 26 个空 patch，三个功能同时启用超出 agent 处理能力。xiangshan（+13）表现最佳，其他项目退步。详细数据见 all/ 目录。


## 结论

### MCP + Locate

MCP + Locate 在所有 5 个项目上全面退步，总净 -22。Locate skill 指导 agent 进行故障定位，但在实际使用中 agent 在定位流程上花费了大量时间，减少了实际修复代码的时间。即使有 WAVES MCP 的波形分析能力辅助，也无法弥补 locate 带来的干扰。

### MCP + Repair

MCP + Repair 总体 +11，在 Chisel 项目上效果较好（xiangshan +11, rocketchip +4），Verilog 项目上有轻微退步（ibex -1, cva6 -1, caliptra -1）。Repair skill 的结构化修复指导在复杂项目上有一定帮助，但在简单项目上有轻微干扰。

### MCP + All (locate + repair)

MCP + All 总体 +1，相比 Baseline 几乎没有提升。三个功能同时启用产生了大量空 patch（26 个），超出了 agent 的处理能力。唯一例外是 xiangshan（+13），在复杂项目上 locate、repair 和 MCP 产生了协同效应。其他 4 个项目均退步，建议不采用此配置。

各配置的详细数据见对应子目录下的 SUMMARY.md 和 per-repo 分析文件。
