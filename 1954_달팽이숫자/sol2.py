# 교수님 방법
# ㄱ ㄴ으로 처리
import sys
sys.stdin = open("input.txt")

T = int(input())


def solution(N):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    # ㄱ은 인덱스가 +만 되고, ㄴ은 인덱스가 -만 된다.
    number = 1
    x = y = 0
    idx_move = +1

    for i in range(N, 0, -1):
        if i == 1:
            matrix[y][x] = number
        else:
            for k in range(i):
                matrix[y][x] = number
                number += 1
                # 틀어지는 시점
                if k == i - 1:
                    # 다음에 가야할 곳을 미리 가놓는다.
                    y += idx_move
                else:
                    x += 1
            for k in range(i-1):
                matrix[y][x] = number
                number += 1
                if k == i - 2:
                    idx_move *= -1
                    # 다음에 가야할 곳을 미리 가놓는다.
                    x += idx_move
                else:
                    y += idx_move
    return '\n'.join([' '.join(map(str, row)) for row in matrix])


for tc in range(1, T+1):
    N = int(input())

    print('#{} {}'.format(tc, solution(N)))
