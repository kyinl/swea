import sys
sys.stdin = open('sample_input.txt')


def solution(N, matrix, start):
    # visited 안써도 된다.
    # else: 아래에 matrix[y][x] = 1 을 넣으면 됨.
    visited = [[False for _ in range(N)] for _ in range(N)]

    def dfs(x, y):
        # 함수 안의 함수에서 상위 함수 변경할때 nonlocal
        # nonlocal found
        global found
        visited[y][x] = True
        if matrix[y][x] == 3:
            found = 1
        else:
            dys = [-1, 1, 0, 0]
            dxs = [0, 0, -1, 1]
            for idx in range(4):
                dy, dx = dys[idx], dxs[idx]
                # 1. 이동하려는 좌표값이 0 <= x, y < N 을 만족 하는지
                # x + dy, y + dy
                if 0 <= x + dx < N and 0 <= y + dy < N:
                    # 2. 벽이 아닌가(길, 목적지, 출발지)
                    if matrix[y + dy][x + dx] != 1:
                        # 3. 방문 안했는지
                        if not visited[y + dy][x + dx]:
                            dfs(x + dx, y + dy)
    dfs(*start)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
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
