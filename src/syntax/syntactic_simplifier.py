__author__ = 's7a'

# All imports
from extras import Logger


# The Syntactic simplification class
class SyntacticSimplifier:

    # Constructor for the Syntactic Simplifier
    def __init__(self, in_dir, out_dir):
        self.in_dir = in_dir
        self.out_dir = out_dir

    # Run the Syntactic Simplifier
    def run(self):
        Logger.log_message('Running Syntactic Simplifier')
        Logger.log_success('Syntactic Simplifier finished successfully')