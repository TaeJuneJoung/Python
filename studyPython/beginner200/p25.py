# 비트 연산자

# 집합을 대상으로 교집합, 합집합, 대칭차집합

a = set([1,2,3])
b = set([3,4,5])



print(a&b) #교집합
print(a|b) #합집합
print(a^b) #대칭차집합(합집합 - 교집합)

c = set(["안녕", "파이썬"])
d = set(["자바", "이제", "안녕"])

print(c&d)
print(c|d)
print(c^d)


# 2진수
a = 0b110 #6
b = 0b101 #5

print(a&b) #0b100
print(a|b) #0b111
print(a^b) #0b011

# 8진수
a = 0o123 #83
b = 0o103 #67

print(a&b) #67
print(a|b) #83
print(a^b) #16