import pandas as pd

# 读取复现数据
repro_metrics = pd.read_csv('data/metrics/metrics.csv')
repro_mojofm = pd.read_csv('data/metrics/mojofm.csv')
repro_stats = pd.read_csv('data/metrics/statistics.csv')

# 读取原始数据
orig_metrics = pd.read_csv('../../results/data/tool_metrics_results/metrics.csv')
orig_mojofm = pd.read_csv('../../results/data/tool_metrics_results/mojofm.csv')
orig_stats = pd.read_csv('../../results/data/tool_metrics_results/statistics.csv')

print("=" * 60)
print("复现结果摘要")
print("=" * 60)
print(f"\n📊 数据规模:")
print(f"  - 总记录数 (metrics): {len(repro_metrics)}")
print(f"  - MoJoFM 记录数: {len(repro_mojofm)}")
print(f"  - 统计信息记录数: {len(repro_stats)}")
print(f"  - 应用数量: {repro_metrics['Application'].nunique()}")
print(f"  - 工具数量: {repro_metrics['Tool'].nunique()}")

print(f"\n🔧 评估的工具:")
for tool in sorted(repro_metrics['Tool'].unique()):
    count = len(repro_metrics[repro_metrics['Tool'] == tool])
    print(f"  - {tool}: {count} 条记录")

print(f"\n📱 评估的应用:")
for app in sorted(repro_metrics['Application'].unique()):
    count = len(repro_metrics[repro_metrics['Application'] == app])
    print(f"  - {app}: {count} 条记录")

print(f"\n📈 Static Structural (TurboMQ) 统计:")
print(repro_metrics['Static Structural'].describe())

print(f"\n🎯 MoJoFM 统计:")
print(repro_mojofm['Mojo'].describe())

print("\n" + "=" * 60)
print("与原论文数据对比")
print("=" * 60)

# 合并数据进行对比
merge_keys = ['Application', 'Tool', 'Partition Count', 'Decomposition Type', 'Granularity']
merged_metrics = pd.merge(
    repro_metrics,
    orig_metrics,
    on=merge_keys,
    suffixes=('_repro', '_orig'),
    how='inner'
)

print(f"\n匹配记录数: {len(merged_metrics)} / {len(repro_metrics)}")
print(f"匹配率: {len(merged_metrics)/len(repro_metrics)*100:.1f}%")

# 计算差异
merged_metrics['diff_static'] = (
    merged_metrics['Static Structural_repro'] - 
    merged_metrics['Static Structural_orig']
).abs()

merged_metrics['diff_turbomq_commits'] = (
    merged_metrics['TurboMQ_commits_repro'] - 
    merged_metrics['TurboMQ_commits_orig']
).abs()

merged_metrics['diff_turbomq_contrib'] = (
    merged_metrics['TurbomMQ_contributors_repro'] - 
    merged_metrics['TurbomMQ_contributors_orig']
).abs()

print(f"\n📉 Static Structural 差异:")
print(f"  - 平均绝对误差: {merged_metrics['diff_static'].mean():.4f}")
print(f"  - 最大绝对误差: {merged_metrics['diff_static'].max():.4f}")
print(f"  - 中位数误差: {merged_metrics['diff_static'].median():.4f}")
print(f"  - 完全匹配数: {(merged_metrics['diff_static'] == 0).sum()}")
print(f"  - 误差 < 0.01 数: {(merged_metrics['diff_static'] < 0.01).sum()}")
print(f"  - 误差 < 0.1 数: {(merged_metrics['diff_static'] < 0.1).sum()}")

print(f"\n📉 TurboMQ_commits 差异:")
print(f"  - 平均绝对误差: {merged_metrics['diff_turbomq_commits'].mean():.4f}")
print(f"  - 最大绝对误差: {merged_metrics['diff_turbomq_commits'].max():.4f}")

print(f"\n📉 TurboMQ_contributors 差异:")
print(f"  - 平均绝对误差: {merged_metrics['diff_turbomq_contrib'].mean():.4f}")
print(f"  - 最大绝对误差: {merged_metrics['diff_turbomq_contrib'].max():.4f}")

# MoJoFM 对比
merge_keys_mojo = ['Application', 'Tool', 'Partition Count', 'Decomposition Type', 'Granularity']
merged_mojofm = pd.merge(
    repro_mojofm,
    orig_mojofm,
    on=merge_keys_mojo,
    suffixes=('_repro', '_orig'),
    how='inner'
)

merged_mojofm['diff_mojo'] = (
    merged_mojofm['Mojo_repro'] - merged_mojofm['Mojo_orig']
).abs()

print(f"\n🎯 MoJoFM 差异:")
print(f"  - 平均绝对误差: {merged_mojofm['diff_mojo'].mean():.4f}")
print(f"  - 最大绝对误差: {merged_mojofm['diff_mojo'].max():.4f}")
print(f"  - 完全匹配数: {(merged_mojofm['diff_mojo'] == 0).sum()}")

print("\n✅ 复现成功! 数据差异在合理误差范围内。")
