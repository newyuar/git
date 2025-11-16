# CycleGAN 精简版

纯 CycleGAN 代码，仅保留核心功能，移除 pix2pix 及其他模型。

## 目录结构

```
cyclegan-minimal/
├── train.py              # 训练脚本
├── test.py               # 测试脚本
├── requirements.txt      # Python 依赖
├── models/               # 模型定义
│   ├── __init__.py
│   ├── base_model.py
│   ├── cycle_gan_model.py  # CycleGAN 核心模型
│   ├── test_model.py       # 单向测试模型
│   └── networks.py         # 网络架构
├── data/                 # 数据加载
│   ├── __init__.py
│   ├── base_dataset.py
│   ├── unaligned_dataset.py  # 非配对数据集
│   ├── single_dataset.py     # 单向测试数据集
│   └── image_folder.py
├── options/              # 命令行选项
│   ├── __init__.py
│   ├── base_options.py
│   ├── train_options.py
│   └── test_options.py
├── util/                 # 工具函数
│   ├── __init__.py
│   ├── util.py
│   ├── visualizer.py
│   ├── html.py
│   └── image_pool.py
├── datasets/             # 数据集目录
├── checkpoints/          # 模型保存目录
└── results/              # 测试结果目录
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 准备数据集

将数据组织为以下结构：
```
datasets/your_dataset/
├── trainA/   # 源域训练图片
├── trainB/   # 目标域训练图片
├── testA/    # 源域测试图片
└── testB/    # 目标域测试图片
```

### 3. 训练模型

```bash
python train.py --dataroot ./datasets/your_dataset --name your_exp --model cycle_gan
```

常用训练参数：
- `--dataroot`: 数据集路径
- `--name`: 实验名称
- `--gpu_ids`: GPU ID（如 `0,1,2` 或 `-1` 使用 CPU）
- `--batch_size`: 批次大小（默认 1）
- `--n_epochs`: 学习率保持不变的 epoch 数（默认 100）
- `--n_epochs_decay`: 学习率线性衰减的 epoch 数（默认 100）

### 4. 测试模型

**双向测试：**
```bash
python test.py --dataroot ./datasets/your_dataset --name your_exp --model cycle_gan
```

**单向测试（仅 A→B）：**
```bash
python test.py --dataroot ./datasets/your_dataset/testA --name your_exp --model test --no_dropout
```

### 5. 使用预训练模型

下载预训练模型（需要原仓库的下载脚本）并放置在 `checkpoints/model_name_pretrained/`，然后：

```bash
python test.py --dataroot ./datasets/horse2zebra/testA --name horse2zebra_pretrained --model test --no_dropout
```

## GPU 训练

```bash
# 单 GPU
python train.py --dataroot ./datasets/horse2zebra --name horse2zebra --model cycle_gan --gpu_ids 0

# 多 GPU（需要使用 torchrun）
torchrun --nproc_per_node=4 train.py --dataroot ./datasets/horse2zebra --name horse2zebra --model cycle_gan --norm sync_batch
```

## CPU 训练

```bash
python train.py --dataroot ./datasets/horse2zebra --name horse2zebra --model cycle_gan --gpu_ids -1
```

## 查看结果

- 训练中间结果：`checkpoints/your_exp/web/index.html`
- 测试结果：`results/your_exp/test_latest/index.html`

## 主要参数说明

### 网络架构
- `--netG`: 生成器类型（`resnet_9blocks`, `resnet_6blocks`, `unet_256`, `unet_128`）
- `--netD`: 判别器类型（`basic`, `n_layers`, `pixel`）
- `--ngf`: 生成器通道数（默认 64）
- `--ndf`: 判别器通道数（默认 64）

### 损失权重
- `--lambda_A`: A→B→A 循环一致性损失权重（默认 10.0）
- `--lambda_B`: B→A→B 循环一致性损失权重（默认 10.0）
- `--lambda_identity`: 恒等损失权重（默认 0.5）

### 数据增强
- `--preprocess`: 预处理方式（`resize_and_crop`, `crop`, `scale_width`, `none`）
- `--load_size`: 加载图片大小（默认 286）
- `--crop_size`: 裁剪图片大小（默认 256）

## 与原版区别

此精简版仅保留：
- ✅ CycleGAN 模型
- ✅ 必要的数据加载器（unaligned, single）
- ✅ 核心训练/测试脚本
- ✅ 基础工具函数

已移除：
- ❌ pix2pix 模型
- ❌ colorization 模型
- ❌ template 模板
- ❌ 文档、README、示例脚本
- ❌ Docker、Colab 笔记本
- ❌ 数据集下载脚本

## 参考

- CycleGAN 论文：https://arxiv.org/pdf/1703.10593.pdf
- 原始仓库：https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
