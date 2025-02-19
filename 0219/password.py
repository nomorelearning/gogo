import sys
sys.stdin = open('in.txt')

from collections import deque

def cycle(q):
    while True:
        for i in range(1,6):
            num = q.popleft()
            num -= i
            if num <= 0:
                q.append(0)
                return q
            q.append(num)

for t in range(1,11):
    no = int(input())
    q = deque(list(map(int,input().split())))
    cycle(q)
    print(f'#{t}', *q)