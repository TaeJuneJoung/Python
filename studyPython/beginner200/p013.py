# for~else문

scope = [1,2,3,4,5]
for i in scope:
    print(i)
    break
else:
    print("End")


"""

책의 내용에서는 break에 주석 처리하고 코드를 실행해야 화면에 1만 출력된다고 하는데
실제 결과로는 주석 없이 현 소스 그대로 하면
1
2
3
4
5
End
    가 출력되고,

주석이 있다면 
1
    만 출력된다.

"""