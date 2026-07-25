# Analysis Template

用这个模板分析每个 repo 的结果：修复率、未解决 case、bug 分类、官方对比，以及文件级修改精度。

## 前置脚本

### 1. analyze_repo.py — 解析基础数据

```bash
cd /path/to/hwe-bench/results-archive/analysis
python3 analyze_repo.py <repo_name> <tarball_path> <official_results_dir>
```

示例:
```bash
python3 analyze_repo.py rocketchip ../baseline/hwe-rocketchip-full.tar.gz ../../hwe-bench-artifacts/results/rocketchip/gpt5.4
```

该脚本会:
- 解压 tarball 并加载 final_report.json
- 列出所有未解决 case 的 PR 号和 test name
- 显示官方是否也未能解决
- 输出汇总统计 (都解了/官方独占/都没解)

### 2. compute_precision.py — 计算文件级修改精度

```bash
cd /path/to/hwe-bench
uv run python results-archive/analysis/compute_precision.py \
  --patches <extracted_dir>/patches/patches.jsonl \
  --dataset datasets/<repo>.jsonl
```

示例:
```bash
uv run python results-archive/analysis/compute_precision.py \
  --patches /tmp/batch/gpt5.4-ibex/results/hwe-ibex-full/patches/patches.jsonl \
  --dataset datasets/lowRISC__ibex.jsonl
```

该脚本会:
- 从 patches.jsonl 解析 agent 修改的所有文件路径
- 从 dataset JSONL 读取 ground-truth 的 modified_files
- 输出 Overall File-Level Precision（论文 Table 3 同口径）和 per-case 明细

#### 精度指标定义

```
precision = |agent_files ∩ ground_truth_files| / |agent_files|
```

- **agent_files**：agent 生成的 patch 中涉及的所有文件
- **ground_truth_files**：官方 PR 实际修改的文件列表（dataset JSONL 中的 `modified_files` 字段）
- **Overall Precision**：所有 case 的匹配文件数总和 / 所有 case 的 agent 修改文件数总和（论文 Table 3 的计算方式）

## 数据来源

| 数据 | 来源 |
|------|------|
| 官方 resolved/unresolved | `/home/username/hwe-bench-artifacts/results/{repo}/gpt5.4/eval/final_report.json` |
| 本地方 resolved/unresolved | tarball 解压后的 `eval/final_report.json` |
| agent 修改文件列表 | tarball 解压后的 `patches/patches.jsonl`（`compute_precision.py` 自动解析） |
| ground-truth 修改文件 | `datasets/{org}__{repo}.jsonl` 的 `modified_files` 字段 |
| 失败 case 的 fix.patch | `eval_workdir/{org}/{repo}/evals/pr-{N}/fix.patch` |
| 失败 case 的 report | `eval_workdir/{org}/{repo}/evals/pr-{N}/report.json` |
| 原始 PR 信息 | GitHub 上 `{org}/{repo}/pull/{N}` |

## 步骤

1. 解压 tarball，找到 `patches/patches.jsonl` 和 `eval/final_report.json`
2. 运行 `analyze_repo.py` 获取 resolved/unresolved 基础数据
3. 运行 `compute_precision.py` 获取文件级精度
4. 对于未解决的每个 PR，查阅 GitHub PR 描述，确定 bug 类别
5. 汇总分类统计
6. 按本模板格式写入对应 md 文件

## Bug 类别

```
logic           - 硬件逻辑错误（状态机、仲裁器、数据路径等）
interface       - 模块间接口/信号连接错误
timing/sync     - 时序/同步问题（流水线冲突、复位、跨时钟域等）
SW:HW Interact  - 软硬件交互问题
Spec            - 架构规范/协议合规性问题
Config/Integ    - 配置/集成问题
SW:HW Config    - 软硬件配置不匹配
SW:FW Logic     - 固件逻辑错误
```

## 输出格式

```markdown
# {Repo} Analysis

## 总体结果

```yaml
official:
  agent: Codex CLI
  model: gpt-5.4
  resolved: {N}
  total: {N}
  pct: {N}
  infra_errors: 0
  precision: {N}    # ← 新增: 官方 agent 的文件级精度

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: {N}
  total: {N}
  pct: {N}
  infra_errors: 0
  precision: {N}    # ← 新增: 我方 agent 的文件级精度
```

## 文件级精度明细

```yaml
precision_detail:
  official:
    overall: {N}            # Overall File-Level Precision（论文同口径）
    average_per_case: {N}   # 每个 case 的 precision 取平均
  opencode:
    overall: {N}
    average_per_case: {N}
  comparison:               # 精度对比
    official_higher_on: [list]    # 官方精度更高的 case
    opencode_higher_on: [list]    # 我方精度更高的 case
```

低精度 case 通常反映:
- 错误的 fault localization（改了不该改的模块）
- 过度修改相邻文件
- 调试过程遗留的中间产物（临时脚本、备份文件）

高精度低修复率说明 agent 找到了正确的文件但未给出正确的逻辑修改。

## 未解决 Case

```json
[
  {"pr": {N}, "test": "{test_name}", "type": "{category}", "desc": "{bug description}"}
]
```

## 按 Bug 类型统计

```yaml
bug_type_breakdown:
  logic: {N}
  interface: {N}
  timing_sync: {N}
  sw_hw_interact: {N}
  spec: {N}
  config_integ: {N}
  sw_hw_config: {N}
  sw_fw_logic: {N}
```

## 对比官方

```yaml
comparison_with_official:
  both_resolved:
    count: {N}
    prs: [list]
  official_only:
    count: {N}
    prs: [list]
  opencode_only:
    count: {N}
    prs: [list]
  neither:
    count: {N}
    prs: [list]
```

## 结论

{prose text summarizing findings}
```
