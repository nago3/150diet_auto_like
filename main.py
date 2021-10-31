# Selenium の初期設定
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 待機処理用
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

# 要素の指定
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# アクション時の設定
from selenium.webdriver.common.action_chains import ActionChains
import random

# 内部で作成したファイルのimport
import config
import tagList

"""
# ヘッドレスモードで動かす場合
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
"""

# ドライバーのインストール
driver = webdriver.Chrome(ChromeDriverManager().install())

# instagram にログイン
driver.get(config.URL)

# ログイン時に取得する要素
## 電話、メールまたはユーザー名のinput要素が読み込まれるまで待機（最大10秒）
elem_user_id_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username")))
## パスワードのinput要素
elem_password_input = driver.find_element(By.NAME, "password")

# ログイン処理
if elem_user_id_input and elem_password_input :
    elem_user_id_input.send_keys(config.USERNAME)
    sleep(1)
    elem_password_input.send_keys(config.PASSWORD)
    sleep(1)

    ## button要素がクリックできるようになるまで待機（最大15秒）
    elem_login_btn = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
    # ボタン押下のアクション
    actions = ActionChains(driver)
    actions.move_to_element(elem_login_btn)
    actions.click(elem_login_btn)
    actions.perform()

    # ログイン処理待機
    sleep(5)

# タブの検索
"""
別ファイルの配列から、ランダムにタグ文字列を拾ってくる
"""
searchedTag = random.choice(tagList.mainTags)
driver.get(config.URL + "explore/tags/" + searchedTag)

# タブ検索時に取得する要素
## 投稿画像が読み込まれるまで待機（最大15秒）
elem_images = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CLASS_NAME, '_9AhH0')))

sleep(2)

# 画面描画を待つ処理の実装
if elem_images :
    sleep(2)
    # 最新の投稿に移動する
    likeTarget = driver.find_elements(By.CLASS_NAME, '_9AhH0')[10]
    actions = ActionChains(driver)
    actions.move_to_element(likeTarget)
    actions.click(likeTarget)
    actions.perform()
    sleep(3)

    # いいねを実行
    driver.find_element(By.CLASS_NAME, 'fr66n').click()
