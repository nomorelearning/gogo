T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    min_val = lst[0]
    max_val = lst[0]
    for i in range(N):
        if lst[i] < min_val:
            min_val = lst[i]
        if lst[i] > max_val:
            max_val = lst[i]
    gap_val = max_val - min_val

    print(f'#{tc} {gap_val}')