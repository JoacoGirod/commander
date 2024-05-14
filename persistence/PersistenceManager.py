import json
import os
from .implementations.JSON.CommandPersistenceDaoJsonImpl import *
from .implementations.YAML.CommandPersistenceDaoYamlImpl import *


class PersistenceManager:
    def __init__(self):
        with open(os.getcwd() + "/config.json", 'r') as config_file:
            self.config = json.loads(config_file.read())

    def get_implementation(self):
        if (self.config.get("type") == "JSON"):
            return CommandPersistenceDaoJsonImpl(self.config)
        if (self.config.get("type") == "YAML"):
            return CommandPersistenceDaoYamlImpl(self.config)