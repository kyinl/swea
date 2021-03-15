import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    temp = 0
    result = 0

    if len(A) > len(B):
        A, B = B, A
    idx = 0
    while idx < len(B) - len(A) + 1:
        for idx2 in range(len(A)):
            temp += A[idx2] * B[idx2 + idx]
        if temp > result:
            result = temp
        temp = 0
        idx += 1
    print('#{} {}'.format(tc, result))
