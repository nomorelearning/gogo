T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    max_fall = 0
    for i in range(N):
        count = 0
        for j in range(i, N):
            if lst[j] < lst[i]:
                count += 1
        if count > max_fall:
            max_fall = count
    print(f'#{tc} {max_fall}')