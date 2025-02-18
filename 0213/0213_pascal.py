
def pascal(n):
    if n == 1 or n == 0:
        return 1
    else:
        return pascal(n-2) + pascal(n-1)

T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = [[1] * i for i in range(1, n+1)]
    for i in range(2,n):
        for j in range(1,i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{t}')
    for lst in arr:
        print(*lst)


# 강사님 방법

N = 10
arr = [[0] * N for _ in range(N)]

for r in range(N):
    for c in range(1, r+1):
        if c == 0 or r == c:
            arr[r][c] = 1
        else:
            arr[r][c] = arr[r-1][c-1] + arr[r-1][c]

