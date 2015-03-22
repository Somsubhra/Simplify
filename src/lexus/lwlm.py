__author__ = 's7a'

# All imports
from n_gram_frequency import NGramFrequency
from os import path


# The Latent Words Language Model
class LWLM:

    # Constructor for the LWLM
    def __init__(self, in_dir):
        self.n_gram_freq = NGramFrequency(3, in_dir, path.join('out', 'ngram.csv'))
        self.n_gram_freq.run()

    # Get the lwlm words for a given word
    def get(self, word):
        result = [word]
        return result