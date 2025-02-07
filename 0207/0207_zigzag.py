arr = [[0] * 10 for _ in range(10)]
row, col, w, h = map(int, input().split())

num = 1
for r in range(row, row + h):
    for c in range(col, col + w):
        n = r - row
        arr[r][c + (col + w - 1 -2 * c)*(n % 2)] = num
        num += 1

for lst in arr:
    print(*lst)