import nltk
from nltk.corpus import wordnet
from .patalib import PataLib
from random import randint

class Anomaly(PataLib):
    """ Anomaly sub class """

    def generate_anomaly(self, input_word, list_of_dict_words, num):
        """ Generate an anomaly. This is done
        via a Psuedo-random number generator.
        """

        results = []
        for i in range(0,num):
            index = randint(0,len(list_of_dict_words)-1)
            name = list_of_dict_words[index]
            if name != input_word and name not in results:
                results.append(PataLib().strip_underscore(name))
            else:
                i = i +1
        results = {'input' : input_word, 'results' : results, 'category' : 'anomaly'} 
        return results

