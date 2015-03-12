__author__ = 's7a'

# All imports
from nltk.corpus import wordnet


# The Synonyms class
class Synonyms:

    # Constructor for the Synonyms class
    def __init__(self):
        # Unused
        pass

    # Get the synonyms of a word
    @staticmethod
    def get(word):
        synonyms = []
        sets = wordnet.synsets(word)

        for item in sets:
            synonyms.append(str(item.name()).split('.')[0])

        return synonyms