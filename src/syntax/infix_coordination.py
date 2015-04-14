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
        self.has_infix_coordination = False
        self.parse_tree(tree)
        print "Infix Coordination: " + str(self.has_infix_coordination)

    # Parse the tree
    def parse_tree(self, tree):
        if type(tree) == Tree:
            sentence_root = tree[0]
            if type(sentence_root) == Tree:
                if sentence_root.label() == "S":
                    print "Valid Tree"
                    for node in sentence_root:
                        if type(node) == Tree:
                            if node.label() == "CC":
                                self.has_infix_coordination |= True
