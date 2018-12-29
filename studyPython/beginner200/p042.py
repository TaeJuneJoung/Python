# 함수 리턴값 이해하기(return)

def reverse(x,y,z):
    return z,y,x

result = reverse(x=3,y=5,z=7)
print(result)   #(7, 5, 3)
print(type(result)) #<class 'tuple'>

v1, v2, v3 = reverse('잘 부탁해','파이썬','안녕')
print(v1,v2,v3) #안녕 파이썬 잘 부탁해