import sys
sys.stdin = open('sample_input.txt')

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    n = len(A)
    total_list = []
    count = 0
    for i in range(1 << n):
        tmp_list = []
        for j in range(n + 1):
            if i & (1 << j):
                tmp_list.append(A[j])
        total_list.append(tmp_list)
    for sub_list in total_list:
        if len(sub_list) == N:
            if sum(sub_list) == K:
                count += 1
    print('#{} {}'.format(tc, count))
