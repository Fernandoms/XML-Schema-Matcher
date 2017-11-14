from nltk.corpus.reader import WordNetError
from nltk.metrics import distance
from nltk.corpus import wordnet
from pyjarowinkler import distance as jaroDistance

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
        print (getWupSimilarity(l1, l2))

class ResnikSymilarity:
    @staticmethod
    def similarity(word1, word2):
        l1 = wordnet.synsets(word1)
        l2 = wordnet.synsets(word2)
        print (getResSimilarity(l1, l2))

class JaroWinkler:
    @staticmethod
    def similarity(word1, word2):
        print (jaroDistance.get_jaro_distance(word1, word2, winkler=True))

class Jaro:
    @staticmethod
    def similarity(word1, word2):
        print (jaroDistance.get_jaro_distance(word1, word2, winkler=False))

class LchSimilarity:
    @staticmethod
    def similarity(word1, word2):
        l1 = wordnet.synsets(word1)
        l2 = wordnet.synsets(word2)
        print(getLchSimilarity(l1, l2))

class PathSimilarity:
    @staticmethod
    def similarity(word1, word2):
        l1 = wordnet.synsets(word1)
        l2 = wordnet.synsets(word2)
        print(getPathSimilarity(l1, l2))

def getWupSimilarity(syn1, syn2):
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

def getResSimilarity(syn1, syn2):
    maxValue = float(0)
    for s1 in syn1:
        for s2 in syn2:
            sim = s1.res_similarity(s2)
            try:
                if sim > maxValue:
                    maxValue = sim
            except (TypeError):
                pass
    return maxValue

def getLchSimilarity(syn1, syn2):
    maxValue = float(0)
    for s1 in syn1:
        for s2 in syn2:
            try:
                sim = s1.lch_similarity(s2)
                if sim > maxValue:
                    maxValue = sim
            except (TypeError, WordNetError):
                pass
    return maxValue

def getPathSimilarity(syn1, syn2):
    maxValue = float(0)
    for s1 in syn1:
        for s2 in syn2:
            try:
                sim = s1.path_similarity(s2)
                if sim > maxValue:
                    maxValue = sim
            except (TypeError, WordNetError):
                pass
    return maxValue


w1 = "boat"
w2 = "ship"

Levenshtein.similarity(w1, w2)
LevenshteinTransposition.similarity(w1, w2)
Jaro.similarity(w1, w2)
JaroWinkler.similarity(w1,w2)

WuPalmerSymilarity.similarity(w1, w2)
LchSimilarity.similarity(w1, w2)
PathSimilarity.similarity(w1,w2)
