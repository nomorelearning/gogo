import sys
sys.stdin = open('test.txt', 'r')


for _ in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    c, r = 0, 99

    for i in range(100):
        if arr[99][i] == 2:
            c = i
            break

    while r != 0:
        if c > 0 and arr[r][c-1] == 1:
            c -= 1
        elif c < 99 and arr[r][c+1] == 1:
            c += 1
        else:
            r -= 1
        arr[r][c] = 0
    print(f'#{N}', c)
