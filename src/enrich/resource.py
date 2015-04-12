__author__ = 's7a'


# The Resources class
class Resource:

    # Constructor for the Resource class
    def __init__(self):
        # Unused
        pass

    # Link the word with the resource
    @staticmethod
    def link(word):
        return '<a href="#">' + word + '</a>'