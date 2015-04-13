__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The infix coordination class
class InfixSubordination:

    # Constructor for the infix coordination
    def __init__(self):
        self.has_infix_subordination = False

    # Break the tree
    def break_tree(self, tree):
        t = Tree.fromstring(str(tree))

        self.has_infix_subordination = False
        self.parse_tree(t)

        print "Infix Subordination: " + str(self.has_infix_subordination)

        result_string = ""
        return result_string

    # Parse the tree
    def parse_tree(self, tree):
        if type(tree) == Tree:
            for node in tree:
                self.parse_tree(node)