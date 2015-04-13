__author__ = 's7a'

# All imports
from appositions import Appositions
from relative_clauses import RelativeClauses
from subordination import Subordination
from infix_coordination import InfixCoordination


# Constructor for the breaker class
class Breaker:

    # Constructor for the breaker class
    def __init__(self):
        self.appositions = Appositions()
        self.relative_clauses = RelativeClauses()
        self.subordination = Subordination()
        self.infix_coordination = InfixCoordination()

    # Break the tree
    def break_tree(self, tree):
        self.appositions.break_tree(tree)
        self.relative_clauses.break_tree(tree)
        self.subordination.break_tree(tree)
        self.infix_coordination.break_tree(tree)