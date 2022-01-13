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


# ------ Tor の起動 ------
def Start_tor():
    try:
        # kill
        subprocess.call(r'taskkill /F /T /IM tor.exe', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1)
        # run
        Tor = f'C:\\Users\\{getpass.getuser()}\\Desktop\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe'
        subprocess.Popen(Tor)
        time.sleep(1)
    except:
        pass


# ------ Selenium の起動 ------
def Start_selenium():
    # kill
    subprocess.call(r'taskkill /F /T /IM chromedriver.exe', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    # User-Agentを定義する
    UA = UserAgent().chrome
    # chrome-option
    options = Options()
    # options.add_argument('--proxy-server=socks5://localhost:9050')  # Tor 使わないならコメントアウト
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--user-agent=' + UA)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--headless')
    prefs = {'profile.default_content_setting_values.notifications' : 2}
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])  # navigator.webdriver=undefined とする設定
    # run
    driver = webdriver.Chrome(ChromeDriverManager(log_level=0, print_first_line=False).install(), options=options)
    # set
    driver.implicitly_wait(60)
    driver.set_window_size('1920', '1080')
    return driver


# ------ driver.getのループ ------
def Selenium(url):
    global driver
    # Webアクセスのリトライ回数を指定する
    retry_count = 5
    try:
        for count in range(retry_count + 1):
            count += 1
            # リトライ回数の上限を超えた場合はエラーにする
            if count > retry_count:
                raise Exception('リトライ回数の上限を超えました')
            # driver.get ⇒ 待機、エラーならtorとselenium起動
            try:
                driver.get(url)
            except:
                Start_tor()
                driver = Start_selenium()
            else:
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located)
                sec = random.uniform(1.0, 3.0)
                time.sleep(sec)
                break
    except Exception as e:
        raise e
    return driver

