T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))
    counts = [0] * 10
    for i in lst:
        counts[i] += 1

    many_count = 0
    for i in range(10):
        if many_count < counts[i]:
            many_count = counts[i]

    for i in range(9, -1, -1):
        if counts[i] == many_count:
            result = i
            break
    print(f'#{tc} {result} {many_count}')