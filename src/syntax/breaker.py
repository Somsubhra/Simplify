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
        apposition_result = self.appositions.break_tree(tree)
        relative_clause_result = self.relative_clauses.break_tree(tree)
        prefix_subordination_result = self.prefix_subordination.break_tree(tree)
        infix_subordination_result = self.infix_subordination.break_tree(tree)
        infix_coordination_result = self.infix_coordination.break_tree(tree)

        return {
            "original": ' '.join(tree.leaves()),
            "apposition": apposition_result,
            "relative_clause": relative_clause_result,
            'prefix_subordination': prefix_subordination_result,
            "infix_subordination": infix_subordination_result,
            "infix_coordination": infix_coordination_result
        }