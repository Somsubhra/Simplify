__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The Prefix Subordination class
class PrefixSubordination:

    # Constructor for Prefix Subordination
    def __init__(self):
        self.has_prefix_subordination = False

    # Break the tree
    def break_tree(self, tree):
        t = Tree.fromstring(str(tree))

        self.has_prefix_subordination = False
        self.parse_tree(t)

        print "Prefix Subordination: " + str(self.has_prefix_subordination)

        result_string = ""
        return result_string

    # Parse the tree
    def parse_tree(self, tree):

        if type(tree) == Tree:

            if tree.label() == "SBAR":
                for node in tree:
                    if type(node) == Tree:
                        self.has_prefix_subordination |= node.label() == "IN"

            for node in tree:
                self.parse_tree(node)