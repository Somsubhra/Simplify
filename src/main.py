__author__ = 's7a'

# All imports
from extras import Logger
from lexus import LexicalSimplifier
from syntax import SyntacticSimplifier
from webapp import WebApp
from os import path
import sys


# The main method
def main():
    if len(sys.argv) > 1:
        Logger.log_message('Running application server')
        if sys.argv[1] == 'server':
            web_app = WebApp('localhost', 8000, True)
            web_app.run()
            return

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