__author__ = 's7a'

# All imports
from extras import Logger
from extras import Sanitizer
from os import walk, stat, path


# Builds up the N-Gram Frequency table
class NGramFrequency:

    # Constructor for the N-Gram Frequency counter
    def __init__(self, n, in_dir, out_file):
        self.n = n
        self.in_dir = in_dir
        self.out_file = out_file
        self.table = {}

    # Run the N-Gram Frequency Counter
    def run(self):
        Logger.log_message('Running N-Gram Frequency counter')

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

        Logger.log_success('N-Gram Frequency counter exited successfully')

    # Parse a given file and build the N-Gram frequency table
    def parse_file(self, in_file):
        Logger.log_message('Running N-Gram Frequency counter on ' + in_file)

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
            for j in range(self.n):
                s += content[i + j]
                if j != self.n - 1:
                    s += '|'

            if s in self.table:
                self.table[s] += 1
            else:
                self.table[s] = 1

        input_file.close()

    # Dump the results to the output file
    def dump_results(self):

        Logger.log_message('Writing N-Gram table to ' + self.out_file)

        output_file = open(self.out_file, 'w+')

        for s in self.table:
            output_file.write(s + ';' + str(self.table[s]) + '\n')

        output_file.close()

        Logger.log_success('Finished writing N-Gram table to ' + self.out_file)