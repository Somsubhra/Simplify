__author__ = 's7a'


# The Sanitizer class
class Sanitizer:

    # Constructor for the sanitizer class
    def __init__(self):
        # Unused
        pass

    # Sanitize a given word
    @staticmethod
    def sanitize_word(word):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        return ''.join(w for w in word if w in alphabets)