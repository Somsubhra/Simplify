__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The Infix Subordination class
class InfixSubordination:

    # Constructor for Infix Subordination
    def __init__(self):
        self.has_infix_subordination = False
        self.subtree_list = []

    # Break the tree
    def break_tree(self, tree):
        self.has_infix_subordination = False
        self.subtree_list = []

        self.parse_tree(tree)

        print "Infix Subordination: " + str(self.has_infix_subordination)

        if self.has_infix_subordination:
            result_string = ' '.join(self.subtree_list)
        else:
            result_string = ' '.join(tree.leaves())

        print "Infix Subordination Result: " + result_string

        return result_string

    # Parse the tree
    def parse_tree(self, tree):
        if type(tree) == Tree:
            sentence_root = tree[0]
            if type(sentence_root) == Tree:
                if sentence_root.label() == "S":
                    for node in sentence_root:
                        if type(node) == Tree:
                            if node.label() == "VP":
                                for node_1 in node:
                                    if type(node_1) == Tree:
                                        if node_1.label() == "SBAR":
                                            for node_2 in node_1:
                                                if type(node_2) == Tree:
                                                    if node_2.label() == "IN":
                                                        self.has_infix_subordination |= True
                                                        self.subtree_list.append('.')
                                                    else:
                                                        self.subtree_list.append(' '.join(node_2.leaves()))
                                                else:
                                                    self.subtree_list.append(node_2)
                                        else:
                                            self.subtree_list.append(' '.join(node_1.leaves()))
                                    else:
                                        self.subtree_list.append(node_1)
                            else:
                                self.subtree_list.append(' '.join(node.leaves()))
                        else:
                            self.subtree_list.append(node)