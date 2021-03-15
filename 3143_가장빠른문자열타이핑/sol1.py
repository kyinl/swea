import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    A = list(A)
    B = list(B)
    idx_limit = len(A) - len(B) + 1
    count = 0
    result = len(A)

    idx = 0
    # 처음에 for 문으로 했다가 인덱스 건너뛰는거 고려 안해서 틀렸고, 중간에 continue 안넣어서 또 틀렸다.
    while idx <= idx_limit:
        if A[idx:len(B) + idx] == B:
            count += 1
            idx += len(B)
            continue
        idx += 1
    result -= (count * len(B) - count)

    print('#{} {}'.format(tc, result))
