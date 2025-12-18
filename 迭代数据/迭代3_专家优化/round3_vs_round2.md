# 迭代3 vs 迭代2 对比

参考口径：见 [docs/EVALUATION_POLICY.md](docs/EVALUATION_POLICY.md)

## 关键变化
- 服务命名与边界稳定；回退共享层，将 `AbstractActionBean` 明确归入 `order`

## 指标
- MoJoFM：持平（95.83% → 95.83%）
- TurboMQ（估算）：维持 85-95 区间

## 服务级指标变化（摘要）

| 服务 | P2 | R2 | F1-2 | P3 | R3 | F1-3 |
|---|---:|---:|---:|---:|---:|---:|
| account | 80.00% | 100.00% | 88.89% | 100.00% | 100.00% | 100.00% |
| catalog | 88.89% | 88.89% | 88.89% | 100.00% | 88.89% | 94.12% |
| order | 83.33% | 100.00% | 90.91% | 83.33% | 100.00% | 90.91% |

说明：`AbstractActionBean` 固化到 `order` 后，account 与 catalog 精确率恢复至 100%/100% 与 100%/88.89%。仍存的主要差异为 `CartActionBean` 归属（现=order，GT=catalog）。

## 后续建议
- 若以GT计分：将 `CartActionBean` 调整至 `catalog`，可望将 MoJoFM 提升至 100%
- 若坚持业务口径：保留差异说明，并在最终总结中明确“评估口径与业务口径”的取舍
