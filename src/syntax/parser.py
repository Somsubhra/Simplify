__author__ = 's7a'

# All imports
import json
import os
from nltk.parse import stanford


# The Parser class
class Parser:

    # Constructor for the Parser class
    def __init__(self):
        with open('config.json') as config_file:
            config = json.load(config_file)
            os.environ['STANFORD_PARSER'] = str(config["stanford_parser_jars_path"])
            os.environ['STANFORD_MODELS'] = str(config["stanford_parser_jars_path"])
            self.parser = stanford.StanfordParser(model_path=str(config["stanford_parser_model_path"]))

    # Parse a sentence
    def parse(self, sentence, plot_tree=False):
        parse_trees = self.parser.raw_parse(sentence)

        if plot_tree:
            for parse_tree in parse_trees:
                parse_tree.draw()

        return parse_trees
