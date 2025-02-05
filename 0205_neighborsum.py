T = int(input())

for ct in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_sum = lst[0] + lst[1]
    for i in range(1, N-1):
        if lst[i] + lst[i+1] > max_sum:
            max_sum =  lst[i] + lst[i+1]
    print(f'#{ct} {max_sum}')