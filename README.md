# markov
マルコフ連鎖するライブラリ

# インストール
pip install git+https://github.com/ctare/markov

# 使い方
```python
from markov import markov

text = """
今日 は いい 天気 でした 。
今日 は 雨降り でした 。
明日 は 雨降り のようだ 。
明後日 は 曇り のようだ 。
""".split()

rule = markov.rule(text)

# 生成されたルールを用いて、ランダムに文章を作成する
print(markov.create_sentence(rule))

# 文頭を決めて文章を作成する
seed = ["今日", "は"]
print(markov.create_sentence(rule, seed=seed))

# 終了条件まで辿りつけない構文が生成された場合、ValueErrorを出す
```
