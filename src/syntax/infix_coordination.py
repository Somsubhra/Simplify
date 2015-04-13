__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The infix coordination class
class InfixCoordination:

    # Constructor for the infix coordination
    def __init__(self):
        self.has_infix_coordination = False

    # Break the tree
    def break_tree(self, tree):
        t = Tree.fromstring(str(tree))

        self.has_infix_coordination = False
        self.parse_tree(t)

        print "Infix Coordination: " + str(self.has_infix_coordination)

        result_string = ""
        return result_string

    # Parse the tree
    def parse_tree(self, tree):
        if type(tree) == Tree:
            for node in tree:
                self.parse_tree(node)