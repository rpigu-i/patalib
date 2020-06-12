import nltk
from nltk.corpus import wordnet
from .patalib import PataLib

class Clinamen(PataLib):
    """ Generate clinamen subclass """

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
        for i in range(-1,lenstr1+1):
            d[(i,-1)] = i+1
        for j in range(-1,lenstr2+1):
            d[(-1,j)] = j+1
 
        for i in range(lenstr1):
            for j in range(lenstr2):
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

