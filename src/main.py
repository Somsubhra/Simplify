__author__ = 's7a'

# All imports
from extras import Logger
from lexus import LexicalSimplifier
from syntax import SyntacticSimplifier

from os import path

# The main method
def main():
    Logger.log_message("Running application Simplify")

    # Lexical simplification
    lexical_simplifier = LexicalSimplifier('corpus', path.join('out', 'lexis'))
    lexical_simplifier.run()

    # Syntactic simplification
    syntactic_simplifier = SyntacticSimplifier('', '')
    syntactic_simplifier.run()

    Logger.log_success("Application exited successfully")

# Call the main method
if __name__ == '__main__':
    main()