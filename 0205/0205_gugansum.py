T = int(input())
for i in range(1, T+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    max_result = 0
    min_result = 99999999
    for j in range(0, N-M+1):
        sumsum = sum(lst[j:j+M])
        max_result = max(max_result, sumsum)
        min_result = min(min_result, sumsum)
    gap_result = max_result - min_result
    print(f'#{i} {gap_result}')
