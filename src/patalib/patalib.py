import nltk
import mmap
import re
from nltk.corpus import wordnet
from random import randint

class PataLib():
    """ Class containing functions for
    generating patadata results
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
             syn = i.name.split('.')
             if syn[index]!= input_word:
                 name = syn[0]
                 results.append(self.strip_underscore(name))
             else:
                 index = index + 1
         results = {'input' : input_word, 'results' : results, 'category' : 'synonym'} 
         return results

 
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
                       name = j.antonyms()[0].name
                       results.append(self.strip_underscore(name))
        results = {'input' : input_word, 'results' : results, 'category' : 'antonym'} 
        return results
 
 
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
                hyp = i.hypernyms()[0].name.split('.')
                if '_' in hyp[0]:
                    hyp[0] = self.strip_underscore(hyp[0])
                syns = wordnet.synsets(hyp[0])
                if len(syns) > 0:
                    name = syns[0].name.split('.')[0]
                    results.append(self.strip_underscore(name))
        results = {'input' : input_word, 'results' : results, 'category' : 'syzygy'} 
        return results
 

    def generate_anomaly(self, input_word, list_of_dict_words, num):
        """ Generate an anomaly. This is done
        via a Psuedo-random number generator.
        """

        results = []
        for i in range(0,num):
            index = randint(0,len(list_of_dict_words)-1)
            name = list_of_dict_words[index]
            if name != input_word and name not in results:
                results.append(self.strip_underscore(name))
            else:
                i = i +1
        results = {'input' : input_word, 'results' : results, 'category' : 'anomaly'} 
        return results
 

    def generate_clinamen(self, input_word, list_of_dict_words, swerve):
        """ Generate a clinamen. Here we
        looks for words via the damerau levenshtein distance
        with a distance of 2.
        """
 
        results = []
        selected_list = []
        for i in list_of_dict_words: #produce a subset for efficency
            if len(i) < len(input_word)+1 and len(i) > len(input_word)/2:
                if '_' not in i:
                    selected_list.append(i)
        for i in selected_list:
            match = self.damerau_levenshtein_distance(input_word,i)
            if match == swerve:
                results.append(i)
        results = {'input' : input_word, 'results' : results, 'category' : 'clinamen'} 
        return results
 
 
    def damerau_levenshtein_distance(self, s1, s2):
        """ Dervied algorithm from the following website:
        https://www.guyrutenberg.com/2008/12/15/damerau-levenshtein-distance-in-python/
        Gives us the distance between two words.
        """
        d = {}
        lenstr1 = len(s1)
        lenstr2 = len(s2)
        for i in xrange(-1,lenstr1+1):
            d[(i,-1)] = i+1
        for j in xrange(-1,lenstr2+1):
            d[(-1,j)] = j+1
 
        for i in xrange(lenstr1):
            for j in xrange(lenstr2):
                if s1[i] == s2[j]:
                    cost = 0
                else:
                    cost = 1
                d[(i,j)] = min(
                               d[(i-1,j)] + 1, # deletion
                               d[(i,j-1)] + 1, # insertion
                               d[(i-1,j-1)] + cost, # substitution
                              )
                if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                    d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
 
        return d[lenstr1-1,lenstr2-1]
 
 
    def strip_underscore(self, input_word):
        """ Remove underscore from word """
        if '_' in input_word:
            return input_word.replace('_',' ')
        else:
            return input_word
 

    def palindrome(self, input_word):  
        """ Check if string is a plaindrome """
        return str(input_word) == str(input_word)[::-1]
