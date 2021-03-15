import sys
sys.stdin = open('sample_input.txt')


dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]


def bfs():
    count = 0
    queue = []
    queue.append(start)
    while queue:
        queue_tmp = []
        while queue:
            x, y = queue.pop(0)

            for idx in range(4):
                dy, dx = dys[idx], dxs[idx]
                if 0 <= x + dx < N and 0 <= y + dy < N:
                    if not matrix[y + dy][x + dx]:
                        matrix[y + dy][x + dx] = 1
                        queue_tmp.append((x + dx, y + dy))
                    if matrix[y + dy][x + dx] == 3:
                        return count
        count += 1
        queue = queue_tmp
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                goal = (x, y)

    print('#{} {}'.format(tc, bfs()))

# https://mungto.tistory.com/166 참조.
