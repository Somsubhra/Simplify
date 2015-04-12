__author__ = 's7a'

from nltk.tree import Tree


# Constructor for the breaker class
class Breaker:

    # Constructor for the breaker class
    def __init__(self):
        pass

    @staticmethod
    def break_tree(tree):

        t = Tree.fromstring(str(tree))

        print len(t)

        Breaker.parse_tree(t)

        result_string = ""

        return result_string

    @staticmethod
    def parse_tree(tree):
        if type(tree) == Tree:
            print tree
            for node in tree:
                Breaker.parse_tree(node)