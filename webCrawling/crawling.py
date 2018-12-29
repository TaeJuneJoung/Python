import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')


#bs4에서는 child를 읽지 못해서 of-type으로 변경하여 진행해야한다.
selector = "#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a"
data = soup.select(selector)

#status_code를 통해 나오는 정보를 받음
if(res.status_code == 200):
    print("접속 완료:)")
    for i in data:
        print(i.text)
else:
    print("접속 실패:(")
