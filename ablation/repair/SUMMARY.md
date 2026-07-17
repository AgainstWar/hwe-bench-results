# MCP + Repair Ablation Report

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode v1.17.4 |
| 模型 | DeepSeek V4 Flash (opencode-go) |
| MCP | WAVES (VCD/FST waveform analysis) |
| Skill | repair (minimal patch) |
| 基础设施错误 | 0 |

## 全量对比

| Repo | Baseline | MCP alone | MCP + Repair | Δ vs Base | Δ vs MCP |
|------|:-------:|:---------:|:--------:|:---------:|:--------:|
| ibex | 27/35 (77%) | 24/35 (69%) | 23/35 (66%) | -4 | -1 |
| cva6 | 28/35 (80%) | 31/35 (89%) | 30/35 (86%) | +2 | -1 |
| caliptra | 13/16 (81%) | 12/16 (75%) | 11/16 (69%) | -2 | -1 |
| rocketchip | 8/32 (25%) | 12/32 (38%) | 12/32 (38%) | +4 | +0 |
| xiangshan | 12/54 (22%) | 18/54 (33%) | 23/54 (43%) | +11 | +5 |
| **Total** | **88/172 (51%)** | **97/172 (56%)** | **99/172 (58%)** | **+11** | **+2** |

## 分项目分析

### Ibex（ibex）
**结果：23/35（66%）**
vs Baseline: -4 | vs MCP alone: -1

**vs Baseline 新解决（+3）：**
- pr-475（spec）
- pr-974（timing_sync）
- pr-1141（interface）

**vs Baseline 丢失（-7）：**
- pr-176（logic）
- pr-293（interface）
- pr-332（spec）
- pr-882（logic）
- pr-1135（config_integ）
- pr-1469（spec）
- pr-1584（spec）

**相对 MCP 新解决（+3）：**
- pr-475（spec）
- pr-1816（spec）
- pr-1865（interface）

**相对 MCP 丢失（-4）：**
- pr-176（logic）
- pr-332（spec）
- pr-882（logic）
- pr-1584（spec）

**Bug Type 影响：**
- config_integ: +0/-1 = -1
- interface: +1/-1 = +0
- logic: +0/-2 = -2
- spec: +1/-3 = -2
- timing_sync: +1/-0 = +1

### CVA6（cva6）
**结果：30/35（86%）**
vs Baseline: +2 | vs MCP alone: -1

**vs Baseline 新解决（+3）：**
- pr-2279（interface）
- pr-2420（config_integ）
- pr-2989（spec）

**vs Baseline 丢失（-1）：**
- pr-2032（logic）

**相对 MCP 丢失（-1）：**
- pr-2032（logic）

**Bug Type 影响：**
- config_integ: +1/-0 = +1
- interface: +1/-0 = +1
- logic: +0/-1 = -1
- spec: +1/-0 = +1

### Caliptra（caliptra）
**结果：11/16（69%）**
vs Baseline: -2 | vs MCP alone: -1


**vs Baseline 丢失（-2）：**
- pr-594（logic）
- pr-633（logic）

**相对 MCP 丢失（-1）：**
- pr-594（logic）

**Bug Type 影响：**
- logic: +0/-2 = -2

### RocketChip（rocketchip）
**结果：12/32（38%）**
vs Baseline: +4 | vs MCP alone: +0

**vs Baseline 新解决（+6）：**
- pr-177（logic）
- pr-404（logic）
- pr-1878（spec）
- pr-2213（interface）
- pr-2368（config_integ）
- pr-2621（config_integ）

**vs Baseline 丢失（-2）：**
- pr-576（logic）
- pr-1069（logic）

**相对 MCP 新解决（+4）：**
- pr-177（logic）
- pr-2368（config_integ）
- pr-2621（config_integ）
- pr-3065（interface）

**相对 MCP 丢失（-4）：**
- pr-576（logic）
- pr-1069（logic）
- pr-1093（sw_hw_interact）
- pr-1176（interface）

**Bug Type 影响：**
- config_integ: +2/-0 = +2
- interface: +1/-0 = +1
- logic: +2/-2 = +0
- spec: +1/-0 = +1

### XiangShan（xiangshan）
**结果：23/54（43%）**
vs Baseline: +11 | vs MCP alone: +5

**vs Baseline 新解决（+15）：**
- pr-739（timing_sync）
- pr-1323（spec）
- pr-1679（interface）
- pr-1820（sw_hw_config）
- pr-2095（logic）
- pr-2513（logic）
- pr-2997（logic）
- pr-3329（interface）
- pr-3555（spec）
- pr-3717（spec）
- pr-3859（spec）
- pr-3955（interface）
- pr-4968（timing_sync）
- pr-5080（logic）
- pr-5593（interface）

**vs Baseline 丢失（-4）：**
- pr-1931（logic）
- pr-2483（logic）
- pr-4943（sw_hw_config）
- pr-5700（logic）

**相对 MCP 新解决（+9）：**
- pr-1323（spec）
- pr-2095（logic）
- pr-3329（interface）
- pr-3859（spec）
- pr-3867（logic）
- pr-3955（interface）
- pr-4968（timing_sync）
- pr-5080（logic）
- pr-5593（interface）

**相对 MCP 丢失（-4）：**
- pr-1931（logic）
- pr-2351（interface）
- pr-2781（interface）
- pr-5182（logic）

**Bug Type 影响：**
- interface: +4/-0 = +4
- logic: +4/-3 = +1
- spec: +4/-0 = +4
- sw_hw_config: +1/-1 = +0
- timing_sync: +2/-0 = +2

## 综合分析

MCP + Repair 组合总体 +11，略高于 MCP 单独的 +9。主要正收益来自 Chisel 项目（xiangshan +11, rocketchip +4），Verilog 项目上轻微退步。Repair skill 的结构化修复指导在复杂 Chisel 项目上有效，但与 MCP 叠加增益有限。

## Bug Type 影响汇总

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +3 | -1 | +2 |
| interface | +7 | -1 | +6 |
| logic | +6 | -10 | -4 |
| spec | +7 | -3 | +4 |
| sw_hw_config | +1 | -1 | +0 |
| timing_sync | +3 | -0 | +3 |

## 结论

MCP + Repair 总体 +11，比 MCP 单独的 +9 略有提升。主要正收益来自 Chisel 项目（xiangshan +11, rocketchip +4），说明 Repair skill 的结构化修复指导对复杂项目有帮助。Verilog 项目上轻微退步（ibex -4, cva6 -2, caliptra -2），显示 skill 对简单项目有干扰。

MCP + Repair 在 Chisel 项目上表现较好（xiangshan +11, rocketchip +4），Verilog 项目上有轻微退步（ibex -1, caliptra -1, cva6 -1）。
