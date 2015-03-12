__author__ = 's7a'

# All imports
from extras import Logger
from os import walk, path, stat, makedirs


# The Lexical simplification class
class LexicalSimplifier:

    # Constructor for the Lexical Simplifier
    def __init__(self, in_dir, out_dir):
        Logger.log_message('Initializing Lexical Simplifier')
        self.in_dir = in_dir
        self.out_dir = out_dir

    # Run the Lexical Simplifier
    def run(self):
        Logger.log_message('Running Lexical Simplifier')

        try:
            stat(self.in_dir)
        except:
            Logger.log_error('Input text not found')
            return

        try:
            stat(self.out_dir)
        except:
            makedirs(self.out_dir)

        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:
                in_file = path.join(dir_path, file_name)
                out_file = path.join(self.out_dir, file_name + '_' + dir_path.replace('/', '_') + '.txt')

                self.simplify(in_file, out_file)

        Logger.log_success('Lexical Simplifier finished successfully')

    # Simplify a given file
    @staticmethod
    def simplify(in_file, out_file):
        Logger.log_message('Running Lexical Simplifier on ' + in_file)

        input_file = open(in_file, 'r')
        output_file = open(out_file, 'w')

        input_file.close()
        output_file.close()

        Logger.log_success('Results have been written to ' + out_file)