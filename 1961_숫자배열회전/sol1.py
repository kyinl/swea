import sys
sys.stdin = open('input.txt')


def r90(mat):
    result = []
    result_converted = []
    for x in range(len(mat)):
        temp = []
        for y in reversed(range(len(mat))):
            temp.append(mat[y][x])
        result.append(temp)
    for x in result:
        result_converted.append(''.join(map(str, x)))
    return result_converted


def r180(mat):
    result = []
    result_converted = []
    for y in reversed(range(len(mat))):
        temp = []
        for x in reversed(range(len(mat))):
            temp.append(mat[y][x])
        result.append(temp)
    for x in result:
        result_converted.append(''.join(map(str, x)))
    return result_converted


def r270(mat):
    result = []
    result_converted = []
    for x in reversed(range(len(mat))):
        temp = []
        for y in range(len(mat)):
            temp.append(mat[y][x])
        result.append(temp)
    for x in result:
        result_converted.append(''.join(map(str, x)))
    return result_converted


def gather(ro90, ro180, ro270):
    result = []
    for x in range(len(ro90)):
        temp = [ro90[x], ro180[x], ro270[x]]
        result.append(temp)
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = gather(r90(matrix), r180(matrix), r270(matrix))
    print('#{}'.format(tc))
    for y in range(len(result)):
        for x in range(len(result[0])):
            print(result[y][x], end=' ')
        print()

