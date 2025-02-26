import sys
sys.stdin = open('in.txt')

from collections import deque

def bfs(S, G):
    visited = [0] *(V+1)
    q = deque()
    q.append(S)
    visited[S] = 1
    while q:
        cur = q.popleft()
        for i in adj_l[cur]:
            if i == G:
                return visited[cur]
            if visited[i] == 0:
                visited[i] = visited[cur]+1
                q.append(i)
    else:
        return 0

T = int(input())

for tc in range(1,T+1):
    # 인접리스트 제작
    V,E = map(int,input().split())
    adj_l = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int,input().split())
        adj_l[a].append(b)
        adj_l[b].append(a)
    S,G = map(int,input().split())

    print(f'#{tc} {bfs(S,G)}')