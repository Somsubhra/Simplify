__author__ = 's7a'

# All imports
from nltk.tree import Tree


# The infix coordination class
class InfixCoordination:

    # Constructor for the infix coordination
    def __init__(self):
        self.has_infix_coordination = False
        self.subtree_list = []

        self.has_infix_coordination_1 = False
        self.np_subtree_list = []
        self.vp_subtree_list = []
        self.other_subtree_list = []

    # Break the tree
    def break_tree(self, tree):
        try:
            self.has_infix_coordination = False
            self.subtree_list = []

            self.has_infix_coordination_1 = False
            self.np_subtree_list = []
            self.vp_subtree_list = []
            self.other_subtree_list = []

            self.parse_tree(tree)

            print "Infix Coordination: " + str(self.has_infix_coordination or self.has_infix_coordination_1)

            if self.has_infix_coordination:
                result_string = ' '.join(self.subtree_list)
            elif self.has_infix_coordination_1:
                result_string = ""
                counter = 0
                l = len(self.vp_subtree_list)
                for vp in self.vp_subtree_list:
                    counter += 1
                    result_string += ' '.join(self.np_subtree_list) + " " + vp
                    if counter != l:
                        result_string += "."

                result_string += ' '.join(self.other_subtree_list)
            else:
                result_string = ' '.join(tree.leaves())

            print "Infix Coordination Result: " + result_string

            return result_string

        except:
            return " ".join(tree.leaves())

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
                            elif node.label() == "NP":
                                self.np_subtree_list.append(' '.join(node.leaves()))
                                self.subtree_list.append(' '.join(node.leaves()))
                            elif node.label() == "VP":
                                self.subtree_list.append(' '.join(node.leaves()))
                                for node_1 in node:
                                    if type(node_1) == Tree:
                                        if node_1.label() == "CC":
                                            self.has_infix_coordination_1 |= True
                                        elif node_1.label() == "VP":
                                            self.vp_subtree_list.append(' '.join(node_1.leaves()))
                                        else:
                                            self.other_subtree_list.append(' '.join(node_1.leaves()))
                                    else:
                                        self.other_subtree_list.append(node_1)
                            else:
                                self.subtree_list.append(' '.join(node.leaves()))
                                self.other_subtree_list.append(' '.join(node.leaves()))
                        else:
                            self.subtree_list.append(node)
                            self.other_subtree_list.append(node)