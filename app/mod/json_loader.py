import json
from types import SimpleNamespace

def load_config(): #Change JSON to Python_Object
    with open("config.json", "r", encoding="utf-8") as json_file:
        json_file = json_file.read()
        config = json.loads(json_file, object_hook=lambda d: SimpleNamespace(**d))
    return config


def load_message(): #Change JSON to Python_Object
    with open("message.json", "r",  encoding="utf-8") as json_file:
        json_file = json_file.read()
        message = json.loads(json_file, object_hook=lambda d: SimpleNamespace(**d))
    return message

