import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    case = input()
    current_pipe = 0
    count = 0

    idx = 0
    while idx < len(case):
        # 만약 ( 를 만나면 현재 파이프갯수 +1
        if case[idx] == '(':
            current_pipe += 1
        # 만약 ) 를 만나면 현재 파이프갯수 -1, 파이프가 끝났기 때문에 조각수 +1
        # 주어진 조건 상, 잘라지지 않는 파이프는 존재하지 않는다
        # 논리의 흐름 상, 파이프가 끝난다는 의미의 ) 보다 () 를 먼저 만나게 되지만,
        # 프로그램 순서 상, 이전 번 루프에 () 를 건너뛰었음에도 불구하고 ) 를 만났다는 의미이기 때문에 이것을 먼저 실행
        if case[idx] == ')':
            current_pipe -= 1
            count += 1
        # 만약 ()를 만나면 ( 를 거쳐서 +1을 한 상태이기 때문에 다시 1을 빼주고
        # 인덱스를 1 건너뛴 후, 현재 파이프의 갯수를 더해준다
        if idx < len(case) - 1 and case[idx] + case[idx + 1] == '()':
            current_pipe -= 1
            idx += 1
            count += current_pipe
        idx += 1

    print('#{} {}'.format(tc, count))

