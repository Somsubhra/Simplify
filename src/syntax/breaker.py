__author__ = 's7a'

# All imports
from parser import Parser
from appositions import Appositions
from relative_clauses import RelativeClauses
from prefix_subordination import PrefixSubordination
from infix_subordination import InfixSubordination
from infix_coordination import InfixCoordination

import re


# The breaker class
class Breaker:

    # Constructor for the breaker class
    def __init__(self):
        self.parser = Parser()
        self.appositions = Appositions()
        self.relative_clauses = RelativeClauses()
        self.prefix_subordination = PrefixSubordination()
        self.infix_subordination = InfixSubordination()
        self.infix_coordination = InfixCoordination()

    # Break the tree
    def break_tree(self, tree, detailed=False):

        res_1 = self.appositions.break_tree(tree)
        res_2 = self.break_tree_with_type(res_1, self.relative_clauses)
        res_3 = self.break_tree_with_type(res_2, self.prefix_subordination)
        res_4 = self.break_tree_with_type(res_3, self.infix_subordination)
        res_5 = self.break_tree_with_type(res_4, self.infix_coordination)

        if detailed:
            apposition_result = self.appositions.break_tree(tree)
            relative_clause_result = self.relative_clauses.break_tree(tree)
            prefix_subordination_result = self.prefix_subordination.break_tree(tree)
            infix_subordination_result = self.infix_subordination.break_tree(tree)
            infix_coordination_result = self.infix_coordination.break_tree(tree)

            return {
                "original": ' '.join(tree.leaves()),
                "final": res_5,
                "apposition": apposition_result,
                "relative_clause": relative_clause_result,
                'prefix_subordination': prefix_subordination_result,
                "infix_subordination": infix_subordination_result,
                "infix_coordination": infix_coordination_result
            }
        else:
            return {
                "final": res_5
            }

    def break_tree_with_type(self, string, breaker_type):
        sentences = re.split('\.|!|\?', string)

        result = ""

        for sentence in sentences:
            sentence += "."

            if sentence == ".":
                continue

            parse_trees = self.parser.parse(sentence, False)

            for parse_tree in parse_trees:
                broken_string = breaker_type.break_tree(parse_tree)
                result += broken_string

        return result