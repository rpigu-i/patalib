import nltk
from nltk.corpus import wordnet
from .patalib import PataLib

class Antonym(PataLib):
    """ Antonym subclass """


    def generate_antonym(self, input_word):
        """ Generate an antonym using a Synset
        and its lemmas.
        """
        results = []
        synset = wordnet.synsets(input_word)
        for i in synset:
            if i.pos in ['n','v']:
                for j in i.lemmas:
                   if j.antonyms():
                       name = j.antonyms()[0].name()
                       results.append(PataLib().strip_underscore(name))
        results = {'input' : input_word, 'results' : results, 'category' : 'antonym'} 
        return results

