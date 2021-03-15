farm = [[1, 4, 0, 5, 4], [4, 4, 2, 5, 0], [0, 2, 0, 3, 2], [5, 1, 2, 0, 4], [5, 2, 2, 1, 2]]
N = len(farm)
total = 0
for y in range(N // 2 + 1):
    print(farm[y][N//2 + 1 - y:N//2 + y])
for y in range(N//2 + 1, N):
    print(farm[y][N//2 + 1 - (N - y):N//2 + 1 + (N - y)])
