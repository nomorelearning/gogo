for tc in range(1,11):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    for r in range(100):
        sumsum = 0
        for c in range(100):
            sumsum += arr[r][c]
        if sumsum > max_sum:
            max_sum = sumsum

        sumsum = 0
        for c in range(100):
            sumsum += arr[c][r]
        if sumsum > max_sum:
            max_sum = sumsum

        sumsum = 0
        sumsum += arr[r][r]
        if sumsum > max_sum:
            max_sum = sumsum

        sumsum = 0
        sumsum += arr[r][99 - r]
        if sumsum > max_sum:
            max_sum = sumsum

    print(f'#{tc} {max_sum}')
    
    # 다시도전