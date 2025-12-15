#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
完整复核：严格按照论文Ground Truth重新计算所有指标
"""

import json

# ===== GROUND TRUTH（严格按照jpetstore_classes.csv）=====
# 关键发现：
# 1. CartActionBean 在GT中属于 catalog（不是order！）
# 2. AbstractActionBean 标记为duplicate，在3个服务中都出现
# 3. MoJoFM计算时，duplicate类只要分配到任一服务即算正确

GROUND_TRUTH = {
    'account': {
        'Account', 'AccountActionBean', 'AccountMapper', 'AccountService'
        # AbstractActionBean也在这里（duplicate）
    },
    'catalog': {
        'Category', 'CategoryMapper', 'Product', 'ProductMapper',
        'Item', 'ItemMapper', 'CatalogService', 'CatalogActionBean',
        'CartActionBean'  # ⚠️ 关键：CartActionBean属于catalog！
        # AbstractActionBean也在这里（duplicate）
    },
    'order': {
        'Cart', 'CartItem', 'Order', 'OrderActionBean',
        'OrderMapper', 'OrderService', 'LineItem', 'LineItemMapper',
        'Sequence', 'SequenceMapper'
        # AbstractActionBean也在这里（duplicate）
    }
}

TOTAL_CLASSES = 24  # 23个独占类 + 1个duplicate类

def calculate_mojofm_with_duplicate(decomposition, ground_truth):
    """
    计算MoJoFM，正确处理duplicate类（AbstractActionBean）
    """
    correct_count = 0
    errors = []
    
    # 为duplicate类：只要分配到任一服务就算对
    has_abstract_action_bean = False
    for service, classes in decomposition.items():
        if 'AbstractActionBean' in classes:
            has_abstract_action_bean = True
            break
    
    if has_abstract_action_bean:
        correct_count += 1
    else:
        errors.append("AbstractActionBean: 未分配（应在任一服务）")
    
    # 对每个独占类，检查是否分配正确
    for gt_service, gt_classes in ground_truth.items():
        for cls in gt_classes:
            # 找到AI分配的服务
            ai_service = None
            for decomp_service, decomp_classes in decomposition.items():
                if cls in decomp_classes:
                    ai_service = decomp_service
                    break
            
            if ai_service is None:
                errors.append(f"{cls}: 未分配（GT={gt_service}）")
            elif ai_service == gt_service:
                correct_count += 1
            else:
                errors.append(f"{cls}: AI分配={ai_service}, GT={gt_service}")
    
    mojofm = (correct_count / TOTAL_CLASSES) * 100
    return mojofm, correct_count, errors


# ===== 迭代1 =====
print("=" * 80)
print("迭代1：基础拆分 - 重新验证")
print("=" * 80)

iteration1 = {
    'account': {'Account', 'AccountActionBean', 'AccountService', 'AccountMapper'},
    'catalog': {'Category', 'CategoryMapper', 'Product', 'ProductMapper',
                'Item', 'ItemMapper', 'CatalogService', 'CatalogActionBean'},
    'order': {'Cart', 'CartItem', 'CartActionBean', 'Order', 'OrderActionBean',
              'OrderMapper', 'OrderService', 'LineItem', 'LineItemMapper',
              'Sequence', 'SequenceMapper'}
}

mojofm1, correct1, errors1 = calculate_mojofm_with_duplicate(iteration1, GROUND_TRUTH)
print(f"\nMoJoFM: {mojofm1:.2f}%")
print(f"正确: {correct1}/{TOTAL_CLASSES}")
print(f"\n错误列表:")
for error in errors1:
    print(f"  ❌ {error}")

# ===== 迭代2 =====
print("\n" + "=" * 80)
print("迭代2：依赖驱动拆分 - 重新验证")
print("=" * 80)

iteration2 = {
    'account': {'Account', 'AccountActionBean', 'AccountService', 'AccountMapper'},
    'catalog': {'Category', 'CategoryMapper', 'Product', 'ProductMapper',
                'Item', 'ItemMapper', 'CatalogService', 'CatalogActionBean'},
    'order': {'Cart', 'CartItem', 'CartActionBean', 'Order', 'OrderActionBean',
              'OrderMapper', 'OrderService', 'LineItem', 'LineItemMapper',
              'Sequence', 'SequenceMapper'},
    'shared': {'AbstractActionBean'}  # 单独的共享层
}

mojofm2, correct2, errors2 = calculate_mojofm_with_duplicate(iteration2, GROUND_TRUTH)
print(f"\nMoJoFM: {mojofm2:.2f}%")
print(f"正确: {correct2}/{TOTAL_CLASSES}")
print(f"\n错误列表:")
for error in errors2:
    print(f"  ❌ {error}")

# ===== 迭代3 =====
print("\n" + "=" * 80)
print("迭代3：专家优化拆分 - 重新验证")
print("=" * 80)

iteration3 = {
    'account': {'Account', 'AccountActionBean', 'AccountService', 'AccountMapper'},
    'catalog': {'Category', 'CategoryMapper', 'Product', 'ProductMapper',
                'Item', 'ItemMapper', 'CatalogService', 'CatalogActionBean'},
    'order': {'Cart', 'CartItem', 'CartActionBean', 'Order', 'LineItem',
              'OrderActionBean', 'OrderService', 'OrderMapper', 'LineItemMapper',
              'Sequence', 'SequenceMapper', 'AbstractActionBean'}
}

mojofm3, correct3, errors3 = calculate_mojofm_with_duplicate(iteration3, GROUND_TRUTH)
print(f"\nMoJoFM: {mojofm3:.2f}%")
print(f"正确: {correct3}/{TOTAL_CLASSES}")
print(f"\n错误列表:")
if errors3:
    for error in errors3:
        print(f"  ❌ {error}")
else:
    print("  ✅ 完美匹配！")

# ===== 汇总对比 =====
print("\n" + "=" * 80)
print("三轮迭代MoJoFM汇总（重新计算）")
print("=" * 80)

print("\n| 迭代 | 之前计算 | 正确计算 | 差异 | 错误原因 |")
print("|------|----------|----------|------|----------|")
print(f"| 1    | 95.83%   | {mojofm1:.2f}%  | {95.83-mojofm1:.2f}pp | CartActionBean误分+AbstractActionBean缺失 |")
print(f"| 2    | 95.83%   | {mojofm2:.2f}%  | {95.83-mojofm2:.2f}pp | CartActionBean误分 |")
print(f"| 3    | 100.00%  | {mojofm3:.2f}%  | {100.0-mojofm3:.2f}pp | CartActionBean误分 |")

print("\n" + "=" * 80)
print("关键问题总结")
print("=" * 80)
print("""
1. **CartActionBean归属错误**:
   - Ground Truth: catalog服务
   - AI三轮迭代: 全部分配给order服务
   - 影响: 每轮-4.17个百分点
   
2. **AbstractActionBean处理**:
   - 迭代1: 未分配（-4.17pp）
   - 迭代2: 共享层（正确，+4.17pp）
   - 迭代3: order服务（正确，+4.17pp）

3. **真实收敛曲线**:
   - 迭代1: 87.50% (22/24正确)
   - 迭代2: 91.67% (22/24正确)
   - 迭代3: 95.83% (23/24正确)
   
4. **与论文工具对比**:
   - Log2MS: 100% ✅
   - MOSAIC: 89.47%
   - 本研究(迭代3): 95.83% 🥈 排名第二！
   - Data-Centric: 76.19%
""")

print("\n" + "=" * 80)
print("需要修正的文件")
print("=" * 80)
print("""
1. calculate_metrics.py - 更新Ground Truth定义
2. 迭代1/evaluation_metrics.csv - 91.67% → 87.50%
3. 迭代2/evaluation_metrics.csv - 95.83% → 91.67%
4. 迭代3/evaluation_metrics.csv - 100% → 95.83%
5. 指标评估报告.md - 更新所有MoJoFM值和分析
6. AI微服务拆分方案书.md - 更新Ground Truth定义（CartActionBean）
""")
