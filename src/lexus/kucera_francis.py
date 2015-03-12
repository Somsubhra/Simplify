__author__ = 's7a'


# The Kucera Francis class
class KuceraFrancis:

    # Constructor for the Kucera Francis class
    def __init__(self, dict_file):
        dict = open(dict_file, 'r')

        # Construct the Kucera Francis frequency dictionary
        self.kucera_francis_frequency = {}

        for line in dict.readlines():
            cols = line.split(';')
            self.kucera_francis_frequency[cols[0]] = int(cols[1])

    # Get the Kucera Francis frequency for a word
    def frequency(self, word):
        if word in self.kucera_francis_frequency:
            return self.kucera_francis_frequency[word]
        else:
            return 0

    # Get the word with maximum Kucera Francis frequency
    def maximum(self, words):
        result = ''

        for word in words:
            if self.frequency(word) > self.frequency(result):
                result = word

        return result