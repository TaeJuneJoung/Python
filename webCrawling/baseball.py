import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?&q=프로야구+순위"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

"""
전체 테이블 위치
#abtColl > div.coll_cont > div > div.tab_body > div:nth-child(1) > div > table

tr의 규칙성 찾기
#abtColl > div.coll_cont > div > div.tab_body > div:nth-child(1) > div > table > tbody > tr:nth-child(1)
#abtColl > div.coll_cont > div > div.tab_body > div:nth-child(1) > div > table > tbody > tr:nth-child(2)

"""
if(requests.get(url).status_code == 200):
    
    selectTr = "#abtColl > div.coll_cont > div > div.tab_body > div:nth-of-type(1) > div > table > tbody"
    pick = soup.select_one(selectTr)
    pick = pick.text
    data = pick.split("    ")
    for i in data:
        print(i)

        
else:
    print(str(requests.get(url).status_code) + "연결 실패")
