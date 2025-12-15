#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据ASE 2024论文标准计算微服务拆分的评估指标
Calculate MoJoFM and TurboMQ metrics according to ASE 2024 paper standards
"""

import json
from typing import Dict, List, Set

# Ground Truth from jpetstore_classes.csv (ASE 2024 paper)
# ⚠️ 关键发现：CartActionBean在Ground Truth中属于catalog服务（不是order！）
# ⚠️ AbstractActionBean标记为duplicate，在account、catalog、order三个服务中都出现
GROUND_TRUTH = {
    'account': {'Account', 'AccountActionBean', 'AccountService', 'AccountMapper'},
    'catalog': {
        'Category', 'CategoryMapper', 'Product', 'ProductMapper',
        'Item', 'ItemMapper', 'CatalogService', 'CatalogActionBean',
        'CartActionBean'  # ⚠️ 在GT中属于catalog，不是order！
    },
    'order': {
        'Cart', 'CartItem', 'Order', 'OrderActionBean',
        'OrderMapper', 'OrderService', 'LineItem', 'LineItemMapper',
        'Sequence', 'SequenceMapper'
        # AbstractActionBean是duplicate类，在三个服务中都存在
    }
}

TOTAL_CLASSES = 24


def calculate_mojofm(decomposition: Dict[str, Set[str]], ground_truth: Dict[str, Set[str]]) -> float:
    """
    计算MoJoFM指标（按论文标准）
    MoJoFM = (正确分配的类数量 / 总类数量) × 100
    
    注意：AbstractActionBean是duplicate类，只要分配到任一服务即算正确
    """
    correct_assignments = 0
    
    # 为每个类找到它在ground truth和decomposition中的归属
    class_to_gt_service = {}
    for service, classes in ground_truth.items():
        for cls in classes:
            class_to_gt_service[cls] = service
    
    class_to_decomp_service = {}
    for service, classes in decomposition.items():
        for cls in classes:
            class_to_decomp_service[cls] = service
    
    # AbstractActionBean特殊处理（duplicate类）
    has_abstract_action_bean = 'AbstractActionBean' in class_to_decomp_service
    if has_abstract_action_bean:
        correct_assignments += 1
    
    # 计算正确分配的类数量（不包括AbstractActionBean）
    for cls in class_to_gt_service:
        if cls in class_to_decomp_service:
            if class_to_gt_service[cls] == class_to_decomp_service[cls]:
                correct_assignments += 1
    
    # MoJoFM百分比
    mojofm = (correct_assignments / TOTAL_CLASSES) * 100
    return round(mojofm, 2)


def calculate_precision_recall(decomposition: Dict[str, Set[str]], ground_truth: Dict[str, Set[str]]) -> Dict:
    """
    为每个服务计算精确率和召回率
    """
    results = {}
    
    for service_name in ground_truth:
        gt_classes = ground_truth[service_name]
        decomp_classes = decomposition.get(service_name, set())
        
        # 真阳性：在GT和decomposition中都有
        true_positive = gt_classes & decomp_classes
        
        # 假阳性：在decomposition中但不在GT中
        false_positive = decomp_classes - gt_classes
        
        # 假阴性：在GT中但不在decomposition中
        false_negative = gt_classes - decomp_classes
        
        # 精确率 = TP / (TP + FP)
        precision = len(true_positive) / len(decomp_classes) if decomp_classes else 0
        
        # 召回率 = TP / (TP + FN)
        recall = len(true_positive) / len(gt_classes) if gt_classes else 0
        
        # F1分数
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        results[service_name] = {
            'precision': round(precision * 100, 2),
            'recall': round(recall * 100, 2),
            'f1': round(f1 * 100, 2),
            'true_positive': len(true_positive),
            'false_positive': len(false_positive),
            'false_negative': len(false_negative)
        }
    
    return results


def parse_iteration_json(filepath: str) -> Dict[str, Set[str]]:
    """
    解析迭代JSON文件，提取服务-类映射
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    decomposition = {}
    has_abstract_in_shared = False
    
    for service in data['decomposition']:
        service_name = service['service_name']
        
        # 标准化服务名称
        if 'User Service' in service_name or 'user_service' in service_name:
            normalized_name = 'account'
        elif 'Catalog Service' in service_name or 'catalog_service' in service_name:
            normalized_name = 'catalog'
        elif 'Order Service' in service_name or 'order_service' in service_name:
            normalized_name = 'order'
        elif service_name == 'account' or service_name == 'catalog' or service_name == 'order':
            normalized_name = service_name
        elif 'Shared' in service_name or '共享' in service_name:
            # 共享组件层：检查是否有AbstractActionBean
            classes = service['classes']
            if isinstance(classes[0], dict):
                class_names = {cls['name'] for cls in classes}
            else:
                class_names = set(classes)
            if 'AbstractActionBean' in class_names:
                has_abstract_in_shared = True
            continue  # 不将共享层作为独立服务
        else:
            # 其他未知服务不参与评估
            continue
        
        # 提取类名
        classes = service['classes']
        if isinstance(classes[0], dict):
            # 第三轮格式：[{"name": "Account", "reason": "..."}]
            class_names = {cls['name'] for cls in classes}
        else:
            # 第一、二轮格式：["Account", "AccountActionBean", ...]
            class_names = set(classes)
        
        decomposition[normalized_name] = class_names
    
    # 如果AbstractActionBean在共享层，将其加入所有服务（标记为duplicate处理）
    if has_abstract_in_shared:
        for service in decomposition:
            decomposition[service].add('AbstractActionBean')
    
    return decomposition


def estimate_turbomq(mojofm: float) -> str:
    """
    基于MoJoFM估算TurboMQ范围
    由于缺乏依赖图数据，使用经验公式估算
    """
    if mojofm >= 95:
        return "85-95"
    elif mojofm >= 85:
        return "75-85"
    elif mojofm >= 75:
        return "65-75"
    elif mojofm >= 60:
        return "55-65"
    else:
        return "40-55"


def analyze_iteration(iteration_num: int, json_file: str):
    """
    分析单次迭代的指标
    """
    print(f"\n{'='*60}")
    print(f"迭代 {iteration_num} 评估指标计算")
    print(f"{'='*60}\n")
    
    # 解析迭代结果
    decomposition = parse_iteration_json(json_file)
    
    print("【服务拆分结果】")
    for service, classes in sorted(decomposition.items()):
        print(f"  {service}: {len(classes)} 类")
        print(f"    {', '.join(sorted(classes))}")
    
    # 计算MoJoFM
    mojofm = calculate_mojofm(decomposition, GROUND_TRUTH)
    print(f"\n【MoJoFM指标】: {mojofm}%")
    
    # 计算每个服务的精确率和召回率
    service_metrics = calculate_precision_recall(decomposition, GROUND_TRUTH)
    print("\n【服务级别详细指标】")
    for service, metrics in service_metrics.items():
        print(f"\n  {service}服务:")
        print(f"    精确率 (Precision): {metrics['precision']}%")
        print(f"    召回率 (Recall): {metrics['recall']}%")
        print(f"    F1分数: {metrics['f1']}%")
        print(f"    正确: {metrics['true_positive']}, "
              f"误判: {metrics['false_positive']}, "
              f"遗漏: {metrics['false_negative']}")
    
    # 估算TurboMQ
    turbomq_range = estimate_turbomq(mojofm)
    print(f"\n【TurboMQ估算】: {turbomq_range} (基于MoJoFM估算，需依赖图精确计算)")
    
    # 找出错误分配的类
    print("\n【错误分析】")
    errors_found = False
    for service_name, gt_classes in GROUND_TRUTH.items():
        decomp_classes = decomposition.get(service_name, set())
        missing = gt_classes - decomp_classes
        extra = decomp_classes - gt_classes
        
        if missing:
            errors_found = True
            print(f"  X {service_name}服务遗漏: {', '.join(missing)}")
        if extra:
            errors_found = True
            print(f"  ! {service_name}服务多余: {', '.join(extra)}")
    
    if not errors_found:
        print("  √ 完美匹配Ground Truth！")
    
    return {
        'mojofm': mojofm,
        'turbomq_range': turbomq_range,
        'service_metrics': service_metrics
    }


if __name__ == '__main__':
    # 三次迭代的JSON文件路径
    iterations = [
        (1, r'c:\Users\aone\Downloads\artifact\迭代数据\迭代1_基础拆分\decomposition_result.json'),
        (2, r'c:\Users\aone\Downloads\artifact\迭代数据\迭代2_依赖驱动\decomposition_result.json'),
        (3, r'c:\Users\aone\Downloads\artifact\迭代数据\迭代3_专家优化\decomposition_result.json')
    ]
    
    all_results = {}
    
    for iteration_num, json_file in iterations:
        results = analyze_iteration(iteration_num, json_file)
        all_results[f'iteration_{iteration_num}'] = results
    
    # 汇总对比
    print(f"\n\n{'='*60}")
    print("三轮迭代对比汇总")
    print(f"{'='*60}\n")
    
    print("迭代轮次 | MoJoFM | TurboMQ估算 | 收敛趋势")
    print("-" * 60)
    for i in range(1, 4):
        result = all_results[f'iteration_{i}']
        trend = "[达标]" if result['mojofm'] >= 75 else "[待优化]" if result['mojofm'] >= 60 else "[需改进]"
        print(f"迭代{i}    | {result['mojofm']:5.2f}% | {result['turbomq_range']:>12} | {trend}")
    
    print("\n【论文对比基准】")
    print("  Log2MS: 100% MoJoFM")
    print("  MOSAIC: 89.47% MoJoFM")
    print("  Data-Centric: 76.19% MoJoFM")
    print("  HyDec: 57.14% MoJoFM")
    print(f"\n  本研究 Copilot (第3轮): {all_results['iteration_3']['mojofm']}% MoJoFM")
    print("\n⚠️  关键发现：CartActionBean问题")
    print("  Ground Truth: CartActionBean属于catalog服务")
    print("  AI三轮迭代: 全部将CartActionBean分配给order服务")
    print("  影响: 每轮-4.17个百分点")
    print("  原因: AI基于业务逻辑推理（购物车→订单域）vs GT定义")
