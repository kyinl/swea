def checker(y, x, color):

    board[y][x] = color

    # 9방향 델타이동
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            # 단 지금 돌을 둔 위치는 볼 필요가 없지
            if dx == dy == 0:
                continue

            # 현재 탐색 방향 일직선 안에서 지금 둔 돌과 색이 같고,
            # 동시에 사이에 다른 돌이 낀 돌의 좌표(cx, cy)를 찾아나서자
            cy = y + dy
            cx = x + dx
            found = False

            # 게임판 범위 내에서
            while 0 <= cx < N and 0 <= cy < N:
                # 내 돌과 다른색 돌이 나온다면 계속 전진
                if board[cy][cx] == 3 - color:
                    cy += dy
                    cx += dx
                # 하다가, 같은색이 나왔다면 STOP!
                elif board[cy][cx] == color:
                    found = True
                    break
                # 빈칸이 나오면 그냥 정지!
                else:
                    break

            # 찾았다면 x, y 부터 cx, cy 까지 이동하며 색을 칠하자!
            if found:
                # px, py 는 이동할 때 쓸 idx
                # x ~ px ~ cx / y ~ py ~ cy
                px, py = x + dx, y + dy
                while px != cx or py != cy:
                    board[py][px] = color
                    px += dx
                    py += dy


T = int(input())
for tc in range(1, T+1):
    N, turns = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    # 보드 중앙 4칸에 색칠
    board[N//2-1][N//2] = board[N//2][N//2-1] = 1
    board[N//2-1][N//2-1] = board[N//2][N//2] = 2

    for _ in range(turns):
        x, y, color = map(int, input().split())
        checker(y-1, x-1, color)

    black = white = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                black += 1
            elif board[y][x] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))
