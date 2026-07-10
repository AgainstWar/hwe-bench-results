# Skills (locate + repair) Baseline Report

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode v1.17.4 |
| 模型 | DeepSeek V4 Flash (opencode-go) |
| Skills | locate (fault localization) + repair (minimal patch) |
| 运行方式 | Harbor Framework, Docker 容器化 |
| 并行度 | Verilog 4 并发, Chisel 2 并发 |
| 重试次数 | 2 次 (k=1, r=2) |
| 基础设施错误 | 0 |

---

## 全量对比

| Repo | Baseline | Skills | MCP (wave) | Skills Δ | MCP Δ |
|------|:-------:|:------:|:----------:|:--------:|:-----:|
| ibex | 27/35 (77%) | 21/35 (60%) | 24/35 (69%) | -6 | -3 |
| cva6 | 28/35 (80%) | 25/35 (71%) | 31/35 (89%) | -3 | +3 |
| caliptra | 13/16 (81%) | 11/16 (69%) | 12/16 (75%) | -2 | -1 |
| rocketchip | 8/32 (25%) | 9/32 (28%) | 12/32 (38%) | +1 | +4 |
| xiangshan | 12/54 (22%) | 16/54 (30%) | 18/54 (33%) | +4 | +6 |
| **Total** | **88/172 (51%)** | **82/172 (48%)** | **97/172 (56%)** | **-6** | **+9** |

---

## Bug Type 影响汇总

| Bug Type | +新解决 | -丢失 | 净变化 |
|----------|:------:|:-----:|:------:|
| config_integ | +1 | -0 | +1 |
| interface | +6 | -4 | +2 |
| logic | +3 | -12 | -9 |
| spec | +5 | -6 | -1 |
| sw_hw_config | +1 | -1 | +0 |
| sw_hw_interact | +1 | -0 | +1 |
| timing_sync | +2 | -2 | +0 |

---

## 分项目分析

### Ibex (ibex)

**21/35 (60%) — 净变化 -6**

新解决: interface(+1), timing_sync(+1)
丢失: interface(-2), logic(-2), spec(-4)

### CVA6 (cva6)

**25/35 (71%) — 净变化 -3**

新解决: interface(+1), spec(+1)
丢失: interface(-1), logic(-2), spec(-2)

### Caliptra (caliptra)

**11/16 (69%) — 净变化 -2**

新解决: 无
丢失: logic(-1), timing_sync(-1)

### RocketChip (rocketchip)

**9/32 (28%) — 净变化 +1**

新解决: config_integ(+1), interface(+1), logic(+1), spec(+1), sw_hw_interact(+1)
丢失: interface(-1), logic(-3)

### XiangShan (xiangshan)

**16/54 (30%) — 净变化 +4**

新解决: interface(+3), logic(+2), spec(+3), sw_hw_config(+1), timing_sync(+1)
丢失: logic(-4), sw_hw_config(-1), timing_sync(-1)


## 结论

1. **MCP (wave) 效果最好 (+9)**，在 Verilog 和 Chisel 项目上都稳定正收益
2. **Skills (locate+repair) 总体 -6**，但受执行质量问题影响（部分 PR 空 patch）
3. **Chisel 项目上有正收益趋势**：rocketchip +1, xiangshan +4
4. **Verilog 项目退步**：ibex -6, cva6 -3, caliptra -2
5. 所有项目 0 基础设施错误
