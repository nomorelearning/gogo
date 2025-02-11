T = int(input())

for t in range(1, T+1):
    max_val = 0
    lst = list(map(int, input().split()))
    for num in lst:
        if max_val < num:
            max_val = num
    print(f'#{t}', max_val)