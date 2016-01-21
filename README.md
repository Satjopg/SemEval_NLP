# SemEval_NLP
## 自然言語処理の中でも英語の文間類似度を測定するためのプログラム

各プログラムの概要は
* 文間の共通単語数から類似度を測定：comword.py
* 最長共通部分列(LCS)の長さから類似度を測定：lcs.py
* n-gramを用いて類似度を測定：ngram.py

である。

また、プログラムでストップワード（：英文内で全体の意味に関係が浅い単語）

は調べない処理をしている。これはstopword.txtに載っている。

## comword.py
２文間の共通単語数を測定し、jaccard係数を利用して文間類似度を算出している。

類似度の算出はget_comsにて行われている。
```python
def get_coms(a, b):
	sent1 = set(word for word in a.split(' ') if not word in get_stopword())
	sent2 = set(word for word in b.split(' ') if not word in get_stopword())
	return (len(sent1.intersection(sent2))*1.0)/(len(sent1.union(sent2))*1.0)
```


