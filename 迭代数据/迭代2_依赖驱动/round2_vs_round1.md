# 迭代2 vs 迭代1 对比

参考口径：见 [docs/EVALUATION_POLICY.md](docs/EVALUATION_POLICY.md)

## 指标变化
- MoJoFM：+4.16pp（91.67% → 95.83%）
- TurboMQ（估算）：75-85 → 85-95（结构更紧凑，估算区间上移）

## 核心变更
- 覆盖完备：引入共享层包含 `AbstractActionBean`，实现 24/24 类覆盖
- 依赖指引：实体-Mapper对齐，减少跨域偶发耦合

## 差异明细

| 类 | 迭代1归属 | 迭代2归属 | 影响 |
|---|---|---|---|
| AbstractActionBean | 未分配 | 共享（在评估口径中等价为各服务可见） | 提升覆盖，轻微稀释 account/catalog 精确率 |
| CartActionBean | order | order | 与GT不一致（GT=catalog），仍是主要差异源 |

## 服务级指标变化（摘要）

| 服务 | P1 | R1 | F1-1 | P2 | R2 | F1-2 |
|---|---:|---:|---:|---:|---:|---:|
| account | 100.00% | 100.00% | 100.00% | 80.00% | 100.00% | 88.89% |
| catalog | 100.00% | 88.89% | 94.12% | 88.89% | 88.89% | 88.89% |
| order | 90.91% | 100.00% | 95.24% | 83.33% | 100.00% | 90.91% |

说明：共享层在评估时等价为类可同时出现于多个服务，导致 account/catalog 出现少量“多余”，但总体 MoJoFM 上升。

## 进入迭代3的动作
- 依据“主要使用者”原则，将 `AbstractActionBean` 固化归入 `order`，恢复精确率
- 若以GT计分，需将 `CartActionBean` 迁回 `catalog`；若坚持业务口径，请在报告中保留差异说明
