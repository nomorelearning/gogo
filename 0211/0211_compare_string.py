T = int(input())

for t in range(1,T+1):
    find = list(input())
    lst = list(input())
    n = len(find)
    count = 0
    for i in range(len(lst) - n + 1):
        if lst[i:i+n] == find:
            count += 1
    print(f'#{t}', count)