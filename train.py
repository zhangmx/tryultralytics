import os
import torch
from ultralytics import YOLO

if __name__ == '__main__':
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA device count:", torch.cuda.device_count())
    torch.cuda.empty_cache()
    # 获取当前脚本的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建相对路径
    data_path = os.path.join(current_dir, "mydataset.yaml")

    # yolo_model_version = "yolov8n"
    yolo_model_version = "yolov8s"
    # yolo_model_version = "yolov8m"
    # yolo_model_version = "yolov8l"
    # yolo_model_version = "yolov8x"

    yolo_model = f"{yolo_model_version}.pt"

    # Load a pretrained model
    model = YOLO(yolo_model)  

    # Train the model using your custom dataset
    # results = model.train(data=data_path, epochs=100, imgsz=640)
    results = model.train(data=data_path, epochs=3, workers=5, batch=8, imgsz=640, device='0')
    # results = model.train(data=data_path, epochs=100, imgsz=640, device='cpu')  # 指定设备为 CPU

    # Save the model
    # x(模型大小) filter 偏光灯  数字是批次编号
    model.save(f"q_{yolo_model_version}_filter_ccd1hf_1.pt")
