#自動タイプ
#ライブラリ設定
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains #マウス操作

#初期化
data_lists=[0,0,0,0,0]
chrome_driver=webdriver.Chrome()
wait = WebDriverWait(chrome_driver, 30)

def extract_stock_data(source):
    soup=BeautifulSoup(source,'html.parser')

    #最新情報取得
    for td_i in range(1,6):
        kabu_data=soup.select_one(f'#highcharts-0 > div.highcharts-tooltip > span > table > tbody > tr:nth-child(1) > td:nth-child({td_i})')
        kabu_data_value=kabu_data.text

        #文字列をdatetimeに変換
        if td_i==1:
            date=datetime.datetime.strptime(kabu_data_value,"%Y/%m/%d")
            kabu_data_value=date.strftime("%Y-%m-%d")
            #print(date.strftime("%Y-%m-%d")) #書式変更確認用

        data_lists[td_i-1]=kabu_data_value

    return data_lists


def get_stock_values(URL_data):

    #日経ページ起動
    chrome_driver.get(URL_data)

    #日経画像表示されるまで待つ
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#PAGE_TOP > div > div > div > a > img')))

    #マウスを動かす
    graph=chrome_driver.find_element(By.CLASS_NAME,'highcharts-background')#グラフ要素取得
    graph_width=graph.rect['width']//2 #横幅取得(半分の距離)

    actions=ActionChains(chrome_driver)#グラフ左端
    actions.move_to_element(graph)#グラフ真ん中に移動

    for i in range(graph_width):

        #HTML取得
        source = chrome_driver.page_source
        actions.move_by_offset(1,0)
        actions.perform()

        #マウスクリック時のHTML情報を渡す
        if i>0:#最初は取り込まない
            extract_stock_data(source)
            print(data_lists) 


URL_data='https://www.nikkei.com/markets/worldidx/chart/nk225/?type=6month'

#取得開始時間
start_time=time.time()

get_stock_values(URL_data)

#取得終了時間
end_time=time.time()

#取得時間
delta_time=end_time-start_time
print(f'スクレイピング時間{delta_time}秒')

 

