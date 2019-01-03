#String 포매팅

print("I eat %d apples" % 3)

number = 3
print("I eat %d apples" % number)

print("I eat %s apples" % "five")

number = 3
strValue = "apples"
print("I eat %d %s" % (number, strValue))


#포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
#print("Error is %d%" %98) #ValueError: incomplete format
print("Error is %d%%" %98)



#포맷코드와 숫자 함께 사용하여 정렬과 공백 및 소수점 표현하기
print("%10s" %"hello")#     hello
print("%-10sjune."%'hi')#hi        june.

print("%10.4f"%3.123456)#    3.1235