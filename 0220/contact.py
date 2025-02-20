from collections import deque

import sys
sys.stdin = open('in.txt')

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0] * (length + 1)
    visited[start] = 1
    max_val = start
    while q:
        cur = q.popleft()
        for i in adj_l[cur]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                if max_val < i:
                    max_val = i
    return max_val


for tc in range(1,11):
    l, s = map(int,input().split())
    lst = list(map(int,input().split()))
    length = max(lst)
    adj_l = [[] for _ in range(length + 1)]
    for i in range(l//2):
        adj_l[lst[i]].append(lst[i+1])

    print(bfs(s))
