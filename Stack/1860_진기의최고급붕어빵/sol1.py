import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    # 손님 도착시간을 시간순으로 정렬한다.
    times.sort()
    last = max(times)
    time = [0] * (last+1)
    current = 0
    result = 'Possible'

    for t in range(last + 1):
        if t != 0 and t % M == 0:
            current += K
            k = t
            while k < t + M:
                time[k] += current
                k += 1
                if k > len(time) - 1:
                    break

    for i in times:
        if time[i]:
            for j in range(len(time)):
                if time[j] != 0:
                    time[j] -= 1
            continue
        if not time[i]:
            result = 'Impossible'
    print('#{} {}'.format(tc, result))