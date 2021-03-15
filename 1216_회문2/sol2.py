# 길이가 긴 회문부터 찾으면서 찾으면 for 를 강제종료하도록 변형해 봤다.
# 실행시간이 아주 미미하게 줄어들었다.
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc_number = input()
    N = 100
    matrix = [list(input()) for _ in range(N)]
    result_row = 0
    result_column = 0
    final = 0
    limited_list = []

    for M in range(N-1, -1, -1):
        for row in matrix:
            for idx_limit in range(N - M + 1):
                count = 0
                limited_list = row[idx_limit:M + idx_limit]
                for idx in range(M // 2):
                    if limited_list[idx] == limited_list[M - idx - 1]:
                        count += 1
                if count == M // 2:
                    result_row = M
                    break
            if result_row != 0:
                break
        if result_row != 0:
            break

    for M in range(N - 1, -1, -1):
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
                    result_column = M
                    break
            if result_column != 0:
                break
        if result_column != 0:
            break

    if result_row > result_column:
        final = result_row
    else:
        final = result_column
    print('#{} {}'.format(tc, final))
