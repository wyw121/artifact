# 评估口径声明（JPetStore）

为确保与论文《Microservice Decomposition Techniques: An Independent Tool Comparison (ASE 2024)》一致，现明确本仓库评估口径：

## Ground Truth 来源
- 使用路径：`artifact/case_studies/data/reference_decomposition/jpetstore_classes.csv`
- 计分依据：以该 CSV 中的服务归属为唯一标准。

## 计分范围与规则
- 粒度：类级（Class-level）
- 服务数：固定为 3（account / catalog / order）
- 指标：
  - MoJoFM：与 Ground Truth 的一致性，相同类集合和服务命名视为一致。
  - TurboMQ：基于结构依赖图（`metrics/scripts/data/relationship_graphs/**/structural_static.csv`）计算的模块化质量。缺少依赖图时可用估算值并标注。

## 特殊类处理
- CartActionBean：
  - Ground Truth 口径：catalog
  - 说明：若 AI 方案将其归入 order，评估时仍以 GT 为准计分。
- AbstractActionBean：
  - Ground Truth 口径：可视作 duplicate（常见处理为计入某一服务以满足完备性）。
  - 本项目默认：按主要使用者原则计入 order 服务（用于形成完备的 3 分组）。

## 文件与回填
- 三轮指标文件：`迭代数据/迭代X_*/roundX_metrics.csv`
  - 建议使用 `metrics/scripts/main.py` 精算后回填，去除“估算”字样。
- 三轮对比文件：`round1_comparison.md`、`round2_vs_round1.md`、`round3_vs_round2.md`
  - 对比表以 `jpetstore_classes.csv` 为权威来源。

## 可复现命令（PowerShell）
```powershell
python metrics/scripts/unzip_data.py
python metrics/scripts/generate_metadata.py
python metrics/scripts/create_dirs.py
python metrics/scripts/main.py
```

> 注：若需生成图表，请运行 `metrics/scripts/analyze_results.py` 或 `metrics/scripts/generate_figures.py`，输出位于 `results/figures/`。
