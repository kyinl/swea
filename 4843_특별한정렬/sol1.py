import sys
sys.stdin = open('sample_input.txt')


def mini(num_list):
    tmp_mini = 2**63 - 1
    for num in num_list:
        if num < tmp_mini:
            tmp_mini = num
    return tmp_mini


def maxi(num_list):
    tmp_maxi = -2**63
    for num in num_list:
        if num > tmp_maxi:
            tmp_maxi = num
    return tmp_maxi


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    sorted_list = []

    for num in range(10):
        if num % 2:
            sorted_list.append(mini(num_list))
            num_list.remove(mini(num_list))
        else:
            sorted_list.append(maxi(num_list))
            num_list.remove(maxi(num_list))
    print('#{} {}'.format(tc, ' '.join(map(str, sorted_list))))
