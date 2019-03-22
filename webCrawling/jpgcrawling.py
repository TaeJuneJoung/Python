import requests
import time

jpg_list = [
]

pageNum = 500 #총페이지 수 기재
startPage = 0 #시작점
for page in range(4, len(jpg_list)):
    cnt_or200 = 0 #200이 아닌 숫자를 체크
    for i in range(pageNum):
        url = "URL"+jpg_list[page]+str(i)+".jpg"
        response = requests.get(url)
        if response.status_code == 200:
            with open("/Users/사용자/Desktop/폴더경로/{}.jpg".format("파일이름"+str(startPage+253)), 'ab') as f:
                f.write(response.content)
                print("jpg_list 순서 :", page, startPage) #중간에 끊겼을 경우 고쳐서 재실행하기 위해 print
                startPage += 1
                time.sleep(1) #디도스 공격이 아님을 나타내기 위해
        else:
            cnt_or200 += 1
            if cnt_or200 > 6:
                break