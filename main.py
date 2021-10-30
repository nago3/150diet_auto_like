import config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""
# ヘッドレスモードで動かす場合
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
"""

# ドライバーのインストール
driver = webdriver.Chrome(ChromeDriverManager().install())

# instagram にアクセス
driver.get(config.URL)

