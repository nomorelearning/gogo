T = int(input())
for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    row, col, w = map(int, input().split())

    num = 1
    for r in range(row, row + w):
        for c in range(w):
            n = r - row
            arr[r][col + c + (w - 1 - 2 * c)*(n % 2)] = num
            num += 1
    
    print(f'#{tc}')
    for lst in arr:
        print(*lst)