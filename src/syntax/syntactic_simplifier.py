__author__ = 's7a'

# All imports
from extras import Logger
from os import walk, path, stat, makedirs


# The Syntactic simplification class
class SyntacticSimplifier:

    # Constructor for the Syntactic Simplifier
    def __init__(self, in_dir, out_dir):
        self.in_dir = in_dir
        self.out_dir = out_dir

    # Run the Syntactic Simplifier
    def run(self):
        Logger.log_message('Running Syntactic Simplifier')

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

                self.simplify_file(in_file, out_file)

        Logger.log_success('Syntactic Simplifier finished successfully')

    def simplify_file(self, in_file, out_file):
        pass

    @staticmethod
    def simplify(content):
        pass