# dp로 풀기
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    dp = [1, 3]

    for i in range(2, N // 10):
        dp.append(dp[i-1] + dp[i-2]*2)

    print('#{} {}'.format(tc, dp[-1]))
