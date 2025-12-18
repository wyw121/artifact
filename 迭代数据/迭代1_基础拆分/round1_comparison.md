# 迭代1 vs Ground Truth 对比

- 对比口径：参考 [artifact/case_studies/data/reference_decomposition/jpetstore_classes.csv](artifact/case_studies/data/reference_decomposition/jpetstore_classes.csv)；细则见 [docs/EVALUATION_POLICY.md](docs/EVALUATION_POLICY.md)
- 维度：类级分配；服务名固定为 account / catalog / order

## 概要
- 服务数：实际 3 / 期望 3（一致）
- MoJoFM：91.67%
- TurboMQ（估算）：75-85
- 主要差异：
  - CartActionBean：实际=order，GT=catalog（与GT不一致）
  - AbstractActionBean：未分配（导致覆盖不完备）

## 差异明细

| 类型 | account | catalog | order |
|---|---|---|---|
| 遗漏（相对GT） | - | CartActionBean | - |
| 多余（相对GT） | - | - | CartActionBean |

## 服务级指标

| 服务 | Precision | Recall | F1 |
|---|---:|---:|---:|
| account | 100.00% | 100.00% | 100.00% |
| catalog | 100.00% | 88.89% | 94.12% |
| order | 90.91% | 100.00% | 95.24% |

说明：catalog 召回受 CartActionBean 误分影响；order 精确率受同一原因影响。

## 结论与改进项（输入迭代2）
- 将 AbstractActionBean 明确处理（共享或按主要使用者计入），补齐覆盖
- 复核 CartActionBean 的GT口径并与AI推理一致性，若以GT计分则应迁回 catalog
- 保持服务命名标准与边界稳定，避免新增跨域耦合
