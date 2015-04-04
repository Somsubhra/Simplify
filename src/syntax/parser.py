__author__ = 's7a'

# All imports
import json


# The Parser class
class Parser:

    # Constructor for the Parser class
    def __init__(self):
        with open('config.json') as config_file:
            config = json.load(config_file)
            self.jars_path = config["stanford_parser_jars"]
            self.model_path = config["stanford_parser_model_path"]