T = int(input())

for t in range(1,T+1):
    find = list(input())
    lst = list(input())
    n = len(find)
    count = [0] * n

    for i in lst:
        for j in range(n):
            if find[j] == i:
                count[j] += 1
                break

    max_val = 0
    for i in count:
        if i > max_val:
            max_val = i

    print(f'#{t}',max_val)