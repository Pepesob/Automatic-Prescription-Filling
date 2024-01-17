import json
import os


class ConfigInfo:
    def __init__(self):
        self.name = ""
        self.version = ""

        self.fetch_info()

    def fetch_info(self):
        with open(os.path.join(os.path.dirname(__file__), "..", "config.json"),encoding='utf-8') as config:
            dict_data = json.load(config)
            self.name = dict_data["name"]
            self.version = dict_data["version"]


configInfo = ConfigInfo()