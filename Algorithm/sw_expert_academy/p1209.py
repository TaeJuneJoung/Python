import sys
sys.stdin = open('input/p1209.txt', 'r')

#2차열 리스트가 아닌 하나의 리스트로 담아진행. But, 느림
for t in range(10):
    t_n = int(input())
    M = list()
    for m in range(100):
        array = list(map(int, input().split()))
        M.extend(array)
        d_x = sum(M[0::101])
        d_y = sum(M[99:9902:99])
        result = d_x if d_x > d_y else d_y
        for i in range(100):
            start = 100*i
            end = 100*(i+1)
            startCol = i
            row = sum(M[start:end])
            col = sum(M[startCol::100])
            result = row if row > result else result
            result = col if col > result else result
    print(f"#{t_n} {result}")