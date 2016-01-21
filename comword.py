## source ./usr/test/bin/activate
## coding: UTF-8

from gensim.models import word2vec
import re
import math
from lcs import *

model = word2vec.Word2Vec.load("example.model")

# 共通単語数(全文)
def get_com(a, b):
	return len(set(word for word in a.split(' ')).intersection(set(word for word in b.split(' ')))) 

# 共通単語数(StopWord)
# ジャッカード係数で類似度算出
def get_coms(a, b):
	sent1 = set(word for word in a.split(' ') if not word in get_stopword())
	sent2 = set(word for word in b.split(' ') if not word in get_stopword())
	return (len(sent1.intersection(sent2))*1.0)/(len(sent1.union(sent2))*1.0)
	
# 共通単語数(StopWord, w2v)
def get_comsw(a,b):
	sent1 = set(word for word in a.split(' ') if not(word in get_stopword()))
	sent2 = set(word for word in b.split(' ') if not(word in get_stopword()))
	cnt = 0
	for w1 in sent1:
		for w2 in sent2:
			try:
				similarity = round(model.similarity(w1, w2), 1)
			except KeyError:
				if w1 == w2:
					similarity = 1.0
				else:
					similarity = 0
			finally:
				if similarity >= 0.8:
					cnt += similarity
	return (cnt*1.0)/(len(sent1.union(sent2))*1.0)

# main文
if __name__ == '__main__':
	
	file = raw_input()

	fr = open(file)
	lines = fr.readlines()
	fr.close()

	file = raw_input()

	fw = open(file, 'w')
	for line1 in lines:
		line2 = re.sub('\\(|\\)|:|;|,|\.|\\n|\\r|\'s|#', '', line1)
		line = re.sub('\-', ' ', line2)
		sentences = line.split('\t')
		sim = get_comsw(sentences[0], sentences[1])
		similarity = round(sim, 1)
		fw.write(str(similarity))
		fw.write('\n')
	fw.close()
