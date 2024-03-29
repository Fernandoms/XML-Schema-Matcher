from nltk.corpus.reader import WordNetError
from nltk.metrics import distance
from nltk.corpus import wordnet, wordnet_ic
from pyjarowinkler import distance as jaroDistance


class Levenshtein:
    @staticmethod
    def similarity(word1, word2):
        return distance.edit_distance(word1, word2)


class LevenshteinTransposition:
    @staticmethod
    def similarity(word1, word2):
        return distance.edit_distance(word1, word2, transpositions=True)


class JaroWinkler:
    @staticmethod
    def similarity(word1, word2):
        return jaroDistance.get_jaro_distance(word1, word2, winkler=True)


class Jaro:
    @staticmethod
    def similarity(word1, word2):
        return jaroDistance.get_jaro_distance(word1, word2, winkler=False)


class WuPalmerSymilarity:
    @staticmethod
    def similarity(l1,l2):
        return getWupSimilarity(l1, l2)
    

class LchSimilarity:
    @staticmethod
    def similarity(l1,l2):
        return getLchSimilarity(l1, l2)


class PathSimilarity:
    @staticmethod
    def similarity(l1,l2):
        return getPathSimilarity(l1, l2)


class ResnikSimilarity:
    @staticmethod
    def similarity(l1,l2):
        brown_ic = wordnet_ic.ic('ic-brown.dat')
        return getResSimilarity(l1, l2, brown_ic)


class JiangConrathSimilarity:
    @staticmethod
    def similarity(l1,l2):
        brown_ic = wordnet_ic.ic('ic-brown.dat')
        return getJcnSimilarity(l1, l2, brown_ic)


class LinSimilarity:
    @staticmethod
    def similarity(l1,l2):
        brown_ic = wordnet_ic.ic('ic-brown.dat')
        return getLinSimilarity(l1, l2, brown_ic)


def getWupSimilarity(syn1, syn2):
    max_value = float(0)
    for s1 in syn1:
        for s2 in syn2:
            sim = s1.wup_similarity(s2)
            try:
                if sim > max_value:
                    max_value = sim
            except TypeError:
                pass
    return max_value


def getLchSimilarity(syn1, syn2):
    max_value = float(0)
    for s1 in syn1:
        for s2 in syn2:
            try:
                sim = s1.lch_similarity(s2)
                if sim > max_value:
                    max_value = sim
            except (TypeError, WordNetError):
                pass
    return max_value


def getPathSimilarity(syn1, syn2):
    max_value = float(0)
    for s1 in syn1:
        for s2 in syn2:
            try:
                sim = s1.path_similarity(s2)
                if sim > max_value:
                    max_value = sim
            except (TypeError, WordNetError):
                pass
    return max_value


def getResSimilarity(syn1, syn2, ic):
    max_value = float(0)
    for s1 in syn1:
        for s2 in syn2:
            try:
                sim = s1.res_similarity(s2, ic=ic)
                if sim > max_value:
                    max_value = sim
            except (TypeError, WordNetError):
                pass
    return max_value


def getLinSimilarity(syn1, syn2, ic):
    max_value = float(0)
    for s1 in syn1:
        for s2 in syn2:
            try:
                sim = s1.lin_similarity(s2, ic=ic)
                if sim > max_value:
                    max_value = sim
            except (TypeError, WordNetError):
                pass
    return max_value


def getJcnSimilarity(syn1, syn2, ic):
    max_value = float(0)
    for s1 in syn1:
        for s2 in syn2:
            try:
                sim = s1.jcn_similarity(s2, ic=ic)
                if sim > max_value:
                    max_value = sim
            except (TypeError, WordNetError):
                pass
    return max_value


def get_sim_methods_by_words():
    return [Levenshtein, LevenshteinTransposition, Jaro, JaroWinkler]


def get_sim_methods_by_synsets():
    return [WuPalmerSymilarity, LchSimilarity, PathSimilarity, ResnikSimilarity, JiangConrathSimilarity, LinSimilarity]

def demo():

    w1 = "boat"
    w2 = "boat"

    print("Levenshtein: " + str(Levenshtein.similarity(w1, w2)))
    print("LevenshteinTransposition: " + str(LevenshteinTransposition.similarity(w1, w2)))
    print("Jaro: " + str(Jaro.similarity(w1, w2)))
    print("JaroWinkler: " + str(JaroWinkler.similarity(w1,w2)))

    l1 = wordnet.synsets(w1)
    l2 = wordnet.synsets(w2)

    print("WuPalmerSymilarity: " + str(WuPalmerSymilarity.similarity(l1, l2)))
    print("LchSimilarity: " + str(LchSimilarity.similarity(l1, l2)))
    print("PathSimilarity: " + str(PathSimilarity.similarity(l1, l2)))

    print("ResnikSimilarity: " + str(ResnikSimilarity.similarity(l1, l2)))
    print("JiangConrathSimilarity: " + str(JiangConrathSimilarity.similarity(l1, l2)))
    print("LinSimilarity: " + str(LinSimilarity.similarity(l1, l2)))


if __name__ == "__main__":
    demo()
