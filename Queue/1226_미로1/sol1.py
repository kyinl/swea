# bfs 이용한 재귀 풀이
import sys
sys.stdin = open('input.txt')


def solution(N, matrix, start):
    visited = [[False for _ in range(N)] for _ in range(N)]

    def dfs(x, y):
        global found
        visited[y][x] = True
        if matrix[y][x] == 3:
            found = 1
        else:
            dys = [-1, 1, 0, 0]
            dxs = [0, 0, -1, 1]
            for idx in range(4):
                dy, dx = dys[idx], dxs[idx]
                if 0 <= x + dx < N and 0 <= y + dy < N and matrix[y + dy][x + dx] != 1 and not visited[y + dy][x + dx]:
                    dfs(x + dx, y + dy)
    dfs(*start)


T = 10

for tc in range(1, T+1):
    num = int(input())
    N = 16
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    found = 0
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                goal = (x, y)
    solution(N, matrix, start)
    print('#{} {}'.format(tc, found))
