## source ./usr/test/bin/activate
## coding: UTF-8

from gensim.models import word2vec
import re
import math

model = word2vec.Word2Vec.load("example.model")

# a,b２つの文のLCS長を求める
def get_lcs(a, b):
	stop = get_stopword()
	cnt = 0
	sent1 = a.split(' ')
	sent2 = b.split(' ')
	LCS = [[0 for i in range(len(sent2) + 1)] for j in range(len(sent1) + 1)] 
	for x in range(len(sent1)):
		if sent1[x] in stop:
			continue;
		for y in range(len(sent2)):
			if sent2[y] in stop:
				continue;
			try:
				similarity = round(model.similarity(sent1[x], sent2[y]), 1)
			except KeyError:
				if sent1[x] == sent2[y]:
					similarity = 1.0
				else:
					similarity = 0
			finally:
				if similarity >= 0.7:
					LCS[x+1][y+1] = max(LCS[x][y+1], LCS[x+1][y], LCS[x][y]+similarity)
				else:
					LCS[x+1][y+1] = max(LCS[x][y+1], LCS[x+1][y], LCS[x][y])
	return LCS[len(sent1)][len(sent2)]

def get_stopword():
	fs = open('stopWord.txt')
	lines = fs.readlines()
	fs.close()
	stop = set()
	for line in lines:
		word = re.sub('\\n|\\r','',line)
		stop.add(word)
	return stop

def get_len(sentence):
	stop = get_stopword()
	count = 0
	for word in sentence:
		if word in stop:
			continue;
		count += 1
	return count

# main文
if __name__ == '__main__':
    fr = open('test.txt')
    lines = fr.readlines() 
    # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    fr.close()
    # lines: リスト。要素は1行の文字列データ
    	
    # 書き込み用
    fw = open('text.txt', 'w')
    
    for line1 in lines:
        line2 = re.sub('\\(|\\)|:|;|,|\.|\\n|\\r|\'s', '', line1)
        line = re.sub('\-', ' ', line2)
        sentences = line.split('\t')
        lcs = get_lcs(sentences[0].lower(), sentences[1].lower())
        simori = (lcs * 2.0) / (min(len(sentences[0].split(' ')), len(sentences[1].split(' '))*1.0))
        #simori = (lcs * 2.0) / (max(get_len(sentences[0].split(' ')), get_len(sentences[1].split(' '))*1.0))
        sim = round(simori, 1)
        fw.write(str(sim))
        fw.write("\n")
    fw.close()
