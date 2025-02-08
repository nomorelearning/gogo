T = int(input())
arr = range(1,13)
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1<<12):
        subset_sum = 0
        subset_count = 0
        for j in range(12):
            if i & (1<<j):
                subset_sum += arr[j]
                subset_count += 1
                
        if subset_sum == K and subset_count == N:
            result += 1
    print(f'#{tc} {result}')