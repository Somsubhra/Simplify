__author__ = 's7a'

# All imports
from extras import Logger


# The Lexical simplification class
class LexicalSimplifier:

    # Constructor for the Lexical Simplifier
    def __init__(self, in_dir, out_dir):
        Logger.log_message('Initializing Lexical Simplifier')
        self.in_dir = in_dir
        self.out_dir = out_dir

    # Run the Lexical Simplifier
    def run(self):
        Logger.log_message('Running Lexical Simplifier')
        Logger.log_success('Lexical Simplifier finished successfully')