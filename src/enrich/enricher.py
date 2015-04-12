__author__ = 's7a'

# All imports
from extras import Sanitizer
from kucera_francis_enricher import KuceraFrancisEnricher


# The text enrichment class
class Enricher:

    # Constructor for the enricher
    def __init__(self):
        self.kfe = KuceraFrancisEnricher()

    # Enrich the text
    def enrich(self, content):
        words = [str(word) for word in content.split()]

        result = ""

        for word in words:
            sanitized_word = Sanitizer.sanitize_word(word)

            if sanitized_word == '':
                continue

            result += self.kfe.enrich_word(sanitized_word) + " "

        return result