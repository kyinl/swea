import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # NxN 퍼즐, K 길이의 단어
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    # 가로만 계산
    for y in range(N):
        count_tmp = 0
        for x in range(N):
            if puzzle[y][x] == 1:
                count_tmp += 1
            if puzzle[y][x] == 0:
                count_tmp = 0
            if count_tmp == K:
                if x + 1 > N - 1:
                    count += 1
                    break
                if puzzle[y][x + 1] != 1:
                    count += 1

    # 전치 행렬
    for i in range(N):
        for j in range(N):
            if i < j:
                puzzle[i][j], puzzle[j][i] = puzzle[j][i], puzzle[i][j]

    # 전치 행렬에서 다시 계산
    for y in range(N):
        count_tmp = 0
        for x in range(N):
            if puzzle[y][x] == 1:
                count_tmp += 1
            if puzzle[y][x] == 0:
                count_tmp = 0
            if count_tmp == K:
                if x + 1 > N - 1:
                    count += 1
                    break
                if puzzle[y][x + 1] != 1:
                    count += 1
    print('#{} {}'.format(tc, count))
