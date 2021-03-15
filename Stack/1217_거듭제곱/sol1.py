import sys
sys.stdin = open('input.txt')


def square(N, M):
    if M == 1:
        return N * M
    else:
        return N * square(N, M-1)


T = 10

for tc in range(1, T+1):
    num = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, square(N, M)))
