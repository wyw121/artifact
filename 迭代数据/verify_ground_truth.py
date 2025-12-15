#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ground Truth 验证与错误修正
根据论文原始CSV数据重新定义Ground Truth
"""

import json
from typing import Dict, Set

# ⚠️ 关键发现：CartActionBean在Ground Truth中归属catalog，不是order！
# AbstractActionBean标记为duplicate，在account、order、catalog中都出现

# 重新定义Ground Truth（严格按照jpetstore_classes.csv）
GROUND_TRUTH_CORRECT = {
    'account': {
        'Account', 'AccountActionBean', 'AccountMapper', 'AccountService',
        'AbstractActionBean'  # duplicate标记，在account中
    },
    'catalog': {
        'Category', 'CategoryMapper', 'Product', 'ProductMapper',
        'Item', 'ItemMapper', 'CatalogService', 'CatalogActionBean',
        'CartActionBean',  # ⚠️ 在GT中归属catalog，不是order！
        'AbstractActionBean'  # duplicate标记，在catalog中
    },
    'order': {
        'Cart', 'CartItem', 'Order', 'OrderActionBean',
        'OrderMapper', 'OrderService', 'LineItem', 'LineItemMapper',
        'Sequence', 'SequenceMapper',
        'AbstractActionBean'  # duplicate标记，在order中
    }
}

# 论文的MoJoFM计算方法需要考虑duplicate类
# 当一个类标记为duplicate时，它可以匹配任何包含它的服务

print("=" * 70)
print("Ground Truth 验证报告")
print("=" * 70)

# 统计每个服务的类数量（不计重复）
unique_classes = set()
for service, classes in GROUND_TRUTH_CORRECT.items():
    unique_classes.update(classes)

print(f"\n总类数: {len(unique_classes)} (包含1个duplicate类AbstractActionBean)")
print(f"唯一类数: {len(unique_classes - {'AbstractActionBean'})} + 1 duplicate")

print("\nGround Truth 各服务类分配:")
for service, classes in GROUND_TRUTH_CORRECT.items():
    non_duplicate = classes - {'AbstractActionBean'}
    print(f"\n{service}服务: {len(non_duplicate)}个独占类 + AbstractActionBean(共享)")
    for cls in sorted(non_duplicate):
        print(f"  - {cls}")

# 关键错误1: CartActionBean
print("\n" + "="*70)
print("⚠️  发现的Ground Truth关键点:")
print("="*70)
print("\n1. CartActionBean 归属 catalog 服务（不是order）")
print("   理由: 在CSV中明确标记为catalog")
print("   影响: 迭代1/2/3都将CartActionBean错误分配给了order")

print("\n2. AbstractActionBean 是 duplicate 类")
print("   标记: duplicate=TRUE")
print("   出现: account, catalog, order 三个服务中都有")
print("   MoJoFM计算: 只要AI将其分配到任一服务即算正确")

# 重新计算MoJoFM
print("\n" + "="*70)
print("重新计算 MoJoFM（考虑CartActionBean错误）")
print("="*70)

# 迭代1的实际分配
iteration1 = {
    'account': {'Account', 'AccountActionBean', 'AccountService', 'AccountMapper'},
    'catalog': {'Category', 'CategoryMapper', 'Product', 'ProductMapper',
                'Item', 'ItemMapper', 'CatalogService', 'CatalogActionBean'},
    'order': {'Cart', 'CartItem', 'CartActionBean', 'Order', 'OrderActionBean',
              'OrderMapper', 'OrderService', 'LineItem', 'LineItemMapper',
              'Sequence', 'SequenceMapper'}
}

# 计算错误
print("\n迭代1错误分析:")
errors = []
# CartActionBean在GT中是catalog，但AI分配给了order
if 'CartActionBean' in iteration1['order']:
    errors.append("CartActionBean: AI分配给order，GT是catalog")
# AbstractActionBean未分配
if 'AbstractActionBean' not in iteration1['account'] and \
   'AbstractActionBean' not in iteration1['catalog'] and \
   'AbstractActionBean' not in iteration1['order']:
    errors.append("AbstractActionBean: AI未分配，GT要求任一服务")

for error in errors:
    print(f"  ❌ {error}")

# 正确的类匹配数
correct_count = 0
total_unique_classes = 24  # 23个独占类 + 1个duplicate类

# account服务: 4个类全部正确
correct_count += 4

# catalog服务: 应该有8个类（包括CartActionBean），但AI只分配了7个（缺CartActionBean）
ai_catalog_correct = iteration1['catalog'] & (GROUND_TRUTH_CORRECT['catalog'] - {'AbstractActionBean'})
correct_count += len(ai_catalog_correct)  # 7个

# order服务: 应该有10个独占类，但AI多了CartActionBean（11个）
ai_order_correct = iteration1['order'] & (GROUND_TRUTH_CORRECT['order'] - {'AbstractActionBean'})
correct_count += len(ai_order_correct)  # 10个

# AbstractActionBean未分配，算错误
# correct_count += 0

mojofm_correct = (correct_count / total_unique_classes) * 100
print(f"\n✅ 正确分配: {correct_count}个类")
print(f"❌ 错误/遗漏: {total_unique_classes - correct_count}个类")
print(f"📊 真实MoJoFM: {mojofm_correct:.2f}%")

print("\n详细分析:")
print(f"  account: 4/4 正确")
print(f"  catalog: 7/8 正确 (缺CartActionBean)")
print(f"  order: 10/10 正确 (CartActionBean不该在这)")
print(f"  AbstractActionBean: 未分配 (应在任一服务)")

print("\n" + "="*70)
print("结论")
print("="*70)
print("\n之前计算的95.83%是**错误的**！")
print(f"实际MoJoFM应该是: {mojofm_correct:.2f}%")
print("\n原因:")
print("1. 未考虑CartActionBean的GT归属是catalog而非order")
print("2. AbstractActionBean未分配确实是错误")
print("\n需要:")
print("1. 更新Ground Truth定义")
print("2. 重新计算所有三轮迭代的MoJoFM")
print("3. 更新evaluation_metrics.csv")
print("4. 更新评估报告")
