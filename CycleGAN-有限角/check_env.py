"""
快速验证脚本 - 检查 CycleGAN 环境是否正确配置
"""

import sys
import importlib

def check_import(module_name, package=None):
    """检查模块是否能正确导入"""
    try:
        if package:
            importlib.import_module(f"{package}.{module_name}")
        else:
            importlib.import_module(module_name)
        return True, "✓"
    except Exception as e:
        return False, f"✗ ({str(e)[:50]})"

def main():
    print("="*70)
    print("  CycleGAN 环境检查")
    print("="*70)
    
    # 检查 Python 包
    print("\n1. Python 依赖包:")
    packages = [
        "torch",
        "torchvision", 
        "numpy",
        "PIL",
        "dominate",
        "visdom",
    ]
    
    all_ok = True
    for pkg in packages:
        status, msg = check_import(pkg)
        print(f"   {pkg:20s} {msg}")
        all_ok = all_ok and status
    
    # 检查 CUDA
    print("\n2. CUDA 支持:")
    try:
        import torch
        print(f"   PyTorch 版本:     {torch.__version__}")
        print(f"   CUDA 可用:        {'✓ 是' if torch.cuda.is_available() else '✗ 否'}")
        if torch.cuda.is_available():
            print(f"   CUDA 版本:        {torch.version.cuda}")
            print(f"   GPU 设备:         {torch.cuda.get_device_name(0)}")
    except Exception as e:
        print(f"   ✗ 错误: {e}")
        all_ok = False
    
    # 检查本地模块
    print("\n3. CycleGAN 模块:")
    modules = [
        ("options", "base_options"),
        ("options", "train_options"),
        ("options", "test_options"),
        ("data", "unaligned_dataset"),
        ("data", "single_dataset"),
        ("models", "cycle_gan_model"),
        ("models", "test_model"),
        ("models", "networks"),
        ("util", "util"),
        ("util", "visualizer"),
    ]
    
    for package, module in modules:
        status, msg = check_import(module, package)
        print(f"   {package}.{module:25s} {msg}")
        all_ok = all_ok and status
    
    # 总结
    print("\n" + "="*70)
    if all_ok:
        print("  ✓ 所有检查通过！环境配置正确。")
        print("\n  你可以开始使用 CycleGAN 了:")
        print("    训练: python train.py --dataroot ./datasets/your_data --name exp1 --model cycle_gan")
        print("    测试: python test.py --dataroot ./datasets/your_data/testA --name exp1 --model test --no_dropout")
    else:
        print("  ✗ 部分检查失败，请安装缺失的依赖:")
        print("    pip install -r requirements.txt")
    print("="*70)
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
