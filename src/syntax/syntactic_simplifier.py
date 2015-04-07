__author__ = 's7a'

# All imports
from parser import Parser


# The Syntactic simplification class
class SyntacticSimplifier:

    # Constructor for the Syntactic Simplifier
    def __init__(self):
        self.parser = Parser()

    # Simplify content
    def simplify(self, content, plot_tree=False):
        self.parser.parse(content, plot_tree)
        results = []
        return results