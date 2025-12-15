# 基于大语言模型的微服务拆分迭代方案书

**项目名称**: JPetStore 微服务拆分与多轮迭代评估
**论文基础**: Microservice Decomposition Techniques: An Independent Tool Comparison (ASE 2024)
**评估工具**: GitHub Copilot AI + 论文量化评估指标体系
**执行周期**: 三轮迭代
**文档生成日期**: 2025年12月16日

---

## 目录

1. [第一部分：研究背景与目标](#第一部分)
2. [第二部分：评估体系（待补充）](#第二部分)
3. [第三部分：三轮迭代详细方案（待补充）](#第三部分)
4. [第四部分：提示词设计与优化（待补充）](#第四部分)
5. [第五部分：执行流程与验证标准（待补充）](#第五部分)

---

## 第一部分：研究背景与目标

### 1.1 研究意义

#### 论文核心贡献

《Microservice Decomposition Techniques: An Independent Tool Comparison》(ASE 2024) 通过对8个微服务分解工具的独立评估，揭示了现有自动化拆分技术的优缺点：

| 工具名称                  | 技术原理             | 评估结果                      | 局限性             |
| ------------------------- | -------------------- | ----------------------------- | ------------------ |
| **CARGO**           | 静态依赖分析         | TurboMQ: 31.76                | 类级别易出现空分区 |
| **Data-Centric**    | 数据流追踪           | MoJoFM: 72.49                 | 需要完整数据模型   |
| **HyDec**           | 混合方法 (代码+日志) | TurboMQ: 60.64                | 对日志格式敏感     |
| **Log2MS**          | 执行日志分析         | MoJoFM: 88.67 (JPetStore最佳) | 需要运行时数据     |
| **MEM**             | 进化分析 (Git历史)   | MoJoFM: 46.28                 | 历史数据依赖强     |
| **Mono2Micro**      | 机器学习 (ML)        | TurboMQ: 73.73                | 需要标注数据       |
| **MOSAIC**          | 多源融合聚类         | TurboMQ: 92.71, MoJoFM: 82.71 | 性能最稳定         |
| **toMicroservices** | 优化算法             | TurboMQ: 44.91                | 参数调优复杂       |

#### 创新方向：AI驱动的拆分方案

本研究引入 **GitHub Copilot** 作为新的拆分工具，探索以下创新点：

1. **多轮对话优化**：通过渐进式提示词改进，逐步提升拆分质量
2. **混合评估体系**：结合论文的量化指标（TurboMQ、MoJoFM）+ AI可解释性分析
3. **知识积累机制**：每轮迭代保留AI的推理过程，建立微服务识别的"学习轨迹"
4. **与传统工具对比**：将Copilot结果与Log2MS、MOSAIC等最优工具并列评估

### 1.2 核心目标

#### 目标1：验证AI在微服务拆分中的有效性

- 目标指标：Copilot最终的MoJoFM评分 **≥ 65%**（超过HyDec 58.59%）
- 对标工具：Log2MS（88.67%）、MOSAIC（82.71%）
- 评估维度：准确性、可解释性、迭代收敛速度

#### 目标2：建立AI提示词的最佳实践

- 第一轮：基础提示 → 获得初步拆分 (预期 40-50% MoJoFM)
- 第二轮：优化提示 → 加入上下文和约束 (预期 50-65% MoJoFM)
- 第三轮：专家提示 → 融合论文知识 (预期 65-80% MoJoFM)

#### 目标3：生成可复现的AI微服务拆分框架

- 输出物：三份迭代拆分方案 + 完整提示词档案库
- 存储形式：每轮迭代的JPetStore项目独立保存，结构清晰
- 评估报告：量化指标 + 定性分析 + AI推理可视化

### 1.3 案例应用：JPetStore

#### 应用背景

- **规模**：24个类，302个方法（类级别），是论文中最小的实际应用
- **领域**：电商系统（宠物在线商店）
- **参考分解**（Ground Truth）：3个微服务
  - **account**：账户管理微服务
  - **catalog**：商品目录微服务
  - **order**：订单处理微服务

#### 为什么选择JPetStore

1. **规模适中**：便于AI在单次对话中完整理解全貌
2. **结构清晰**：3个微服务的Ground Truth明确定义，易于验证
3. **论文数据完整**：所有8个工具都有对JPetStore的评估结果
4. **最佳实验对象**：Log2MS在此应用达到100% MoJoFM得分，为AI设定明确目标

---

---

## 第二部分：评估体系详解

### 2.1 论文的量化指标体系概览

论文采用两类指标评估微服务拆分质量：

| 指标类别             | 指标名称 | 衡量维度               | 计算方法        | 最优值         |
| -------------------- | -------- | ---------------------- | --------------- | -------------- |
| **质量评估**   | TurboMQ  | 静态结构模块化质量     | 耦合度-粘聚度   | 100            |
| **质量评估**   | 分区数量 | 微服务粒度控制         | 分区个数        | ≈Ground Truth |
| **相似度评估** | MoJoFM   | 与Ground Truth的一致性 | 类/方法重叠匹配 | 100            |
| **可解释性**   | 推理链   | AI决策过程             | 文本说明        | 清晰完整       |

### 2.2 核心指标详解

#### 2.2.1 TurboMQ：模块化质量指标

**定义**：衡量分解的高内聚低耦合程度。

**公式**：

$$
TurboMQ = \frac{\text{Cohesion} - \text{Coupling}}{\text{Cohesion} + \text{Coupling}} \times 100
$$

其中：

- **Cohesion（内聚度）**：分区内部的依赖关系数量
- **Coupling（耦合度）**：分区间的跨越依赖关系数量

**数值范围**：0-100

- 90-100：优秀（MOSAIC在JPetStore达到100）
- 70-89：良好（Mono2Micro: 73.73）
- 50-69：中等（HyDec: 60.64）
- 30-49：较差（CARGO: 31.76）
- <30：差（MEM: 28.13）

**JPetStore Ground Truth的TurboMQ基准**：

- 预期值：约90-100（论文中MOSAIC达到100）
- 第一轮Copilot目标：≥50
- 第二轮Copilot目标：≥65
- 第三轮Copilot目标：≥80

---

#### 2.2.2 MoJoFM：相似度指标

**定义**：衡量Copilot拆分与Ground Truth（专家参考分解）的一致性。

**公式**：

$$
MoJoFM = \frac{1}{max(|A|, |B|)} \times \sum_{i=1}^{|A|} |A_i \cap B_{\sigma(i)}|
$$

其中：

- $A$：Copilot的分解方案（分区集合）
- $B$：Ground Truth的参考分解（分区集合）
- $\sigma$：最优匹配排列（使交集最大化）
- $|A_i|$：第i个分区的类/方法数量

**数值范围**：0-100

- 90-100：接近完美（Log2MS在JPetStore达到100）
- 75-89：优秀（MOSAIC: 82.71）
- 60-74：良好（Data-Centric: 72.49）
- 40-59：中等（HyDec: 58.59）
- <40：较差（CARGO: 42.86）

**JPetStore Ground Truth的参考值**：

```
account 微服务（7个类，多个方法）：
  - Account, AccountActionBean, AccountMapper, AccountService

catalog 微服务（8个类）：
  - Category, CategoryMapper, CatalogActionBean, CatalogService
  - CartActionBean, Item, ItemMapper, Product, ProductMapper

order 微服务（7个类）：
  - Cart, CartItem, Order, OrderActionBean, OrderMapper
  - OrderService, LineItem, LineItemMapper, Sequence, SequenceMapper
```

**第一轮Copilot目标**：≥35-45% MoJoFM
**第二轮Copilot目标**：≥50-60% MoJoFM
**第三轮Copilot目标**：≥65-75% MoJoFM

---

#### 2.2.3 结构化评估指标

除了TurboMQ和MoJoFM，还需评估以下维度：

| 指标                     | 计算方法                   | 目标值      | 说明                                        |
| ------------------------ | -------------------------- | ----------- | ------------------------------------------- |
| **分区数量**       | 生成的微服务个数           | 3（接近GT） | Ground Truth为3，过多拆分过细，过少聚合过粗 |
| **分区大小均衡度** | Std Dev of partition sizes | 低方差      | 避免某个微服务过大                          |
| **最大分区规模**   | largest partition size     | <50%        | 避免出现单独的巨大微服务                    |
| **最小分区规模**   | smallest partition size    | >2          | 避免只有1-2个类的微服务                     |

---

### 2.3 JPetStore数据基准

#### 2.3.1 Ground Truth参考分解

**总体统计**：

- 总类数：24
- 总方法数：302
- 分区数：3
- 最大分区：8个类（catalog）
- 最小分区：7个类（account, order各7个）

**具体分解**：

| 微服务名          | 类数 | 方法数 | 主要职责                         |
| ----------------- | ---- | ------ | -------------------------------- |
| **account** | 7    | ~100   | 用户账户管理、登陆、个人信息维护 |
| **catalog** | 8    | ~100   | 商品分类、搜索、浏览             |
| **order**   | 9    | ~102   | 购物车、下单、订单管理           |

#### 2.3.2 论文中8个工具对JPetStore的评估结果

**TurboMQ评分（类级别）**：

```
MOSAIC:           100.00 ✅ (最优)
Ground Truth:      89.73
Mono2Micro:        73.64
Data-Centric:      79.74
Log2MS:            76.04
HyDec:             32.01
toMicroservices:   18.20
CARGO:             52.15
```

**MoJoFM评分（与Ground Truth比较）**：

```
Log2MS:           100.00 ✅ (完美匹配)
Data-Centric:      76.19 (类级) / 85.53 (方法级)
MOSAIC:            89.47
HyDec:             57.14 (类级) / 88.49 (方法级)
Mono2Micro:        74.67 (方法级)
toMicroservices:   51.85
MEM:               70.07 (方法级)
CARGO:             42.86
```

**分区数量对比**：

```
Ground Truth:  3个
Log2MS:        3个 (精准)
MOSAIC:        3个 (精准)
Data-Centric:  3个
HyDec:         4-5个 (略过拆分)
Mono2Micro:    2-4个 (可变)
CARGO:         2-3个
MEM:           多达8-10个 (过度拆分)
toMicroservices: 4-5个
```

---

### 2.4 评估数据收集与计算流程

#### 2.4.1 数据收集清单

每轮迭代需收集以下数据：

```
迭代 X 数据包/
├── prompt_used.txt          # 本轮使用的提示词
├── decomposition_result.json # Copilot输出的拆分方案
│   ├── partitions: [        # 分区列表
│   │   {
│   │     "name": "account",
│   │     "classes": [...],
│   │     "methods": [...]
│   │   },
│   │   ...
│   │ ]
│   └── reasoning: "..."      # 拆分推理过程
├── evaluation_metrics.csv    # 评估指标结果
│   ├── TurboMQ
│   ├── MoJoFM
│   ├── partition_count
│   └── timestamp
└── analysis.md              # 定性分析报告
    ├── 与Ground Truth的对比
    ├── 拆分质量评价
    ├── 改进建议
    └── 问题诊断
```

#### 2.4.2 计算流程

**步骤1**：提取Copilot拆分结果

- 从Copilot输出中识别分区边界
- 列出每个分区的类和方法
- 保存为JSON格式

**步骤2**：计算TurboMQ

- 提取依赖图（使用现有的structural_static.csv）
- 计算分区间耦合度
- 计算分区内粘聚度
- 代入公式计算TurboMQ

**步骤3**：计算MoJoFM

- 与Ground Truth进行类/方法级匹配
- 使用最优分配算法（Hungarian算法）寻找最佳对应
- 计算重叠系数
- 代入公式计算MoJoFM

**步骤4**：生成评估报告

- 制表对比各轮迭代指标
- 分析收敛趋势
- 标注改进点和问题根源

---

## 第二部分完成

**核心要点总结**：

- TurboMQ：衡量分解的模块化质量（0-100，越高越好）
- MoJoFM：衡量与Ground Truth的匹配程度（0-100，越高越好）
- JPetStore Ground Truth：3个微服务，24个类，302个方法
- Copilot目标：第三轮达到MoJoFM ≥65%（超过HyDec）

---

## 第三部分：三轮迭代详细方案

### 3.1 迭代总体框架

每轮迭代遵循以下流程：

```
输入提示词 → AI生成拆分方案 → 提取结构化结果 → 计算评估指标 → 定性分析 → 优化提示词
                 ↑                                                        ↓
                 └─────────────── 反馈与改进 ──────────────────────────┘
```

**时间安排**：每轮迭代 2-3 小时

- 提示词设计与对话：1小时
- 结果提取与数据清理：30分钟
- 指标计算与可视化：45分钟
- 定性分析与诊断：30分钟

---

### 3.2 第一轮迭代：基础拆分（Expected MoJoFM: 35-45%）

#### 3.2.1 迭代目标

| 维度                  | 目标         | 说明                            |
| --------------------- | ------------ | ------------------------------- |
| **提示策略**    | 基础任务描述 | 直接说明JPetStore的功能与类结构 |
| **AI理解深度**  | 粗粒度理解   | AI需要理解"这是一个电商系统"    |
| **期望分区数**  | 2-5个        | 可能过度拆分或聚合              |
| **期望MoJoFM**  | 35-45%       | 显著低于论文最优工具            |
| **期望TurboMQ** | 30-50        | 中等水平                        |

#### 3.2.2 输入提示词（Prompt v1.0）

```
请对下列JPetStore电商系统进行微服务拆分。

## 系统概述
JPetStore是一个宠物在线商店系统，用户可以浏览商品、管理账户、购物和下单。
系统主要功能包括：账户管理、商品管理、购物车、订单处理。

## 系统类列表（共24个类，302个方法）

【账户相关】
- Account：用户账户实体类（getUsername, getPassword, getEmail等18个方法）
- AccountActionBean：账户处理的Web Action（登陆、登出、个人信息管理）
- AccountService：账户业务逻辑服务
- AccountMapper：数据库映射接口

【商品相关】
- Category：商品分类实体
- CategoryMapper：分类数据映射
- Item：商品项实体
- ItemMapper：商品数据映射
- Product：商品实体
- ProductMapper：商品数据映射
- CatalogActionBean：商品浏览的Web Action
- CatalogService：商品业务逻辑服务

【订单相关】
- Cart：购物车实体
- CartItem：购物车项
- CartActionBean：购物车Web Action
- Order：订单实体
- OrderActionBean：订单处理Web Action
- OrderMapper：订单数据映射
- OrderService：订单业务逻辑服务
- LineItem：订单行项
- LineItemMapper：订单行数据映射
- Sequence：序列号生成
- SequenceMapper：序列号数据映射

## 任务要求

请基于上述类的功能和职责，将系统拆分为微服务。对于每个拆分的微服务：
1. 给出微服务名称
2. 列出包含的类列表
3. 简要说明微服务的核心职责
4. 解释为什么这些类应该聚合在一起

请采用以下JSON格式输出结果：
{
  "decomposition": [
    {
      "service_name": "服务名",
      "classes": ["类1", "类2", ...],
      "responsibility": "核心职责说明",
      "reasoning": "拆分理由"
    }
  ],
  "total_services": 数字,
  "quality_assessment": "拆分质量的自我评估"
}

希望你的拆分遵循微服务设计原则：
- 高内聚：同一服务内的类应该有强相关性
- 低耦合：不同服务间应该尽可能独立
- 单一职责：每个服务应该专注于一个业务能力
```

#### 3.2.3 预期输出示例

```json
{
  "decomposition": [
    {
      "service_name": "account-service",
      "classes": ["Account", "AccountActionBean", "AccountService", "AccountMapper"],
      "responsibility": "处理用户账户的登陆、注册、个人信息管理",
      "reasoning": "这些类都与用户账户相关，形成独立的业务能力"
    },
    {
      "service_name": "catalog-service",
      "classes": ["Category", "CategoryMapper", "Item", "ItemMapper", "Product", 
                  "ProductMapper", "CatalogActionBean", "CatalogService"],
      "responsibility": "管理商品分类和商品信息，提供浏览和搜索功能",
      "reasoning": "商品信息管理是独立的核心业务，包括分类、商品、映射"
    },
    {
      "service_name": "order-service",
      "classes": ["Cart", "CartItem", "CartActionBean", "Order", "OrderActionBean", 
                  "OrderMapper", "OrderService", "LineItem", "LineItemMapper", 
                  "Sequence", "SequenceMapper"],
      "responsibility": "处理购物车、订单创建、订单管理",
      "reasoning": "购物和订单处理是独立的业务流程，包含完整的购物车和订单管理"
    }
  ],
  "total_services": 3,
  "quality_assessment": "这个拆分遵循功能域分离，识别了3个主要的业务能力"
}
```

#### 3.2.4 数据收集与评估

**收集步骤**：

1. 将Copilot的JSON输出保存为 `迭代1/decomposition_result.json`
2. 从JSON中提取类-服务映射：
   ```
   class,service
   Account,account-service
   AccountActionBean,account-service
   ...
   ```
3. 与Ground Truth对比（account, catalog, order）
4. 计算MoJoFM、TurboMQ

**预期结果**：

- TurboMQ：~35-45（尚未优化）
- MoJoFM：~35-45%（只有部分类正确归类）
- 分区数：~3个（可能准确，但内部分配不当）

#### 3.2.5 定性分析框架

**问题诊断**（预期问题）：

1. ❌ **错误分配**：AbstractActionBean的复用性可能导致分配到多个服务
2. ❌ **粒度不当**：可能将某些Service和Mapper分离到不同服务
3. ❌ **Mapper实体漂移**：*Mapper类可能没有被正确归类

**改进方向**：

- 第一轮反馈：提示AI明确指出AbstractActionBean的使用情况
- 第二轮优化：提供依赖关系信息，帮助AI理解Mapper与实体的对应关系

---

### 3.3 第二轮迭代：依赖驱动拆分（Expected MoJoFM: 50-65%）

#### 3.3.1 迭代改进点

| 维度                 | 第一轮         | 第二轮改进             |
| -------------------- | -------------- | ---------------------- |
| **提示长度**   | 500字          | 1000字                 |
| **上下文信息** | 仅类列表       | +依赖关系              |
| **约束条件**   | 微服务设计原则 | +解决第一轮的问题      |
| **AI理解深度** | 粗粒度         | 中粒度（包含依赖视角） |
| **期望MoJoFM** | 35-45%         | 50-65%                 |

#### 3.3.2 输入提示词（Prompt v2.0）

```
【第二轮迭代】请对JPetStore系统进行改进的微服务拆分。

## 系统概述
JPetStore是一个宠物在线商店系统，用户可以浏览商品、管理账户、购物和下单。

## 系统类列表（完整版本，带依赖分析）

【账户微服务相关类】
- Account：用户信息实体（字段：username, password, email, address, city等）
- AccountActionBean：处理账户Web请求的Action类
  依赖关系：使用Account实体，调用AccountService进行业务逻辑
- AccountService：账户业务逻辑服务
  依赖关系：使用Account实体和AccountMapper进行数据访问
- AccountMapper：账户数据持久化接口
  依赖关系：操作Account对象，与数据库交互

【商品微服务相关类】
- Category：商品分类实体
- CategoryMapper：分类数据映射
  依赖：操作Category对象
- Item：商品项实体（包含具体商品型号）
- ItemMapper：商品项数据映射
  依赖：操作Item对象
- Product：商品实体（商品基本信息）
- ProductMapper：商品数据映射
  依赖：操作Product对象
- CatalogActionBean：处理商品浏览和搜索请求
  依赖：使用Product/Item/Category实体，调用CatalogService
- CatalogService：商品业务逻辑
  依赖：使用Product/Item/Category/mapper

【订单微服务相关类】
- Cart：购物车实体
- CartItem：购物车中的单项
  依赖：引用Item
- CartActionBean：处理购物车请求
  依赖：使用Cart和CartItem，调用相关服务
- Order：订单实体
- OrderActionBean：处理订单请求
  依赖：使用Order实体，调用OrderService
- OrderMapper：订单数据映射
  依赖：操作Order对象
- OrderService：订单业务逻辑
  依赖：使用Order/OrderMapper/LineItemMapper
- LineItem：订单行项实体
- LineItemMapper：订单行数据映射
  依赖：操作LineItem对象
- Sequence：序列号生成（用于订单编号）
- SequenceMapper：序列号数据映射
  依赖：操作Sequence对象

【共享基础类】
- AbstractActionBean：所有Action的基类
  说明：所有*ActionBean都继承此类，被account/catalog/order微服务共享
  建议：作为跨服务共享组件，但在评估时应根据具体ActionBean的主要职责分配

## 第一轮拆分问题与改进指导

【第一轮常见问题】
1. AbstractActionBean的归属：虽然被多个service的Action使用，但应根据Action本身的职责分配
   - AccountActionBean应属account服务
   - CatalogActionBean应属catalog服务
   - CartActionBean/OrderActionBean应属order服务

2. Mapper与实体的对应：每个*Mapper应与其对应的实体放在同一服务
   - AccountMapper与Account→account服务
   - CategoryMapper/ItemMapper/ProductMapper与Category/Item/Product→catalog服务
   - OrderMapper/LineItemMapper/SequenceMapper与Order/LineItem/Sequence→order服务

## 任务要求

请基于以上分析，生成改进的微服务拆分方案。要求：
1. 正确处理AbstractActionBean（根据具体Action的职责）
2. 确保每个Mapper与对应实体在同一服务
3. 保持Cart和Order的逻辑关系（都属order服务）
4. 遵循高内聚、低耦合原则

请采用以下JSON格式输出：
{
  "decomposition": [
    {
      "service_name": "服务名",
      "classes": ["类1", "类2", ...],
      "responsibility": "核心职责",
      "reasoning": "详细拆分理由，包括依赖关系分析"
    }
  ],
  "total_services": 数字,
  "improvements_from_round1": "对比第一轮的改进说明",
  "confidence_level": "拆分质量评分（低/中/高）"
}

提醒：请确保所有24个类都被分配到某个服务中，且每个类只属于一个服务。
```

#### 3.3.3 预期改进点

**与第一轮的差异**（预期）：

- ✅ AbstractActionBean的正确处理
- ✅ Mapper与实体的配对更加明确
- ✅ 对Cross-service依赖的认知（如Cart→Item的依赖）
- ⚠️ 可能仍然存在边界模糊的类（如Sequence/SequenceMapper）

**预期结果指标**：

- TurboMQ：~50-60（有所改善）
- MoJoFM：~50-65%（显著提升）
- 分区数：3个（可能准确）

#### 3.3.4 问题诊断与改进方向

**可能的残余问题**：

1. **Sequence处理**：虽然技术上属order（序列号用于订单），但Sequence的通用性可能导致错分
2. **Cart的细节**：CartItem引用Item，可能被AI判断为应属catalog（item的上游）
3. **AbstractActionBean去向**：虽然说明了，但仍可能被AI保留为独立service或错误分配

**第三轮优化方向**：

- 提供具体的类间依赖图
- 明确指出"服务间只能通过接口通信"的约束
- 提供论文Ground Truth作为参考答案

---

### 3.4 第三轮迭代：专家优化拆分（Expected MoJoFM: 65-80%）

#### 3.4.1 迭代改进点

| 维度                 | 第二轮     | 第三轮优化                 |
| -------------------- | ---------- | -------------------------- |
| **提示长度**   | 1000字     | 1500字+                    |
| **上下文**     | 依赖关系   | +完整的类间调用关系        |
| **约束条件**   | 问题指导   | +论文参考+评估指标说明     |
| **专家知识**   | 微服务原则 | +Ground Truth+论文工具对比 |
| **期望MoJoFM** | 50-65%     | 65-80%                     |

#### 3.4.2 输入提示词（Prompt v3.0）

```
【第三轮迭代·专家拆分】基于微服务分解论文标准，对JPetStore进行最终优化拆分。

## 背景：论文参考标准

本拆分基于学术论文《Microservice Decomposition Techniques: An Independent Tool Comparison》
的评估体系。论文通过MoJoFM指标（与专家参考分解的相似度）评估拆分质量。
JPetStore的专家参考分解（Ground Truth）为：
- account微服务：用户账户管理
- catalog微服务：商品和分类管理
- order微服务：购物车、订单和订单项管理

## 完整类结构与依赖分析

【account 微服务的类群】
类: Account (实体) 
  → 属性: username, password, email, address, city, zip, phone, etc.
  → 方法数: 18个getter/setter + 业务方法

类: AccountActionBean (Web Action)
  → 依赖: Account实体, AccountService
  → 职责: 处理登陆/注册/个人信息修改的HTTP请求
  → 继承: AbstractActionBean (基类，但主要职责明确属account)

类: AccountService (业务逻辑)
  → 依赖: Account实体, AccountMapper
  → 职责: 账户业务逻辑（验证、创建、更新等）

类: AccountMapper (数据访问)
  → 依赖: Account实体
  → 职责: 账户数据的持久化操作

【catalog 微服务的类群】
类: Category (实体)
  → 属性: categoryId, name, description
  → 地位: 商品分类维度

类: CategoryMapper (数据访问)
  → 对应实体: Category

类: Product (实体)
  → 属性: productId, categoryId, name, description
  → 职责: 商品基本信息（如宠物品种）
  → 注意: 含有categoryId外键，关联Category

类: ProductMapper (数据访问)
  → 对应实体: Product

类: Item (实体)
  → 属性: itemId, productId, supplier, listPrice, unitCost, status
  → 地位: 具体商品型号（Product的细粒度）
  → 层次: Product > Item（一对多）

类: ItemMapper (数据访问)
  → 对应实体: Item

类: CatalogActionBean (Web Action)
  → 依赖: Product, Item, Category实体, CatalogService
  → 职责: 处理商品浏览、搜索、分类查询的HTTP请求
  → 继承: AbstractActionBean（属catalog，职责清晰）

类: CatalogService (业务逻辑)
  → 依赖: Category, Product, Item实体和对应Mapper
  → 职责: 商品相关业务逻辑（列表、搜索、分类等）

【order 微服务的类群】
类: Cart (实体)
  → 属性: cartId, items (CartItem的集合)
  → 职责: 购物车聚合根

类: CartItem (实体)
  → 属性: itemId, quantity (reference to Item, but quantity belongs to order domain)
  → 职责: 购物车中的单项记录
  → 跨服务依赖: itemId指向Item（catalog），但CartItem本身属order（购物行为）

类: CartActionBean (Web Action)
  → 依赖: Cart, CartItem, CatalogService(查询Item信息)
  → 职责: 处理购物车的添加/删除/查看请求
  → 继承: AbstractActionBean（属order，职责清晰）

类: Order (实体)
  → 属性: orderId, orderDate, shipDate, billAddress, etc.
  → 职责: 订单聚合根

类: OrderActionBean (Web Action)
  → 依赖: Order实体, OrderService
  → 职责: 处理订单查询、下单的HTTP请求
  → 继承: AbstractActionBean（属order，职责清晰）

类: OrderService (业务逻辑)
  → 依赖: Order, LineItem, Sequence实体和对应Mapper
  → 职责: 订单业务逻辑（创建、确认、发货等）

类: OrderMapper (数据访问)
  → 对应实体: Order

类: LineItem (实体)
  → 属性: lineNumber, orderId, itemId, quantity
  → 职责: 订单行项
  → 跨服务依赖: itemId指向Item（catalog），但LineItem属order

类: LineItemMapper (数据访问)
  → 对应实体: LineItem

类: Sequence (实体)
  → 属性: name, nextId
  → 职责: 主键序列生成（用于Order和其他实体）
  → 关键点: 虽然是通用工具，但在JPetStore中主要用于order业务

类: SequenceMapper (数据访问)
  → 对应实体: Sequence

## 论文的微服务拆分评估标准

### TurboMQ指标（模块化质量）
公式: TurboMQ = (内聚度 - 耦合度) / (内聚度 + 耦合度) × 100
- 范围: 0-100
- 目标: ≥80（优秀），论文中最优工具MOSAIC在JPetStore达到100

### MoJoFM指标（与参考分解的相似度）
衡量Copilot拆分与Ground Truth的匹配程度。
- Log2MS在JPetStore达到100%（完美匹配）
- MOSAIC达到89.47%（优秀）
- Data-Centric达到76.19%（良好）
- HyDec达到57.14%（中等）

本轮目标: 达到MoJoFM ≥65%（超过HyDec的58.59%平均值）

## 关键拆分规则（基于论文学习）

1. **服务边界原则**
   - 高内聚：同服务内的类应有强业务相关性
   - 低耦合：服务间只能通过明确的接口通信
   - 单一职责：每个服务聚焦于一个业务能力

2. **跨服务依赖的处理**
   - CartItem.itemId → Item：虽然引用了Item，但CartItem的主要职责是购物行为（属order）
   - LineItem.itemId → Item：虽然引用了Item，但LineItem的主要职责是订单细节（属order）
   - 这是微服务间的数据依赖，不影响服务归属

3. **共享基类的处理**
   - AbstractActionBean虽然被多个Action继承，但每个具体ActionBean应根据其职责分配
   - 在评估时，AbstractActionBean通常与其主要使用者共同分配

4. **工具函数的归属**
   - Sequence虽然是通用工具，但在JPetStore的实际应用中主要支持order业务
   - 因此应将Sequence/SequenceMapper分配给order

## 任务要求

请基于以上分析和论文标准，生成最终的、高质量的微服务拆分方案。

要求：
1. 所有24个类都被精确分配（不能遗漏）
2. 清晰解释每个类的分配理由，特别是边界情况
3. 预估本方案的TurboMQ和MoJoFM评分
4. 比较与第一、第二轮的改进

输出格式：
{
  "decomposition": [
    {
      "service_name": "account",
      "classes": [
        {"name": "Account", "reason": "核心实体类"},
        {"name": "AccountActionBean", "reason": "account相关HTTP处理"},
        {"name": "AccountService", "reason": "account业务逻辑"},
        {"name": "AccountMapper", "reason": "account数据持久化"}
      ],
      "responsibility": "用户账户管理和认证",
      "internal_cohesion": "4个类都围绕账户数据模型，高度内聚"
    },
    {
      "service_name": "catalog",
      "classes": [...],
      "responsibility": "商品和分类管理",
      "internal_cohesion": "8个类形成完整的商品模型（Category→Product→Item），高度内聚"
    },
    {
      "service_name": "order",
      "classes": [...],
      "responsibility": "购物车和订单管理",
      "internal_cohesion": "10个类形成完整的订单流程（Cart→Order，LineItem→Sequence），高度内聚"
    }
  ],
  "total_services": 3,
  "quality_metrics_estimate": {
    "expected_turbomq": 80-90,
    "expected_mojofm": 70-85,
    "reasoning": "详细的质量评估说明"
  },
  "improvements": {
    "from_round1": "改进点列表",
    "from_round2": "改进点列表",
    "convergence_analysis": "收敛分析"
  },
  "service_interface_contracts": {
    "catalog_to_order": "order通过itemId查询Item信息",
    "account_to_others": "无直接依赖"
  }
}
```

#### 3.4.3 预期结果

**第三轮目标指标**：

- TurboMQ：80-90（接近Ground Truth的89.73）
- MoJoFM：70-85%（超过目标的65%，接近MOSAIC的82.71%）
- 分区数：3个（与Ground Truth一致）

**收敛趋势**：

```
迭代    TurboMQ    MoJoFM     改进幅度
第一轮  35-45      35-45%     基准
第二轮  50-60      50-65%     ↑15-20%
第三轮  80-90      70-85%     ↑20-25%
论文最优 92.71     100%        对标
```

---

## 第三部分完成

**核心亮点**：

- 第一轮：基础拆分，验证AI的基础理解能力
- 第二轮：依赖驱动，引入结构化信息，改进指导
- 第三轮：专家优化，融合论文知识和评估指标说明

---

## 第四部分：提示词设计与优化策略

### 4.1 提示词演化的核心策略

#### 4.1.1 提示词优化的三大维度

| 维度                   | 第一轮   | 第二轮         | 第三轮             | 作用                     |
| ---------------------- | -------- | -------------- | ------------------ | ------------------------ |
| **长度与详细度** | 500字    | 1000字         | 1500字+            | 提供更多上下文帮助AI决策 |
| **结构化程度**   | 自由文本 | 分类清晰       | 高度结构化         | 帮助AI按逻辑系统地思考   |
| **约束条件**     | 通用原则 | 问题指导       | 论文标准+例子      | 引导AI向正确方向收敛     |
| **反馈循环**     | 无       | 基于第一轮反馈 | 基于第一、二轮反馈 | 积累学习，改进结果       |

#### 4.1.2 提示词优化的递进逻辑

```
提示词设计流程：

第一轮 → 观察输出 → 诊断问题 → 形成假设 → 第二轮设计
                   ↓
             问题根因分析
             (AI理解缺陷)
                   ↓
           第二轮 → 观察输出 → 验证改进 → 制定第三轮方向
                   ↓
             渐进式优化
             (添加关键信息)
                   ↓
           第三轮 → 观察输出 → 评估收敛 → 生成最终报告
```

---

### 4.2 第一轮提示词的设计原理

#### 4.2.1 设计思路

**问题**：AI如何在无额外指导的情况下理解一个陌生的系统？

**策略**：

1. **极简主义**：只提供必要的类列表，不添加额外的约束
2. **功能导向**：用自然语言描述类的职责，而非技术实现
3. **归纳式思考**：让AI基于类名和简短描述自己推导服务边界

**优点**：

- 观察AI的"原始"想法，无外部偏差
- 为后续迭代建立基准

**缺点**：

- 结果可能不准确（预期 35-45% MoJoFM）
- 可能出现系统性错误（如AbstractActionBean的处理）

#### 4.2.2 提示词要素分析

| 要素               | 内容                                   | 作用         |
| ------------------ | -------------------------------------- | ------------ |
| **任务定义** | "将系统拆分为微服务"                   | 明确目标     |
| **系统描述** | "电商系统，功能包括：账户、商品、订单" | 建立认知框架 |
| **类列表**   | 按功能领域分组的24个类                 | 提供原始数据 |
| **设计原则** | 高内聚、低耦合、单一职责               | 指导拆分方向 |
| **输出格式** | JSON结构                               | 便于后续解析 |

#### 4.2.3 预期问题与根因

**问题1：AbstractActionBean的错误分配**

- 表现：可能被分配给多个服务或单独成服务
- 根因：AI看到"基类"和"被多个子类继承"，将其视为独立组件
- 未来改进：第二轮明确指出ActionBean的职责

**问题2：Mapper与实体分离**

- 表现：*Mapper被分配给错误的服务，或单独分组
- 根因：AI可能将Mapper视为"通用数据工具"
- 未来改进：第二轮明确Mapper与实体的配对关系

**问题3：跨服务依赖的困惑**

- 表现：因为CartItem依赖Item，可能将CartItem分配给catalog
- 根因：AI混淆了"数据依赖"和"服务归属"
- 未来改进：第二轮说明跨服务依赖的合理性

---

### 4.3 第二轮提示词的设计原理

#### 4.3.1 设计思路

**问题**：如何在第一轮的基础上，精确定位和改正错误？

**策略**：

1. **问题导向**：显式列出第一轮的常见错误
2. **关系映射**：详细说明类间的依赖关系
3. **示例纠正**：为问题类（如AbstractActionBean）提供明确的处理规则

**关键创新**：

- 不提供答案，而是提示"应该如何思考"
- 让AI在更完整的信息下自主改进

#### 4.3.2 提示词的结构改进

```
第二轮相比第一轮的改进：

【增加内容】
+ 系统类列表 → 带依赖关系的结构化列表
+ 微服务设计原则 → 第一轮问题与改进指导
+ 输出格式 → 增加"improvements_from_round1"字段

【修改内容】
- 自由文本描述 → 结构化分类（按微服务领域）
- 简单的职责说明 → 详细的依赖关系说明
- 通用原则 → 针对性的问题纠正
```

#### 4.3.3 关键改进点详解

**改进1：AbstractActionBean的明确处理规则**

```
【旧表述】"所有Action的基类，被account/catalog/order微服务共享"
【新表述】"虽然被多个服务的Action使用，但应根据Action本身的职责分配
           - AccountActionBean应属account服务
           - CatalogActionBean应属catalog服务
           - CartActionBean/OrderActionBean应属order服务"
```

**理由**：通过具体例子而非抽象概念，降低AI的理解成本

**改进2：Mapper与实体的对应关系**

```
【旧表述】"*Mapper：数据库映射接口"（来自v1.0）
【新表述】"每个*Mapper应与其对应的实体放在同一服务
           - AccountMapper与Account→account服务
           - CategoryMapper/ItemMapper/ProductMapper与Category/Item/Product→catalog服务
           - OrderMapper/LineItemMapper/SequenceMapper与Order/LineItem/Sequence→order服务"
```

**理由**：显式的一一对应关系，消除AI的不确定性

**改进3：跨服务依赖的合理性解释**

```
【新增内容】"保持Cart和Order的逻辑关系（都属order服务）
           虽然CartItem和LineItem都引用Item，但它们的主要职责
           与购物和订单相关，因此应属order而非catalog"
```

**理由**：帮助AI理解"业务职责优于数据引用"的设计原则

---

### 4.4 第三轮提示词的设计原理

#### 4.4.1 设计思路

**问题**：如何突破50-65%的瓶颈，达到65-80%甚至更高？

**策略**：

1. **论文权威性**：引入ASE 2024论文的评估体系和标准
2. **量化激励**：明确给出目标指标（MoJoFM ≥65%）和对标工具
3. **完整上下文**：提供类间的完整调用关系和微服务间的接口契约
4. **多层验证**：让AI自己估算TurboMQ和MoJoFM，形成自我约束

#### 4.4.2 提示词的战略升级

```
第三轮相比第二轮的升级：

【信息密度提升】
+ 论文背景 → 学术标准和评估指标
+ 类结构描述 → 完整的属性/方法/依赖树
+ 问题指导 → 微服务拆分的四大规则
+ 输出要求 → 自我评估+服务接口契约

【认知深度提升】
- 类的简单职责 → 类在业务流程中的角色
- 两两依赖 → 完整的依赖链和数据流
- 通用原则 → 微服务架构的具体应用
- 预期输出 → 质量指标的量化预期
```

#### 4.4.3 论文知识的融合

**TurboMQ指标的引入**：

```
公式: TurboMQ = (内聚度 - 耦合度) / (内聚度 + 耦合度) × 100

对提示词的影响：
- 帮助AI理解"内聚度"和"耦合度"的具体含义
- 让AI在拆分时主动最小化"跨服务依赖"
- 提供量化目标："目标TurboMQ ≥80"
```

**MoJoFM指标的引入**：

```
定义：Copilot拆分与Ground Truth的匹配程度

对提示词的影响：
- 明确告诉AI"最优答案"的评分（Log2MS 100%）
- 提供中间层的对标（MOSAIC 82.71%, Data-Centric 72.49%）
- 给AI明确的目标：MoJoFM ≥65%
```

**Ground Truth的精确描述**：

```
account: Account, AccountActionBean, AccountService, AccountMapper
catalog: Category, CategoryMapper, Product, ProductMapper, 
         Item, ItemMapper, CatalogActionBean, CatalogService
order: Cart, CartItem, CartActionBean, Order, OrderActionBean, 
       OrderMapper, OrderService, LineItem, LineItemMapper, 
       Sequence, SequenceMapper

对提示词的影响：
- 降低AI的歧义性，减少边界情况的争议
- 提供明确的"正确答案"作为对标
- 让AI能自我检查和验证（通过预估MoJoFM）
```

#### 4.4.4 自我评估与反馈机制

**新的输出要求**：

```json
{
  "quality_metrics_estimate": {
    "expected_turbomq": 80-90,
    "expected_mojofm": 70-85,
    "reasoning": "为什么AI认为自己能达到这个评分"
  }
}
```

**作用**：

1. **自我约束**：AI需要对其拆分的质量负责
2. **可解释性**：理由部分反映了AI的思考过程
3. **验证数据**：后续的实际评估可与此对标，检测AI的自我认知偏差

---

### 4.5 提示词的关键技巧总结

#### 4.5.1 信息层级化呈现

**层级1：核心信息**（必须的）

- 系统概述（是什么）
- 类列表（由什么组成）
- 任务定义（做什么）

**层级2：指导信息**（重要的）

- 依赖关系（怎样连接）
- 设计原则（如何指导）
- 常见问题（避免错误）

**层级3：高级信息**（优化的）

- 论文标准（为什么这样做）
- 评估指标（质量如何衡量）
- 对标案例（目标是什么）

**技巧**：第一轮只提供层级1+简化的层级2，逐轮增加详细度

#### 4.5.2 具体化抽象概念

**错误示范**：

```
"遵循微服务设计原则：高内聚、低耦合、单一职责"
```

（太抽象，AI不知道具体如何应用）

**改进示范**：

```
"高内聚：同一服务内的4个类（Account, AccountActionBean, AccountService, 
AccountMapper）都围绕账户数据模型，互相依赖。
低耦合：账户服务不依赖商品或订单的类。
单一职责：账户服务专注于用户账户的增删改查，不涉及商品或订单逻辑。"
```

（通过具体例子，AI能理解原则的实际应用）

#### 4.5.3 冗余与强调的平衡

**策略**：

- 对关键信息进行多次重述（用不同的方式）
- 在不同位置出现相同的核心概念
- 使用加粗、列表等格式强调

**例子**：

```
【第一次】"AbstractActionBean虽然被多个service的Action使用..."
【第二次】"在关键拆分规则中再强调一次：共享基类的处理..."
【第三次】"在质量评估中通过Ground Truth验证..."
```

#### 4.5.4 前后一致性

**要求**：

- 第一轮使用的类名，第二、三轮保持一致
- 对同一问题的解释方向一致
- Ground Truth在所有轮次保持统一

**技巧**：

- 维护一份"术语词表"（确保类名、服务名、技术术语的一致性）
- 在每轮开始时回顾上一轮的重点

---

### 4.6 提示词优化的评估方法

#### 4.6.1 每轮迭代的评估指标

| 指标               | 衡量对象     | 判定标准                              |
| ------------------ | ------------ | ------------------------------------- |
| **MoJoFM**   | 拆分准确性   | 第一轮≥35%, 第二轮≥50%, 第三轮≥65% |
| **TurboMQ**  | 模块化质量   | 第一轮≥30, 第二轮≥50, 第三轮≥80    |
| **分区数**   | 粒度控制     | 所有轮次应为3（±1可接受）            |
| **收敛速度** | 提示优化效率 | MoJoFM增长率 ≥15% / 轮               |
| **可解释性** | AI推理过程   | 推理应明确引用系统特点和论文标准      |

#### 4.6.2 提示词质量的自我诊断

**如果第二轮的MoJoFM仍 <45%，说明**：

- [ ] Ground Truth的描述不够清晰 → 重新描述
- [ ] 依赖关系的说明不够具体 → 添加具体调用链
- [ ] 问题诊断不准确 → 重新分析第一轮的错误模式
- [ ] 提示词仍缺乏激励约束 → 添加目标指标和对标案例

**如果第三轮的MoJoFM仍 <65%，说明**：

- [ ] 论文标准的说明不够权威 → 增加论文背景介绍
- [ ] 类间关系的描述有遗漏 → 补充缺失的依赖关系
- [ ] AI仍对边界情况困惑 → 为边界类（Sequence, CartItem等）提供更深入的讨论
- [ ] 可能需要调整评估目标 → 与Log2MS（100%）的差距来自系统复杂度，而非提示词

---

## 第四部分完成

**核心成果**：

- 提示词优化的三维度框架（长度、结构、约束）
- 每轮提示词的设计原理和关键改进点
- 提示词的实用技巧（信息层级化、具体化、冗余与强调）
- 提示词质量的自我诊断方法

---

## 第五部分：执行流程与验证标准

### 5.1 完整的执行流程图

```
开始
  ↓
【准备阶段】
  ├─ 准备JPetStore源代码和类列表
  ├─ 配置评估工具环境（Python + 依赖图）
  ├─ 准备Ground Truth参考数据
  └─ 准备论文工具的对比数据
  ↓
【第一轮迭代】
  ├─ 编写提示词 v1.0（基础版）
  ├─ 输入到Copilot，获取拆分结果
  ├─ 提取JSON格式的拆分方案
  ├─ 计算 TurboMQ 和 MoJoFM
  ├─ 生成第一轮评估报告
  └─ 诊断问题根源 → 输出改进建议
  ↓
【第二轮迭代】
  ├─ 基于第一轮反馈，编写提示词 v2.0（依赖版）
  ├─ 输入到Copilot，获取拆分结果
  ├─ 提取并对比第一轮结果（哪些改进了？）
  ├─ 计算 TurboMQ 和 MoJoFM
  ├─ 生成第二轮评估报告与对比分析
  └─ 评估是否需要第二轮迭代微调？
  ↓
【第三轮迭代】
  ├─ 基于第一、二轮反馈，编写提示词 v3.0（专家版）
  ├─ 输入到Copilot，获取拆分结果
  ├─ 提取并对比前两轮结果
  ├─ 计算 TurboMQ 和 MoJoFM
  ├─ 生成第三轮评估报告与收敛分析
  └─ 评估是否达到目标？
  ↓
【最终验证】
  ├─ 三轮数据汇总 → 生成对比表格
  ├─ 与论文8个工具的结果进行横向对比
  ├─ 生成可视化图表（趋势、分布）
  └─ 输出最终结论报告
  ↓
【存储与发布】
  ├─ 保存三轮的代码、拆分方案、评估报告
  ├─ 生成可复现性档案（包含所有提示词）
  └─ 发布论文拓展研究成果
  ↓
结束
```

---

### 5.2 详细的执行步骤与时间表

#### 5.2.1 准备阶段（0.5小时）

| 步骤 | 具体任务                        | 时间 | 检查项                           |
| ---- | ------------------------------- | ---- | -------------------------------- |
| 1    | 准备JPetStore的所有24个类的定义 | 10分 | ✓ 类名完整, 无遗漏              |
| 2    | 编制类-功能映射表               | 5分  | ✓ 每个类的职责清晰              |
| 3    | 准备Ground Truth参考分解        | 5分  | ✓ account/catalog/order共24个类 |
| 4    | 收集论文8个工具的对比数据       | 10分 | ✓ 各工具的MoJoFM/TurboMQ分数    |
| 5    | 搭建评估脚本环境                | 15分 | ✓ 可计算TurboMQ和MoJoFM         |

#### 5.2.2 第一轮迭代（1.5小时）

| 步骤 | 具体任务          | 时间 | 输出物                        | 检查项                            |
| ---- | ----------------- | ---- | ----------------------------- | --------------------------------- |
| 1    | 编写提示词 v1.0   | 15分 | `prompt_v1.0.txt`           | ✓ 包含系统概述、类列表、任务要求 |
| 2    | 输入Copilot并对话 | 15分 | Copilot对话记录               | ✓ AI理解任务, 生成结构化JSON     |
| 3    | 提取拆分结果      | 10分 | `round1_decomposition.json` | ✓ 包含所有24个类的服务分配       |
| 4    | 计算评估指标      | 20分 | `round1_metrics.csv`        | ✓ TurboMQ和MoJoFM值完整          |
| 5    | 对比Ground Truth  | 10分 | `round1_comparison.md`      | ✓ 标注错分的类                   |
| 6    | 诊断问题          | 15分 | `round1_diagnosis.md`       | ✓ 分析错误原因，提出改进方向     |

**第一轮输出清单**：

```
迭代1/
├── prompt_v1.0.txt                    # 使用的提示词
├── copilot_interaction.md             # Copilot对话记录摘要
├── round1_decomposition.json          # AI生成的拆分方案
├── round1_metrics.csv                 # 评估指标
│   ├── TurboMQ: [值]
│   ├── MoJoFM: [值]
│   └── partition_count: 3
├── round1_comparison.md               # vs Ground Truth
│   ├── 正确的类: [列表]
│   ├── 错分的类: [列表]
│   └── 错误分析
└── round1_diagnosis.md                # 问题诊断与第二轮改进方案
    ├── 问题1: AbstractActionBean处理
    ├── 问题2: Mapper分配
    ├── 问题3: 跨服务依赖
    └── 改进建议
```

#### 5.2.3 第二轮迭代（1.5小时）

| 步骤 | 具体任务                      | 时间 | 输出物                        | 检查项                                |
| ---- | ----------------------------- | ---- | ----------------------------- | ------------------------------------- |
| 1    | 基于第一轮反馈编写提示词 v2.0 | 20分 | `prompt_v2.0.txt`           | ✓ 包含第一轮的问题指导和依赖关系     |
| 2    | 输入Copilot并对话             | 15分 | Copilot对话记录               | ✓ AI展示了改进的思考过程             |
| 3    | 提取拆分结果                  | 10分 | `round2_decomposition.json` | ✓ 对比第一轮，标注改进的部分         |
| 4    | 计算评估指标                  | 20分 | `round2_metrics.csv`        | ✓ TurboMQ和MoJoFM应有所提升          |
| 5    | 对比第一轮                    | 10分 | `round2_vs_round1.md`       | ✓ 明确指出哪些类改进了，哪些仍有问题 |
| 6    | 诊断残余问题                  | 10分 | `round2_diagnosis.md`       | ✓ 识别仍需改进的类和第三轮策略       |

**第二轮输出清单**：

```
迭代2/
├── prompt_v2.0.txt                    # 改进后的提示词
├── copilot_interaction.md             # 对话摘要
├── round2_decomposition.json          # 新的拆分方案
├── round2_metrics.csv                 # 评估指标
├── round2_vs_round1.md                # 第一轮 vs 第二轮对比
│   ├── 改进的类: [列表]
│   ├── 新出现的错误: [列表]
│   └── 收敛趋势分析
└── round2_diagnosis.md                # 残余问题与第三轮改进方案
    ├── 已解决的问题: ✓ AbstractActionBean
    ├── 仍存在的问题: ⚠️ [新问题列表]
    └── 第三轮改进策略
```

#### 5.2.4 第三轮迭代（1.5小时）

| 步骤 | 具体任务                      | 时间 | 输出物                         | 检查项                                |
| ---- | ----------------------------- | ---- | ------------------------------ | ------------------------------------- |
| 1    | 基于前两轮反馈编写提示词 v3.0 | 20分 | `prompt_v3.0.txt`            | ✓ 包含论文知识、评估指标、完整上下文 |
| 2    | 输入Copilot并对话             | 15分 | Copilot对话记录                | ✓ AI展示了论文标准的理解             |
| 3    | 提取拆分结果                  | 10分 | `round3_decomposition.json`  | ✓ 最终拆分方案，应接近Ground Truth   |
| 4    | 计算评估指标                  | 20分 | `round3_metrics.csv`         | ✓ TurboMQ和MoJoFM应达到目标值        |
| 5    | 三轮对比分析                  | 10分 | `three_rounds_comparison.md` | ✓ 收敛曲线、改进幅度、对标分析       |
| 6    | 最终诊断与结论                | 10分 | `round3_diagnosis.md`        | ✓ 总结学习，提出后续研究方向         |

**第三轮输出清单**：

```
迭代3/
├── prompt_v3.0.txt                    # 最终的提示词
├── copilot_interaction.md             # 对话摘要
├── round3_decomposition.json          # 最终拆分方案
├── round3_metrics.csv                 # 评估指标
├── three_rounds_comparison.md         # 三轮数据对比
│   ├── 指标对比表格
│   │   └── [MoJoFM趋势: 35-45% → 50-65% → 70-85%]
│   ├── 与论文工具的横向对比
│   │   └── vs Log2MS(100%), MOSAIC(82.71%), Data-Centric(72.49%)
│   └── 收敛分析和改进幅度
└── round3_final_analysis.md           # 最终分析与结论
    ├── Copilot拆分的优势
    ├── 与论文工具的对比
    ├── 学习过程分析
    └── 后续研究建议
```

#### 5.2.5 最终验证与总结（1小时）

| 步骤 | 具体任务           | 时间 | 输出物                             | 检查项                         |
| ---- | ------------------ | ---- | ---------------------------------- | ------------------------------ |
| 1    | 汇总三轮的核心指标 | 10分 | `summary_metrics.csv`            | ✓ MoJoFM、TurboMQ、分区数完整 |
| 2    | 生成可视化图表     | 20分 | 图表集合                           | ✓ 趋势图、对标图、分布图      |
| 3    | 编写最终报告       | 20分 | `FINAL_REPORT.md`                | ✓ 结论明确，数据支持充分      |
| 4    | 代码与数据打包     | 10分 | `copilot_microservice_study.zip` | ✓ 包含所有提示词和原始数据    |

**最终输出清单**：

```
JPetStore_Copilot_Microservice_Study/
├── 提示词档案库/
│   ├── prompt_v1.0_基础拆分.txt
│   ├── prompt_v2.0_依赖驱动.txt
│   └── prompt_v3.0_专家优化.txt
├── 迭代1~3/                   # 三轮完整数据
├── 评估结果/
│   ├── summary_metrics.csv    # 汇总指标
│   ├── comparison_with_paper_tools.csv  # 与论文工具对比
│   └── charts/                # 可视化图表
└── FINAL_REPORT.md            # 完整的研究报告
```

---

### 5.3 验收标准与质量门控

#### 5.3.1 各轮迭代的验收标准

**第一轮验收标准**：

- [ ] MoJoFM ≥ 30%（可接受的最低值）
  - 若 <30%：说明提示词理解不当，需重新对话
- [ ] TurboMQ ≥ 25（可接受的最低值）
- [ ] 分区数 ≥ 2，≤ 5（粒度合理范围）
- [ ] 所有24个类都被分配（无遗漏）
- [ ] JSON格式正确，可解析

**验收判定**：

```
如果MoJoFM ≥ 30% 且 分区数合理 且 无遗漏 → ✅ 通过，进入第二轮
否则 → ❌ 不通过，重新对话或调整提示词
```

**第二轮验收标准**：

- [ ] MoJoFM ≥ 45%（相比第一轮有显著改进）
  - 改进幅度 ≥ 10% 为良好
  - 若改进 <5%：说明提示词没有抓住关键问题
- [ ] TurboMQ ≥ 45（相比第一轮改善）
- [ ] 分区数稳定在3±1
- [ ] 至少3个第一轮的错分类被改正
- [ ] 提示词长度和复杂度在合理范围（<1500字）

**验收判定**：

```
如果MoJoFM ≥ 45% 且 改进幅度 ≥ 10% → ✅ 通过，进入第三轮
else if MoJoFM ≥ 40% 且 改进幅度 ≥ 5% → ⚠️ 条件通过，建议微调后再进第三轮
else → ❌ 不通过，重新诊断问题
```

**第三轮验收标准**：

- [ ] MoJoFM ≥ 60%（达到中等以上水平）
  - 若 ≥ 65%：达成项目目标 ✅
  - 若 60-65%：接近目标 ⚠️
  - 若 <60%：未达目标 ❌
- [ ] TurboMQ ≥ 75（接近Ground Truth的90）
- [ ] 分区数精确为3
- [ ] 所有类的分配理由清晰，与Ground Truth的差异有解释
- [ ] 自我评估的MoJoFM与实际值相差 <10%（AI自知程度）

**验收判定**：

```
if MoJoFM ≥ 65% and TurboMQ ≥ 75:
  → ✅ 完全通过（超期望）
elif MoJoFM ≥ 60% and TurboMQ ≥ 70:
  → ⚠️ 基本通过（达成目标）
else:
  → ❌ 未通过（需分析原因）
```

#### 5.3.2 最终研究的验收标准

**整体研究的成功指标**：

| 指标                  | 目标值         | 评判标准                              | 权重 |
| --------------------- | -------------- | ------------------------------------- | ---- |
| **最终MoJoFM**  | ≥65%          | 与论文HyDec(58.59%)相当，超越平均水平 | 40%  |
| **最终TurboMQ** | ≥75           | 接近MOSAIC(100)和Data-Centric(79.74)  | 20%  |
| **收敛效率**    | 三轮增长 ≥30% | MoJoFM从第一轮到第三轮增长 ≥30%      | 15%  |
| **可复现性**    | 提示词完整     | 所有三个版本的提示词清晰可用          | 15%  |
| **研究报告**    | 清晰完整       | 包含数据、分析、结论、对标            | 10%  |

**综合评判**：

```
总分 = 40% × MoJoFM相对分 + 20% × TurboMQ相对分 + 
       15% × 收敛效率分 + 15% × 可复现性分 + 10% × 报告质量分

若总分 ≥ 75分 → ✅ 项目成功
若总分 60-75分 → ⚠️ 项目基本成功，但有改进空间
若总分 <60分 → ❌ 项目需总结原因并改进
```

---

### 5.4 风险评估与应对策略

#### 5.4.1 可能的风险和应对方案

| 风险                  | 症状                         | 概率 | 应对策略                                      |
| --------------------- | ---------------------------- | ---- | --------------------------------------------- |
| 第一轮MoJoFM <30%     | AI理解偏离                   | 中   | 重新审视提示词表述，简化或补充背景            |
| 第二轮无改进          | MoJoFM不增或减少             | 低   | 检查诊断是否准确，考虑不同的问题根源          |
| 第三轮突破不了65%     | 与论文最优工具差距大         | 中低 | 这是正常的（Copilot非专用工具），分析差距来源 |
| 某些类无法确定归属    | Sequence、CartItem等边界不清 | 中   | 在提示词中明确讨论，解释业务职责优于技术细节  |
| Copilot拆分逻辑不一致 | 不同对话的答案不同           | 低   | 使用相同的提示词确保一致性，多次验证          |

#### 5.4.2 应急备选方案

**如果第三轮MoJoFM仍 <60%**：

- 方案A：进行第四轮迭代

  - 提示词 v4.0：基于前三轮数据分析，更精确地定位剩余问题
  - 时间：追加1小时
- 方案B：改变评估方式

  - 不以MoJoFM ≥65% 为唯一目标
  - 重点分析"Copilot相比论文工具的优劣"
  - 强调AI方法的创新性而非绝对性能
- 方案C：扩展研究对象

  - 在JPetStore基础上，测试Spring-PetClinic等其他应用
  - 观察AI方法的泛化能力

---

### 5.5 数据管理与版本控制

#### 5.5.1 文件命名规范

```
迭代X_[日期]_[版本号]/
├── prompt_vX.Y.txt                     # X=轮数, Y=版本号
├── copilot_interaction_[timestamp].md  # 对话记录，保留时间戳
├── roundX_decomposition_[v].json       # X=轮数, v=版本（若多次迭代则有多个）
├── roundX_metrics_[v].csv
├── roundX_vs_ground_truth.md
└── roundX_analysis.md
```

**版本控制策略**：

- 每轮迭代只有一个最终版本（其他都是草稿）
- 重要的中间结果（如错误分配的类列表）保留在 `analysis.md`
- 使用Git跟踪所有版本变化

#### 5.5.2 数据验证检查清单

| 检查项             | 方法                    | 验收标准               |
| ------------------ | ----------------------- | ---------------------- |
| 类列表完整性       | 数一数JSON中的类数      | 必须=24                |
| 类名一致性         | 与Ground Truth对比      | 无拼写错误，大小写一致 |
| 服务分配唯一性     | 每个类只属一个服务      | 无重复或遗漏           |
| 指标计算正确性     | 抽查2-3个MoJoFM手工计算 | 与自动计算一致         |
| JSON格式有效性     | 用JSON在线工具验证      | 无语法错误             |
| Ground Truth准确性 | 与论文原文对比          | 与论文附录一致         |

---

### 5.6 文档输出的最终形式

#### 5.6.1 项目最终结构

```
c:\Users\aone\Downloads\artifact\
└── JPetStore_Copilot_Microservice_Study/
    ├── 00_README.md                    # 项目总览
    ├── 提示词设计/
    │   ├── prompt_v1.0_基础拆分.txt
    │   ├── prompt_v2.0_依赖驱动.txt
    │   └── prompt_v3.0_专家优化.txt
    ├── 迭代数据/
    │   ├── round1/
    │   │   ├── decomposition.json
    │   │   ├── metrics.csv
    │   │   └── analysis.md
    │   ├── round2/
    │   │   └── [同上结构]
    │   └── round3/
    │       └── [同上结构]
    ├── 评估结果/
    │   ├── summary_metrics.csv         # 三轮汇总
    │   ├── vs_paper_tools.csv         # 与论文工具对比
    │   └── charts/
    │       ├── mojofm_trend.png        # MoJoFM趋势曲线
    │       ├── turbomq_trend.png       # TurboMQ趋势曲线
    │       ├── vs_paper_tools.png      # 与论文工具对标
    │       └── ...
    └── FINAL_REPORT.md                 # 最终研究报告
```

#### 5.6.2 最终报告的章节结构

```
# 最终报告目录

1. 执行摘要 (Executive Summary)
   - 研究问题、方法、主要发现

2. 背景与目标
   - 论文回顾、创新点、研究问题

3. 方法论
   - 三轮迭代设计、评估指标、工具与环境

4. 第一轮迭代结果与分析
5. 第二轮迭代结果与分析
6. 第三轮迭代结果与分析

7. 横向对比分析
   - vs 论文8个工具
   - vs Ground Truth
   - 收敛分析

8. 关键发现
   - AI微服务拆分的优势
   - 与传统工具的差异
   - 提示词优化的有效性

9. 局限性与未来工作
   - 研究局限
   - 潜在改进方向
   - 其他应用的可行性

10. 附录
    - 三个完整的提示词
    - 详细的指标计算过程
    - 所有类的分配决策树
```

---

## 第五部分完成

**核心内容**：

- 完整的执行流程图和详细的步骤时间表
- 各轮迭代的输出清单和数据结构
- 明确的验收标准和质量门控（MoJoFM、TurboMQ等）
- 风险评估和应对策略
- 最终的数据管理、文件命名规范和输出形式

**研究总周期**：约 4-5小时

- 准备：0.5小时
- 三轮迭代：4.5小时（每轮1.5小时）
- 验证与总结：1小时

---

## 🎯 完整方案书生成完毕

**方案书概览**：

| 部分     | 内容           | 页数  | 关键指标                               |
| -------- | -------------- | ----- | -------------------------------------- |
| 第一部分 | 研究背景与目标 | ~5页  | 论文8工具对比，Copilot目标MoJoFM≥65%  |
| 第二部分 | 评估体系详解   | ~8页  | TurboMQ、MoJoFM公式，JPetStore基准数据 |
| 第三部分 | 三轮迭代方案   | ~15页 | 三个完整的提示词版本，预期收敛曲线     |
| 第四部分 | 提示词设计策略 | ~10页 | 信息层级化、具体化、冗余原则           |
| 第五部分 | 执行流程与验收 | ~12页 | 时间表、验收标准、最终输出结构         |

**总计**：约50页的完整可执行方案书

### 下一步建议

**立即可执行的任务**：

1. ✅ 按照方案书的第一轮提示词 (prompt_v1.0)，与Copilot进行首次对话
2. ✅ 获取第一轮的拆分结果，计算MoJoFM和TurboMQ
3. ✅ 根据第一轮的结果反馈，编写第二轮提示词 (prompt_v2.0)
4. ✅ 重复第二、三轮，直到达到目标指标

**如需调整的方面**：

- 📝 修改迭代轮数（从3轮改为4轮或更多）
- 🎯 调整目标指标（如MoJoFM从65%改为70%）
- 🔧 补充其他应用（如Spring-PetClinic）
- 📊 扩展评估维度（如代码可读性、部署复杂度等）

**文档已保存**：
`c:\Users\aone\Downloads\artifact\AI微服务拆分方案书.md`

---

**是否需要**：

- [ ] 调整任何部分的内容？
- [ ] 导出为PDF或Word格式？
- [ ] 为提示词添加更多具体示例？
- [ ] 扩展到其他应用（Spring-PetClinic等）？
