import sys
sys.stdin = open('input/p1213.txt', 'r', encoding='UTF8')

"""
T - 테스트케이스 번호 담는 변수
findStr - 찾는 문자를 담는 변수
enterStr - 입력 문자를 담는 변수

start - 시작인덱스
end - enterStr의 길이 -1
k - findStr의 길이

count - 카운트 변수

python스럽게 슬라이싱으로 처리
슬라이싱을 문자열로 '반복문과 += 연산'을 통해 확인할 수도 있음

[주의할점]
#끝나는 인덱스 처리
TestCase 10번 문제와 같은 경우
"""

for t in range(1,11):
    T = input()
    findStr = input()
    enterStr = input()
    start = 0
    end = len(enterStr)-1
    k = len(findStr)
    count = 0
    while start < end :
        if enterStr[start:start+k] == findStr:
            count += 1
        start += 1
    print(f"#{t} {count}")