import shutil
import os

cache_dir = 'D:\\lab\\python\\tryultralytics\\runs'

# 检查目录是否存在
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)
    print(f"缓存目录 {cache_dir} 已删除。")
else:
    print(f"缓存目录 {cache_dir} 不存在。")
