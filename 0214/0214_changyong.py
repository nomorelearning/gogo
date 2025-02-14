import sys
sys.stdin = open('test.txt')

def dfs(s):
    visited[s] = 1
    result.append(s)
    for nxt in graph[s]:
        if not visited[nxt]:
            dfs(nxt)

T = int(input())
for t in range(1,T+1):
    n, e = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(e):
        v, w = map(int,input().split())
        graph[v].append(w)

    # 그래프 행을 순회하며 가능한 도착지 리스트 만들어 최종 행렬에 삽입
    result_arr = [[] for _ in range(n+1)]
    for s in range(1,n+1):
        if not graph[s]:
            continue
        result = []
        visited = [0] * (n+1)
        dfs(s)
        result_arr[s].extend(result)

    ans = 0
    if i in range(1, n+1):
        for j in result_arr[i]:
            if i in result_arr[j]:
                ans += 1

    print(ans)