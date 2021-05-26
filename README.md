## 宿題1

eval_partという関数を追加した。

### eval_partの仕様
以下の1〜3を行うことで**tokens: 1 + 2*3 + 4/2** を **new_tokens: 1 + 6 + 2** に変換する。

1. 空の配列new_tokens，変数index・tmpを用意する。<br/>
eval_part内のindexは，式の中の符号の位置を表す。上の例では，最初の符号は1+...の+なので，index=1
(もし式が-から始まっていたら(ex. -1 + 2*3)，index=2)から始まる。その後， tokensの中身を見ていくと2つおきに符号が来るはずなので，ループするごとにindexに2を足していく。<br/>
また，変数tmpで式の中のかけ算・わり算の結果を保持する。<br/>

2. tokensの中身を見ていく。<br/>
  - tokens[index]が+または-ならtmpとtoken[index]をnew_tokensに追加する。
  - tokens[index]が*または/ならtmpにかけ算・割り算を行う。
  - index += 2

3. 2を繰り返してtokensを最後まで参照したら，最後に保持しているtmpをnew_tokensに追加する。

具体例 (1 + 2*3 + 4/2) を使って流れを見ていく。(青字が更新部分)
***
index = 1, tmp = 1 <font color="Blue">-> 2</font><br/>
tokens: 1 <font color="Blue">+</font> 2 * 3 + 4 / 2<br/>
new_tokens: <font color="Blue">1 +</font>

***
index = 3, tmp = 2 <font color="Blue">-> 6 (2 * 3)</font><br/>
tokens: 1 + 2 <font color="Blue">*</font> 3 + 4 / 2<br/>
new_tokens: 1 +

***
index = 5, tmp = 6<font color="Blue">-> 4</font><br/>
tokens: 1 + 2 * 3 <font color="Blue">+</font> 4 / 2<br/>
new_tokens: 1 + <font color="Blue">6 +</font>

***
index = 7, tmp = 4 <font color="Blue">-> 2 ( 4 / 2)</font><br/>
tokens: 1 + 2 * 3 + 4 <font color="Blue">/</font> 2<br/>
new_tokens: 1 + 6 + 

***
ループ脱出<br/>
new_tokens: 1 + 6 + <font color="Blue">2</font>


## 宿題2


## 宿題3

