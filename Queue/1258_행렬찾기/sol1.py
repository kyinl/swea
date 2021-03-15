import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = []
    count = 0
    y = x = 0
    for y in range(n):
        for x in range(n):
            if matrix[y][x] != 0:
                tmp_x = x
                tmp_y = y
                while tmp_y < n and matrix[tmp_y][x] != 0:
                    tmp_y += 1
                while tmp_x < n and matrix[y][tmp_x] != 0:
                    tmp_x += 1
                result.append([tmp_y - y, tmp_x - x])

                # 초기화 하는 작업.
                for a in range(y, tmp_y):
                    for b in range(x, tmp_x):
                        matrix[a][b] = 0

    result.sort(key=lambda x: (x[0] * x[1], x[0]))
    print('#{} {}'.format(tc, len(result)), end=' ')
    for i in range(len(result)):
        print('{} {}'.format(result[i][0], result[i][1]), end=' ')
    print()
