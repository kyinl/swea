import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    scores = list(map(int, input().split()))
    result = []
    for score in scores:
        if score < 40:
            score = 40
        result.append(score)

    print('#{} {}'.format(tc, sum(result) // 5))
