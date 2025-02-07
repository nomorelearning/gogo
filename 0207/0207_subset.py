T = int(input())
arr = range(1,13)
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1<<12):
        subset = []
        for j in range(12):
            if i & (1<<j):
                if :
                    subset.append(arr[j])

    print(f'#{tc} {subset}')


    # print(f'#{tc} {count}')