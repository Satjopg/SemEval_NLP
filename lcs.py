## coding: UTF-8

import re
import math

# a,b２つの文のLCS長を求める
def get_lcs(a, b):
#	stop = get_stopword()
	sent1 = a.split(' ')
	sent2 = b.split(' ')
	LCS = [[0 for i in range(len(sent2) + 1)] for j in range(len(sent1) + 1)] 
	for x in range(len(sent1)):
		for y in range(len(sent2)):
			if sent1[x] == sent2[y]:
				LCS[x+1][y+1] = max(LCS[x][y+1], LCS[x+1][y], LCS[x][y]+1)
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

# main文
if __name__ == '__main__':
    fr = open('test.txt')
    lines = fr.readlines() 
    fr.close()
    	
    fw = open('text.txt', 'w')
    for line1 in lines:
        line2 = re.sub('\\(|\\)|:|;|,|\.|\\n|\\r|\'s', '', line1)
        line = re.sub('\-', ' ', line2)
        sentences = line.split('\t')
        lcs = get_lcs(sentences[0].lower(), sentences[1].lower())
        sim = (lcs * 1.0) / (max(len(sentences[0].split(' ')), len(sentences[1].split(' '))*1.0))
        fw.write(str(round(sim,1))+"\n")
    fw.close()
