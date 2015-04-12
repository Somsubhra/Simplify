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
    @staticmethod
    def enrich(content):
        return content