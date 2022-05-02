# coding:utf-8
import subprocess
import time
import getpass
import random

from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ------ Starting Tor ------
def Start_tor():
    global running
    ## kill
    subprocess.call(r'taskkill /F /T /IM tor.exe', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    ## run
    Tor = f'C:\\Users\\{getpass.getuser()}\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe'
    running = subprocess.Popen(Tor)
    time.sleep(1)


# ------ Starting selenium ------
def Start_selenium():
    ## kill
    subprocess.call(r'taskkill /F /T /IM chromedriver.exe', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    ## ------ ChromeDriver option ------
    options = Options()
    if 'running' in globals():
        ### Tor Proxy Settings
        options.add_argument('--proxy-server=socks5://localhost:9050')
        ### Define User-Agent
        UA = UserAgent().chrome
        options.add_argument('--user-agent=' + UA)
    options.add_argument('--blink-settings=imagesEnabled=false')                    # 画像の非表示
    options.add_argument('--disable-blink-features=AutomationControlled')           # navigator.webdriver=false とする設定
    options.add_argument('--disable-browser-side-navigation')                       # Timed out receiving message from renderer: の修正
    options.add_argument('--disable-dev-shm-usage')                                 # ディスクのメモリスペースを使う
    options.add_argument('--disable-extensions')                                    # すべての拡張機能を無効
    options.add_argument('--disable-gpu')                                           # GPUハードウェアアクセラレーションを無効
    # options.add_argument('--headless')                                            # ヘッドレスモードで起動
    options.add_argument('--ignore-certificate-errors')                             # SSL認証(この接続ではプライバシーが保護されません)を無効
    options.add_argument('--incognito')                                             # シークレットモードで起動
    options.add_argument('--no-sandbox')                                            # Chromeの保護機能を無効
    # options.add_argument('--start-maximized')                                     # 初期のウィンドウサイズを最大化
    options.add_argument('--window-size=1920,1080')                                 # 初期のウィンドウサイズを指定
    options.add_experimental_option("excludeSwitches", ['enable-automation'])       # Chromeは自動テスト ソフトウェア~~ を非表示
    prefs = {
        'profile.default_content_setting_values.notifications' : 2,                 # 通知ポップアップを無効
        'credentials_enable_service' : False,                                       # パスワード保存のポップアップを無効
        'profile.password_manager_enabled' : False,                                 # パスワード保存のポップアップを無効
        # 'download.default_directory' : download_dir                               # ダウンロード先のディレクトリを指定
    }
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option('useAutomationExtension', False)                # 拡張機能の自動更新を停止

    ## ------ Launch of ChromeDriver ------
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver


# ------ driver.get LOOP ------
def Selenium(url):
    global driver
    ## Webアクセスのリトライ回数を指定する
    retry_count = 5
    try:
        for count in range(retry_count + 1):
            count += 1
            ### リトライ回数の上限を超えた場合はエラーにする
            if count > retry_count:
                raise Exception('リトライ回数の上限を超えました')
            ### driver.get ⇒ 待機、エラーならtorとselenium起動
            try:
                driver.get(url)
            except:
                Start_tor() # Tor を使わないならコメントアウト
                driver = Start_selenium()
            else:
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located)
                sec = random.uniform(1.0, 3.0)
                time.sleep(sec)
                break
    except Exception as e:
        raise e
    return driver


# ------ TRY ------
url = 'https://www.hogehoge.jp'
driver = Selenium(url)
print(driver.current_url)
# >>> https://www.hogehoge.jp

