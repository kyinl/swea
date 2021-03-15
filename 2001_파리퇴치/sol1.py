import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # NxN 영역, MxM 파리채
    N, M = map(int, input().split())
    fly_list = []

    for y in range(N):
        fly_list.append(list(map(int, input().split())))

    result_max = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            result = 0
            for my in range(M):
                for mx in range(M):
                    result += fly_list[y+my][x+mx]
            if result > result_max:
                result_max = result
    print('#{} {}'.format(tc, result_max))
