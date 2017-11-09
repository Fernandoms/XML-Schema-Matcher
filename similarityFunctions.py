from nltk.metrics import distance
from nltk.corpus import wordnet
class Levenshtein:
    @staticmethod
    def similarity(word1, word2):
        print (distance.edit_distance(word1, word2))

class LevenshteinTransposition:
    @staticmethod
    def similarity(word1, word2):
        print (distance.edit_distance(word1, word2, transpositions=True))

class WuPalmerSymilarity:
    @staticmethod
    def similarity(word1, word2):
        l1 = wordnet.synsets(word1)
        l2 = wordnet.synsets(word2)
        print (getSynonymsSimilarity(l1, l2))

def getSynonymsSimilarity(syn1, syn2):
    maxValue = float(0)
    for s1 in syn1:
        for s2 in syn2:
            sim = s1.wup_similarity(s2)
            try:
                if sim > maxValue:
                    maxValue = sim
            except (TypeError):
                pass
    return maxValue

w1 = "bare"
w2 = "bear"

Levenshtein.similarity(w1, w2)
LevenshteinTransposition.similarity(w1, w2)
WuPalmerSymilarity.similarity(w1, w2)
