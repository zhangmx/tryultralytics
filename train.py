from ultralytics import YOLO

# Load a pretrained model
model = YOLO("yolov8n.pt")  # or yolov8s.pt, yolov8m.pt, etc.

# Train the model using your custom dataset
results = model.train(data="D:\\lab\\python\\tryultralytics\\mydataset.yaml", epochs=100, imgsz=640)

model.save("q1.pt")