import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    x_result = 0
    for row in arr:
        x_result += min(row)
    y_result = 0
    for x in range(N):
        tmp_min = 10
        for y in range(N):
            if arr[y][x] < tmp_min:
                tmp_min = arr[y][x]
        y_result += tmp_min
    print(arr)
    print('#{} {} {}'.format(tc, x_result, y_result))
