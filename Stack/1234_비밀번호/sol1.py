import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N, case = input().split()
    case = list(case)
    idx = 0

    while idx < len(case) - 1:
        if idx < 0:
            idx = 0
        elif len(case) == 1:
            break
        elif case[idx] == case[idx+1]:
            case.pop(idx)
            case.pop(idx)
            idx -= 1
            continue
        else:
            idx += 1

    print('#{} {}'.format(tc, ''.join(case)))
