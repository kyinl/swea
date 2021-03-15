import sys
sys.stdin = open('input.txt')


def dfs(V, graph, S, G):
    visited = [False for _ in range(V+1)]
    stack = [S]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited[node] = True
            stack.extend(graph[node])
    return int(visited[G])


T = 10

for tc in range(1, T+1):
    num, E = map(int, input().split())
    V = 99
    S = 0
    G = 99
    graph = [[] for _ in range(V)]
    tmp_list = list(map(int, input().split()))
    for idx in range(len(tmp_list)):
        if not idx % 2:
            graph[tmp_list[idx]].append(tmp_list[idx+1])

    print('#{} {}'.format(tc, dfs(V, graph, S, G)))
