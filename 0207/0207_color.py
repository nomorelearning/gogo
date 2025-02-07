T = int(input())
for tc in range(1, T+1):
    arr_1 = [[0] * 10 for _ in range(10)]
    arr_2 = [[0] * 10 for _ in range(10)]
    count = 0
    N = int(input())

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    arr_1[r][c] = 1
        else:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    arr_2[r][c] = 1

    for r in range(10):
        for c in range(10):
            if arr_1[r][c] == arr_2[r][c] == 1:
                count += 1
    print(f'#{tc} {count}')