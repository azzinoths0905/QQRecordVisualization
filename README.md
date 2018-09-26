# QQ聊天记录可视化

## 1. 介绍
QQRecordVisualization可以接收用户的QQ聊天记录文件，将其解析为结构化数据存入数据库，并输出JSON类型的Option配置供前端Echarts使用。

目前支持的可视化类型有：
- 词云（Word Cloud）

本项目后端的Github地址为：[https://github.com/Azzinothz/QQRecordVisualization](https://github.com/Azzinothz/QQRecordVisualization)

本项目前端的Github地址为：[https://github.com/Azzinothz/QQRecordVisualization-FrontEnd](https://github.com/Azzinothz/QQRecordVisualization-FrontEnd)

## 2. 安装方法
>请确保Python版本>=3.4

下载源码后，进入项目根目录，输入命令：
```shell
pip install -r requirements.txt
```

编辑项目根目录下的`config.py.template`，填写数据库相关的配置，保存后将文件名改为`config.py`。

数据表结构相关内容可以参考`/database/initiate.sql`文件。

## 3. 使用方法
直接运行`main.py`文件：
```shell
python main.py
```

## 4. API

### POST /upload

#### request: form data

- `log_file`: (bin) txt格式聊天记录文件

#### response

- (str) 对应的服务器中的文件名

### GET /api/qqrv/v1/word_cloud

#### request: arg
- file: (str) 对应的服务器中的文件名

#### response
(json) Echarts词云配置，例如:
```json
{
    "option": {
        "series": [{
            "type": "wordCloud",
            "data": [
                {"name": "Amy", "value": 724}, 
                {"name": "Ben", "value": 656}, 
                {"name": "Cindy", "value": 381}, 
                {"name": "Dick", "value": 280}, 
                {"name": "Eddy", "value": 3}
                ]
        }]
    }, 
    "error": ""
}
```