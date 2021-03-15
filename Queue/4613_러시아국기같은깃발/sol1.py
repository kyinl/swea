import sys
sys.stdin = open('sample_input.txt')


def perm(idx, sub_sum):
    # 유망성 검사 아래의 조건문에 걸리게 되면
    # 이후 작업은 의미가 없음.
    global ans
    if sub_sum > N:
        return
    if idx == 3:
        if sub_sum == N:
            cnt = 0

            st = sel[0]
            st2 = st + sel[1]

            # 흰색 칠하기
            for i in flag[:st]:
                for j in i:
                    if j != 'W':
                        cnt += 1
            # 파란색 칠하기
            for i in flag[st:st2]:
                for j in i:
                    if j != 'B':
                        cnt += 1

            for i in flag[st2:]:
                for j in i:
                    if j != 'R':
                        cnt += 1

            if ans>cnt:
                ans = cnt

        return
    # 중복순열 살짝응용
    for i in range(1, N-1):
        sel[idx] = i
        perm(idx+1, sub_sum+i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    flag = [list(input()) for _ in range(N)]
    sel = [0] * 3
    ans = 987654321

    perm(0, 0)

    print('#{} {}'.format(tc, ans))
