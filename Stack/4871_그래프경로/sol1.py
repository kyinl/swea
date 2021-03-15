import sys
sys.stdin = open('sample_input.txt')


def dfs(V, E, graph, S, G):
    visited = [False for _ in range(V+1)]
    stack = [S]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited[node] = True
            stack.extend(graph[node])
    return visited[G]


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, dfs(V, E, graph, S, G)))



