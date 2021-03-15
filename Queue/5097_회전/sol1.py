import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(M):
        numbers.append(numbers.pop(0))
        if i == M - 1:
            result = numbers[0]
    print('#{} {}'.format(tc, result))
