# 뒤부터 보기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    last = prices[-1]
    income = 0
    for i in reversed(range(len(prices))):
        if last > prices[i]:
            income += last - prices[i]
        else:
            last = prices[i]
    print("#{} {}".format(tc, income))