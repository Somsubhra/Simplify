__author__ = 's7a'

# All imports
from nltk.stem import PorterStemmer


# The stemmed Kucera Francis Frequency class
class StemmedKuceraFrancis:

    # Constructor for the stemmed Kucera Francis class
    def __init__(self, dict_file):
        dict = open(dict_file, 'r')

        # Construct the Kucera Francis frequency dictionary
        self.frequencies = {}

        for line in dict.readlines():
            cols = line.split(";")
            stemmed_word = PorterStemmer().stem_word(cols[0])
            self.frequencies[stemmed_word] = int(cols[1])

    # Calculate the stemmed Kucera Francis frequency of the word
    def frequency(self, word):
        stemmed_word = PorterStemmer().stem_word(word)

        if stemmed_word in self.frequencies:
            return self.frequencies[stemmed_word]
        else:
            return 0
