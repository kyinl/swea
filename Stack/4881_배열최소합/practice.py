import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for x in range(N):
        tmp_sum = 0
        for y in range(N):
            for x in range(N):
                pass
