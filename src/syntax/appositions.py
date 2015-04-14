__author__ = 's7a'

# All imports
from nltk.tree import Tree


# Break the sentence according to appositions
class Appositions:

    # Constructor for the Appositions class
    def __init__(self):
        self.has_apposition = False
        self.np_subtrees = []
        self.other_subtrees = []

    # Break the tree
    def break_tree(self, tree):
        try:
            self.has_apposition = False

            self.parse_tree(tree)

            print "Apposition: " + str(self.has_apposition)

            if self.has_apposition:
                result_string = self.np_subtrees[0] + " is " + " ".join(self.np_subtrees[1:]) + "."
                result_string += (self.np_subtrees[0] + " ".join(self.other_subtrees)).replace(",", "")
            else:
                result_string = " ".join(tree.leaves())

            print "Apposition Result: " + result_string

            return result_string

        except:
            return " ".join(tree.leaves())

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
                                    else:
                                        self.other_subtrees.append(' '.join(node.leaves()))
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

        self.has_apposition |= len(self.np_subtrees) > 1