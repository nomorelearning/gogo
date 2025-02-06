T = int(input())

for ct in range(T):
    no = int(input())
    lst = list(map(int, input().split()))

    counts = [0] * 101
    for i in lst:
        counts[i] += 1
    
    max_count = counts[0]
    for i in range(1, 101):
        if max_count < counts[i]:
            max_count = counts[i]
    max_indx = 0
    for i in range(100, -1, -1):
        if counts[i] == max_count:
            max_indx = i
            break
    print(f'#{no} {max_indx}')