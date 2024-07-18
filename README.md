# try ultralytics

Learn form [ultralytics document](https://docs.ultralytics.com/).

### 训练的步骤

1. 给图片打标签。使用  [Anylabeling](https://github.com/vietanhdev/anylabeling) or [LabelMe](https://github.com/wkentaro/labelme) 等工具。
2. 创建训练目录结构。执行`yolo train model=yolov8n-seg.pt data=coco8-seg.yaml` 示例后，参考目录结构。
3. 打标签工具使用的是`json`格式，需要转成 `yolo`的`txt`格式。[Anylabeling-LabelMe-json-to-yolo-txt](https://github.com/ThijsCol/Anylabeling-LabelMe-json-to-yolo-txt) OR [Labelme2YOLO](https://github.com/rooneysh/Labelme2YOLO)
4. 修改yaml配置文件。参考: [coco8-seg doc](https://docs.ultralytics.com/datasets/segment/coco8-seg/) 或 [coco8-seg.yaml file](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco8-seg.yaml)
5. 执行训练脚本。```python train.py```
6. 如果有迭代增加的上述几个步骤的新的图片数据，需要编辑新的训练脚本。

### 脚本功能：

1. 转换训练数据的脚本:`jsontoyolo.py(未使用)` OR `jsontoyolo_simple.py`。
2. 清理yolo训练缓存的脚本:`clean.py`。
3. 训练脚本:`train.py`。
4. 中断后接续训练的脚本:`train_continue.py`。


## 训练：

```shell
python train.py

```

## 检测：

```shell
python detect.py

```