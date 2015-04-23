__author__ = 's7a'

# All imports
import syllables_en
from sanitizer import Sanitizer
import re


# The Flesch Kincaid class
class FleschKincaid:

    # Constructor for the Flesch Kincaid class
    def __init__(self):
        pass

    # Calculate the Flesch Kincaid grade level
    # Formula: 0.39 (Total Words / Total Sents) + 11.8 (Total Syllables / Total Words) - 15.59
    @staticmethod
    def calculate_grade_level(content):
        words = []
        tokens = content.split()
        garbage_words = ["", ";", ",", "!", "?", "."]

        number_of_syllables = 0

        for token in tokens:
            sanitized_word = Sanitizer.sanitize_word(token)

            if sanitized_word in garbage_words:
                continue
            else:
                number_of_syllables += syllables_en.count_syllables(sanitized_word)
                words.append(sanitized_word)

        token_arrays = re.split('\.|!|\?', content)
        sentences = []

        for sentence in token_arrays:
            if sentence not in garbage_words:
                sentences.append(sentence)

        number_of_sentences = len(sentences)
        number_of_words = len(words)

        print "Syllables: " + str(number_of_syllables)
        print "Words: " + str(number_of_words)
        print str(words)
        print "Sentences: " + str(number_of_sentences)
        print str(sentences)

        grade_level = 0.39 * (float(number_of_words) / float(number_of_sentences)) +\
                      11.8 * (float(number_of_syllables) / float(number_of_words)) - 15.59

        return grade_level
