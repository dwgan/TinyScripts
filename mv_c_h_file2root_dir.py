import os
import shutil

# 设置当前工作目录（可按需更改）
current_dir = os.getcwd()

# 遍历当前目录和所有子目录
for root, dirs, files in os.walk(current_dir):
    for file in files:
        # 检查文件扩展名是否为 .c 或 .h
        if file.endswith('.c') or file.endswith('.h'):
            # 构建文件的完整路径
            full_file_path = os.path.join(root, file)
            # 构建目标路径
            target_path = os.path.join(current_dir, file)

            # 移动文件
            shutil.move(full_file_path, target_path)
            print(f"Moved: {file} to {current_dir}")
