__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The Prefix Subordination class
class PrefixSubordination:

    # Constructor for Prefix Subordination
    def __init__(self):
        self.has_prefix_subordination = False
        self.subtree_list = []

    # Break the tree
    def break_tree(self, tree):
        self.has_prefix_subordination = False
        self.subtree_list = []

        self.parse_tree(tree)

        print "Prefix Subordination: " + str(self.has_prefix_subordination)

        if self.has_prefix_subordination:
            result_string = " ".join(self.subtree_list)
            result_string = result_string.replace(',', '', 1)
        else:
            result_string = " ".join(tree.leaves())

        print "Prefix Subordination Results: " + result_string
        return result_string

    # Parse the tree
    def parse_tree(self, tree):
        if type(tree) == Tree:
            sentence_root = tree[0]
            if type(sentence_root) == Tree:
                if sentence_root.label() == "S":
                    first_node = sentence_root[0]
                    if type(first_node) == Tree:
                        if first_node.label() == "SBAR":
                            for node_1 in first_node:
                                if type(node_1) == Tree:
                                    if node_1.label() == "IN":
                                        self.has_prefix_subordination |= True
                                    else:
                                        self.subtree_list.append(' '.join(node_1.leaves()))
                                else:
                                    self.subtree_list.append(node_1)
                        else:
                            self.subtree_list.append(' '.join(first_node.leaves()))
                    else:
                        self.subtree_list.append(first_node)

                    self.subtree_list.append('.')
                    flag = 0

                    for node in sentence_root:
                        if flag == 0:
                            flag = 1
                            continue

                        if type(node) == Tree:
                            self.subtree_list.append(' '.join(node.leaves()))
                        else:
                            self.subtree_list.append(node)