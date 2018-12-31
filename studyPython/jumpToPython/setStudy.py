s1 = set([1,2,3])
print(s1)

s2 = set("Hello Python")
print(s2)

#리스트로 변환하여 인덱싱
l1 = list(s1)
l1[0:3]
print(l1[0:3])

t1 = tuple(s1)
print(t1[0:3])



s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#intersection 교집합
result = s1 & s2
print(result)
result = s1.intersection(s2)
print(result)


#union 합집합
result = s1 | s2
print(result)
result = s1.union(s2)
print(result)


#difference 차집합
result = s1 - s2 #{1, 2, 3}
print(result)

result = s2 - s1 #{8, 9, 7}
print(result)

result = s1.difference(s2) #{1, 2, 3}
print(result)


#대칭차집합
result = s1 ^ s2 #{1, 2, 3, 7, 8, 9}
print(result)

#add - 1개의 값 추가
s1 = set([1,2,3])
s1.add(4)
 #unhashable type: 'list' list로 아래와 같이 추가할 수 없음
print(s1)

#update - 여러개의 값 추가
s1.update([5,6,7])
print(s1)

#remove - 1개의 값 제거
s1.remove(7)
print(s1)

'''
[문제1] 집합의 중복

중복을 허용하지 않는 집합 자료형의 특징을 이용하여 다음 a 리스트에서 중복된 숫자들을 제거해 보자.
'''
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
#set은 중복x
a = set(a)
print(a)


'''
[문제2] 집합 만들기

집합 자료형은 다음과 같이 만들 수 있다.
>>> a = {'a', 'b', 'c'}
>>> a
{'a', 'b', 'c'}
>>> type(a)
<class 'set'>

값이 하나도 없는 비어있는 set을 만들기 위해 다음과 같이 시도 해 보자.

>>> a = {}
>>> type(a)
<class 'dict'>

위와 같이 값이 있을 경우에는 집합 자료형으로 인식했지만 값이 없을경우에는 딕셔너리로 인식하게 된다.
그렇다면 값이 비어있는 집합 자료형은 어떻게 만들 수 있을까?
'''
a = set()
print(a)
print(type(a))

#문제의 의도는 아래형식 같음.
a = {}
a = set(a)
print(a)
print(type(a))