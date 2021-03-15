import sys
sys.stdin = open('sample_input.txt')


def solution(V, E, graph, S, G):
    visited = [False for _ in range(V + 1)]
    # 가야할 곳
    to_visits = [S]
    # 탐색중에 걸어온 길
    path = []
    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            path.append(current)
            to_visits += graph[current]
    print(path)
    return int(visited[S])


T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    S, G = map(int, input().split())

