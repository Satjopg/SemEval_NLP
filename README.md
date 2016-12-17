# SemEval_NLP
## 自然言語処理の中でも英語の文間類似度を測定するためのプログラム

各プログラムの概要は
* 文間の共通単語数から類似度を測定：comword.py
* 最長共通部分列(LCS)の長さから類似度を測定：lcs.py
* n-gramを用いて類似度を測定：ngram.py

である。

また、プログラムでストップワード(:英文内で全体の意味に関係が浅い単語)  
は調べない処理をしている。この一覧はstopWord.txtに載っている。

### comword.py
２文間の共通単語数を測定し、jaccard係数を利用して文間類似度を算出している。

類似度の式は  
*(共通単語数)/(２文の総単語数)*  
となる。  
＊ただし、総単語数に重複単語の数は含まない。

類似度の算出は以下のget_comsにて行われている。
```python
def get_coms(a, b):
	sent1 = set(word for word in a.split(' ') if not word in get_stopword())
	sent2 = set(word for word in b.split(' ') if not word in get_stopword())
	return (len(sent1.intersection(sent2))*1.0)/(len(sent1.union(sent2))*1.0)
```
入力は比較する２文、返り値はjaccard係数を用いた類似度である。

#### --実行結果(精度)
```
Pearson: 0.70017
```

精度はピアソン相関で算出し1に近いほど精度は良いということになる。

この結果は当時のSemEvalで上から15番目くらいの精度である。

### lcs.py
2文間の最長共通部分列（LCS）の長さ(以下LCS長)を求めることで類似度を求めている。

類似度算出の式は
*(LCS長)/(長い方の文の単語数)*  
である。

プログラムでは、以下のget_lcsでLCS長を求めている。
```python
def get_lcs(a, b):
	sent1 = a.split(' ')
	sent2 = b.split(' ')

	LCS = [[0 for i in range(len(sent2) + 1)] for j in range(len(sent1) + 1)]

	LCS = [[0 for i in range(len(sent2) + 1)] for j in range(len(sent1) + 1)] 

	for x in range(len(sent1)):
		for y in range(len(sent2)):
			if sent1[x] == sent2[y]:
				LCS[x+1][y+1] = max(LCS[x][y+1], LCS[x+1][y], LCS[x][y]+1)
			else:
				LCS[x+1][y+1] = max(LCS[x][y+1], LCS[x+1][y], LCS[x][y])
	return LCS[len(sent1)][len(sent2)]

```
LCS長は動的計画法で求めている。入力は比較する２文、出力は２文のLCS長である。

#### --実行結果(精度)
```
Pearson: 0.40424
```
使用したデータは共通単語数と同様のもの。  
共通単語数のが精度が良い。  
<<<<<<< HEAD
ただし、word2vecなどを組み込んだりすることで精度の向上が見込める。

### ngram.py
n-gramを用いて, 語の並びを考慮して文間類似度の測定を行う。

このプログラムでは, モノグラム, バイグラム, トリグラム, などを  
単体で使用するのではなく,
n-gramごとの類似度の平均を, 文間類似度として採用している。

ただし, 平均で求めてしまうと全て同じ重みとなってしまうのでそれぞれにペナルティを与えることで調整している。

#### --実行結果(精度)
```
Pearson: 0.50153
```
実験環境は同じである。  
結果的には共通単語をjaccard係数で類似度を求めたものが精度が良い。  
しかし, ペナルティの取り方などの調整次第で精度向上が見込まれる。

