import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    avg = sum(income) / len(income)
    result = 0
    for num in income:
        if num <= avg:
            result += 1
    print('#{} {}'.format(tc, result))
