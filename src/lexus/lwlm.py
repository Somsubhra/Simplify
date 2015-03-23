__author__ = 's7a'

# All imports
from extras import Logger
from n_gram_frequency import NGramFrequency
from os import path


# The Latent Words Language Model
class LWLM:

    # Constructor for the LWLM
    def __init__(self, in_dir):
        self.three_gram_freq = NGramFrequency(3, in_dir, path.join('out', '3gram.csv'))
        self.three_gram_freq.run()
        self.three_gram_neighbors = self.three_gram_freq.get_neighbors()

        self.five_gram_freq = NGramFrequency(5, in_dir, path.join('out', '5gram.csv'))
        self.five_gram_freq.run()
        self.five_gram_neighbors = self.five_gram_freq.get_neighbors()

        self.dump_results()

    # Get the lwlm words for a given word
    def get(self, word, neighbors, n):

        # Construct the neighbor string
        neighbor_str = ""

        for i in range(n - 1):
            neighbor_str += neighbors[i] + '|'

            if i == n / 2 - 1:
                neighbor_str += '|'

        if n == 3:
            neighbors_dict = self.three_gram_neighbors
        elif n == 5:
            neighbors_dict = self.five_gram_neighbors
        else:
            Logger.log_error('n = ' + str(n) + ' not supported in LWLM')
            return []

        if neighbor_str in neighbors_dict:
            alt_words = list(neighbors_dict[neighbor_str])
        else:
            alt_words = []

        if word not in alt_words:
            alt_words.append(word)

        return alt_words

    # Dump the results in an output file
    def dump_results(self):

        out_file = path.join('out', '3neighbors.csv')
        Logger.log_message('Writing 3-Gram neighbors to ' + out_file)
        output_file = open(out_file, 'w+')

        for neighbors in self.three_gram_neighbors:
            words = set(self.three_gram_neighbors[neighbors])
            col = ' '.join(w for w in words)
            output_file.write(neighbors + ';' + col + '\n')

        output_file.close()
        Logger.log_success('3-Gram neighbors have been written to ' + out_file)

        out_file = path.join('out', '5neighbors.csv')
        Logger.log_message('Writing 5-Gram neighbors to ' + out_file)
        output_file = open(out_file, 'w+')

        for neighbors in self.five_gram_neighbors:
            words = set(self.five_gram_neighbors[neighbors])
            col = ' '.join(w for w in words)
            output_file.write(neighbors + ';' + col + '\n')

        output_file.close()
        Logger.log_success('5-Gram neighbors have been written to ' + out_file)