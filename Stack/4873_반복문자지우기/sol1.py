import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    case = list(input())
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

    print('#{} {}'.format(tc, len(case)))
