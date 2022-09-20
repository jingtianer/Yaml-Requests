from baseFunc import *
from contentType import ContentType
import json
creator = locals()

class Methods():
    def __init__(self, methods):
        for method_name, method_para in methods.items():
            if method_para['async']:
                pass
            else:
                setattr(self,method_name, genSyncMethod(method_para))

def genConfigParas(data):
    for key, val in data.items():
        creator[key] = val

def genMethods(methods):
    return Methods(methods)

def genSyncMethod(method_para):
    path = method_para['path']
    resType = method_para['res-type']
    yaml_params = method_para['params']
    save = method_para['save'] if 'save' in method_para else None
    contentType = ContentType.Json if resType == "json" else ContentType.Binary if resType == "binary" else ContentType.Text if resType == "text" else None
    if method_para['type'] == "post":
        return lambda body: genPost(body, path, yaml_params, contentType, save)
    elif method_para['type'] == "get":
        return lambda req_params, body: genGet(req_params, body, path, yaml_params, contentType, save)
    else :
        raise Exception("No Such type" + method_para['type'])

def genGet(req_params, body, path, yaml_params, contentType, save):
    req_params.update(yaml_params)
    res = baseGet(url, port, path, body, req_params, contentType)
    saveFile(save, res)
    return res

def genPost(body, path, yaml_params, contentType, save):
    body.update(yaml_params)
    res = basePost(url, port, path, json.dumps(body), None, contentType)
    saveFile(save, res)
    return res

def saveFile(save, res):
    if save is not None:
        with open(save, 'w') as f:
            f.write(res)
    
