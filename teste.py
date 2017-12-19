import similarityFunctions as sf

methods = sf.get_sim_methods_by_words()

w1 = "boat"
w2 = "boat"

for a in methods:
    print(a.similarity(w1, w2))

methods = sf.get_sim_methods_by_synsets()
syn1 = sf.wordnet.synsets(w1)
syn2 = sf.wordnet.synsets(w2)

for b in methods:
    print(b.similarity(syn1, syn2))