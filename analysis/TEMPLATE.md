# Analysis Template

用这个模板分析每个 repo 的失败补丁。

## 前置脚本

先运行 `analyze_repo.py` 获取未解决 case 列表和与官方的对比:

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

## 数据来源

- 官方结果: `/home/username/hwe-bench-artifacts/results/{repo}/gpt5.4/eval/final_report.json`
- OpenCode 结果: 从 `results-archive/baseline/` 对应 tarball 解压后找到 `eval/final_report.json`
- 失败 case 的 fix.patch: `eval_workdir/{org}/{repo}/evals/pr-{N}/fix.patch`
- 失败 case 的 report: `eval_workdir/{org}/{repo}/evals/pr-{N}/report.json`
- 原始 PR 信息: GitHub 上 `{org}/{repo}/pull/{N}`

## 步骤

1. 运行 `analyze_repo.py` 获取基础数据
2. 对于 OpenCode 未解决的每个 PR，查阅 GitHub PR 描述，确定 bug 类别
3. 汇总分类统计
4. 按 TEMPLATE 格式写入对应 md 文件

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

opencode:
  agent: OpenCode
  model: gpt-5.4
  resolved: {N}
  total: {N}
  pct: {N}
  infra_errors: 0
```

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
