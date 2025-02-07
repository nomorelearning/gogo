T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(i+1, N):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    print(f'#{tc}', *lst)