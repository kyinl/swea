import sys
sys.stdin = open('input.txt')

# 세로길이, 가로길이 순으로 출력
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = []
    rows = []
    cols = []
    row = 0  # 세로길이
    col = 0  # 가로길이
    for y in range(n):
        xs = []
        for x in range(n):
            if matrix[y][x] != 0:
                col += 1
                xs.append(x)
            if matrix[y][x] == 0 and row != 0:
                rows.append(row)
                col = 0
                row = 0

