import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline


def dfs(now):
    global count

    for nxt in graph[now]:
        if not visited[nxt]:
            count += 1
            visited[nxt] = True # 방문 처리
            dfs(nxt)


for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] * (N + 1) for _ in range(N + 1)] # 다음으로 갈 수 있는 위치 저장
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    count = 0
    visited = [False] * (N + 1)
    visited[1] = True # 방문 처리
    dfs(1) # 1 ~ N 무엇으로 시작하든 상관 없음
    print(count)
