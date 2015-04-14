__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The Relative clauses class
class RelativeClauses:

    # Constructor for the Relative Clauses class
    def __init__(self):
        self.has_wh_word = False
        self.np_subtrees = []
        self.wh_subtrees = []
        self.other_subtrees = []

    # Break the tree
    def break_tree(self, tree):
        self.has_wh_word = False
        self.np_subtrees = []
        self.wh_subtrees = []
        self.other_subtrees = []

        self.parse_tree(tree)

        print "Relative Clause: " + str(self.has_wh_word)

        if self.has_wh_word:
            wh_part = " ".join(" ".join(self.wh_subtrees).split()[1:])
            result_string = " ".join(self.np_subtrees) + " " + wh_part + "."
            result_string += (" ".join(self.np_subtrees) + " ".join(self.other_subtrees)).replace(",", "")
        else:
            result_string = " ".join(tree.leaves())

        print "Relative Clause Result: " + result_string

        return result_string

    # Parse the tree
    def parse_tree(self, tree):
        if type(tree) == Tree:
            sentence_root = tree[0]
            if type(sentence_root) == Tree:
                if sentence_root.label() == "S":
                    first_node = sentence_root[0]
                    if type(first_node) == Tree:
                        if first_node.label() == "NP":
                            for node in first_node:
                                if type(node) == Tree:
                                    if node.label() == "NP":
                                        self.np_subtrees.append(' '.join(node.leaves()))
                                    elif node.label() == "SBAR":
                                        node_1 = node[0]
                                        if type(node_1) == Tree:
                                            if node_1.label() == "WHNP":
                                                self.has_wh_word |= True
                                                self.wh_subtrees.append(' '.join(node.leaves()))
                                            else:
                                                self.other_subtrees.append(' '.join(node.leaves()))
                                    else:
                                        self.other_subtrees.append(' '.join(' '.join(node.leaves())))
                                else:
                                    self.other_subtrees.append(node)
                        else:
                            self.other_subtrees.append(' '.join(first_node.leaves()))
                    else:
                        self.other_subtrees.append(first_node)

                    flag = 0

                    for node in sentence_root:
                        if flag == 0:
                            flag = 1
                            continue

                        if type(node) == Tree:
                            self.other_subtrees.append(' '.join(node.leaves()))
                        else:
                            self.other_subtrees.append(node)