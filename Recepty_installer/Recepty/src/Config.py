import json
import os
from dataclasses import dataclass

@dataclass
class Config:
    name: str
    version: str


class ConfigService:
    def __init__(self):
        self.data_file_path = os.path.join(os.path.dirname(__file__), "resources", "config.json")

    def get_config(self) -> Config:
        with open(self. data_file_path, encoding='utf-8') as config:
            dict_data = json.load(config)
            return Config(**dict_data)
