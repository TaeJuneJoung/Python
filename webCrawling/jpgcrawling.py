import requests
import time

#try except으로 처리하여 보다 완성도를 높일 수 있음
for i in range(100):
    url = "URL주소"+str(i)+".jpg"
    response = requests.get(url)
    if response.status_code == 200:
        with open("/Users/유저이름/Desktop/폴더경로(존재해야함)/{}.jpg".format("파일이름"+str(i+1)), 'wb') as f:
            f.write(response.content)
            print(str(i)+"완료")
    time.sleep(1) #디도스 공격이 아님을 나타내기 위해