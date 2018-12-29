import os

os.chdir(r"C:\Users\student\change\submit")#change diractory - 경로를 위해서 r을 "" 앞에 써준다

for fileName in os.listdir("."):#listdir(".") .:현재 폴더, listdir 모든 파일을 보여줘
    data = fileName.split("PEOPLE_")
    os.rename(fileName,"SUBMIT_"+str(data[1]))
    #os.rename(fileName,"PEOPLE_"+fileName)#os.rename으로 이름을 변경(기존이름, 바꿀이름)


###Replace를 이용한 해결방법###

# for fileName in os.listdir("."):
#     data = fileName.replace("PEOPLE","SUBMIT")
#     os.rename(fileName,data)#replace를 시키는 것이기에 다음 이름이 필요하지 않다.