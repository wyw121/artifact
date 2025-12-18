# 三轮迭代最终总结

评估口径：见 [docs/EVALUATION_POLICY.md](docs/EVALUATION_POLICY.md)；GT 源于 [artifact/case_studies/data/reference_decomposition/jpetstore_classes.csv](artifact/case_studies/data/reference_decomposition/jpetstore_classes.csv)

## 结果总览

| 轮次 | MoJoFM | TurboMQ（估算） | 关键变化 | 主要差异 |
|---|---:|---:|---|---|
| 迭代1 | 91.67% | 75-85 | 初版拆分完成 | `CartActionBean` 误分到 order；`AbstractActionBean` 未分配 |
| 迭代2 | 95.83% | 85-95 | 引入共享层补齐覆盖 | `CartActionBean` 仍为 order（与GT不符） |
| 迭代3 | 95.83% | 85-95 | 将 `AbstractActionBean` 固化到 order，命名边界稳定 | `CartActionBean` 仍与GT不符 |

最佳成绩：MoJoFM 95.83%（迭代2/3），TurboMQ 估算 85-95。

## 对标 ASE 2024 工具（MoJoFM）

- Log2MS：100.00%
- MOSAIC：89.47%
- Data-Centric：76.19%
- HyDec：57.14%

本复现（第3轮）：95.83%（位列 Log2MS 之后，高于 MOSAIC）。

## 关键分歧与口径说明
- `CartActionBean`：AI 按业务完整性倾向归入 order；GT 规定为 catalog。评估计分严格使用 GT。
- `AbstractActionBean`：最终计入 order（“主要使用者”原则）。若采用“duplicate”工具口径，可在评估时按重复类处理。

## 产物索引
- 迭代拆分与指标：
	- [迭代1](迭代数据/迭代1_基础拆分) · [对比报告](迭代数据/迭代1_基础拆分/round1_comparison.md) · [指标](迭代数据/迭代1_基础拆分/round1_metrics.csv)
	- [迭代2](迭代数据/迭代2_依赖驱动) · [对比报告](迭代数据/迭代2_依赖驱动/round2_vs_round1.md) · [指标](迭代数据/迭代2_依赖驱动/round2_metrics.csv)
	- [迭代3](迭代数据/迭代3_专家优化) · [对比报告](迭代数据/迭代3_专家优化/round3_vs_round2.md) · [指标](迭代数据/迭代3_专家优化/round3_metrics.csv)
- 评估管线产物：
	- 指标汇总： [artifact/results/data/tool_metrics_results/metrics.csv](artifact/results/data/tool_metrics_results/metrics.csv)
	- MoJoFM明细： [artifact/results/data/tool_metrics_results/mojofm.csv](artifact/results/data/tool_metrics_results/mojofm.csv)
	- 可视化： [data/decomposition_visualizations](data/decomposition_visualizations)

## 后续可选工作
- 精算 TurboMQ：将“自定义 LLM 拆分”接入 metrics/scripts 数据源（新增工具名，如 `copilot_llm`），生成依赖图与标准化分解文件后重跑主流程
- 生成对比图表到 [artifact/results/figures](artifact/results/figures) 并在各轮报告内嵌引用
- 若以GT计分并追求上限，可将 `CartActionBean` 调整至 `catalog` 以冲击 100% MoJoFM
