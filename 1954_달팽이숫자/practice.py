N = 3
tc = 1
result = []
matrix = [[0]*N for _ in range(N)]

# 우하좌상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

mode = 0
x = y = 0

print(matrix)
for num in range(2, N**2+1):
    x += dx[mode]
    y += dy[mode]

    matrix[y][x] = num

    if 0 <= x + dx[mode] < N and 0 <= y + dy[mode] < N and not matrix[y+dy[mode]][x+dx[mode]]:
        continue

    if mode != 3:
        mode += 1
    else:
        mode = 0

print('#{}'.format(tc))
for i in matrix:
    print(*i)