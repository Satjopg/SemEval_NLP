## source ./usr/test/bin/activate
## coding: UTF-8

import re
from lcs import *

# 共通単語数(StopWord)
# ジャッカード係数で類似度算出
def get_coms(a, b):
	sent1 = set(word for word in a.split(' ') if not word in get_stopword())
	sent2 = set(word for word in b.split(' ') if not word in get_stopword())
	return (len(sent1.intersection(sent2))*1.0)/(len(sent1.union(sent2))*1.0)
	
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
		sim = get_coms(sentences[0], sentences[1])
		fw.write(str(round(sim, 1))+'\n')
	fw.close()
