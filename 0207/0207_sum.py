# 두 개의 값을 받아 큰 값을 출력하는 함수
def who_is_max(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2

# 리스트를 받아 합을 출력하는 함수
def sumsum(lst):
    result = 0
    for i in range(100):
        result += lst[i]
    return result

for tc in range(1, 11):
    no = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
        
    # 초기 최댓값으로 대각선 합을 부여
    max_val = 0
    for n in range(100):
        max_val += arr[n][n]

    # 역대각선 합과 최댓값 비교
    sum_val = 0
    for n in range(100):
        sum_val += arr[99-n][n]
    max_val = who_is_max(max_val, sum_val)

    # 행 기준 합과 최댓값 비교
    for r in arr:
        row_sum = sumsum(r)
        max_val = who_is_max(max_val, row_sum)

    # 열 기준 합과 최댓값 비교
    for arr_1 in zip(*arr):
        col_sum = sumsum(arr_1)
        max_val = who_is_max(max_val, col_sum)

    print(f'#{tc}', max_val)