__author__ = 's7a'

# All imports
from appositions import Appositions
from relative_clauses import RelativeClauses
from prefix_subordination import PrefixSubordination
from infix_subordination import InfixSubordination
from infix_coordination import InfixCoordination


# Constructor for the breaker class
class Breaker:

    # Constructor for the breaker class
    def __init__(self):
        self.appositions = Appositions()
        self.relative_clauses = RelativeClauses()
        self.prefix_subordination = PrefixSubordination()
        self.infix_subordination = InfixSubordination()
        self.infix_coordination = InfixCoordination()

    # Break the tree
    def break_tree(self, tree):
        self.appositions.break_tree(tree)
        self.relative_clauses.break_tree(tree)
        self.prefix_subordination.break_tree(tree)
        self.infix_subordination.break_tree(tree)
        self.infix_coordination.break_tree(tree)