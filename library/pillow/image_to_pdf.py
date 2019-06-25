import os
from PIL import Image

#이미지파일 경로폴더
path_dir = 'img'
imagelist = os.listdir(path_dir)

#img담을 리스트 -> append_images를 위해 사용
img_list = []

#pdf파일 이름 설정
pdf_filename = "example.pdf"

img_base = Image.open('img/'+str(imagelist[0]))
for i in range(1,len(imagelist)):
    img_list.append(Image.open('img/'+str(imagelist[i])))
img_base.save(pdf_filename, "PDF", resolution=100.0, save_all=True, append_images=img_list)