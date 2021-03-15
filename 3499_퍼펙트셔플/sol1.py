import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())

    first_half = []
    second_half = []
    result = []

    for idx in range(len(cards)):
        if idx < len(cards) / 2:
            first_half.append(cards[idx])
        else:
            second_half.append(cards[idx])

    for idx in range(len(second_half)):
        result.append(first_half[idx])
        result.append(second_half[idx])
    if len(first_half) > len(second_half):
        result.append(first_half[-1])
    print('#{} {}'.format(tc, ' '.join(result)))
