__author__ = 's7a'

# All imports
from extras import Logger
from n_gram import NGram
from os import path


# The Latent Words Language Model
class LWLM:

    # Constructor for the LWLM
    def __init__(self, in_file):

        # Build up the LWLM tables
        input_file = open(in_file)
        self.alt_words_table = {}

        for line in input_file.readlines():
            cols = line.split(";")
            self.alt_words_table[str(cols[0])] = str(cols[1]).split()

        input_file.close()

    # Get the LWLM alternate words for a given word
    def get(self, word):
        if word in self.alt_words_table:
            return list(set(self.alt_words_table[word]))
        else:
            return [word]

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

        LWLM.build_alt_words_table(3)
        LWLM.build_alt_words_table(5)

    # Build the LWLM alt words table based on n-grams
    @staticmethod
    def build_alt_words_table(n):

        Logger.log_message('Building alternate words table based on ' + str(n) + '-grams')
        alt_words = {}

        in_file = path.join('out', str(n) + '-gram-regexp.csv')
        Logger.log_message('Reading ' + in_file)

        input_file = open(in_file)

        for line in input_file.readlines():
            words = str(line.split(';')[1]).split()
            for word in words:
                for alt_word in words:
                    if word in alt_words:
                        if alt_word not in alt_words[word]:
                            alt_words[word].append(alt_word)
                    else:
                        alt_words[word] = [alt_word]

        input_file.close()
        Logger.log_success('Finished reading ' + in_file)

        out_file = path.join('out', 'lwlm-alt-words-' + str(n) + '-grams.csv')
        Logger.log_message('Writing alternate words table to ' + out_file)
        output_file = open(out_file, 'w+')

        for word in alt_words:
            words = set(alt_words[word])
            col = ' '.join(w for w in words)
            output_file.write(word + ';' + col + '\n')

        output_file.close()
        Logger.log_success('Alternate words table has been written to ' + out_file)
