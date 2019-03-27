T = int(input())
for t in range(1,T+1):
    N = int(input())
    print("#"+str(t))

    S = [0 for i in range(N)]
    M = [0 for i in range(N)]
    cnt = 0
    line = 0
    for i in range(N):
        S[i], temp = map(str, input().split())
        M[i] = int(temp)
    
    cnt = 0
    for i in range(N):
        for j in range(M[i]):
            cnt += 1
            print(S[i], end="")
            if cnt == 10:
                cnt -= 10
                print()
    print()