import os

# 设置当前工作目录（可按需更改）
current_dir = os.getcwd()

# 遍历当前目录和所有子目录，topdown=False确保从子目录开始向上遍历
for root, dirs, files in os.walk(current_dir, topdown=False):
    for dir in dirs:
        # 构建目录的完整路径
        full_dir_path = os.path.join(root, dir)
        
        # 检查目录是否为空
        if not os.listdir(full_dir_path):
            # 删除空目录
            os.rmdir(full_dir_path)
            print(f"Deleted empty directory: {full_dir_path}")
