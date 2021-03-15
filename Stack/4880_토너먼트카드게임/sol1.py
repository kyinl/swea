import sys
sys.stdin = open('sample_input.txt')


def regroup(group):
    if len(group) == 1:
        return group
    else:
        return regroup()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
