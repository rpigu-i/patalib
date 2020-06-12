import nltk
from nltk.corpus import wordnet
from random import randint
from .patalib import PataLib

class Synonym(PataLib):
    """ Sub class of PataLib
    """
    
    def generate_synonym(self, input_word):
         """ Generate Synonym using a WordNet
         synset.
         """
         results = []
         results.append(input_word)
         synset = wordnet.synsets(input_word)
         for i in synset:
             index = 0
             syn = i.name().split('.')
             if syn[index]!= input_word:
                 name = syn[0]
                 results.append(PataLib().strip_underscore(name))
             else:
                 index = index + 1
         results = {'input' : input_word, 'results' : results, 'category' : 'synonym'} 
         return results
