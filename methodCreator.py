from baseFunc import *
from contentType import ContentType
import json
from asyncExecutor import exeTask, exeTaskAsync
creator = locals()

class Methods():
    def __init__(self, methods):
        for method_name, method_para in methods.items():
            setattr(self,method_name, genMethod(method_para))

def genMethod(method_para):
    path = method_para['path']
    resType = method_para['res-type']
    yaml_params = method_para['params']
    save = method_para['save'] if 'save' in method_para else None
    contentType = ContentType.Json if resType == "json" else ContentType.Binary if resType == "binary" else ContentType.Text if resType == "text" else None
    if method_para['async']:
        return genAsyncMethod(method_para, path, yaml_params, save, contentType)
    else :
        return genSyncMethod(method_para, path, yaml_params, save, contentType)


def genConfigParas(data):
    for key, val in data.items():
        creator[key] = val


def genAsyncMethod(method_para, path, yaml_params, save, contentType):
    if method_para['type'] == "post":
        return lambda body, callBack: exeTaskAsync(lambda :genPost(body, path, yaml_params, contentType, save), callBack)
    elif method_para['type'] == "get":
        return lambda req_params, body, callBack: exeTaskAsync(lambda :genGet(req_params, body, path, yaml_params, contentType, save), callBack)
    else :
        raise Exception("No Such type" + method_para['type'])


def genSyncMethod(method_para, path, yaml_params, save, contentType):
    if method_para['type'] == "post":
        return lambda body: exeTask(lambda :genPost(body, path, yaml_params, contentType, save))
    elif method_para['type'] == "get":
        return lambda req_params, body: exeTask(lambda :genGet(req_params, body, path, yaml_params, contentType, save))
    else :
        raise Exception("No Such type" + method_para['type'])

async def genGet(req_params, body, path, yaml_params, contentType, save):
    req_params.update(yaml_params)
    res = baseGet(url, port, path, body, req_params, contentType)
    saveFile(save, res)
    return res

async def genPost(body, path, yaml_params, contentType, save):
    body.update(yaml_params)
    res = basePost(url, port, path, json.dumps(body), None, contentType)
    saveFile(save, res)
    return res

def saveFile(save, res):
    if save is not None:
        with open(save, 'w') as f:
            f.write(res)
    
