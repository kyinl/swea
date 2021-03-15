import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    result = 'NO'

    # 가로 방향
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == '.':
                continue
            if x + 4 < N and matrix[y][x] == 'o' and matrix[y][x+1] == 'o' and matrix[y][x+2] == 'o' and matrix[y][x+3] == 'o' and matrix[y][x+4] == 'o':
                result = 'YES'
                break

    # 세로 방향
    for x in range(N):
        for y in range(N):
            if matrix[y][x] == '.':
                continue
            if y + 4 < N and matrix[y][x] == 'o' and matrix[y+1][x] == 'o' and matrix[y+2][x] == 'o' and matrix[y+3][x] == 'o' and matrix[y+4][x] == 'o':
                result = 'YES'
                break

    # 대각선 우하 방향
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == '.':
                continue
            if x + 4 < N and y + 4 < N and matrix[y][x] == 'o' and matrix[y+1][x+1] == 'o' and matrix[y+2][x+2] == 'o' and matrix[y+3][x+3] == 'o' and matrix[y+4][x+4] == 'o':
                result = 'YES'
                break

    # 대각선 좌하 방향
    for y in range(N):
        for x in range(N-1, -1, -1):
            if matrix[y][x] == '.':
                continue
            if x - 4 >= 0 and y + 4 < N and matrix[y][x] == 'o' and matrix[y+1][x-1] == 'o' and matrix[y+2][x-2] == 'o' and matrix[y+3][x-3] == 'o' and matrix[y+4][x-4] == 'o':
                result = 'YES'
                break

    print('#{} {}'.format(tc, result))

