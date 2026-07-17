# MCP + Locate Ablation Report

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode v1.17.4 |
| 模型 | DeepSeek V4 Flash (opencode-go) |
| MCP | WAVES (VCD/FST waveform analysis) |
| Skill | locate (fault localization) |
| 基础设施错误 | 0 |

## 全量对比

| Repo | Baseline | MCP alone | MCP + Locate | Δ vs Base | Δ vs MCP |
|------|:-------:|:---------:|:--------:|:---------:|:--------:|
| ibex | 27/35 (77%) | 24/35 (69%) | 19/35 (54%) | -8 | -5 |
| cva6 | 28/35 (80%) | 31/35 (89%) | 24/35 (69%) | -4 | -7 |
| caliptra | 13/16 (81%) | 12/16 (75%) | 8/16 (50%) | -5 | -4 |
| rocketchip | 8/32 (25%) | 12/32 (38%) | 7/32 (22%) | -1 | -5 |
| xiangshan | 12/54 (22%) | 18/54 (33%) | 8/54 (15%) | -4 | -10 |
| **Total** | **88/172 (51%)** | **97/172 (56%)** | **66/172 (38%)** | **-22** | **-31** |

## 分项目分析

### Ibex（ibex）
**结果：19/35（54%）**
vs Baseline: -8 | vs MCP alone: -5

**vs Baseline 新解决（+2）：**
- pr-155（logic）
- pr-1229（interface）

**vs Baseline 丢失（-10）：**
- pr-222（logic）
- pr-293（interface）
- pr-377（logic）
- pr-465（logic）
- pr-882（logic）
- pr-1135（config_integ）
- pr-1469（spec）
- pr-1584（spec）
- pr-1735（logic）
- pr-1865（interface）

**相对 MCP 新解决（+3）：**
- pr-155（logic）
- pr-1229（interface）
- pr-1816（spec）

**相对 MCP 丢失（-8）：**
- pr-222（logic）
- pr-377（logic）
- pr-465（logic）
- pr-882（logic）
- pr-974（timing_sync）
- pr-1141（interface）
- pr-1584（spec）
- pr-1735（logic）

**Bug Type 影响：**
- config_integ: +0/-1 = -1
- interface: +1/-2 = -1
- logic: +1/-5 = -4
- spec: +0/-2 = -2

### CVA6（cva6）
**结果：24/35（69%）**
vs Baseline: -4 | vs MCP alone: -7

**vs Baseline 新解决（+2）：**
- pr-2279（interface）
- pr-2989（spec）

**vs Baseline 丢失（-6）：**
- pr-2017（logic）
- pr-2282（logic）
- pr-2468（logic）
- pr-2916（interface）
- pr-2944（logic）
- pr-3168（logic）

**相对 MCP 丢失（-7）：**
- pr-2017（logic）
- pr-2282（logic）
- pr-2420（config_integ）
- pr-2468（logic）
- pr-2916（interface）
- pr-2944（logic）
- pr-3168（logic）

**Bug Type 影响：**
- interface: +1/-1 = +0
- logic: +0/-5 = -5
- spec: +1/-0 = +1

### Caliptra（caliptra）
**结果：8/16（50%）**
vs Baseline: -5 | vs MCP alone: -4

**vs Baseline 新解决（+1）：**
- pr-725（logic）

**vs Baseline 丢失（-6）：**
- pr-298（logic）
- pr-633（logic）
- pr-757（timing_sync）
- pr-786（logic）
- pr-1073（logic）
- pr-1089（logic）

**相对 MCP 新解决（+1）：**
- pr-725（logic）

**相对 MCP 丢失（-5）：**
- pr-298（logic）
- pr-757（timing_sync）
- pr-786（logic）
- pr-1073（logic）
- pr-1089（logic）

**Bug Type 影响：**
- logic: +1/-5 = -4
- timing_sync: +0/-1 = -1

### RocketChip（rocketchip）
**结果：7/32（22%）**
vs Baseline: -1 | vs MCP alone: -5

**vs Baseline 新解决（+3）：**
- pr-485（interface）
- pr-1878（spec）
- pr-3600（timing_sync）

**vs Baseline 丢失（-4）：**
- pr-576（logic）
- pr-1330（logic）
- pr-2984（logic）
- pr-3065（interface）

**相对 MCP 新解决（+2）：**
- pr-485（interface）
- pr-3600（timing_sync）

**相对 MCP 丢失（-7）：**
- pr-404（logic）
- pr-576（logic）
- pr-1093（sw_hw_interact）
- pr-1176（interface）
- pr-1330（logic）
- pr-2213（interface）
- pr-2984（logic）

**Bug Type 影响：**
- interface: +1/-1 = +0
- logic: +0/-3 = -3
- spec: +1/-0 = +1
- timing_sync: +1/-0 = +1

### XiangShan（xiangshan）
**结果：8/54（15%）**
vs Baseline: -4 | vs MCP alone: -10

**vs Baseline 新解决（+4）：**
- pr-1679（interface）
- pr-2513（logic）
- pr-3717（spec）
- pr-5080（logic）

**vs Baseline 丢失（-8）：**
- pr-39（logic）
- pr-2483（logic）
- pr-2845（timing_sync）
- pr-3182（logic）
- pr-3867（logic）
- pr-4337（logic）
- pr-4943（sw_hw_config）
- pr-4959（logic）

**相对 MCP 新解决（+2）：**
- pr-5080（logic）
- pr-5700（logic）

**相对 MCP 丢失（-12）：**
- pr-39（logic）
- pr-739（timing_sync）
- pr-1820（sw_hw_config）
- pr-2351（interface）
- pr-2781（interface）
- pr-2845（timing_sync）
- pr-2997（logic）
- pr-3182（logic）
- pr-3555（spec）
- pr-4337（logic）
- pr-4959（logic）
- pr-5182（logic）

**Bug Type 影响：**
- interface: +1/-0 = +1
- logic: +2/-6 = -4
- spec: +1/-0 = +1
- sw_hw_config: +0/-1 = -1
- timing_sync: +0/-1 = -1

## 综合分析

MCP + Locate 组合在所有项目上全面退步，总净 -22。Locate skill 让 agent 在故障定位上花费大量时间，即使有 WAVES MCP 辅助也无法弥补。Locate 单独测试中净 -64 已表明该 skill 对 agent 有严重干扰作用，加入 MCP 后仍无法挽救。建议放弃。

## Bug Type 影响汇总

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +0 | -1 | -1 |
| interface | +4 | -4 | +0 |
| logic | +4 | -24 | -20 |
| spec | +3 | -2 | +1 |
| sw_hw_config | +0 | -1 | -1 |
| timing_sync | +1 | -2 | -1 |

## 结论

MCP + Locate 在所有 5 个项目上全面退步，总净 -22。Locate skill 指导 agent 进行故障定位，但实际效果是让 agent 花费大量时间在定位流程上，反而减少了实际修复代码的时间。即便配合 WAVES MCP 的波形分析能力，也无法补偿 locate 带来的干扰。
