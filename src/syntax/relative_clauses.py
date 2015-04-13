__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The Relative clauses class
class RelativeClauses:

    # Constructor for the Relative Clauses class
    def __init__(self):
        self.has_wh_word = False
        self.result_string = ""

    # Break the tree
    def break_tree(self, tree):
        t = Tree.fromstring(str(tree))

        self.has_wh_word = False
        self.result_string = ""

        self.parse_tree(t)

        print "Relative Clause: " + str(self.has_wh_word)

        return self.result_string

    # Parse the tree
    def parse_tree(self, tree):

        if type(tree) == Tree:
            if tree.label() == "SBAR":
                for node in tree:
                    if type(node) == Tree:
                        self.has_wh_word |= node.label() == "WHNP"

            for node in tree:
                self.parse_tree(node)