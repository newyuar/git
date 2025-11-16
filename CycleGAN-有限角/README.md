# 🚀 CycleGAN 精简版 - 快速启动

## 📦 这是什么？

这是一个**纯净的 CycleGAN 实现**，从原版 pytorch-CycleGAN-and-pix2pix 中提取，**移除了所有非 CycleGAN 相关的代码**。

- ✅ **体积减少 97%**：从 8.78 MB 缩减到 0.24 MB
- ✅ **代码简洁**：只有 23 个核心文件
- ✅ **功能完整**：保留 CycleGAN 所有功能
- ✅ **完全兼容**：可直接使用原版的预训练模型

## ⚡ 5 分钟快速开始

### 步骤 1：安装依赖

```bash
pip install -r requirements.txt
```

**最低要求**：
- Python 3.8+
- PyTorch 2.0+
- 约 300MB 磁盘空间（用于依赖包）

### 步骤 2：检查环境

```bash
python check_env.py
```

如果看到 "✓ 所有检查通过"，说明环境配置正确。

### 步骤 3：准备数据

创建数据集目录并放入图片：

```bash
# Windows
mkdir datasets\horse2zebra\trainA datasets\horse2zebra\trainB
mkdir datasets\horse2zebra\testA datasets\horse2zebra\testB

# Linux/Mac
mkdir -p datasets/horse2zebra/{trainA,trainB,testA,testB}
```

**目录结构**：
```
datasets/horse2zebra/
├── trainA/    # 马的训练图片
├── trainB/    # 斑马的训练图片
├── testA/     # 马的测试图片
└── testB/     # 斑马的测试图片
```

### 步骤 4A：训练新模型

```bash
python train.py --dataroot ./datasets/horse2zebra --name horse2zebra_exp --model cycle_gan
```

**常用参数**：
- `--gpu_ids 0`: 使用 GPU 0（`-1` 表示 CPU）
- `--batch_size 4`: 批次大小（默认 1）
- `--n_epochs 200`: 训练轮数

### 步骤 4B：使用预训练模型（推荐）

如果你有原版的预训练模型，放到 `checkpoints/horse2zebra_pretrained/` 目录：

```bash
python test.py --dataroot ./datasets/horse2zebra/testA \
               --name horse2zebra_pretrained \
               --model test \
               --no_dropout
```

### 步骤 5：查看结果

- **训练中间结果**：`checkpoints/horse2zebra_exp/web/index.html`
- **测试结果**：`results/horse2zebra_pretrained/test_latest/index.html`

用浏览器打开 HTML 文件即可查看。

## 📝 常用命令

### GPU 训练
```bash
python train.py --dataroot ./datasets/horse2zebra --name exp1 --model cycle_gan --gpu_ids 0
```

### CPU 训练
```bash
python train.py --dataroot ./datasets/horse2zebra --name exp1 --model cycle_gan --gpu_ids -1
```

### 多 GPU 训练
```bash
torchrun --nproc_per_node=2 train.py --dataroot ./datasets/horse2zebra --name exp1 --model cycle_gan --norm sync_batch
```

### 恢复训练
```bash
python train.py --dataroot ./datasets/horse2zebra --name exp1 --model cycle_gan --continue_train
```

### 双向测试（A→B 和 B→A）
```bash
python test.py --dataroot ./datasets/horse2zebra --name exp1 --model cycle_gan
```

### 单向测试（仅 A→B）
```bash
python test.py --dataroot ./datasets/horse2zebra/testA --name exp1 --model test --no_dropout
```

## 🎯 使用场景示例

### 1. 风格迁移（马→斑马）
```bash
# 训练
python train.py --dataroot ./datasets/horse2zebra --name h2z --model cycle_gan

# 测试
python test.py --dataroot ./datasets/horse2zebra/testA --name h2z --model test --no_dropout
```

### 2. 照片风格化（照片→莫奈画作）
```bash
python train.py --dataroot ./datasets/monet2photo --name monet --model cycle_gan --lambda_identity 0.5
```

### 3. 季节转换（夏天→冬天）
```bash
python train.py --dataroot ./datasets/summer2winter --name seasons --model cycle_gan
```

## 🔧 常见问题

### Q1: 内存不足怎么办？
```bash
# 减小批次大小
python train.py ... --batch_size 1

# 减小图像尺寸
python train.py ... --crop_size 128 --load_size 143

# 使用 CPU
python train.py ... --gpu_ids -1
```

### Q2: 训练速度太慢？
```bash
# 使用更少的判别器更新
python train.py ... --n_layers_D 2

# 减少生成器层数
python train.py ... --netG resnet_6blocks
```

### Q3: 如何调整生成质量？
```bash
# 增加循环一致性损失权重
python train.py ... --lambda_A 20.0 --lambda_B 20.0

# 添加恒等损失（保持颜色）
python train.py ... --lambda_identity 1.0
```

### Q4: 如何使用自己的数据？

1. 准备图片（jpg/png，推荐 256x256）
2. 按目录结构组织：`trainA/`, `trainB/`, `testA/`, `testB/`
3. 运行训练命令

## 📚 更多文档

- **详细使用说明**：查看 `USAGE.md`
- **与原版对比**：查看 `COMPARISON.md`
- **原版文档**：https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
- **CycleGAN 论文**：https://arxiv.org/pdf/1703.10593.pdf

## 💬 需要帮助？

1. 运行 `python check_env.py` 检查环境
2. 查看 `USAGE.md` 了解详细参数
3. 参考原版仓库的 FAQ：https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/qa.md

## 🎉 开始使用

```bash
# 安装
pip install -r requirements.txt

# 检查
python check_env.py

# 训练
python train.py --dataroot ./datasets/your_data --name your_exp --model cycle_gan

# 测试
python test.py --dataroot ./datasets/your_data/testA --name your_exp --model test --no_dropout
```

祝你使用愉快！🚀
