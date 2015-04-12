__author__ = 's7a'

# All imports
from extras import KuceraFrancis
from resource import Resource
from os import path


# The Kucera Francis enrichment class
class KuceraFrancisEnricher:

    # Constructor for the Kucera Francis Enricher
    def __init__(self):
        self.kf = KuceraFrancis(path.join('data', 'kucera_francis.csv'))

    # Enrich the word
    def enrich_word(self, word):
        if self.kf.frequency(word) == 0:
            return Resource.link(word)
        return word