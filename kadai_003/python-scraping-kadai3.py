#ライブラリー
from selenium import webdriver #ブラウザ操作
from selenium.webdriver.common.by import By #HTML要素取得
from selenium.webdriver.support.ui import WebDriverWait #待機処理
from selenium.webdriver.support import expected_conditions as EC #待機処理
from getpass import getpass #パスワード用
import time


#動きを確認したかったので、ヘッドレスモードいれていません

#Chrom起動
chrome_driver=webdriver.Chrome()

#アクセス
chrome_driver.get('https://terakoya.sejuku.net/register')

#ログインボタンが表示されるまで待つ
wait=WebDriverWait(chrome_driver,30)
header_login_botton=wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,'#root>header>div')
    )
)

#ログインボタンクリック
header_login_botton.click()

#入力フォーム
email_address = input('メールアドレスを入力してください: ')
password = getpass('パスワードを入力してください: ')

#ログイン入力箇所を取得
parnet_element=chrome_driver.find_element(By.CSS_SELECTOR,'div.sc-pyfCe.cZfPwB')
email_input=parnet_element.find_element(By.NAME,'email')
password_input=parnet_element.find_element(By.NAME,'password')

#id/pass入力
email_input.send_keys(email_address)
password_input.send_keys(password)

#ログインボタンの場所を取得
form_login_button=wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,'#root>div.sc-pyfCe.cZfPwB>div.sc-kDvujY.eCJBhf>div.sc-eDWCr.dePrRH>button')
    )
)

#ログインクリック
form_login_button.click()

#Top画面が表示されるまで待つ
wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,'nav>img')
    )
)

#紹介ページへ移動
chrome_driver.get('https://terakoya.sejuku.net/account/profile')

#編集ボタンが表示されるまで待つ
hensyu_buttom=wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,'button.sc-eDvSVe.cnuKRu')
    )
)

#編集クリック
hensyu_buttom.click()

#自己紹介文
my_data = 'プログラミング学習中です！今はスクレイピングに挑戦しています！'
#入力欄CSSセレクタ取得
my_data_input=chrome_driver.find_element(By.CSS_SELECTOR,'textarea.sc-kRkRkg.hZlvcS')

#入力欄に入力
my_data_input.send_keys(my_data)

#更新ボタン取得
upload_buttom=chrome_driver.find_element(By.CSS_SELECTOR,'button.sc-eDvSVe.iklejs.sc-eGqszx.jewcaj')

#更新するクリック
upload_buttom.click()

#更新がうまく行っているか確認用のスリープ
time.sleep(10)
