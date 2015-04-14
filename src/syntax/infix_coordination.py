__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The infix coordination class
class InfixCoordination:

    # Constructor for the infix coordination
    def __init__(self):
        self.has_infix_coordination = False
        self.subtree_list = []

    # Break the tree
    def break_tree(self, tree):
        self.has_infix_coordination = False
        self.subtree_list = []

        self.parse_tree(tree)

        print "Infix Coordination: " + str(self.has_infix_coordination)

        if self.has_infix_coordination:
            result_string = ' '.join(self.subtree_list)
        else:
            result_string = ' '.join(tree.leaves())

        print "Infix Coordination Result: " + result_string

        return result_string

    # Parse the tree
    def parse_tree(self, tree):
        if type(tree) == Tree:
            sentence_root = tree[0]
            if type(sentence_root) == Tree:
                if sentence_root.label() == "S":
                    for node in sentence_root:
                        if type(node) == Tree:
                            if node.label() == "CC":
                                self.has_infix_coordination |= True
                                self.subtree_list.append('.')
                            else:
                                self.subtree_list.append(' '.join(node.leaves()))
                        else:
                            self.subtree_list.append(node)