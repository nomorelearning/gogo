t = int(input())
for tc in range(1, t+1):
    arr = [[0] * 10 for _ in range(10)]     # 0으로 구성된 정렬 생성
    row, col, n = map(int, input().split())

    for i in range(n):
        arr[row + i][col + i] = 1           # 행과 열의 상대 위치가 같은 곳에 1
        arr[row + i][col + n - 1 - i] = 1   # 열의 마지막 위치 - i에도 1

    print(f'#{tc}')
    for lst in arr:
        print(*lst)    