__author__ = 's7a'

# All imports
from appositions import Appositions


# Constructor for the breaker class
class Breaker:

    # Constructor for the breaker class
    def __init__(self):
        self.appostions = Appositions()

    # Break the tree
    def break_tree(self, tree):
        self.appostions.break_tree(tree)