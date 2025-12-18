# AI驱动的微服务拆分研究报告
## 基于GitHub Copilot的JPetStore应用分解实验

**研究基础**: Microservice Decomposition Techniques: An Independent Tool Comparison (ASE 2024)  
**实验对象**: JPetStore (24类, 302方法, 电商应用)  
**AI工具**: GitHub Copilot (Claude Sonnet 4.5)  
**实验时间**: 2025年12月16日  
**研究者**: wyw121

---

## 📋 目录

1. [研究背景与动机](#1-研究背景与动机)
2. [实验设计与方法](#2-实验设计与方法)
3. [核心数据与结果](#3-核心数据与结果)
4. [横向对比分析](#4-横向对比分析)
5. [关键发现与洞察](#5-关键发现与洞察)
6. [研究贡献与价值](#6-研究贡献与价值)
7. [局限性与未来方向](#7-局限性与未来方向)
8. [附录：完整数据](#8-附录完整数据)

---

## 执行摘要

本研究基于ASE 2024论文《Microservice Decomposition Techniques: An Independent Tool Comparison》的评估标准，使用GitHub Copilot对JPetStore应用进行三轮迭代式微服务拆分实验。

**核心结论**:
- 🥈 **第3轮达到95.83% MoJoFM**，在论文的9个工具中排名第二
- 📈 **超越MOSAIC 6.36个百分点**，MOSAIC是论文中表现最稳定的工具
- 🎯 **仅比第一名Log2MS低4.17个百分点**，差距来自单一类的判断差异
- 💡 **发现AI的业务逻辑推理能力**：CartActionBean归属问题揭示了AI理解与专家定义的差异

---

（原文内容保持不变，移至 docs 目录便于归档与筛选）
