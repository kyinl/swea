import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))
    ci_with_number = []
    for i in range(M):
        ci_with_number.append([ci[i], i])
    oven = [ci_with_number[i] for i in range(N)]
    left = ci_with_number[N:]
    while oven:
        a = oven.pop(0)
        a[0] //= 2
        if a[0] != 0:
            oven.append(a)
        elif a[0] == 0 and len(left) > 0:
            oven.append(left.pop(0))

        if len(oven) == 1:
            result = oven.pop(0)[1]

    print('#{} {}'.format(tc, result + 1))
