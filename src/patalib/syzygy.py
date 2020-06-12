import nltk
from nltk.corpus import wordnet
from .patalib import PataLib



class Syzygy(PataLib):
    """ Syzygy subclass """

    def generate_syzygy(self, input_word):
        """ Generate a syzygy.  Here we
        generate a list of hypernyms associated
        with an input word. Using the hypernym we
        then generate another synonym. For example:
        The input word 'weed' will result in a syzgy
        of 'band' as in rock band.
        """
        results = []
        synset = wordnet.synsets(input_word)
        for i in synset:
            if i.hypernyms():
                hyp = i.hypernyms()[0].name().split('.')
                if '_' in hyp[0]:
                    hyp[0] = PataLib().strip_underscore(hyp[0])
                syns = wordnet.synsets(hyp[0])
                if len(syns) > 0:
                    name = syns[0].name().split('.')[0]
                    results.append(PataLib().strip_underscore(name))
        results = {'input' : input_word, 'results' : results, 'category' : 'syzygy'} 
        return results

