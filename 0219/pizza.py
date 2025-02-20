import sys
sys.stdin = open('in.txt')


# 마이쮸
# p = 1
# q = deque()
# N = 20
# m = 0
# v = 0
#
# while m<N:
#     q.append((p,1,0))
#     v,c,my = q.popleft()
#     m += c
#     q.append((v,c+1,my+c))
#     p += 1
#     print(f'마지막 받은 사람 : {v}')

from collections import deque

T = int(input())
for t in range(1,T+1):
    n,m= map(int,input().split())
    arr = list(map(int,input().split()))
    oven = deque()
    pizza = deque()
    # 처음 화덕에 들어갈 n개의 도우
    for i in range(n):
        oven.append((i, arr[i]))
    # 남아있는 피자들
    for i in range(n,m):
        pizza.append((i,arr[i]))

    while len(oven) > 1:
        pizza_num, cheeze = oven.popleft()
        cheeze //= 2
        if cheeze != 0:
            oven.append((pizza_num, cheeze))
        else:
            if pizza:
                oven.append(pizza.popleft())
    print(f'#{t} {oven[0][0]+1}')