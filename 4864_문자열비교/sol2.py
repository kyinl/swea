import sys
sys.stdin = open("input.txt")

def 브루트포스1(p, t):
    # for 문

    for i in range(len(t)-len(p)+1):
        # 패턴의 길이만큼 반복
        for j in range(len(p)):
            if p[j] != t[i+j]:
                break
        else:
            return 1

    return 0

T = int(input())


def 브루트포스2(p, t):
    i = 0  # t 텍스트를 컨트롤 하는 인덱스
    j = 0  # p 패턴을 컨트롤 하는 인덱스

    # j가 패턴의 길이가 된다면 찾았다면 멈춘다.
    # i가 텍스트의 길이가 된다면 멈춘다.
    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            i = i-j  # 시작 위치로 돌아가고
            j = -1

        i += 1
        j += 1

    if j == len(p):
        return 1
    else:
        return 0



for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print(브루트포스1(str1, str2))