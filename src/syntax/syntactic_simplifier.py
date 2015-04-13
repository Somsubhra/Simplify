__author__ = 's7a'

# All imports
from parser import Parser
from breaker import Breaker


# The Syntactic simplification class
class SyntacticSimplifier:

    # Constructor for the Syntactic Simplifier
    def __init__(self):
        self.parser = Parser()
        self.breaker = Breaker()

    # Simplify content
    def simplify(self, content, plot_tree=False):
        results = []

        parse_trees = self.parser.parse(content, plot_tree)

        for parse_tree in parse_trees:
            broken_string = self.breaker.break_tree(parse_tree)

            results.append({
                "tree": str(parse_tree),
                "broken_string": broken_string
            })

        return results