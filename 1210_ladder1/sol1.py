import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    num = int(input())
    N = 100
    matrix = [
        list(map(int,input().split())) for _ in range(N)
    ]
    # 2의 위치 찾기
    two_location = 0
    for number in matrix[-1]:
        two_location += 1
        if number == 2:
            break
    two_location -= 1
    # 출발지점의 x, y좌표
    x = two_location
    y = N - 1

    while y > 0:
        # 왼쪽으로 가는 경우
        if x - 1 >= 0 and matrix[y][x - 1] == 1:
            x -= 1
            # 위의 칸이 0이면 계속 간다
            while matrix[y - 1][x] == 0:
                x -= 1
        # 오른쪽으로 가는 경우
        elif x + 1 <= N - 1 and matrix[y][x + 1] == 1:
            x += 1
            # 위의 칸이 0이면 계속 간다
            while matrix[y - 1][x] == 0:
                x += 1
        # x좌표 이동 끝나면 위로 한칸
        y -= 1

    print('#{} {}'.format(tc, x))