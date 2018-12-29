# 함수 인자 이해하기

def add_string(str1, str2="파이썬"):
    print(str1 + ' : ' + str2)

add_string("프로그램 언어") #프로그램 언어 : 파이썬
add_string(str2='Java',str1 = "이전의 언어는?") #이전의 언어는? : Java

def function1(*args):
    print(args)

def function2(width, height, **kwargs):
    print(kwargs)

function1() #()
function1("안녕하세요. 파이썬입니다.")  #('안녕하세요. 파이썬입니다.',)
function1(3,5,1,2,3,5)  #(3, 5, 1, 2, 3, 5)

function2(5,3)  #{}
function2(5,3,text="안녕",color='Blue',number=5)    #{'text': '안녕', 'color': 'Blue', 'number': 5}
