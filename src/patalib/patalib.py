import nltk
from nltk.corpus import wordnet
from random import randint

class PataLib():
    """ Class containing functions for
    generating patadata results
    """

    def strip_underscore(self, input_word):
        """ Remove underscore from word """
        if '_' in input_word:
            return input_word.replace('_',' ')
        else:
            return input_word
 

    def palindrome(self, input_word):  
        """ Check if string is a plaindrome """
        return str(input_word) == str(input_word)[::-1]
