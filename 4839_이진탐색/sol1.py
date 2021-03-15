import sys
sys.stdin = open('sample_input.txt')


def binary_search(P, A):
    l = 1
    r = P
    count = 0

    while l <= r:
        c = int((l+r)/2)
        count += 1
        if c == A:
            return count
        elif c < A:
            l = c
        elif c > A:
            r = c
    return None


T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    win = 0

    if binary_search(P, A) > binary_search(P, B):
        win = 'B'
    if binary_search(P, A) < binary_search(P, B):
        win = 'A'
    print('#{} {}'.format(tc, win))
