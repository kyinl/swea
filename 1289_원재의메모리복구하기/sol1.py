import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    case = input()
    temp = '0'
    count = 0

    for idx in range(len(case)):
        if case[idx] != temp:
            temp = case[idx]
            count += 1
    print('#{} {}'.format(tc, count))