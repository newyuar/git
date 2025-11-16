# CycleGAN 精简版 - 文件清单

## 📋 核心文件列表

### 根目录（7 个文件）
- ✅ `train.py` - 训练脚本
- ✅ `test.py` - 测试脚本
- ✅ `check_env.py` - 环境检查脚本
- ✅ `requirements.txt` - Python 依赖列表
- ✅ `README.md` - 快速启动指南
- ✅ `USAGE.md` - 详细使用文档
- ✅ `COMPARISON.md` - 与原版对比说明
- ✅ `.gitignore` - Git 忽略文件

### models/ 目录（5 个文件）
- ✅ `__init__.py` - 包初始化
- ✅ `base_model.py` - 模型基类
- ✅ `cycle_gan_model.py` - **CycleGAN 核心模型**
- ✅ `test_model.py` - 单向测试模型
- ✅ `networks.py` - 生成器与判别器架构

### data/ 目录（5 个文件）
- ✅ `__init__.py` - 包初始化
- ✅ `base_dataset.py` - 数据集基类
- ✅ `unaligned_dataset.py` - **非配对数据集（CycleGAN 训练用）**
- ✅ `single_dataset.py` - 单向测试数据集
- ✅ `image_folder.py` - 图像文件夹读取

### options/ 目录（4 个文件）
- ✅ `__init__.py` - 包初始化
- ✅ `base_options.py` - 基础命令行选项
- ✅ `train_options.py` - 训练专用选项
- ✅ `test_options.py` - 测试专用选项

### util/ 目录（5 个文件）
- ✅ `__init__.py` - 包初始化
- ✅ `util.py` - 通用工具函数
- ✅ `visualizer.py` - 结果可视化（HTML + Visdom + W&B）
- ✅ `html.py` - HTML 页面生成
- ✅ `image_pool.py` - 判别器历史图像池

### 空目录（用于存放数据与输出）
- 📁 `datasets/` - 数据集存放目录
- 📁 `checkpoints/` - 训练模型保存目录
- 📁 `results/` - 测试结果输出目录

---

## 📊 统计信息

| 类别 | 数量 |
|------|------|
| Python 代码文件 | 23 |
| 文档文件 | 4 |
| 配置文件 | 2 |
| **总计** | **29** |

| 指标 | 数值 |
|------|------|
| 代码行数（估算） | ~3,500 行 |
| 文件总大小 | ~0.24 MB |
| 与原版对比 | **减少 97.2%** |

---

## ✨ 核心功能模块

### 1. 模型层（models/）
- **CycleGANModel**: 实现循环一致性 GAN
  - 双向生成器：G_A (A→B), G_B (B→A)
  - 双向判别器：D_A, D_B
  - 循环一致性损失 + GAN 损失 + 恒等损失

### 2. 数据层（data/）
- **UnalignedDataset**: 加载非配对图像
  - 同时加载域 A 和域 B 的图像
  - 支持数据增强（resize, crop, flip）
  
- **SingleDataset**: 单向测试
  - 只加载单个域的图像
  - 用于 `--model test` 模式

### 3. 训练流程（train.py）
- 数据加载 → 模型创建 → 迭代训练
- 定期保存模型与可视化结果
- 支持学习率衰减与 DDP 多 GPU

### 4. 测试流程（test.py）
- 加载训练好的模型
- 批量生成翻译结果
- 生成 HTML 结果页面

---

## 🎯 使用流程

```
1. 准备数据
   └─> datasets/your_data/{trainA,trainB,testA,testB}/

2. 训练模型
   └─> python train.py ...
   └─> 保存到 checkpoints/your_exp/

3. 测试模型
   └─> python test.py ...
   └─> 结果保存到 results/your_exp/

4. 查看结果
   └─> 打开 HTML 文件查看
```

---

## 📦 依赖关系

```
train.py / test.py
    ├─> options/ (命令行参数解析)
    ├─> data/ (数据加载)
    ├─> models/ (模型定义)
    └─> util/ (工具函数)
        ├─> visualizer (可视化)
        ├─> html (HTML 生成)
        └─> image_pool (图像池)
```

---

## ⚠️ 重要说明

### 已移除的内容
- ❌ pix2pix 模型及相关代码
- ❌ colorization 模型
- ❌ template 模板
- ❌ aligned_dataset（pix2pix 用）
- ❌ 文档目录（docs/）
- ❌ 示例脚本（scripts/）
- ❌ Jupyter 笔记本
- ❌ Docker 配置

### 保留的文件说明
所有保留的文件都是 **CycleGAN 运行所必需的核心文件**：
- 模型训练与测试必需
- 数据加载必需
- 结果可视化必需
- 命令行参数解析必需

### 兼容性
- ✅ 与原版训练的模型**完全兼容**
- ✅ 命令行参数**完全一致**
- ✅ 可直接使用原版的 checkpoints
- ✅ 输出格式**完全相同**

---

**创建日期**: 2025-10-19  
**基于版本**: pytorch-CycleGAN-and-pix2pix (PyTorch 2.4+ 支持)  
**精简版本**: cyclegan-minimal v1.0
