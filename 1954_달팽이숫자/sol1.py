import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 0으로 채워진 matrix 선언
    matrix = [[0] * N for _ in range(N)]

    # 우하좌상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 사용할 변수들 선언
    mode = x = y = 0

    # 1행 1열의 값 1로 초기화
    matrix[0][0] = 1
    # 오름차순으로 2부터 N**2 + 1까지 총 N**2 - 1개
    for num in range(2, N ** 2 + 1):
        # 모드에 해당하는 방향으로 이동
        x += dx[mode]
        y += dy[mode]
        # 현재의 num 값을 이동한 위치에 넣는다
        matrix[y][x] = num
        # 만약 현재의 방향으로 한번 더 이동한다고 가정했을 때,
        # index range 를 벗어나지 않거나,
        # 이미 0이 아닌 숫자가 채워져 있지 않다면 continue
        if 0 <= x + dx[mode] < N and 0 <= y + dy[mode] < N and matrix[y + dy[mode]][x + dx[mode]] == 0:
            continue
        # 벗어나거나 0이 아닌 숫자가 채워져 있다면 모드 + 1, 모드가 3일때만 0으로 변경
        if mode != 3:
            mode += 1
        else:
            mode = 0

    print('#{}'.format(tc))
    for i in matrix:
        print(*i)