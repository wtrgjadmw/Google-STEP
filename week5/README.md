tsp_exact.pyは厳密解を，tsp_approximate.pyは近似解を求めるコードである。計算量の問題から，tsp_exact.pyはinput_3.csv（N＝64）以降は使えない （後で詳しく述べる）。

## 共通の関数

## read_input_file

input_{x}.csvファイルを読み込み，座標をcitiesという配列に入れる。

## write_output_file

output_{x}.csvファイルにノードを訪れる順番を書き込む。

## distance

2つのノード間の距離を求める。

## distance_matrix

```python
dist[i][j] = ノードiとノードjの間の距離
```
となるような配列を作る。

---

# tsp_exact.py
ノードを訪れた順番も実装したいのですが，まだ未完成です。

## dfs

動的計画法を用いる。
```python
dp[S][city_now] = 部分集合Sに含まれるノードにすでに訪問済みであり，今city_nowにいる時，一周してノード0に戻るのに必要な残りの最短距離
```
この時，部分集合Sはbitで表す。n番目のbitが1ならこの部分集合はノードnを含むと考える。

例）
<img src="Google Step-9.jpg">

Sのn番目のbitが0ならノードnは未訪問なので，部分集合S2(:= S + {city_now})とすると，
```python
dp[S][city_now] = dp[S2][city_next] + (city_nowとcity_nextの距離)
```
となる。これを再帰で求める。計算量はO(N^2 * 2^N)となるので，N=64の時は膨大な時間量になってしまう。

## solve

```python
dp[0][0] = ループの最短距離
```
となるので，これを求める。

# tsp_approximate.py

## loop_distance

入力したvisitation_orderの順にノードを訪れた時の距離の総和を求める。

## initialize_visitation_order

visitation_orderを初期化する。
ノード0からスタートし，残ってるノードの中で最も近いノードに移動するのを繰り返す。

## exchange_two_node

2つのノードの順番を交換した方が距離の総和が短くなる（つまり交差している）なら交換を行う。

## solve

全てのノードの組み合わせをみていき，交差していればノードを交換する，というのを100回繰り返す。すると，交差はほとんどなくなり，できるだけ短い距離が求められる。