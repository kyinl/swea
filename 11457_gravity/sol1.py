import sys
sys.stdin = open('input.txt')
# 각 상자 우측에 존재하는 빈칸의 최댓값이 곧 정답이다.
T = int(input())
# 우측에 있는 빈칸의 갯수들을 담을 리스트 생성
empty_count_list = []
for tc in range(2*T):
    boxes = list(map(int, input().split()))
    # 빈칸의 갯수를 담을 변수 선언
    empty_count = 0
    # 빈칸의 최댓값을 담을 변수 선언
    empty_count_maximum = 0
    for idx in range(len(boxes)):
        # 각 인덱스 경우마다 0으로 초기화한다.
        empty_count = 0
        # 각 인덱스 경우마다, 본인보다 인덱스 넘버가 높은 경우만 고려하면 된다.
        for idx_2 in range(idx + 1, len(boxes)):
            # 만약 idx 본인에 해당하는 상자 높이가 idx_2에 해당하는 상자 높이보다 높다면
            if boxes[idx] - boxes[idx_2] > 0:
                # 빈 상자의 갯수를 하나 추가한다.
                empty_count += 1
        # 최댓값을 구하기 위해 리스트에 넣어준다.
        empty_count_list.append(empty_count)
        # 최댓값을 구하는 과정
        for empty_count in empty_count_list:
            if empty_count > empty_count_maximum:
                empty_count_maximum = empty_count
    # 다음 반복을 위해 리스트 비우기
    empty_count_list = []
    # 최대값이 0이 아닌 경우만
    if empty_count_maximum != 0:
        print('#{} {}'.format(tc // 2 + 1, empty_count_maximum))
