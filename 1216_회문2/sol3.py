def my_pal(string):
    matrix = list(string)
    N = len(matrix)
    result = 0
    for M in range(N-1, -1, -1):
        for idx_slice in range(N - M + 1):
            count = 0
            sliced_list = matrix[idx_slice:M + idx_slice]
            for idx in range(M // 2):
                if sliced_list[idx] == sliced_list[M - idx - 1]:
                    count += 1
            if count == M // 2:
                result = M
                break
        if result != 0:
            break
    return result
