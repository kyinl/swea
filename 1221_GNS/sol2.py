# 교수님 카운팅 정렬
import sys
sys.stdin = open('GNS_test_input.txt')


def solution(N, alien_list):
    aliens = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    counts = [0 for _ in range(10)]

    for a_num in alien_list:
        for idx in range(10):
            if a_num == aliens[idx]:
                counts[idx] += 1

    result = ''

    for idx in range(10):
        result += (aliens[idx] + ' ') * counts[idx]
    return result.rstrip()


T = int(input())

for tc in range(1, T+1):
    # N = int(input()[3:])
    N = int(input().split()[1])
    print("#{}\n{}".format(tc, solution(N, input().split())))