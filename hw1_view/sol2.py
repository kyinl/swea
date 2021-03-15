import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    # 아파트 단지의 가로 길이
    length = int(input())  # 인풋의 홀수 줄
    buildings = list(map(int, input().split()))  # 인풋의 짝수 줄

    # 조망권 확보된 집의 갯수
    total = 0
    # for idx in range(2, length-2):  # 양 끝에 2개씩 제외
    idx = 2
    while idx < length-2:
        # 5개 집
        l1, l2, current, r1, r2 = [buildings[idx+n] for n in range(-2, 3)]

        sides = [l1, l2, r1, r2]

        highest = sides[0]
        for side in sides:
            if side > highest:
                highest = side

        if current > highest:
            total += current - highest
            idx += 3 # 뒤 두개 집은 어차피 view 가 안좋음
        else:
            idx += 1

    print('#{} {}'.format(tc, total))
