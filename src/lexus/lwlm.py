__author__ = 's7a'

# All imports
from extras import Logger
from n_gram import NGram


# The Latent Words Language Model
class LWLM:

    # Constructor for the LWLM
    def __init__(self, in_file):

        # Build up the LWLM tables
        input_file = open(in_file)
        self.regexp_table = {}

        for line in input_file.readlines():
            cols = line.split(";")
            self.regexp_table[str(cols[0])] = str(cols[1])

        input_file.close()

    # Get the LWLM words for a given word
    def get(self, word, neighbors):
        l = len(neighbors)

        # Build up the regular expression
        regexp = ""

        for i in range(l):
            regexp += neighbors[i]

            if i == l - 1:
                break

            if i == l / 2 - 1:
                regexp += '|*|'
            else:
                regexp += '|'

        # Get the alternate words from LWLM
        alt_words = []

        if regexp in self.regexp_table:
            words = str(self.regexp_table[regexp]).split()

            for w in words:
                alt_words.append(str(w))

        if word not in alt_words:
            alt_words.append(word)

        return list(set(alt_words))

    # Build the LWLM tables
    @staticmethod
    def build_tables(in_dir):
        Logger.log_message('Building 3-Gram LWLM tables')
        ng = NGram(3, in_dir)
        ng.run()
        Logger.log_success('Finished building 3-Gram LWLM tables')

        Logger.log_message('Building 5-Gram LWLM tables')
        ng = NGram(5, in_dir)
        ng.run()
        Logger.log_success('Finished building 5-Gram LWLM tables')
