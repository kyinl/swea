import sys
sys.stdin = open('input.txt')


def solution(N, matrix):
    sub_matrix = []
    # 행 우선탐색
    for y in range(N):
        for x in range(N):
            if matrix[y][x]:
                # 좌상단 찾기
                lt = (x, y)
                dx = dy = 0
                while 0 <= x + dx + 1 < N and matrix[y][x+dx+1]:
                    dx += 1
                while 0 <= y + dy + 1 < N and matrix[y+dy+1][x]:
                    dy += 1
                # 우하단 찾기
                rb = (x + dx, y + dy)
                # (열길이, 행길이) 를 sub_matrix 에 추가
                sub_matrix.append((rb[1]-lt[1]+1, rb[0]-lt[0]+1))
                # 확인한 부분행렬 삭제
                for ry in range(y, y + dy + 1):
                    for rx in range(x, x + dx + 1):
                        matrix[ry][rx] = 0

    # (row * col) 결과로 선택정렬
    # 면적이 같은 경우 처리하는 과정이 빠져있지만, 통과가 된다.
    length = len(sub_matrix)
    for i in range(length-1):
        min_idx = i
        for j in range(i+1, length):
            y1, x1 = sub_matrix[min_idx]
            y2, x2 = sub_matrix[j]
            if x1 * y1 > x2 * y2:
                min_idx = j
        sub_matrix[i], sub_matrix[min_idx] = sub_matrix[min_idx], sub_matrix[i]

    return str(length) + ' ' + ' '.join(map(lambda t: ' '.join(map(str, t)), sub_matrix))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, solution(N, matrix)))
