# File-Level Precision 分析

> Work In Progress, Not use!

计算 HWE-Bench 论文 Table 3 中的 **File-Level Precision** 指标。

## 指标定义

来自论文第 4.1 节 Metrics：

> **File-Level Precision** measures patch focus: the fraction of files modified by the agent that also appear in the ground-truth patch.

```
precision = |agent_files ∩ ground_truth_files| / |agent_files|
```

- agent_files：agent 生成的 patch 中修改的所有文件路径
- ground_truth_files：官方 PR 的 ground-truth patch 中修改的文件列表
- 反映 agent 的 fault localization 准确度，patch 越聚焦在真正需要修改的文件上，precision 越高

论文 Table 3 中的参考值：

| Model | Precision |
|-------|-----------|
| GPT-5.4 xhigh (Codex CLI) | 0.619 |
| Claude Opus 4.6 (Claude Code) | 0.928 |
| Claude Sonnet 4.6 (Claude Code) | 0.916 |
| GLM 5.1 (OpenHands) | 0.892 |
| Qwen3.6 Plus (OpenHands) | 0.878 |
| DeepSeek V3.2 (OpenHands) | 0.865 |
| Kimi K2.5 (Kimi CLI) | 0.859 |

## 数据来源

| 需要 | 来源 | 字段 | 说明 |
|------|------|------|------|
| agent 修改的文件列表 | `patches.jsonl` | `fix_patch` | 运行 `compute_precision.py` 自动解析 |
| ground-truth 修改的文件 | 数据集 JSONL | `modified_files` | s05 extract_patches 阶段写入 |

## 前置脚本

`compute_precision.py` 用于从 patches.jsonl + dataset JSONL 计算 File-Level Precision。

```bash
cd /path/to/hwe-bench/results-archive/analysis

# 单 repo
uv run python compute_precision.py \
  --patches results/hwe-ibex-full/patches/patches.jsonl \
  --dataset datasets/lowRISC__ibex.jsonl

# 按 repo 过滤（patches.jsonl 包含多个 repo 时）
uv run python compute_precision.py \
  --patches results/all-repos/patches/patches.jsonl \
  --dataset datasets/hwe_bench_full.jsonl \
  --repo ibex
```

## 输出示例

```
Total cases: 35
Overall File-Level Precision: 0.8254
Average (per-case) Precision:    0.8012

Per-case detail:
instance_id                                     match  total  precision
lowRISC/ibex:pr-45                                  3      4     0.7500
lowRISC/ibex:pr-48                                  2      2     1.0000
lowRISC/ibex:pr-54                                  5      7     0.7143
...
```

- **Overall Precision**：所有 case 的匹配文件数总和 / 所有 case 的 agent 修改文件数总和（论文 Table 3 用的是这个）
- **Average Precision**：每个 case 单独算 precision 后取平均

## 注意事项

1. 论文中的 HWE-Bench 代码库本身没有内置 File-Level Precision 计算，是论文作者外部统计的
2. ground-truth 的 `modified_files` 是 s05 阶段从 `fix_patch` + `test_patch` 的**全部文件**中提取的（即 PR 实际修改了的所有文件）
3. `compute_precision.py` 从 agent 的 `fix_patch` 中解析文件路径时，会自动去掉 `a/` / `b/` 前缀
4. 论文的 Overall 精度可能和你的结果有微小误差（浮点数/边缘 case 处理差异），但应该非常接近
