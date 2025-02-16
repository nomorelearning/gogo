import sys
sys.stdin = open('test.txt')


def dfs(start):
    visited[start] = 1      # 지금 위치 방문 처리
    result.append(start)        # 방문 기록부에 저장
    for next_node in graph[start]:      # 지금 위치에서 갈 수 있는 목록 호출
        if not visited[next_node]:      # 갈 수 있는 목록이 방문하지 않은 경우 재귀
            dfs(next_node)



T = int(input())
for t in range(1,T+1):
    v, e = map(int,input().split())     # v는 정점 개수, e는 간선 개수
    graph = [[] for _ in range(v+1)]    # graph는 graph[from노드] = *to노드를 기록
    visited = [0] * (v+1)               # 방문 기록부
    result = []                         # 출발선으로부터 방문할 수 있는 노드 저장
    ans = 0                             # 리저트에 y가 있으면 1, 없으면 0

    for i in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
# 실행
    x, y = map(int,input().split())     # x는 궁금한 출발점, y는 궁금한 도착점
    dfs(x)
    if y in result:
        ans = 1

    print(f'#{t}',ans)

