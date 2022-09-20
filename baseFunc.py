import requests
from contentType import ContentType

def basePost(baseUrl:str, port:str, path:str, body, params:dict, resType:ContentType):
    url = "http://" + baseUrl + ":" + port + path
    response = requests.post(url, data=body, params=params)
    res = response.json() if resType == ContentType.Json else response.content if resType == ContentType.Binary else response.text if resType == ContentType.Text else None
    return res

def baseGet(baseUrl:str, port:str, path:str, body, params:dict, resType:ContentType):
    url = "http://" + baseUrl + ":" + port + path
    response = requests.get(url, data=body, params=params)
    res = response.json() if resType == ContentType.Json else response.content if resType == ContentType.Binary else response.text if resType == ContentType.Text else None
    return res
