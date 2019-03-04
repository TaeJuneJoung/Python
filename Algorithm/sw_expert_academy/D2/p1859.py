import sys
sys.stdin = open('../input/p1859.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    save_num = arr[N-1]
    sum_num = 0
    for i in range(N-2, -1, -1):
        if arr[i] < save_num :
            sum_num += (save_num - arr[i])
        save_num = arr[i] if arr[i] > save_num else save_num
    print(f"#{t} {sum_num}")