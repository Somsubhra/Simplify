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

        try:
            print t[0]
        except Exception as x:
            print x.message

        result_string = ""

        return result_string