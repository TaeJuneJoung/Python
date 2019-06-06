"""
여러가지 사진이 있을 때,
사진의 크기를 파악하기 위해 만든 소스
"""
import os
#Pillow패키지 import
from PIL import Image

#img폴더 경로선택
path_dir = 'img'
file_list = os.listdir(path_dir)

#파일 이름순 정렬
file_list.sort()

row_min = 10001#가로
row_name = ""
col_min = 10001#세로
col_name = ""
for file_ in file_list:
    img = Image.open(f'img/{file_}')
    if row_min > img.size[0]:
        row_min = img.size[0]
        row_name = file_
    if col_min > img.size[1]:
        col_min = img.size[1]
        col_name = file_
print(row_min, row_name)
print(col_min, col_name)