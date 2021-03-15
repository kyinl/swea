import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    total = 0
    # y방향 인덱스 기준 0부터 중간값까지 계산 : 슬라이싱 이용
    for y in range(N // 2 + 1):
        total += sum(farm[y][N // 2 - y:N // 2 + 1 + y])
    # 중간값 + 1 부터 끝까지 계산
    for y in range(N // 2 + 1, N):
        total += sum(farm[y][N // 2 - (N - y - 1):N // 2 + 1 + (N - y - 1)])
    print('#{} {}'.format(tc, total))


