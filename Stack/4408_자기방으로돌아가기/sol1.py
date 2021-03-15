# 잘 모르겠다.
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N)]
    count = [0] * 400
    for i in range(N):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]
        if not students[i][0] % 2:
            students[i][0] += 1
        if students[i][1] % 2:
            students[i][1] += 1
        for j in range(students[i][0], students[i][1]):
            count[j] += 1
    print('#{} {}'.format(tc, max(count)))