__author__ = 's7a'

# All imports
from appositions import Appositions
from relative_clauses import RelativeClauses


# Constructor for the breaker class
class Breaker:

    # Constructor for the breaker class
    def __init__(self):
        self.appostions = Appositions()
        self.relative_clauses = RelativeClauses()

    # Break the tree
    def break_tree(self, tree):
        self.appostions.break_tree(tree)
        self.relative_clauses.break_tree(tree)