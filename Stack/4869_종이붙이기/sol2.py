# 재귀로 풀기
import sys
sys.stdin = open('sample_input.txt')


def paper(N):
    if N == 0:
        return 0
    elif N == 10:
        return 1
    elif N == 20:
        return 3
    return paper(N-10) + 2*paper(N-20)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print('#{} {}'.format(tc, paper(N)))
