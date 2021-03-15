import sys
sys.stdin = open('sample_input.txt')


def solution(y, x):
    visited = [[False for _ in range(N)] for _ in range(N)]

    def dfs(y, x):
        visited[y][x] = True
        for new_y in range(N):
            for new_x in range(N):
                if not visited[new_y][new_x]:
                    dfs(new_y, new_x)

    #
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == dy == 0:
                continue

            cy = y + dy
            cx = x + dx
            result = False

            while 0 <= cx < N and 0 <= cy < N:
                if maze[cy][cx] == 0:
                    cy += dy
                    cx += dx
                elif maze[cy][cx] == 1:
                    solution(cy, cx)
                    break
                else:
                    result = True
    return int(result)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발점 찾기
    x = 0
    y = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x = j
                y = i

    print(maze, x, y)
    print('#{} {}'.format(tc, solution(y, x)))
