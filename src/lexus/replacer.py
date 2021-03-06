__author__ = 's7a'

# All imports
from os import path

from lwlm import LWLM
from extras import KuceraFrancis
from synonyms import Synonyms



# The Replacer class
class Replacer:

    # Constructor for the Replacer class
    def __init__(self, lwlm_n):
        self.kf = KuceraFrancis(path.join('data', 'kucera_francis.csv'))
        self.lwlm = LWLM(path.join('out', 'lwlm-alt-words-' + str(lwlm_n) + '-grams.csv'))

    # Give a detailed analysis along with the replacement
    def detailed_replacement(self, word):

        replaced_word = ''

        if word == '':
            return {
                'word': word,
                'alt_word': replaced_word,
                'wordnet': '',
                'lwlm': '',
                'intersection': ''
            }

        wordnet_words = Synonyms.get(word)
        lwlm_words = self.lwlm.get(word)
        intersection_words = list(set(wordnet_words) & set(lwlm_words))

        intersection_results = []

        for intersection_word in intersection_words:
            intersection_results.append(intersection_word + '(KFF=' + str(self.kf.frequency(intersection_word)) + ')')

        return {
            'word': word,
            'alt_word': self.kf.maximum(intersection_words),
            'wordnet': str(wordnet_words),
            'lwlm': str(lwlm_words),
            'intersection': str(intersection_results)
        }