import sys
sys.stdin = open('1_input_sample.txt')

T = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']
for tc in range(1, T+1):
    string = input()
    string_list = list(string)
    result = []
    for letter in string_list:
        if letter not in vowels:
            result.append(letter)
    result = ''.join(result)
    print('#{} {}'.format(tc, result))
