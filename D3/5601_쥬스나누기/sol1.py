import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = input()
    print('#{}'.format(tc), end=' ')
    for _ in range(int(N)):
        print('1/'+N, end=' ')
    print()
