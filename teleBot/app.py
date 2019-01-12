from flask import Flask, request
import os
from pprint import pprint as pp#pprint - json을 깔끔하게 꺼내주기 위해서
import requests
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Telegram Bot"
    
api_url = "https://api.telegram.org"

#Telegram API를 사용하기 위한 변수
token = os.getenv('TELE_TOKEN')

@app.route(f"/{token}", methods=['POST'])
def telegram():
    
    
    #NAVER API를 사용하기 위한 변수
    naver_client_id = os.getenv('NAVER_ID')
    naver_secret = os.getenv('NAVER_SECRET')
    
    
    tele_dict = request.get_json()
    tele_msg = tele_dict.get("message")
    
    #유저 정보
    chat_id = tele_msg.get("from").get("id")
    
    #유저가 입력한 데이터
    if tele_msg.get("text") is None:
        text = "Draft text"
    else:
        text = tele_msg.get("text")
    
    #공백
    whiteTab = "\t\t"
    whiteEnter = "\n"
    
    #명령어 리스트
    commandList = ["!번역", "!메뉴","!menu","!로또","!lotto","!develope"]
    
    
    #사진인지 Text인지 구별필요
    isTrans = False
    isPhoto = False
    isVideo = False
    isDocument = False
    isLocation = False
    isContact = False
    isSticker = False
    isVoice = False
    
    
    #사용자 입력 체크
    if tele_msg.get("photo") is not None:
        isPhoto = True
    elif tele_msg.get("video") is not None:
        isVideo = True
    elif tele_msg.get("document") is not None:
        isDocument = True
    elif tele_msg.get("location") is not None:
        isLocation = True
    elif tele_msg.get("contact") is not None:
        isContact = True
    elif tele_msg.get("sticker") is not None:
        isSticker = True
    elif tele_msg.get("voice") is not None:
        isVoice = True
        
    elif text[:4].rstrip() == "!명령어":
        text = whiteEnter.join(commandList)
        
    else:
        #Naver Papago
        if text[:3] == "!번역":
            isTrans = True
            text = text.replace(text,text[3:])

    
    
    if isTrans:
        papago = requests.post("https://openapi.naver.com/v1/papago/n2mt",
                    headers = {
                        "X-Naver-Client-Id":naver_client_id,
                        "X-Naver-Client-Secret":naver_secret
                    },
                    data = {
                        "source":'ko',
                        "target":'en',
                        "text":text
                    }
        )

        if(papago.status_code==200):
            text = papago.json()["message"]["result"]["translatedText"]
        else:
            text = "에러가 발생하였습니다.\n다시 시도해주세요\n문제가 계속 발생시 얘기해주세요"
        
    elif isPhoto :
        #텔레그램에게 사진 정보 가져오기
        file_id = tele_msg.get("photo")[-1].get("file_id")
        file_path = requests.get(f"{api_url}/bot{token}/getFile?file_id={file_id}").json()["result"]['file_path']
        file_url = f"{api_url}/file/bot{token}/{file_path}"
        #사진을 네이버 유명인 인식 API 넘겨주기
        file = requests.get(file_url, stream=True)
        clova = requests.post("https://openapi.naver.com/v1/vision/celebrity",
            headers = {
                "X-Naver-Client-Id":naver_client_id,
                "X-Naver-Client-Secret":naver_secret
            },
            files = {
                "image":file.raw.read()#원본데이터
            }
        )
        
        #인식이 되었을 때
        #pp(clova.json())
        if clova.json().get('info').get('faceCount'):
            value = clova.json()['faces'][0]['celebrity']['value']
            confidence = clova.json()['faces'][0]['celebrity']['confidence']
            confidence = round(float(confidence),3)
            result = ["닮은 연애인 : ", value, "\n", "닮은 비율 : ", str(confidence)]
            text = "".join(result)
            
        #인식이 되지 않았을 때
        else :
            text = "인식이 되지 않습니다."
        
    elif(text.lower() == '!menu' or text.lower() == '!메뉴'):
        #메뉴리스트
        menu_list = ["한식","중식","양식","일식","선택식..."]
        text = random.choice(menu_list)
    elif(text.lower() == '!lotto' or text.lower() == '!로또'):
        #lotto
        lotto_list = random.sample(range(1,46),6)
        lotto_list.sort()
        lotto_number = list()
        for i in lotto_list:
            lotto_number.append(str(i))
        text = whiteTab.join(lotto_number)
    elif(text.lower() == '!develope' or text.lower() == '!개발'):
        text = "Dev.J"
    
    #유저에게 그대로 돌려주기
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    #이미지 메아리
    #requests.get(f'{api_url}/bot{token}/sendPhoto?chat_id={chat_id}&photo={file_id}')
    return '', 200
    
    
#해당 명령어를 사용하면 python app.py로 연결할 수 있다.
# app.run(host=os.getenv('IP','0.0.0.0'), port=int(os.getenv('PORT',8080)))
#os.getenv('IP','0.0.0.0') -> IP값을 가져오고 없으면 0.0.0.0으로 한다.