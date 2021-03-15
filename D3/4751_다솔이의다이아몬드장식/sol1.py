import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    char_list = list(input())
    first = []
    second = []
    third = []
    for idx in range(len(char_list)):
        if idx == 0:
            first.append('..#..')
        else:
            first.append('.#..')

    for idx in range(len(char_list)):
        if idx == 0:
            second.append('.#.#.')
        else:
            second.append('#.#.')

    for idx in range(len(char_list) * 2 + 1):
        if not idx % 2:
            if idx == 0:
                third.append('#.')
            elif idx == len(char_list) * 2:
                third.append('.#')
            else:
                third.append('.#.')
        else:
            third.append(char_list[idx//2])

    print(''.join(first))
    print(''.join(second))
    print(''.join(third))
    print(''.join(second))
    print(''.join(first))
