import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    # * 인풋 처리 *

    # [A_i, B_i]를 담을 2차원 리스트 bus_list 선언
    bus_list = []
    # C 아래로 input 되는 C_i들을 담을 리스트 C_list 선언
    C_list = []

    N = int(input())
    for i in range(1, N+1):
        AB = list(map(int, input().split()))
        bus_list.append(AB)
    C = int(input())

    # 결과를 담을 길이 C짜리 리스트 result_list 선언
    result_list = [0] * C

    for _ in range(1, C+1):
        C_list.append(int(input()))

    # * 문제 풀이 *

    # bus_list 안의 AB 리스트들
    for AB_i in bus_list:
        # C_list 는 인덱스로 접근
        for idx in range(len(C_list)):
            # 만약 C_i 가 A_i와 B_i의 범위 내에 있다면
            if C_list[idx] in range(AB_i[0], AB_i[1]+1):
                # result_list 의 해당 인덱스 값에 +1을 해준다.
                result_list[idx] += 1
    print('#{} {}'.format(tc, ' '.join(list(map(str, result_list)))))
