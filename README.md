## 宿題１

code: matrix.py

行列の計算部分には3重ループが必要になるので，正方行列の次数をNとすると，行列の計算量はO(N^3)となる。

Nと実行時間の関係のグラフは以下のようになっている。

<img src="HW1.png" width="400"/>

グラフからも行列の計算量がO(N^3)になっていることがわかる。

## 宿題２

ハッシュテーブルより木構造が好まれる理由として，以下の二つを考えました。

- ハッシュテーブルは大きな配列が必要になるため，使用するとメモリ消費が大きくなり，動作が重くなり逆に低速になってしまうから
- できるだけ衝突を避けるようなハッシュ関数を選ぶのが難しいから


## 宿題３

直近にアクセスされた上位X個のページを保存するデータ構造として，ハッシュテーブルと双方向連結リストを使った以下のようなものを考えた。<br/><br/>
ハッシュテーブルにはリストのノードを保存し，ノードにはページのデータ（<URL, Webページ>）をそれぞれ保存する。<br/>
- ページを訪れた時，そのページのハッシュ値に既にノードのデータがあり，そのノードがリストの中にあれば，リストの先頭に付け替える。
- ハッシュテーブルにデータがない，またはデータはあるがリストの中にない時，ノードを新しく作り先頭に加え，最後尾のものは捨てる。最後尾のノードが持つデータのハッシュ値を求め，ハッシュテーブルから最後尾のノードのデータを消す。

参考図
<img src="HW3.jpg" width="400"/>

## 宿題４

X個の<URL, Webページ>を保存する(今回はX=3とした)ため，宿題3で述べたようなデータ構造を実装しました。<br/>

しかし，実装してみると，連結リストの長さがX以下なのかどうかを数える必要があり，その工程でO(X)の実行時間がかかってしまいました。

また，仕組みが分かりやすいように，webページの名前とurlを入力すると連結リストの中身を出力するようにしました。結果は以下のようになりました。

<img src="HW4.png"/>