# tuple

tuple1 = (1,2,3,'a','b')

# 튜플 요소값 삭제 시 오류
#del tuple1[0]
'''
Traceback (most recent call last):
  File "tupleStudy.py", line 6, in <module>
    del tuple1[0]
TypeError: 'tuple' object doesn't support item deletion
'''

# 튜플 요소값 변경 시 오류
#tuple1[0] = 5
'''
Traceback (most recent call last):
  File "tupleStudy.py", line 15, in <module>
    tuple1[0] = 5
TypeError: 'tuple' object does not support item assignment
'''

#튜플 인덱싱
result = tuple1[0]
print(result)

#튜플 슬라이싱
result = tuple1[3:]
print(result)

#튜플 더하기
tuple2 = (4,5,'c')
result = tuple1 + tuple2
print(result)

#튜플 곱하기
result = tuple1*3
print(result)

#튜플 길이 구하기
result = len(tuple1)
print(result)

'''
[문제1] 튜플 추가

(1,2,3)이라는 튜플에 4라는 값을 추가하여 (1,2,3,4)처럼 만들어 출력해 보자.

'''

tupleEx = 1,2,3
plusNum = (4,) #(4)면은 int로 인식되니 (4,)로 써서 튜플로 인식시켜줌
result = tupleEx + plusNum
print("문제 풀이 :",result)
print(len(plusNum))

# 하나 더 이해하고 넘어갈 것
beforeId = id(tupleEx)
tupleEx = tupleEx + (4,)
afterId = id(tupleEx)
print(tupleEx)
print(beforeId, afterId) # 두 값은 다름
#튜플의 값이 변경된 것이 아니라 새로운 tupleEx가 생겨 값을 저장했음을 알 수 있다.