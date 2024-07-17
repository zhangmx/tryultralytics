import cv2
import math
from ultralytics import YOLO

# 加载训练好的 YOLOv8 模型
model = YOLO('q1.pt')

# 读取要检测的图片
img_path = 'pictures\\train\\Pic_2024_07_02_164747_10.bmp'
img = cv2.imread(img_path)

# 使用模型进行检测
results = model(img)

# 打印结果
# for result in results:
#     print(result)
# output_base_path = 'pictures\\detect'
# for idx, result in enumerate(results):
#     output_path = f'{output_base_path}_{idx}.jpg'
#     result.save(output_path)

# 提取检测结果
for result in results:
    boxes = result.boxes  # 检测到的边界框
    for box in boxes:
                # 调试信息，查看 box.xyxy 的实际内容和类型
        print(f'box.xyxy type: {type(box.xyxy)}')
        print(f'box.xyxy content: {box.xyxy}')

        # 将边界框坐标转换为列表，然后解包为四个标量值
        # coords = box.xyxy[0].tolist() if hasattr(box.xyxy, 'tolist') else box.xyxy
        # x1, y1, x2, y2 = map(int, coords)  # 边界框坐标
        # # x1, y1, x2, y2 = map(int, box.xyxy.tolist())  # 边界框坐标
        # conf = box.conf  # 置信度
        # cls = box.cls  # 类别


        # 将边界框坐标转换为列表，然后解包为四个标量值
        coords = box.xyxy[0].tolist() if hasattr(box.xyxy, 'tolist') else box.xyxy[0]
        x1, y1, x2, y2 = map(int, coords)  # 边界框坐标
        conf = float(box.conf[0].item())  # 置信度，转换为标量
        cls = int(box.cls[0].item())  # 类别，转换为标量

        # 获取类别名称
        class_name = result.names[cls]

        # 计算圆心和半径
        # center_x = (x1 + x2) // 2
        # center_y = (y1 + y2) // 2
        # radius = min((x2 - x1) // 2, (y2 - y1) // 2)

        # # 在图像上画圆
        # cv2.circle(img, (center_x, center_y), radius, (0, 255, 0), 2)


        # 计算圆心和半径
        center_x = x1
        center_y = y1
        # radius = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2)
        radius = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2) )
        # 在图像上画圆
        cv2.circle(img, (center_x, center_y), radius, (0, 255, 0), 2)
        
        # 绘制置信度和类别
        # label = f'Class: {cls}, Conf: {conf:.2f}'
        # label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        # label_x = x1
        # label_y = y1 - 10 if y1 - 10 > 10 else y1 + 10
        # cv2.putText(img, label, (label_x, label_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        
        
        # 绘制置信度和类别
        label = f'{class_name}: {conf:.2f}'
        font_scale = 6  # 字体大小
        thickness = 16  # 字体粗细
        label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
        label_x = x1 - radius + 10
        label_y = y1 - 10 if y1 - 10 > 10 else y1 + 10
        cv2.putText(img, label, (label_x, label_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), thickness)
        
        # 打印检测结果
        print(f"Class: {cls}, Confidence: {conf}, Center: ({center_x}, {center_y}), Radius: {radius}")

# 保存带有圆形标记的图片
output_path = 'pictures\\Pic_2024_07_02_164747_10_marked.jpg'
cv2.imwrite(output_path, img)
print(f"Marked image saved at {output_path}")

