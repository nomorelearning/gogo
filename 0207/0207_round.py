
T = int(input())
for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]

    row, col, k = map(int,input().split())
    for r in range(row, row+k):
        for c in range(col, col + k):
            if row < r < row+k-1 and col < c < col+k-1:
                continue
            arr[r][c] = 1
    print(f'#{tc}')
    for i in range(10):
        print(*arr[i])