T = int(input())

for t in range(1, T+1):
    lst = list(map(int, input().split()))
    sum_val = 0
    for num in lst:
        sum_val += num
    result = round(sum_val/10)

    print(f'#{t}', result)