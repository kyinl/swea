import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    no = int(input())
    number = list(map(int, input().split()))
    i = 1
    while number[0] >= 0:
        # < 0으로 했다가 다르게 나와서 헤맸다.
        if number[0] - i <= 0:
            number.pop(0)
            number.append(0)
            break
        number.append(number.pop(0) - i)
        i += 1
        if i == 6:
            i = 1
    print('#{} {}'.format(tc, ' '.join(map(str, number))))


