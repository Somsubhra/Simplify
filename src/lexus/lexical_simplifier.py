__author__ = 's7a'

# All imports
from extras import Sanitizer
from replacer import Replacer


# The Lexical simplification class
class LexicalSimplifier:

    # Constructor for the Lexical Simplifier
    def __init__(self):
        # Unused
        pass

    # Simplify a given content
    @staticmethod
    def simplify(content, lwlm_n):
        words = [str(word) for word in content.split()]

        results = []
        replacer = Replacer(lwlm_n)

        for word in words:

            sanitized_word = Sanitizer.sanitize_word(word)

            if sanitized_word == '':
                continue

            result = replacer.detailed_replacement(sanitized_word)
            results.append(result)

        return results