__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The Relative clauses class
class RelativeClauses:

    # Constructor for the Relative Clauses class
    def __init__(self):
        self.has_wh_word = False

    # Break the tree
    def break_tree(self, tree):
        t = Tree.fromstring(str(tree))

        self.has_wh_word = False
        self.parse_tree(t)

        print "Relative Clause: " + str(self.has_wh_word)

        result_string = ""
        return result_string

    # Parse the tree
    def parse_tree(self, tree):
        if type(tree) == Tree:
            self.has_wh_word |= tree.label() == "WHNP"
            for node in tree:
                self.parse_tree(node)