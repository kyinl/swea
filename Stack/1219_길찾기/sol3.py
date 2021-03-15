# 재귀
import sys
sys.stdin = open('input.txt')


def solution(G):
    visited = [False for _ in range(100)]

    def dfs(v):
        visited[v] = True
        for new_v in G[v]:
            if not visited[new_v]:
                dfs(new_v)
    dfs(0)
    return int(visited[99])


T = 10
for _ in range(1, T+1):
    tc, E = input().split()
    G = [[] for _ in range(100)]
    edge_list = list(map(int, input().split()))
    for idx in range(0, len(edge_list), 2):
        fr = edge_list[idx]
        to = edge_list[idx+1]
        G[fr].append(to)

    print("#{} {}".format(tc, solution(G)))