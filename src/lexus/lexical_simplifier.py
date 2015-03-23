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

        length = len(words)

        results = []

        for i in range(length):

            sanitized_word = Sanitizer.sanitize_word(words[i])

            if sanitized_word == '':
                continue

            neighbors = []

            if not(i < lwlm_n / 2 or i > length - 1 - lwlm_n / 2):
                for j in range(1, lwlm_n / 2 + 1):
                    neighbors.append(Sanitizer.sanitize_word(words[i - j]))
                for j in range(1, lwlm_n / 2 + 1):
                    neighbors.append(Sanitizer.sanitize_word(words[i + j]))

            replacer = Replacer()
            result = replacer.detailed_replacement(sanitized_word, neighbors)
            results.append(result)

        return results