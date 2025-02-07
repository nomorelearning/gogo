T = int(input())
arr = range(1,13)
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1<<12):
        subset = []
        for j in range(12):
            if i & (1<<j):
                subset.append(arr[j])
        if K in subset:
            result = subset.count(K)

    print(f'#{tc} {result}')


    # print(f'#{tc} {count}')