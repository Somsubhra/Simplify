__author__ = 's7a'

# All imports
from nltk.tree import Tree


# Break the sentence according to appositions
class Appositions:

    # Constructor for the Appositions class
    def __init__(self):
        self.has_apposition = False

    # Break the tree
    def break_tree(self, tree):
        t = Tree.fromstring(str(tree))

        self.has_apposition = False
        self.parse_tree(t)

        print self.has_apposition

        result_string = ""
        return result_string

    # Parse the tree
    def parse_tree(self, tree):
        if type(tree) == Tree:

            np_label = 0

            for node in tree:
                if type(node) == Tree:
                    if node.label() == "NP":
                        np_label += 1

            self.has_apposition |= np_label > 1

            for node in tree:
                self.parse_tree(node)