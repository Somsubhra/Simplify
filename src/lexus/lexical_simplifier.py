__author__ = 's7a'

# All imports
from extras import Logger
from extras import Sanitizer
from replacer import Replacer
from os import walk, path, stat, makedirs


# The Lexical simplification class
class LexicalSimplifier:

    # Constructor for the Lexical Simplifier
    def __init__(self, in_dir, out_dir):
        Logger.log_message('Initializing Lexical Simplifier')
        self.in_dir = in_dir
        self.out_dir = out_dir

        self.replacer = Replacer()

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

                self.simplify_file(in_file, out_file)

        Logger.log_success('Lexical Simplifier finished successfully')

    # Simplify a given file
    def simplify_file(self, in_file, out_file):
        Logger.log_message('Running Lexical Simplifier on ' + in_file)

        input_file = open(in_file, 'r')
        output_file = open(out_file, 'w')

        for line in input_file.readlines():
            words = [str(word) for word in line.split()]
            new_words = []

            for word in words:
                sanitized_word = Sanitizer.sanitize_word(word)

                if sanitized_word == '':
                    continue

                replaced_word = self.replacer.replacement(sanitized_word)
                new_words.append(replaced_word)

            output_file.write(' '.join(new_words) + '\n')

        input_file.close()
        output_file.close()

        Logger.log_success('Results have been written to ' + out_file)

    # Simplify a given content
    @staticmethod
    def simplify(content):
        words = [str(word) for word in content.split()]
        new_words = []

        for word in words:
            sanitized_word = Sanitizer.sanitize_word(word)

            if sanitized_word == '':
                continue

            replacer = Replacer()
            replaced_word = replacer.replacement(sanitized_word)
            new_words.append(replaced_word)

        return ' '.join(new_words)