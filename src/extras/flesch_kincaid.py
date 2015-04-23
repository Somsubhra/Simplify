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

        sentences = re.split('\.|!|\?', content)

        number_of_sentences = len(sentences)
        number_of_words = len(words)

        grade_level = 0.39 * (number_of_words / number_of_sentences) +\
                      11.8 * (number_of_syllables / number_of_words) - 15.59

        return grade_level
