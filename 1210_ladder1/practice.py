N = 7
matrix = [
    [1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 2]
]
# 상좌우
dx = [0, -1, 1]
dy = [-1, 0, 0]

mode = 0
# 2의 위치 찾기
two_location = 0
for number in matrix[-1]:
    two_location += 1
    if number == 2:
        break
two_location -= 1
x = two_location
y = N-1

while y > 0:

    if x - 1 >= 0 and matrix[y][x-1]:
        x -= 1
        while not matrix[y-1][x]:
            x -= 1
    elif x + 1 <= N - 1 and matrix[y][x+1]:
        x += 1
        while not matrix[y-1][x]:
            x += 1
    y -= 1

print('#{} {}'.format(x, x))


# for y in range(N-1, -1, -1):
#     for x in range(N):
#         if x+1 <= N-1 and x-1 >= 0 and y+1 <= N-1:
#             if matrix[y][x+1] == 0 and matrix[y][x-1] == 0:
#                 mode = 0
#             if matrix[y][x+1] == 1:
#                 mode = 1
#             if matrix[y][x-1] == 1:
#                 mode = 2
#         if x+1 > N-1:
#             if matrix[y][x-1] == 0:
#                 mode = 0
#             if matrix[y][x-1] == 1:
#                 mode = 2
#         if x-1 < 0:
#             if matrix[y][x+1] == 0:
#                 mode = 0
#             if matrix[y][x+1] == 1:
#                 mode = 1
#         testX += dx[mode]
#         testY += dy[mode]
#     print(matrix[testY][testX])
