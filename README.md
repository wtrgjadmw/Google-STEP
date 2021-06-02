# 必須課題
wikipedia_sample.pyに記載
## 仕様
```shell
python3 wikipedia_sample.py <探したいページ名>
```
で実行すると，Googleから探したいページまでの経路を返します。<br/>
存在しないページ名を入れると，
```shell
The graph doesn't have the route
```
と出力されます。
<br/><br/>
具体例）Googleと渋谷の経路を探す場合は，
```shell
python3 wikipedia_sample.py Google 渋谷
```
で実行すると，
```shell
['Google', 'セグウェイ', '渋谷']
```
と出力されます。

## コードの説明
### read_pages(), read_links()
Yukiさんが作成してくださったコードそのままです。それぞれpages, linksを返します。

### bfs_route_search(pages, links, arrived_time, prev_spot, start_word, goal_word)
- index_start: スタートのid<br/>
- index_goal: ゴールのid<br/>
- arrived_time: スタートからそのページへの距離を保存する配列
- prev_spot: スタートからそのページへ行く時，その地点の一個前に訪れるページのidを保存する配列。
  例えばGoogle-渋谷の例で言うと，```prev_spot[渋谷のid]=セグウェイのid```です。

上記の変数を用いて，bfsでキューが空になるまでループをし，arrived_time, prev_spot, index_goalを返します。

### print_route(max_page_id, pages, links, start_word, goal_word)
prev_spotから逆算し，スタートからゴールまでの経路を出力します。

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
と出力されるはずです。

## コードの説明
### read_pages(), read_links()
wikipedia_sample.pyと同じです。

### page_ranking(pages, links, page_rank)

### print_highrank(pages, links, max_page_id))
最もページランクの高いページ名とそのスコアを出力します。