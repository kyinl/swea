import sys
sys.stdin = open('sample_input.txt')


def solution(V, E, graph, S, G):
    # 인덱스와 숫자 맞추기 위해 V+1 사용
    # vertex No. == visited idx == graph idx
    visited = [False for _ in range(V+1)]
    # 가야할 곳
    to_visits = [S]
    # 탐색중에 걸어온 길
    path = []
    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            path.append(current)
            # 갔든지 안갔든지 다 넣는다.
            # 아래 코드 생략가능
            # for v in graph[current]:
            #     if not visited[v]:
            #         to_visits.append(v)
            to_visits += graph[current]
    # print(path)
    return int(visited[S])


T = int(input())

for tc in range(1, T+1):

    # Vertex, Edge 의 갯수
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        # graph[end].append(start) 무방향인 경우 추가
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, solution(V, E, graph, S, G)))


    """
    [
        0 [],
        1 [4, 3],
        2 [3, 5],
        3 [],
        4 [6],
        5 [],
        6 []
    ]
    
    """



