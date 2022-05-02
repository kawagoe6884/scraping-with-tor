# Jpn
### これは何？
url = 'https://www.hogehoge.jp'
<br>上記の変数"url"にアクセスしたい

1. 関数Start_torを使ってグローバルIPを変更する
1. 変数"url"にアクセスする
1. 何回かアクセスする
1. IPアドレス制限を受けてアクセス不可になった
1. 最初に戻る

というごく一部の層に需要がありそうで無さそうな処理

<br>



### Tor の準備
1. https://www.torproject.org/download/tor/ から"Windows Expert Bundle"をダウンロードする
1. デスクトップに解凍する(任意のディレクトリでも可)
1. 解凍したフォルダを開いて、"tor.exe"までのフルパスをコピー
1. 22行目の変数"Tor"にフルパスを入れる



### UserAgent の準備
1. https://pypi.org/project/fake-useragent-ex/ から"fake-useragent-ex 0.1.12"をインストールする
1. import fake_useragent<br>print(fake_useragent.VERSION)<br>で"0.1.12"が出力されればok

<br>



# Eng
### What's this
url = 'https://www.hogehoge.jp'
<br>I want to access the "url" variable above.


1. Change global IP using function Start_tor.
1. Access the variable "url".
1. Access the variable "url" several times.
1. Access is disabled due to IP address restriction.
1. Back to the beginning.

The process is likely to be in demand by a small segment of the population called.

<br>



### Prepare for Tor
1. Download the "Windows Expert Bundle" from https://www.torproject.org/download/tor/
1. Unzip the file to your desktop (or any directory).
1. Open the extracted folder and copy the full path to "tor.exe"
1. Put the full path in the variable "Tor" on line 22.



### Prepare for UserAgent
1. Install "fake-useragent-ex 0.1.12" from https://pypi.org/project/fake-useragent-ex/
1. import fake_useragent<br>print(fake_useragent.VERSION)<br>If "0.1.12" is output, OK.

