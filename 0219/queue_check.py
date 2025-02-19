import sys
sys.stdin = open('in.txt')


from collections import deque

T = int(input())
for t in range(1, T+1):
    n,m = map(int,input().split())
    q = deque(list(map(int, input().split())))
    for _ in range(m):
        num = q.popleft()
        q.append(num)

    print(f'#{t} {q.popleft()}')