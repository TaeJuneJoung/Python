import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

# """
# 전체 테이블 위치
# #tableAsset > tbody

# tr의 규칙성 찾기
# #tableAsset > tbody > tr:nth-child(1)
# #tableAsset > tbody > tr:nth-child(2)
# """

selectTr = "#tableAsset > tbody > tr"
selectName = "#tableAsset > tbody > tr > td:nth-of-type(1) > p > a > strong"
selectPrice = "#assetRealBTC"

pick = soup.select("#tableAsset > tbody > tr")

for coin in pick:
    #print(coin.text+" ")
    #print("----------------------")
    print(coin.select_one("td:nth-of-type(1) a strong").text,coin.select_one("td:nth-of-type(2) strong").text)
    print("-----------------------")
    