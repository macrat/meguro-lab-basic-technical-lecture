# 第一回 プロトタイピングを支える技術 資料まとめ

この資料は主に[スライド](slide.pdf)の補足として、あるいは後々見直すことを想定したものです。ノートの代わりにどうぞ。

## プロトタイピングとは
試しに作ってみること。
作ってみたものは **プロトタイプ** 。

ビジネスモデルで卒業するならほぼ確実に作ることになる。

プロトタイピングでの鉄則は **手を抜く** こと。
あくまで試しでしかないので、手を抜けるところはなるべく手を抜いて、重要なところにだけ注力すべき。

## サービス提供の選択肢
1. Webサイト

	よくあるWebサイト。gmail的な高機能なやつも含む。

	一番手っ取り早く作れるけれど、出来ることは限定される。

	PCやスマホのようなデバイスや、AndroidやiOSのようなOSをほとんど気にせず作れるのが最大の強み。

2. アプリ

	PC向けのソフトを含む。インストールして使うやつ全般。

	Webサイトよりちょっと面倒臭いけれど、割と何でも出来る。

	デバイスやOSに合わせて作らないといけないが、その分だけ環境に合わせた最適なものを作れるのが強み。

3. PWA

	Webの手軽さで、アプリのような機能を使える。

	Webサイトを作って、それをPWAに変換するようなイメージで実装すると良いかも。

	PWAという名前のツールとかではなく、色んなものの集合体。
	なので、新しく勉強するのはちょっと面倒かもしれない。

4. ハードウェア

	電子工作というやつ。別に日曜大工を含めても良いけど。

	想像しうる限りありとあらゆるものを作ることが出来るが、想像しうる限りありとあらゆる知識が必要になってつらい。

	デバイス？ OS？ 最適なのを自分で作れば良いじゃない。

## Webサイトの仕組みと関連技術

### クライアント
ブラウザのことをクライアントと言う。ついでにブラウザで動くものもクライアントと言ったりする。
クライアントサイドとかも言う。細かい事を気にしてはいけない。

#### HTML
サイトのコンテンツを書くときに使うやつ。多分皆さんご存知なのでは。なので詳細は端折ります。

[HTMLクイックリファレンス](http://www.htmq.com/)というサイトがかなり詳細に網羅しているのでオススメ。

#### CSS
サイトのデザインを定義するために使うやつ。ほぼHTMLとセットなので、皆さんご存知なはず。なのでやっぱり端折ります。

これについても[HTMLクイックリファレンス](http://www.htmq.com/)がかなり便利。

#### Javascript
サイトを動かすときに使うもの。雰囲気としてはCSSっぽい感じでHTMLから読み込んだりHTMLに埋め込んだりして使う。

以下の例はボタンをクリックしたら **hello world!** という表示を出すやつ。
```
window.body.onLoad = function() {
	var button = document.querySelector('#button');
	button.addEventListener('click', function() {
	    alert('hello world!');
	});
}
```

##### JQuery
JavascriptでWebサイトを動かすのを楽にしてくれるやつ。Javascriptのライブラリ。

以下の例は上記の例をJQueryで書き直したもの。ちょっと短かくなっている。
```
$(function(){
	var button = $('#button');
	button.click(function() {
		alert('hello world!');
	});
});
```

[公式サイト](https://jquery.com/)からダウンロードして使う。
せむーさんの[日本語リファレンス](http://semooh.jp/jquery/)が色々充実してておすすめ。

#### SPA: Single Page Application
Javascriptだけでサイトを全て完結させるイケイケな技術。

SPAという何かがあるわけではなく、諸々の関連技術を含めた総称。

あまりにもイケイケなので、腕に自信がある人か、ものすごいやる気のある人向け。

[React](https://reactjs.org/)とか[vue.js](https://jp.vuejs.org/index.html)とか[AngularJS](https://angularjs.org/)とか。

### Webアプリケーションサーバー
動的なWebサイトを動かすためのもの。変化の無いHTMLを配信するだけなら要らない。

#### Python / Flask
[Python](http://www.python.jp/)という言語と、[Flask](http://flask.pocoo.org/)というライブラリの組み合わせ。

かなり手軽に書ける。が、複雑なサイトになってくるとややこしくなってくる。
ページ数の少ないシンプルなサイトにおすすめ。

目安としては、10ページくらいが何も考えずに作れる限界な気がする。
それ以上になると色々考えて整理しなきゃいけなくなる。
といっても整理すれば綺麗に書けるので、挑戦しても良いかも。

#### Python / Django
[Python](http://www.python.jp/)という言語と、[Django](https://docs.djangoproject.com/ja/)というライブラリの組み合わせ。

複雑なアプリケーションもわりと手軽に作れる。
最初はちょっと面倒臭いかもしれない。
ページ数が多かったり、複雑な機能が必要になるサイトにおすすめ。

ページ数が多い場合に管理が楽というだけではなく、管理者向けのページを簡単に実装出来たり、データベースを手軽に扱えたり色々出来る。
ただ、多機能な分だけ複雑なので注意。

#### Ruby / Ruby on Rails
[Ruby](https://www.ruby-lang.org/ja/)という言語と、[Ruby on Rails](http://rubyonrails.org/)というライブラリの組み合わせ。

言えば言わずと知れたWebアプリケーション作るやつ。
Webアプリと言えばこれ（だった）。

使ったことがないのでよく分からない。さくさく作れて幸せらしい。
よく分からないので詳細は書きませんが、高度なこと(API開発とか？)をするときに強いらしいです？

#### Javascript / Node.js
我等がJavascriptと[Node.js](https://nodejs.org/ja/)という実行環境の組み合わせ。これだけライブラリではない。

クライアントもサーバーもJavascriptだけで書けるから学習コストが低いかと思われがちだけれど、そもそもJavascriptの学習コストがとても高いので総じてつらい。
とはいえWeb特化な言語なだけあって、使いこなすとかなり良い感じ。

クライアントとリアルタイムで通信したい場合、おそらくNode.jsで[socket.io](https://socket.io/)というものを使って通信することになると思われる。
[チャット](https://qiita.com/hosomichi/items/66b309a6c3c20d910218)とか、そんなものを作りたいときに。

### サーバー / クラウドサービス

Webアプリケーションサーバーの実行環境。動かないHTMLを扱う場合でも、ファイルの配信にはクラウドサービスを使っておくと手っ取り早くて楽。

[Google Cloud Platform](https://cloud.google.com/)か[AWS(Amazon Web Service)](https://aws.amazon.com/jp/)が選択肢になるかと思われる。
とりあえず動かすだけなら[heroku](https://www.heroku.com/)というのもおすすめ。

クラウドサービスで実行するために開発する場合、自分でサーバーを立てるときと若干開発の仕方が変わったりするので、可能であれば最初からクラウドサービス上で開発しておいた方が良い。

## アプリ
いわゆるスマホアプリ。だけでなく、デスクトップアプリも含む。

### Andoid
世界的に普及率が高いけど、日本だとなぜかイマイチ。

開発も公開も楽なのでとてもおすすめ。

[公式リファレンス](https://developer.android.com/reference/index.html)がかなり充実しているのでおすすめ。
Java向けだけど、Kotlinでもほぼ同じ使い方が出来ます。

#### Java
みんなだいすきなJava。

以下は画面上のボタンをクリックすると **hello world!** という表示が出るサンプル。
```
class Application extends Activity {
	@Override
	public void onCreate(Bundle savedInstanceState) {
		findViewById(R.id.button).setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View view) {
				((TextView)findViewById(R.id.message)).setText("hello world!");
			}
		});
	}
}
```

#### Kotlin
最近出て来たモダンなやつ。

すごく簡単に書けて幸せ。と思いきや、結局Javaの知識も必要になったりする。

JavaからKotlinに変換するツールもあるので、JavaでのAndroid開発に慣れてから始めても遅くはない。

以下は先ほどのJavaでのサンプルをKotlinで書き直したもの。
```
class Application: Activity {
	override fun onCreate(savedInstanceState: Bundle) {
		button.setOnClickListener {
			message.text = "hello world!";
		}
	}
}
```

### iOS
日本での普及率がすごいやつ。外国人向けには向いてない気がしないでもない。

開発から公開までが凄くしんどい。おすすめできない。

#### Objective-C
やばいやばいと噂のやばい言語。
幸せにはなれない。

以下は画面に **Hello World!** と表示するサンプル。
書いたことが無いのでググって出てきたものを流用しました。
```
@interface ViewController ()
@end

@implementation ViewController
- (void)viewDidLoad {
  [super viewDidLoad];
  UILabel *label = [[UILabel alloc] init];
  label.text = @"Hello World!";
  [label sizeToFit];
  label.center = self.view.center;
  [self.view addSubview:label];
}
- (void)didReceiveMemoryWarning {
  [super didReceiveMemoryWarning];
}
@end
```

#### Swift
比較的新しめの言語。Objective-Cをゆるやかに置き換えつつあるらしい。

簡単なことはすごく簡単に書ける。簡単じゃないことは結局Objective-Cを書くことになる。
立ち位置としてはKotlinに非常に似ている。

以下は **Hello World!** と表示するサンプル。これもググって出てきたものの流用。
```
class ViewController: UIViewController {
  override func viewDidLoad() {
    super.viewDidLoad()

    let label = UILabel(frame: CGRect(x: 100, y: 100, width: 200, height: 50))
    label.text = "Hello World!"
    self.view.addSubview(label)
  }

  override func didReceiveMemoryWarning() {
    super.didReceiveMemoryWarning()
  }
}
```

### Android / iOS 両対応
両方対応する場合。

大抵の場合、個別に開発するより手間が減る。
ただし、ハードウェアの機能に依存したアプリを開発しようとするとむしろ手間が増えることもあるので要注意。

#### Xamarin
C#という言語で使う[Xamarin](https://www.xamarin.com/)というフレームワーク。

簡単なアプリを作る上ではかなり手軽なのでおすすめ。

#### Unity
ゲームを作るやつ。
言語はC#かJavascriptのどちらか。

3Dゲームのために作られているものの、2Dでも開発出来る。
一応普通にゲームじゃないアプリを作ることも出来る。

[チュートリアル](https://unity3d.com/jp/learn/tutorials)がそこそこ充実している。ゲームを作れるようにしかならないかもしれないけれど。

### PC
発表では端折ったPC向けのアプリ開発について。

日本では普及率が徐々に下がりつつあるとか。

#### UWP: Universal Windows Platform
Windows向けのアプリをサクサクっと開発出来るもの。
[Visual Studio](https://www.microsoft.com/ja-jp/dev/default.aspx)上でマウスを使ってぽちぽちデザインして、C#という言語で動きを定義する。

詳しく知らないので詳細は書きませんが、かなり楽らしい。

作ったアプリはそのままWindowsストアで配信出来る。

#### Electron
Javascript（Node.js）でPC向けのアプリを作るやつ。
ほぼほぼWeb開発と同じノリでローカル向けに開発出来る。

慣れればさくさく開発出来るが、慣れないと色々大変。全体的にNode.jsと共通な感じ。

実行効率があまり良くないので、高負荷なアプリには微妙かもしれない。

#### Qt / Gtk
C言語で開発する[Gtk](https://www.gtk.org/)、C++で開発する[Qt](https://www.qt.io/)ほか、色々。
Windows / mac / Linux ほか色々対応出来るものの、色々苦労が絶えない。おすすめしない。

#### Xamarin
なんとXamarinはPC向けにも対応出来る。
詳細はクロスプラットフォームの項を参照。

### PWA: Progressive Web Application
上手くいけばかなり良いものが出来る。
でも最初からやろうとすると多分すごくつらい。

とりあえずWebサイトとして実装してみるときっと幸せ。

### ハードウェア

#### 計測機器
**アイトラッキング**とか研究室で時々話題に出る。
[Kinect](https://developer.microsoft.com/ja-jp/windows/kinect)で姿勢を取ったりも。

どちらも自前でプログラムを書こうとするとかなり大変。

何をしたいかによって選択肢が無数にあるので、個別に聞いてください。

#### 電子工作
[Arduino](https://www.arduino.cc/)とか使えばそこそこ幸せ。C言語。
性能が足りなければ[mbed](https://os.mbed.com/)とか。C++。
それでも足りなければ**RX**とかになりそうだけど、それはもう工学部に行くべき。

確実に泥沼に入るので、やめておくべき。

## 何で開発するか
- Q1. 普通のスマホ or PC以外で動く？

	eg. 特殊なセンサーが必要、専用の筐体が必要、etc...

	-> YESならハードウェア。さようなら。

- Q2. 常に起動してなきゃいけない？

	eg. スマホのGPSを追跡する、フィットネスデータの記録、etc...

	-> YESならアプリ。多分Android特化が良い。

- Q3. 沢山リソースを使う？

	eg. 大量の画像を使うゲーム、重い計算をするツール、etc...

	-> YESならアプリ。Xamarinでも良いかも。

- Q4. 頻繁に使うもの？

	eg. よく使うツール、毎日やるゲーム、隙あらば見るSNS、etc...

	-> YESならWebアプリ。PWAに出来ると幸せ。

- Q5. 全部NOだった？

	eg. 観光や不動産ほかの情報提供、ショッピング、etc...

	-> YESならWebサイト。
