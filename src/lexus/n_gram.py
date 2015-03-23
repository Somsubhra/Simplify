__author__ = 's7a'

# All imports
from extras import Logger
from extras import Sanitizer
from os import walk, stat, path


# The N-Gram class
class NGram:

    # Constructor for the N-Gram class
    def __init__(self, n, in_dir):
        self.n = n
        self.in_dir = in_dir
        self.table = {}
        self.neighbors = {}

    # Run the N-Gram utility
    def run(self):
        Logger.log_message('Running ' + str(self.n) + '-Gram Frequency counter')

        try:
            stat(self.in_dir)
        except:
            Logger.log_error('Input text not found')
            return

        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:
                in_file = path.join(dir_path, file_name)
                self.parse_file(in_file)

        self.dump_results()

        Logger.log_success(str(self.n) + '-Gram Frequency counter exited successfully')

    # Parse a given file and build the N-Gram tables
    def parse_file(self, in_file):
        Logger.log_message('Running ' + str(self.n) + '-Gram Frequency counter on ' + in_file)

        input_file = open(in_file)

        # Create a sanitized content string
        content = ""

        for line in input_file.readlines():
            words = line.split()
            for word in words:
                content += Sanitizer.sanitize_word(word) + " "

        content = content.split()

        length = len(content)

        # Parse the content
        for i in range(length - self.n + 1):
            s = ""
            neighbor_str = ""
            word = ""

            for j in range(self.n):
                s += content[i + j]

                if j == self.n / 2:
                    neighbor_str += '*'
                    word = content[i + j]
                else:
                    neighbor_str += content[i + j]
                    pass

                if j != self.n - 1:
                    s += '|'
                    neighbor_str += '|'

            if s in self.table:
                self.table[s] += 1
            else:
                self.table[s] = 1

            if neighbor_str in self.neighbors:
                self.neighbors[neighbor_str].append(word)
            else:
                self.neighbors[neighbor_str] = [word]

        input_file.close()

    # Dump the results to the output file
    def dump_results(self):

        out_file = path.join('out', str(self.n) + '-gram.csv')
        Logger.log_message('Writing ' + str(self.n) + '-Gram table to ' + out_file)
        output_file = open(out_file, 'w+')

        for s in self.table:
            output_file.write(s + ';' + str(self.table[s]) + '\n')

        output_file.close()
        Logger.log_success('Finished writing ' + str(self.n) + '-Gram table to ' + out_file)

        out_file = path.join('out', str(self.n) + '-gram-regexp.csv')
        Logger.log_message('Writing ' + str(self.n) + '-Gram Regular Expressions to ' + out_file)
        output_file = open(out_file, 'w+')

        for nb in self.neighbors:
            words = set(self.neighbors[nb])
            col = ' '.join(w for w in words)
            output_file.write(nb + ';' + col + '\n')

        output_file.close()
        Logger.log_success(str(self.n) + '-Gram Regular Expressions have been written to ' + out_file)
