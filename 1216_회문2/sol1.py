import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc_number = input()
    N = 100
    matrix = [list(input()) for _ in range(N)]
    result = 0
    final = 0
    limited_list = []

    for M in range(N):
        for row in matrix:
            for idx_limit in range(N - M + 1):
                count = 0
                limited_list = row[idx_limit:M + idx_limit]
                for idx in range(M // 2):
                    if limited_list[idx] == limited_list[M - idx - 1]:
                        count += 1
                if count == M // 2:
                    result = M
                if result > final:
                    final = result

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
                    result = M
                if result > final:
                    final = result

    print('#{} {}'.format(tc, final))
