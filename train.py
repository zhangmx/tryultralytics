import os
from ultralytics import YOLO

# 获取当前脚本的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构建相对路径
data_path = os.path.join(current_dir, "mydataset.yaml")

# Load a pretrained model
model = YOLO("yolov8x.pt")  # or yolov8s.pt, yolov8m.pt, etc.

# Train the model using your custom dataset
results = model.train(data=data_path, epochs=100, imgsz=640)

# Save the model： x(模型大小) filter 偏光灯  数字是批次编号
model.save("q_x_filter_1.pt")