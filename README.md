# 必須課題
wikipedia_sample.pyに記載
## 仕様
```shell
python3 wikipedia_sample.py <探したいページ名>
```
で実行すると，Googleから探したいページまでの経路を返します。<br/>
存在しないページ名を入れると，
```shell
The graph doesn't have the word
```
を返します。
<br/><br/>
具体例）Googleと渋谷の経路を探す場合は，
```shell
python3 wikipedia_sample.py 渋谷
```
で実行すると，
```shell
['Google', 'セグウェイ', '渋谷']
```
が返ります。

# 発展課題

ページランクを実装しました。（page_rank.pyに記載）
## 仕様
```shell
python3 page_rank.py
```
で実行すると，最もページランクの高いページ名とそのスコアが返されます。
```shell
日本 751625.391684508
```
が返されるはずです。