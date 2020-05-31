## 环境初始化

Python 环境初始化，首先初始化虚拟环境，然后在虚拟环境中安装依赖包：

``` shell
# 进入当前项目文件夹
# 创建 Python3 虚拟环境并激活
$ python3 -m venv .venv
$ source .venv/bin/activate

# 安装依赖
$ pip install -r requirements.txt

# 提前在系统安装 CUDA ，地址：https://developer.nvidia.com/cuda-downloads
# 其中 pytorch 的安装需要根据系统、CUDA版本、安装方式的差异选择不同的安装包
# pytorch 官网安装地址：https://pytorch.org/get-started/locally/
# 选择 Stable(1.5)/Windows/Pip/Python/10.2 进行安装，命令如下：
$ pip install torch===1.5.0 torchvision===0.6.0 -f https://download.pytorch.org/whl/torch_stable.html

# Python 环境准备好之后可以使用 Pycharm 作为 Python 编辑器，需要调整项目的 Python interface，选择之前创建的虚拟环境
```

## 使用模型检测图片

都准备完毕后可以使用如下命令使用已经训练好的模型预测样例图片：

    $ python3 detect.py --image_folder data/samples/
    
## 训练模型

若需训练模型，主要代码文件为 `train.py`，相关说明如下：

### 初始化模型参数
使用脚本初始化模型定义，需要指明训练目标的种类数，如检测船舶，为 1：

```
$ cd config/
$ bash create_custom_model.sh 1
```

### 指明种类名称
需要在文件中指明训练目标的种类名称，如船舶 boat，将其添加至 `data/custom/classes.names` 文件中

### 图片训练集目录

将所有训练所需的图片放至 `data/custom/images` 中。

### 注解信息目录

将所有训练模型所需的注解信息放入 `data/custom/labels` 目录中，主要是训练集中目标框的坐标点。

### 定义训练集和验证集

在 `data/custome/train.txt` 中定义训练集图片列表，在 `data/custom/valid.txt` 中定义验证集图片列表，建议比例为 9:1 。

### 训练
使用如下命令进行训练：

```
$ python3 train.py --model_def config/yolov3-custom.cfg --data_config config/custom.data
```

添加 `--pretrained_weights weights/darknet53.conv.74` 可以添加预训练权重，如 darknet53 网络。
