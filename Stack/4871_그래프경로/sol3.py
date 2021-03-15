# 재귀
import sys
sys.stdin = open('sample_input.txt')


def solution(V, E, graph, S, G):
    visited = [False for _ in range(V+1)]

    def dfs(v):
        visited[v] = True
        for new_v in graph[v]:
            if not visited[new_v]:
                dfs(new_v)

    dfs(S)
    return int(visited[G])


T = int(input())

for tc in range(1, T + 1):
    # Vertex, Edge 의 갯수
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        # graph[end].append(start) 무방향인 경우 추가
    S, G = map(int, input().split())
    print(S, G)
    print('#{} {}'.format(tc, solution(V, E, graph, S, G)))

