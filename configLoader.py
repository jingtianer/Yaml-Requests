from utils.yamlUtils import read_yaml, get_value, set_value, has_value
from methodCreator import Methods, genConfigParas

var_list = ['url', 'port', 'methods']

def check_yaml(data):
    for key in var_list:
        if not has_value(key, data):
            raise Exception("Expect config " + key + "in yaml")


def init(yamlfile):
    data = read_yaml(yamlfile)
    methods = get_value('methods', data)
    check_yaml(data)
    genConfigParas(data)
    return Methods(methods)
