matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum_list = []
tmp_list = []
# 우, 하, 우하, 좌하
dx = [1, 0, 1, -1]
dy = [0, 1, 1, 1]
mode = 0

for y in range(len(matrix)):
    tmp_sum = 0
    testX = 0
    testY = 0
    for x in range(len(matrix[0])):
        if tmp_sum == 0:
            tmp_sum += matrix[y][x]

        testX = x + dx[mode]
        testY = y + dy[mode]

        if 0 <= x + dx[mode] < len(matrix) and 0 <= y + dy[mode] < len(matrix):
            tmp_sum += matrix[testY][testX]
            continue
        sum_list.append(tmp_sum)

mode += 1
for x in range(len(matrix)):
    tmp_sum = 0
    testX = 0
    testY = 0
    for y in range(len(matrix[0])):
        if tmp_sum == 0:
            tmp_sum += matrix[y][x]

        testX = x + dx[mode]
        testY = y + dy[mode]

        if 0 <= x + dx[mode] < len(matrix) and 0 <= y + dy[mode] < len(matrix):
            tmp_sum += matrix[testY][testX]
            continue
        sum_list.append(tmp_sum)


mode += 1
for y in range(len(matrix)):
    tmp_sum = 0
    testX = 0
    testY = 0
    for x in range(len(matrix[0])):
        if tmp_sum == 0:
            tmp_sum += matrix[y][x]

        testX += dx[mode]
        testY += dy[mode]

        if 0 <= x + dx[mode] < len(matrix) and 0 <= y + dy[mode] < len(matrix):
            tmp_sum += matrix[testY][testX]
            continue
        sum_list.append(tmp_sum)
    break

mode += 1
for y in range(len(matrix)):
    tmp_sum = 0
    testX = 0
    testY = 0
    for x in range(len(matrix[0]) - 1, -1, -1):
        if tmp_sum == 0:
            tmp_sum += matrix[y][x]

        testX = x + dx[mode]
        testY += dy[mode]

        if 0 <= x + dx[mode] < len(matrix) and 0 <= y + dy[mode] < len(matrix):
            tmp_sum += matrix[testY][testX]
            continue
        sum_list.append(tmp_sum)
    break

print(sum_list)
