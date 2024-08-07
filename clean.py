import shutil
import os

# 获取当前脚本的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构建相对路径
cache_dir = os.path.join(current_dir, "runs")

# 检查目录是否存在
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)
    print(f"缓存目录 {cache_dir} 已删除。")
else:
    print(f"缓存目录 {cache_dir} 不存在。")
