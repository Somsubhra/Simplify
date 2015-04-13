__author__ = 's7a'

# All imports
from appositions import Appositions
from relative_clauses import RelativeClauses
from prefix_subordination import PrefixSubordination


# Constructor for the breaker class
class Breaker:

    # Constructor for the breaker class
    def __init__(self):
        self.appostions = Appositions()
        self.relative_clauses = RelativeClauses()
        self.prefix_subordination = PrefixSubordination()

    # Break the tree
    def break_tree(self, tree):
        self.appostions.break_tree(tree)
        self.relative_clauses.break_tree(tree)
        self.prefix_subordination.break_tree(tree)