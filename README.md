# SemEval_NLP
## 自然言語処理の中でも英語の文間類似度を測定するためのプログラム

各プログラムの概要は
* 文間の共通単語数から類似度を測定：comword.py
* 最長共通部分列(LCS)の長さから類似度を測定：lcs.py
* n-gramを用いて類似度を測定：ngram.py

である。

また、プログラムでストップワード（：英文内で全体の意味に関係が浅い単語）

は調べない処理をしている。この一覧はstopWord.txtに載っている。

### comword.py
２文間の共通単語数を測定し、jaccard係数を利用して文間類似度を算出している。

jaccard係数は今回の場合　(共通単語数)/(２文の総単語数)　となる。

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

使用したデータはSemEvalで配布されている過去のテストデータ。

このデータには比較文が750組記述されており、それぞれの文の類似度を測定する。

そして、実行結果とSemEvalが決めたgs(答え)とのピアソン相関を取ることで精度を出す。

ピアソン相関は-1~1で表され、1に近いほど精度は良いということになる。

この結果は当時のSemEvalで上から15番目くらいの精度である。


