# def is_this_max(list_1):        # 가운데 값이 최댓값인지 확인
#     x = list_1[2]
#     for k in list_1:
#         if k > x:
#             return False
#     return True
#
# def how_floor(list_2):          # 두번째 큰 값과 차이를 계산
#     second = 0
#     for l in [0, 1, 3, 4]:
#         if list_2[l] > second:
#             second = list_2[l]
#     return second
#
# for tc in range(1, 11):
#     n = int(input())
#     lst = list(map(int,input().split()))
#
#     result = 0
#     for i in range(2, n-2):
#         list_now = lst[i-2:i+3]         # i를 중앙 인덱스로 하는 길이 5인 리스트 임시 생성
#         if is_this_max(list_now):       # 가운데가 최댓값인지 확인 후 차이 계산산
#             second = how_floor(list_now)
#             result += list_now[2] - second      # 차이를 누적하여 result 만들기기
#         else:
#             continue
#
#     print(f'#{tc}', result)
#


import sys
sys.stdin = open('test.txt')

for t in range(1,11):
    n = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    for i in range(2,n-2):
        max = 0
        for j in range(-2,3):
            if lst[i+j] > max:
                max = lst[i+j]
        if lst[i] != max:
            continue
        second = 0
        for j in [-2, -1, 1, 2]:
            if second < lst[i+j]:
                second = lst[i+j]
            cnt += max - second
    print(cnt)
print(list(range(-2,3)))