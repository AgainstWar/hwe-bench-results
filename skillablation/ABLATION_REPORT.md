# Skills Ablation Study

## 实验配置

| 项目 | 详情 |
|------|------|
| Agent | OpenCode v1.17.4 |
| 模型 | DeepSeek V4 Flash (opencode-go) |
| Skill | locate (fault localization) vs repair (minimal patch) |
| 运行方式 | Harbor Framework, Docker 容器化 |
| 基础设施错误 | 0 |

---

## 全量对比

| Repo | Baseline | Locate | Repair | L Δ | R Δ |
|------|:-------:|:------:|:------:|:---:|:---:|
| ibex | 27/35 (77%) | 7/35 (20%) | 25/35 (71%) | -20 | -2 |
| cva6 | 28/35 (80%) | 11/35 (31%) | 31/35 (89%) | -17 | +3 |
| caliptra | 13/16 (81%) | 3/16 (19%) | 13/16 (81%) | -10 | +0 |
| rocketchip | 8/32 (25%) | 2/32 (6%) | 13/32 (41%) | -6 | +5 |
| xiangshan | 12/54 (22%) | 1/54 (2%) | 19/54 (35%) | -11 | +7 |

| **Total** | **88/172 (51%)** | **24/172 (14%)** | **101/172 (59%)** | **-64** | **+13** |

---

## 结论

1. **Locate 单独：净 -64** — 定位 skill 严重干扰 agent，所有项目大幅退步
2. **Repair 单独：净 +13** — 修复 skill 效果显著，在 4/5 项目上正收益
3. **Locate 单独比 Both（-6）还差** — 说明 locate 是拖后腿的，有它不如没它
4. **Repair 单独比 Both 好** — 两个 skill 同时启用会互相干扰
5. **下一步：只保留 repair skill，删除 locate skill 或将两者合并**
