# 方案书合规执行清单（JPetStore 微服务拆分）

本清单对照《AI微服务拆分方案书.md》要求，检查三轮迭代的产物是否齐备，并标注本次修补/新增内容。若标注为“占位/模板”，需后续补充内容或由脚本计算后回填。

---

## 总览
- 复现实例：JPetStore（24类，3个微服务）
- 方案书要求：三轮迭代，每轮产物包含提示词、结构化结果、指标、对比/分析报告
- 本次状态：已按标准命名补齐各轮产物；根目录 Markdown 已归档至 docs/

---

## 迭代1（基础拆分）
目录：`迭代数据/迭代1_基础拆分`

- [x] prompt_used.txt（原有）
- [x] prompt_v1.0.txt（新增：从 prompt_used.txt 复制）
- [x] decomposition_result.json（原有）
- [x] round1_decomposition.json（新增：从 decomposition_result.json 复制）
- [x] evaluation_metrics.csv（原有）
- [x] round1_metrics.csv（新增：从 evaluation_metrics.csv 复制）
- [x] analysis.md（原有）
- [x] round1_comparison.md（新增：模板，占位）
- [x] round1_diagnosis.md（新增：模板，占位）
- [x] copilot_interaction.md（新增：模板，占位，用于粘贴对话要点）

待办建议：
- 使用 metrics/scripts 计算并核对 TurboMQ、MoJoFM，更新 round1_metrics.csv 注释中的“估算”字样。

---

## 迭代2（依赖驱动）
目录：`迭代数据/迭代2_依赖驱动`

- [x] prompt_used.txt（原有）
- [x] prompt_v2.0.txt（新增：从 prompt_used.txt 复制）
- [x] decomposition_result.json（原有）
- [x] round2_decomposition.json（新增：从 decomposition_result.json 复制）
- [x] evaluation_metrics.csv（原有）
- [x] round2_metrics.csv（新增：从 evaluation_metrics.csv 复制）
- [x] analysis.md（原有）
- [x] round2_vs_round1.md（新增：模板，占位）
- [x] round2_diagnosis.md（新增：模板，占位）
- [x] copilot_interaction.md（新增：模板，占位）

待办建议：
- 合并“共享组件层”与 GT 对齐的口径，在文档中注明评估口径（是否允许 Shared Library 计入某服务）。

---

## 迭代3（专家优化）
目录：`迭代数据/迭代3_专家优化`

- [x] prompt_used.txt（原有）
- [x] prompt_v3.0.txt（新增：从 prompt_used.txt 复制）
- [x] decomposition_result.json（原有）
- [x] round3_decomposition.json（新增：从 decomposition_result.json 复制）
- [x] evaluation_metrics.csv（原有）
- [x] round3_metrics.csv（新增：从 evaluation_metrics.csv 复制）
- [x] analysis.md（如缺可后补，当前未强制）
- [x] round3_vs_round2.md（新增：模板，占位）
- [x] final_summary.md（新增：模板，占位，汇总三轮结果与结论）
- [x] copilot_interaction.md（新增：模板，占位）

待办建议：
- 在 final_summary.md 中固化：目标、对标工具、分歧类（如 CartActionBean）与最终 MoJoFM/TurboMQ。

---

## 文档归档
- [x] 根目录 Markdown 已移至 docs/：
  - docs/AI复现研究报告.md
  - docs/AI微服务拆分方案书.md
  - docs/REPRODUCTION_REPORT.md

说明：若其他子目录内的 README/说明文与工具代码绑定，暂不迁移，避免破坏引用。

---

## 重要一致性备注（需确认后执行）
- CartActionBean 的 GT 归属在资料中存在“catalog vs order”的表述差异。建议在 docs/ 中添加一条口径声明：MoJoFM 计算以 `case_studies/data/reference_decomposition/jpetstore_classes.csv` 为准。
- AbstractActionBean 的计入方式：若 GT 将其视为 duplicate（多处重复），请在评估时采用论文口径（通常记入某一服务以满足分配完备性）。

---

## 快速核验命令（PowerShell）

```powershell
# 查看三轮规范命名文件是否存在
Get-ChildItem -Path "迭代数据/迭代*/" -Include "round*_*", "prompt_v*.txt", "*interaction.md" -Recurse

# 运行评估脚本（如需）
python metrics/scripts/unzip_data.py
python metrics/scripts/generate_metadata.py
python metrics/scripts/create_dirs.py
python metrics/scripts/main.py
```

---

如需我继续：
- 使用 metrics/scripts 重新计算并回填三轮精确指标；
- 生成对比图表并存放到 results/figures/；
- 在 docs/ 中固化“评估口径声明”。
