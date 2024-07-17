# tryultralytics

训练的步骤

1. 给图片打标签。使用 `labelme`、`anylabeling`等工具。
2. 创建训练目录结构。执行`yolo train model=yolov8n-seg.pt data=coco8-seg.yaml` 示例后，参考目录结构。
3. 打标签工具使用的是json格式，需要转成 yolo的txt格式。https://github.com/ThijsCol/Anylabeling-LabelMe-json-to-yolo-txt OR https://github.com/rooneysh/Labelme2YOLO
4. 修改yaml配置文件。参考: https://docs.ultralytics.com/datasets/segment/coco8-seg/ 或 https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco8-seg.yaml
5. 执行训练脚本。```python train.py```
6. 如果有迭代增加的上述几个步骤的新的图片数据，需要编辑新的训练脚本。

脚本功能：

1. 转换训练数据的脚本。jsontoyolo.py(未使用) 和 jsontoyolo_simple.py
2. 清理yolo训练缓存的脚本。clean.py
3. 训练脚本。train.py
4. 中断或接续训练的脚本。train_continue.py


## 训练：

```shell
python train.py

```


# Anylabeling-LabelMe-json-to-yolo-txt
Python scripts for converting .json annotations from [Anylabeling](https://github.com/vietanhdev/anylabeling) or [LabelMe](https://github.com/wkentaro/labelme) to YOLO .txt files.

-**jsontoyolo.py** will convert the .json annotation files to YOLO .txt files, split them into 'train' and 'validate' folders and copy over the corresponding pictures. 
Tracks progress using a progress bar. Requires *scikit-learn* and *tqdm*.

-**jsontoyolo_simple.py** will only convert the .json files to YOLO .txt files and copy them to your specified directory. Only uses built-in Python modules.

**Usage:**

-Define the `class_labels` for your dataset, example: `{"car": 0, "bike": 1, "plane": 2}`.

-Change `input_dir` and `output_dir` to your required directories.

-set the `split_ratio`, example: `0.2 # 20% of the data will go to the validation set`.           

-If your pictures are a different file extension then *'.jpg', '.png', '.jpeg'* you have to modify or add the required extension to lines: 29, 47 and 48.

-Run the script and it should generate the .txt files in the specified directory.

---
