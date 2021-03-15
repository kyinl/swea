import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

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
    maximum = 0
    for num in sum_list:
        if maximum < num:
            maximum = num
    print('#{} {}'.format(tc, maximum))
