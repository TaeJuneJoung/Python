import sys
sys.stdin = open("py4836.txt","r")

T = int(input())
for t in range(1,T+1):
    N = int(input())
    for n in range(N):
        C = list(map(int, input().split()))
        red, blue = [], []
        result = []
        if C[4] == 1:
            red = C
        else:
            blue = C
        
        print(red&blue)
