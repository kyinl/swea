import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    case = list(input())

    count = 0
    for string in case:
        if string == '(':
            count += 1
        if string == '{':
            count += 1
        if string == ')':
            count -= 1
        if string == '}':
            count -= 1

    if count == 0:
        count = 1
    elif count != 0:
        count = 0

    print('#{} {}'.format(tc, count))
