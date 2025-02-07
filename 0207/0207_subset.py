#
# arr = range(1,13)
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     count = 0
#     for subset in range(1<<3):
#         for j in range(12):
#             if i & (1<<j):
#                 if sum(arr[j]) ==