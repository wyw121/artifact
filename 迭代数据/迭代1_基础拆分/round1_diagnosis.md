# 迭代1 问题诊断（模板）

## 关键问题
1) AbstractActionBean 未分配 → 影响评估完整性
2) CartActionBean 归属与 GT 不一致（order vs catalog）

## 根因假设
- 基类被误当作“共享而不计入服务”
- 业务完整性优先导致将 CartActionBean 绑定到 order

## 改进方案（供迭代2参考）
- 明确：基类按主要使用者分配（或采用论文 duplicate 口径）
- 说明：跨服务 ID 引用不改变服务归属（CartItem/LineItem→Item）
- 强化：实体-Mapper 一一对应，同服务内聚
