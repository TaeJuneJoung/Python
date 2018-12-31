list1 = []
list1 = list()
list2 = [1, 2, 3]
list3 = ['Hello', 1,'My', (2, 3, 4), ['python','java']]
print(list3)

# 리스트의 인덱싱
list3[0]
print(list3[0])
print(list3[0],list3[2],list3[-1][0]) #Hello My python

# 리스트의 슬라이싱
list3[0::2]
print(list3[0::2])

# 리스트 더하기
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 + list2
print(list1 + list2)

# 리스트 반복하기
list1*3
print(list1*3)

# 리스트 길이구하기
len(list3)
print(len(list3)) #5

# 주의해야할 TypeError
#print(list3[0] + list3[1]) #TypeError: must be str, not int
print(list3[0] + str(list3[1])) #Hello1
print(list3[0], list3[1]) #Hello 1



# 리스트 값 수정하기
beforeId = id(list1)
list1[2] = 5
afterId = id(list1)
if(beforeId==afterId):
    print("동일함")
else:
    print("다름")

print(list1)

# del 이용한 리스트 요소 삭제하기
result = list1 + list2 #[1, 2, 5, 4, 5, 6]

del list1[2]

del result[2:]

if(id(list1)==id(result)):
    print("같다")
else:
    print("역시 다르다")

print(list1)

x = [4,5]

#append
list1.append(3)
print(list1) #[1, 2, 3]

#extend
list1.extend(x)
print(list1) #[1, 2, 3, 4, 5]

#insert
list1 = [1,2,4]
list1.insert(2,3)
print(list1)

#remove
#list1.remove(5) #ValueError: list.remove(x): x not in list
list1.remove(4)
print(list1)

#pop
for i in range(0,len(list1)):
   print(list1.pop())

print(list1)

#index
list1 = [1,2,3]
result = list1.index(3)
print(result) #3의 값이 있는 index 번호는 2

list1 = [1,2,3,4,5,2,3,4,5,1]
result = list1.index(4,4) #4의 값이 있는 index를 4번 index부터 찾아라
print(result)

#count
list1 = [1,2,3,2,3,2]
result = list1.count(2)
print(result) #3

#sort
list1.sort()
print(list1) #[1, 2, 2, 2, 3, 3]
list1.sort(reverse=True)
print(list1) #[3, 3, 2, 2, 2, 1]

'''
[문제1] 리스트 조인

['Life', 'is', 'too', 'short'] 라는 리스트를 Life is too short라는 문자열로 만들어 출력해 보자.
(힌트. 문자열의 join 함수를 이용해 보자.)
'''
problem = ['Life', 'is', 'too', 'short']
result = " ".join(problem)
print(result)



'''
[문제2] 리스트 정렬

[1, 3, 5, 4, 2]라는 리스트를 [5, 4, 3, 2, 1]로 만들어보자.
(힌트. 리스트의 내장함수인 sort와 reverse를 활용해 보자.)
'''
problem = [1, 3, 5, 4, 2]
problem.sort(reverse=True)
print(problem)

#문제의 의도대로 푸는 방법
problem = [1, 3, 5, 4, 2]
problem.sort()
problem.reverse()
print(problem)