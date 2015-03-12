__author__ = 's7a'

# All imports
from kucera_francis import KuceraFrancis
from synonyms import Synonyms
from os import path


# The Replacer class
class Replacer:

    # Constructor for the Replacer class
    def __init__(self):
        self.kf = KuceraFrancis(path.join('data', 'kucera_francis.csv'))

    # Replace the word with its alternative
    def replacement(self, word):
        words = Synonyms.get(word)
        return self.kf.maximum(words)