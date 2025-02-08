T = int(input())

for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]     # 0으로 된 행렬 만들어주기
    row, col, w, h = map(int, input().split())

    num = 1                                 # 자리에 넣을 숫자 num 변수 생성
    for c in range(col, col + w):
        for r in range(row, row + h):           # 열 우선 순회 만들기
            arr[r][c] = num
            num += 1                        # 삽입할 숫자를 하나씩 증가
    
    print(f'#{tc}')
    for lst in arr:
        print(*lst)