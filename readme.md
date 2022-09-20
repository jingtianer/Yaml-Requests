# Yaml-Requests简介

- 对request库的封装，用于处理与chainCode http 接口的交互
- 方便对http api的使用
- 提供异步、同步两种方式
- 通过配置文件获取http请求的url，port等信息。调用者只需关注业务，请求的参数部分已经在配置文件中写好，调用者不必关注过多细节
    - async : true/false
    - content-type : json/file/none/...
    - url
    - port
    - path
- 处理文件读写
- 动态生成函数
- 并发任务

# 使用方法
## config的编写
编写yaml文件，包括：
- url: http服务的BaseUrl
- port: 服务端口
- methods: 定义方法

## yaml中method的定义
- 样例如下
```yaml
method_name:
    type: 'post'
    async: true
    res-type: 'json'
    path: '/invokeChaincode/json'
    save: './xxx/xxx'
    params:
        para1: 'val1'
        para2: 'val2'
        para3: 'val3'
```

- type: 表示接口方法类型，可选`post/get`
- async: 是否异步调用，异步调用需要提供回调函数
- res-type: 返回值类型，可选`text/json/binary`
- path: 请求的path
- save: （可选）保存请求返回体的文件
- params: 请求的固定参数

## 调用
- 以调用`sample_config.yaml`中的函数为例
```python
from configLoader import init
def callBack(ret):
    print("callBack: " + ret)

print("invoke: %s" % init("./sample_config.yaml").get({"key":"a", "val":"bb"}))
print("invoke: %s" % init("./sample_config.yaml").set({"key":"a", "val":"bb"}))
print("invoke: %s" % init("./sample_config.yaml").get({"key":"a", "val":"bb"}))
print("invoke: %s" % init("./sample_config.yaml").get_async({"key":"a", "val":"cc"}, callBack))
print("invoke: %s" % init("./sample_config.yaml").set_async({"key":"a", "val":"cc"}, callBack))
print("invoke: %s" % init("./sample_config.yaml").get_async({"key":"a", "val":"cc"}, callBack))
```

# 应用场景
1. 配合docker容器，不同容器使用同一套代码，根据不同的配置文件，进行不同参数的http请求