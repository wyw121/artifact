# 项目总览与复现实验核查指南

本仓库用于复现与验证 ASE 2024 论文 “Microservice Decomposition Techniques: An Independent Tool Comparison” 在 JPetStore 等应用上的微服务拆分评估，并对 AI（GitHub Copilot）三轮迭代拆分进行对比分析与度量。

- 论文指标与工具：MoJoFM（与 Ground Truth 一致性）、TurboMQ（模块化质量）；对标工具包含 Log2MS、MOSAIC、Mono2Micro、HyDec 等。
- 复现实验对象：JPetStore（24 类、302 方法）为主；同时保留 Spring-PetClinic、PartsUnlimitedMRP、7ep-demo 的工具评估产物。

---

## 项目结构全览（Tree）

```text
artifact/
├─ README.md
├─ docs/
│  ├─ AI微服务拆分方案书.md
│  ├─ EVALUATION_POLICY.md
│  ├─ COMPLIANCE_CHECKLIST.md
│  ├─ AI复现研究报告.md
│  └─ REPRODUCTION_REPORT.md
├─ 迭代数据/
│  ├─ README.md
│  ├─ calculate_metrics.py
│  ├─ full_verification.py
│  ├─ verify_ground_truth.py
│  ├─ 指标评估报告.md, 数据复核与错误修正报告.md, 修正完成确认清单.md
│  ├─ 迭代1_基础拆分/
│  │  ├─ prompt_used.txt, prompt_v1.0.txt
│  │  ├─ decomposition_result.json, round1_decomposition.json
│  │  ├─ evaluation_metrics.csv, round1_metrics.csv
│  │  └─ analysis.md, round1_comparison.md, round1_diagnosis.md, copilot_interaction.md
│  ├─ 迭代2_依赖驱动/
│  │  ├─ prompt_used.txt, prompt_v2.0.txt
│  │  ├─ decomposition_result.json, round2_decomposition.json
│  │  ├─ evaluation_metrics.csv, round2_metrics.csv
│  │  └─ analysis.md, round2_vs_round1.md, round2_diagnosis.md, copilot_interaction.md
│  └─ 迭代3_专家优化/
│     ├─ prompt_used.txt, prompt_v3.0.txt
│     ├─ decomposition_result.json, round3_decomposition.json
│     ├─ evaluation_metrics.csv, round3_metrics.csv
│     └─ analysis.md, round3_vs_round2.md, final_summary.md, copilot_interaction.md
├─ artifact/
│  ├─ metrics/
│  │  └─ scripts/
│  │     ├─ main.py, generate_metadata.py, unzip_data.py, create_dirs.py, create_vis_output_dirs.py
│  │     └─ models/, utils/, calculator/, cleaning/, casestudies/, resources/, access/, data/ 等
│  ├─ case_studies/
│  │  └─ data/reference_decomposition/
│  │     ├─ jpetstore_classes.csv, jpetstore_methods.csv
│  │     ├─ spring-petclinic_classes.csv, spring-petclinic_methods.csv
│  │     ├─ partsunlimited_classes.csv, partsunlimited_methods.csv
│  │     └─ 其他
│  ├─ guidelines/
│  └─ results/
│     ├─ data/tool_metrics_results/
│     │  ├─ metrics.csv, mojofm.csv, statistics.csv, entropy.csv
│     │  └─ tool_qualitative_results/, tool_raw_results/
│     └─ figures/
└─ data/
  └─ decomposition_visualizations/
    ├─ 1_jpetstore/
    ├─ 2_spring-petclinic/
    ├─ 3_partsunlimited/
    └─ 4_demo/
```

## 仓库结构（关键路径）

- 文档与口径
  - [docs/AI微服务拆分方案书.md](docs/AI微服务拆分方案书.md)：复现的权威执行方案书
  - [docs/EVALUATION_POLICY.md](docs/EVALUATION_POLICY.md)：评估口径与 Ground Truth 声明
  - [docs/COMPLIANCE_CHECKLIST.md](docs/COMPLIANCE_CHECKLIST.md)：方案书合规检查清单
  - [docs/AI复现研究报告.md](docs/AI复现研究报告.md)、[docs/REPRODUCTION_REPORT.md](docs/REPRODUCTION_REPORT.md)
- 三轮迭代产物（JPetStore）
  - [迭代数据/迭代1_基础拆分](迭代数据/迭代1_基础拆分)
  - [迭代数据/迭代2_依赖驱动](迭代数据/迭代2_依赖驱动)
  - [迭代数据/迭代3_专家优化](迭代数据/迭代3_专家优化)
- 指标产物与可视化（工具评估管线）
  - [artifact/results/data/tool_metrics_results/metrics.csv](artifact/results/data/tool_metrics_results/metrics.csv)
  - [artifact/results/data/tool_metrics_results/mojofm.csv](artifact/results/data/tool_metrics_results/mojofm.csv)
  - [data/decomposition_visualizations](data/decomposition_visualizations)
- 工具与脚本
  - [artifact/metrics/scripts](artifact/metrics/scripts)：主评估管线脚本 `main.py` 等
  - [迭代数据/calculate_metrics.py](迭代数据/calculate_metrics.py)：对三轮 AI 拆分计算 MoJoFM 与服务级指标
  - Ground Truth： [artifact/case_studies/data/reference_decomposition/jpetstore_classes.csv](artifact/case_studies/data/reference_decomposition/jpetstore_classes.csv)

---

## 复现方案与执行步骤（概述）

- 方案书执行（三轮迭代）
  - 迭代1：基础拆分；产物标准化（prompt、decomposition、metrics、对比/诊断模板）
  - 迭代2：依赖驱动；引入共享层（`AbstractActionBean`）补齐覆盖；对比与指标提升
  - 迭代3：专家优化；命名与边界稳定；`AbstractActionBean` 固化到 `order`
- 评估管线（工具产物）
  - 运行 [artifact/metrics/scripts/main.py](artifact/metrics/scripts/main.py)：清洗工具分解、构建/过滤分解、生成可视化、计算 TurboMQ/MoJoFM（工具维度）
  - 输出到 [artifact/results/data/tool_metrics_results](artifact/results/data/tool_metrics_results) 与 [data/decomposition_visualizations](data/decomposition_visualizations)
- 回填与口径声明
  - 通过 [迭代数据/calculate_metrics.py](迭代数据/calculate_metrics.py) 对三轮 AI 拆分计算 MoJoFM 和服务级 P/R/F1，回填 `roundX_metrics.csv`
  - 评估口径与特殊类处理详见 [docs/EVALUATION_POLICY.md](docs/EVALUATION_POLICY.md)

---

## 一键核查（老师检查用）

- 核查文件是否齐备（Windows PowerShell）：

```powershell
# 检查三轮标准产物是否存在
Get-ChildItem -Path "迭代数据/迭代1_基础拆分" | Select-Object Name
Get-ChildItem -Path "迭代数据/迭代2_依赖驱动" | Select-Object Name
Get-ChildItem -Path "迭代数据/迭代3_专家优化" | Select-Object Name

# 查看评估管线产物
Get-ChildItem -Path "artifact/results/data/tool_metrics_results" | Select-Object Name
Get-ChildItem -Path "data/decomposition_visualizations" | Select-Object Name
```

- 复现实验重跑（可选）：

```powershell
# 1) 运行工具评估主流程（产生工具对标的 TurboMQ/MoJoFM 与可视化）
Push-Location "artifact/metrics/scripts"
python main.py
Pop-Location

# 2) 计算三轮 AI 拆分的 MoJoFM 与服务级指标（并在控制台输出对比）
Push-Location "迭代数据"
python calculate_metrics.py
Pop-Location
```

- 快速定位报告与口径：
  - 方案书：[docs/AI微服务拆分方案书.md](docs/AI微服务拆分方案书.md)
  - 合规清单：[docs/COMPLIANCE_CHECKLIST.md](docs/COMPLIANCE_CHECKLIST.md)
  - 评估口径：[docs/EVALUATION_POLICY.md](docs/EVALUATION_POLICY.md)
  - 最终总结：[迭代数据/迭代3_专家优化/final_summary.md](迭代数据/迭代3_专家优化/final_summary.md)

---

## 复现产物清单（JPetStore）

- 迭代1：
  - 提示词：prompt_v1.0.txt
  - 结果与指标：round1_decomposition.json、round1_metrics.csv
  - 报告：round1_comparison.md、round1_diagnosis.md、copilot_interaction.md
- 迭代2：
  - 提示词：prompt_v2.0.txt
  - 结果与指标：round2_decomposition.json、round2_metrics.csv
  - 报告：round2_vs_round1.md、round2_diagnosis.md、copilot_interaction.md
- 迭代3：
  - 提示词：prompt_v3.0.txt
  - 结果与指标：round3_decomposition.json、round3_metrics.csv
  - 报告：round3_vs_round2.md、final_summary.md、copilot_interaction.md

---

## 结论与关键发现（本次复现）

- 结论摘要
  - 第3轮 AI 拆分 **MoJoFM = 95.83%**（23/24 类正确），位列论文工具第二，仅次于 Log2MS（100%），高于 MOSAIC（89.47%）。
  - 主要差异来源：`CartActionBean` 的归属（AI=order，GT=catalog），按 GT 计分时形成 4.17pp 的差距。
  - `AbstractActionBean` 的处理：迭代2采用共享层以补齐覆盖；迭代3按“主要使用者”原则计入 `order`，恢复 account/catalog 的精确率。
- 证据与产物
  - 工具 MoJoFM/TurboMQ：见 [artifact/results/data/tool_metrics_results](artifact/results/data/tool_metrics_results)
  - 三轮 AI 拆分指标与对比：见各轮 `roundX_metrics.csv` 与 `roundX_*` 对比文档
  - Ground Truth 来源：见 [artifact/case_studies/data/reference_decomposition/jpetstore_classes.csv](artifact/case_studies/data/reference_decomposition/jpetstore_classes.csv)

---

## 说明与注意事项

- TurboMQ 值：三轮 AI 拆分目前为估算区间（55-95），若需精算，需要将自定义拆分接入 `metrics/scripts` 数据源并生成依赖图（可新增工具名如 `copilot_llm` 再跑主流程）。
- 文档归档：根目录的 Markdown 已统一归档至 [docs](docs)，以该目录为唯一来源。
- 环境：Windows + Python 3.12（建议），如需虚拟环境可自建并安装 `pandas, scipy, nltk, networkx`。

---

## 版本控制与推送

- 当前分支：`master`，已领先远端若干提交。需要时可执行：

```powershell
git push origin master
```

---

## 致谢与引用

- 论文：Microservice Decomposition Techniques: An Independent Tool Comparison (ASE 2024)
- 数据与脚本：本仓库 `artifact/metrics/scripts` 及 `case_studies` 数据集
