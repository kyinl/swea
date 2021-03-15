import sys
sys.stdin = open('input.txt')

T = int(input())
result = 0

for tc in range(1, T+1):
    # 띄어쓰기 없는 string 값들은 list 처리하면 된다.
    numbers = list(map(int, list(input())))

    tmp_list = [0] * 10

    for idx in range(len(numbers)):
        tmp_list[numbers[idx]] += 1

    # triplet 검사
    triplet = 0
    for idx in range(len(tmp_list)):
        if tmp_list[idx] == 6:
            triplet += 2
            tmp_list[idx] -= 6
        if tmp_list[idx] >= 3:
            triplet += 1
            tmp_list[idx] -= 3
    # run 검사
    run_count = 0
    for idx in range(len(tmp_list)):
        if idx >= len(tmp_list) - 2:
            continue
        if tmp_list[idx] == 2 and tmp_list[idx+1] == 2 and tmp_list[idx+2] == 2:
            run_count += 2
            tmp_list[idx] -= 2
            tmp_list[idx + 1] -= 2
            tmp_list[idx + 2] -= 2
        if tmp_list[idx] and tmp_list[idx + 1] and tmp_list[idx + 2]:
            run_count += 1
            tmp_list[idx] -= 1
            tmp_list[idx+1] -= 1
            tmp_list[idx+2] -= 1

    if run_count + triplet == 2:
        result = 1
    print('#{} {}'.format(tc, result))
    result = 0
# while - continue (반복문 처음으로 되돌아감) 문을 이용해 index 올라가지 않고 계속 검사하게 할 수 있다.
