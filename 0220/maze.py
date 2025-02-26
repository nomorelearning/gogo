import sys
sys.stdin = open('in.txt')

from collections import deque

def find_start():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j

def bfs(i, j):
    visited = [[0]*16 for _ in range(16)]
    q = deque([(i,j)])
    visited[i][j] = 1
    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            wi, wj = ti + di, tj + dj
            if 0<=wi<16 and 0<=wj<16 and visited[wi][wj] == 0 and maze[wi][wj] != 1:
                visited[wi][wj] = 1
                q.append((wi,wj))
    else:
        return 0


for _ in range(10):
    tc = input()
    maze = [list(map(int,input())) for _ in range(16)]
    start_i, start_j = find_start()
    ans = bfs(start_i,start_j)
    print(f'#{tc} {ans}')