import sys
sys.stdin = open('input.txt')

# input 은 총 20줄
T = 20

for tc in range(1, T+1):

    buildings = list(map(int, input().split()))
    # 사용할 변수들 선언
    count = 0
    count_tmp_1 = 0
    count_tmp_2 = 0
    count_tmp_3 = 0
    count_tmp_4 = 0
    tmp_list = []

    for idx in range(len(buildings)):
        # 인덱스가 0, 1, -1, -2면 넘어간다.
        if idx == 0 or idx == 1 or idx == len(buildings) - 1 or idx == len(buildings) - 2:
            continue
        # 현재 건물의 높이에서 앞뒤로 2 건물의 높이를 빼준다.
        count_tmp_1 = buildings[idx] - buildings[idx - 1]
        count_tmp_2 = buildings[idx] - buildings[idx - 2]
        count_tmp_3 = buildings[idx] - buildings[idx + 1]
        count_tmp_4 = buildings[idx] - buildings[idx + 2]
        # 만약 모든 높이 차이가 양수라면
        if count_tmp_1 > 0 and count_tmp_2 > 0 and count_tmp_3 > 0 and count_tmp_4 > 0:
            tmp_list = [count_tmp_1, count_tmp_2, count_tmp_3, count_tmp_4]
            # 그 차이의 최솟값을 count 에 축적한다.
            # 주어진 조건에서 건물의 최대 높이는 255이므로 초기 minimum 값을 256으로 잡았다.
            minimum = 256
            for count_tmp in tmp_list:
                if count_tmp < minimum:
                    minimum = count_tmp
            # 임시 변수들을 재사용하기 위해 0으로 초기화
            count_tmp_1 = 0
            count_tmp_2 = 0
            count_tmp_3 = 0
            count_tmp_4 = 0
            count += minimum
    # count 가 0이 아닌 경우만
    if count != 0:
        # test case 번호는 홀수행에 존재하므로 2로 나눈 몫을 출력해준다.
        print('#{} {}'.format(tc // 2, count))
