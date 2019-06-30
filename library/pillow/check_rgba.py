from PIL import Image
import os

file_list = os.listdir('img')

for file_ in file_list:
    img = Image.open(f'img/{file_}')
    if img.mode == 'RGBA':
        print(img.mode)