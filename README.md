# Name
scraping-with-tor

アクセス過多によるサーバーから接続規制を回避する。

Avoid connection restrictions from the server due to excessive access.

# DEMO

用意する予定は今のところ無し。

No plans to prepare it at the moment.

# Features

とある1行のコメントアウトの切り替えでTorを使うか使わないか決める。

気晴らし程度だが、ヘッダーにランダムなユーザーエージェント。

ついでに ”navigator.webdriver=undefined” の設定も織り込み済み。

Decide whether you want to use Tor or not by switching the comment out of one line.

Just a distraction, but a random user agent in the header.

The "navigator.webdriver=undefined" setting is also factored in.

# Requirement

* Python 3.8.7 64-bit
* selenium 3.141.0
* fake-useragent 0.1.11
* webdriver-manager 3.5.2

# Installation

```bash
pip install fake-useragent
pip install webdriver_manager
```

# Usage

```bash
driver = Selenium(url)
print(driver.page_source)
```

# Note

tor.exe が必要。main.pyでは適当なパスを通しているので必要に応じて変更すること。

You will need tor.exe. main.py has an appropriate path, so change it if necessary.

# Author

* 作成者: kawagoe6884
* 所属: 
* E-mail: 

# Special thanks

このテンプレートの参照先URL

Reference URL for this template.

https://cpp-learning.com/readme/
