# 조합을 이용한 풀이

import sys
sys.stdin = open('input.txt')


def fac(n):
    f = 1

    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            f = f * i
        return f


def comb(n, r):
    return int(fac(n) / fac(r) / fac(n - r))


def pascal(N):
    for col in range(N):
        for row in range(col+1):
            print(comb(col, row), end=' ')
        print()


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print('#{}'.format(tc))
    pascal(N)
