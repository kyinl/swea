import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area_list = []
    red_list = []
    blue_list = []
    count = 0

    for area in range(1, N+1):
        tmp_list = list(map(int, input().split()))
        area_list.append(tmp_list)
    for area in area_list:
        for y in range(area[1], area[3]+1):
            for x in range(area[0], area[2]+1):
                if area[4] == 1:
                    red_list.append([x, y])
                else:
                    blue_list.append([x, y])

    for area in red_list:
        if area in blue_list:
            count += 1
    print('#{} {}'.format(tc, count))
