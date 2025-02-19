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
    dough = list(map(int,input().split()))
    cq = deque()
    # 처음 화덕에 들어갈 n개의 도우
    for v in range(n):
        cq.append((v+1, dough[v]))
    # 처음 들어가는 도우 인덱스 v
    v = n
    while len(cq) > 1:
        pizza_num, cheeze = cq.popleft()
        cheeze //= 2
        if cheeze != 0:
            cq.append((pizza_num, cheeze))
        else:
            if v < m:
                cq.append((v+1, dough[v]))
                v += 1
    print(f'#{t} {cq[0][0]}')