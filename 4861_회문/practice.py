import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]
result = ''
limited_list = []
for row in matrix:
    for idx_limit in range(N - M + 1):
        count = 0
        limited_list = row[idx_limit:M + idx_limit]
        for idx in range(M // 2):
            if limited_list[idx] == limited_list[M - idx - 1]:
                count += 1
        if count == M // 2:
            result = ''.join(row[idx_limit:idx_limit + M])


for x in range(N):
    for idx_limit in range(N - M + 1):
        count = 0
        limited_list = []
        for y in range(idx_limit, M + idx_limit):
            limited_list.append(matrix[y][x])

        for idx in range(M // 2):
            if limited_list[idx] == limited_list[M - idx - 1]:
                count += 1
        if count == M // 2:
            result = ''.join(limited_list)

print('#{} {}'.format(N, result))