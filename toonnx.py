from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("q_x_filter_1.pt")

# Export the model to ONNX format
model.export(format="onnx")  # creates 'q1.onnx'