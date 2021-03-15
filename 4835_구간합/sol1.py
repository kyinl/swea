import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    numbers = list(map(int, input().split()))

    subtotal = 0
    subtotal_min = 10000 * N
    subtotal_max = 0

    for idx in range(len(numbers) - M + 1):
        for i in range(M):
            subtotal += numbers[idx + i]
        if subtotal > subtotal_max:
            subtotal_max = subtotal
        if subtotal < subtotal_min:
            subtotal_min = subtotal
        subtotal = 0
    print('#{} {}'.format(tc, subtotal_max - subtotal_min))
