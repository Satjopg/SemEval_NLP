## coding: UTF-8

import re
from lcs import get_stopword

def ngram_sim(a, b, n):
	asent = [word for word in a.split(' ') if not(word in get_stopword())]
	bsent = [word for word in b.split(' ') if not(word in get_stopword())]
	sim = 0
	for x in xrange(1, (n+1)):
		sent1 = nword_set(asent, x)
		sent2 = nword_set(bsent, x)
		if sent1 == set() or sent2 == set():
			if sim > 1.0:
				return 1.0
			return sim
		try:
			sim += (len(sent1.intersection(sent2))*1.0)/(len(sent1.union(sent2))*1.0)*(1.0/x)
		except ZeroDivisionError:
			sim += 0
	if sim > 1.0:
		return 1.0
	return sim

def nword_set(sent, n):
	word = ""
	st = set()
	for x in range(len(sent)-(n-1)):
		for z in xrange(0, n):
			if word == "":
				word = word + sent[x+z]
			else:
				word = word + " " + sent[x+z]
		st.add(word)
		word = ""
	return st

if __name__ == '__main__':
	file = raw_input()
	fr = open(file)
	lines = fr.readlines()
	fr.close()
	
	file = raw_input()
	fw = open(file, 'w')
	
	n = int(raw_input())

	for line1 in lines:
		line2 = re.sub('\\(|\\)|:|;|,|\.|\\n|\\r|\'s|#', '', line1)
		line = re.sub('\-', ' ', line2)
		sentences = line.split('\t')
		sim = ngram_sim(sentences[0], sentences[1], n)
		fw.write(str(round(sim, 1))+'\n')
	fw.close()
