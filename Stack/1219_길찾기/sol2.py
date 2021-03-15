import sys
sys.stdin = open('input.txt')


def solution(V, E, graph, S, G):
    # 인덱스와 숫자 맞추기 위해 V+1 사용
    # vertex No. == visited idx == graph idx
    visited = [0 for _ in range(V+1)]
    # 가야할 곳
    to_visits = [S]

    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = 1
            # 갔든지 안갔든지 다 넣는다.
            to_visits += graph[current]

    return visited[G]


T = 10

for tc in range(1, T+1):
    num, E = map(int, input().split())
    V = 99
    S = 0
    G = 99
    graph = [[] for _ in range(V+1)]
    tmp_list = list(map(int, input().split()))
    for idx in range(len(tmp_list)):
        if not idx % 2:
            graph[tmp_list[idx]].append(tmp_list[idx+1])
    print('#{} {}'.format(tc, solution(V, E, graph, S, G)))
