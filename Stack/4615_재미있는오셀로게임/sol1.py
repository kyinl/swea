import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    game = [list(map(int, input().split())) for _ in range(M)]
    # 게임 시작 전의 board 제작
    board = [[0] * N] * (N // 2 - 1)
    bottom = [[0] * N] * (N // 2 - 1)
    center = [[2, 1], [1, 2]]
    center = [[0]*(N//2 - 1) + center[0] + [0]*(N//2 - 1), [0]*(N//2 - 1) + center[1] + [0]*(N//2 - 1)]
    board.extend(center)
    board.extend(bottom)

    # game 에 저장된 돌을 두는 좌표를 index 와 일치시키기 위해 각각 -1 해줌
    for turn in game:
        turn[0] -= 1
        turn[1] -= 1
    for turn in game:
        board[turn[1]][turn[0]] = turn[2]
        # 검사
        y = turn[1]
        x = turn[0]
        # 하단
        if y < len(board) - 2:
            y = turn[1]
            x = turn[0]
            count = 0
            while y < len(board):
                if y + 1 >= len(board):
                    break
                if board[y + 1][x] == 0:
                    break
                if board[y + 1][x] != turn[2] and board[y + 1][x] != 0:
                    count += 1
                if board[y + 1][x] == turn[2]:
                    for c in range(count):
                        board[y - c][x] = turn[2]
                y += 1

        # 우측
        y = turn[1]
        x = turn[0]
        count = 0
        if x < len(board) - 2:

            while x < len(board):
                if x + 1 >= len(board):
                    break
                if board[y][x + 1] == 0:
                    break
                if board[y][x + 1] != turn[2] and board[y][x + 1] != 0:
                    count += 1
                if board[y][x + 1] == turn[2]:
                    for c in range(count):
                        board[y][x - c] = turn[2]
                x += 1
        # 상단
        y = turn[1]
        x = turn[0]
        count = 0
        if 2 <= y:

            while 0 <= y:
                if 0 > y - 1:
                    break
                if board[y - 1][x] == 0:
                    break
                if board[y - 1][x] != turn[2] and board[y - 1][x] != 0:
                    count += 1
                if board[y - 1][x] == turn[2]:
                    for c in range(count):
                        board[y + c][x] = turn[2]
                y -= 1
        # 좌측
        y = turn[1]
        x = turn[0]
        count = 0
        if 2 <= x:

            while 0 <= x:
                if 0 > x - 1:
                    break
                if board[y][x - 1] == 0:
                    break
                if board[y][x - 1] != turn[2] and board[y][x - 1] != 0:
                    count += 1
                if board[y][x - 1] == turn[2]:
                    for c in range(count):
                        board[y][x + c] = turn[2]
                x -= 1
        # 우하
        y = turn[1]
        x = turn[0]
        count = 0
        if y < len(board) - 2 and x < len(board) - 2:

            while y < len(board) and x < len(board):
                if y + 1 >= len(board):
                    break
                if x + 1 >= len(board):
                    break
                if board[y + 1][x + 1] == 0:
                    break
                if board[y + 1][x + 1] != turn[2] and board[y + 1][x + 1] != 0:
                    count += 1
                if board[y + 1][x + 1] == turn[2]:
                    for c in range(count):
                        board[y - c][x - c] = turn[2]
                y += 1
                x += 1

        # 좌하
        y = turn[1]
        x = turn[0]
        count = 0
        if y < len(board) - 2 and 2 <= x:

            while y < len(board) and 0 <= x:
                if y + 1 >= len(board):
                    break
                if 0 > x - 1:
                    break
                if board[y + 1][x - 1] == 0:
                    break
                if board[y + 1][x - 1] != turn[2] and board[y + 1][x - 1] != 0:
                    count += 1
                if board[y + 1][x - 1] == turn[2]:
                    for c in range(count):
                        board[y - c][x + c] = turn[2]
                y += 1
                x -= 1
        # 우상
        y = turn[1]
        x = turn[0]
        count = 0
        if 2 <= y and x < len(board) - 2:

            while 0 <= y and x < len(board):
                if 0 > y - 1:
                    break
                if x + 1 >= len(board):
                    break
                if board[y - 1][x + 1] == 0:
                    break
                if board[y - 1][x + 1] != turn[2] and board[y - 1][x + 1] != 0:
                    count += 1
                if board[y - 1][x + 1] == turn[2]:
                    for c in range(count):
                        board[y + c][x - c] = turn[2]
                y -= 1
                x += 1
        # 좌상
        y = turn[1]
        x = turn[0]
        count = 0
        if 2 <= y and 2 <= x:

            while 0 <= y and 0 <= x:
                if 0 > y - 1:
                    break
                if 0 > x - 1:
                    break
                if board[y - 1][x - 1] == 0:
                    break
                if board[y - 1][x - 1] != turn[2] and board[y - 1][x - 1] != 0:
                    count += 1
                if board[y - 1][x - 1] == turn[2]:
                    for c in range(count):
                        board[y + c][x + c] = turn[2]
                y -= 1
                x -= 1

    count_1 = count_2 = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 1:
                count_1 += 1
            if board[y][x] == 2:
                count_2 += 1
    print('#{} {} {}'.format(tc, count_1, count_2))