# 앞부터 보기
# 결과는 잘 나오지만 swea 사이트에서 런타임 에러가 난다.
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    expense = 0
    max_result = 0
    count = 0
    idx = 0
    while idx < len(prices):
        if idx < len(prices) - 1:
            partial_max = max(prices[idx:])
        if idx == len(prices) - 1:
            income = prices[idx] * count - expense
        for idx2 in range(idx, len(prices)):
            if prices[idx2] == partial_max:
                income = prices[idx2] * count - expense
                count = 0
                expense = 0
                max_result += income
                idx = idx2 + 1
                break
            else:
                expense += prices[idx2]
                count += 1
                idx += 1
        if max_result < 0:
            max_result = 0
    print('#{} {}'.format(tc, max_result))
