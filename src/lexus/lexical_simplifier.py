__author__ = 's7a'

# All imports
from extras import Logger
from extras import Sanitizer
from replacer import Replacer


# The Lexical simplification class
class LexicalSimplifier:

    # Constructor for the Lexical Simplifier
    def __init__(self):
        pass

    # Simplify a given content
    @staticmethod
    def simplify(content):
        words = [str(word) for word in content.split()]
        new_words = []

        for word in words:
            sanitized_word = Sanitizer.sanitize_word(word)

            if sanitized_word == '':
                continue

            replacer = Replacer()
            replaced_word = replacer.replacement(sanitized_word)
            new_words.append(replaced_word)

        return ' '.join(new_words)