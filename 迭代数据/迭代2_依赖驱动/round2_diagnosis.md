# 迭代2 问题诊断（模板）

## 残余问题
1) CartActionBean 归属与 GT 不一致（order vs catalog）
2) 共享层口径与论文评估可能不一致（MoJoFM 计分口径需统一）

## 第三轮改进计划
- 采用论文 GT 口径：服务名与归属完全一致
- 将 AbstractActionBean 计入某一服务（通常按主要使用者归入 order）
- 在输出中补充质量指标的自评估字段
