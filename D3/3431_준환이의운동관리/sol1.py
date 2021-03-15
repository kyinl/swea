import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    result = 0
    if X > U:
        result = -1
    elif X > L:
        result = 0
    else:
        result = L - X
    print('#{} {}'.format(tc, result))
