__author__ = 's7a'

# All imports
from extras import Logger
from n_gram import NGram


# The Latent Words Language Model
class LWLM:

    # Constructor for the LWLM
    def __init__(self):
        pass

    # Get the lwlm words for a given word
    def get(self, word, neighbors):
        pass

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
