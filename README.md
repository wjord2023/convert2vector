# 使用 gRPC 调用 CLIP 模型，将文字和图片转换为向量，以实现图像和文本的相似度搜索功能

## 目录

- [安装](#安装)
- [使用方法](#使用方法)
- [API接口](#API接口)

## 安装

### 环境配置

1. 创建Conda环境

```bash
conda env create -f environment.yml
```

2. 激活Conda环境

```bash
conda activate clip-env
```

## 使用方法

### 启动gRPC服务器

```bash
python server.py
```

### 调用gRPC接口

请参见`client.py`中的示例代码

## API接口

### 文本向量转换

- 方法： `GetTextVector`
- 请求参数：
    - `text` (string): 要转换的文本
- 返回参数：
    - `vector` (list of float): 转换后的向量


### 图像向量转换

- 方法： `GetImageVector`
- 请求参数：
    - `image` (bytes): 要转换的图像，采用base64编码
- 返回参数：
    - `vector` (list of float): 转换后的向量