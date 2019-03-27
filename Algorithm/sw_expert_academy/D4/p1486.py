def nPr(n, r, s):
    if s >= H:
        if s not in res_set:
            res_set.add(s)
        else:
            return
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                nPr(n, r+1, s+M[i])
                used[i] = 0
            else:
                return

T = int(input())
for t in range(1,T+1):
    N, H = map(int, input().split())
    M = list(map(int,input().split()))
    used = [0] * N
    res_set = set()
    nPr(N, 0, 0)
    print("#"+str(t), min(res_set)-H)