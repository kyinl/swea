import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    deck = input()
    deck_converted = []
    is_error = ''
    result = ''
    S = D = H = C = 13

    idx = 0
    while idx < len(deck) - 2:
        deck_converted.append(deck[idx:idx+3])
        idx += 3

    for card in deck_converted:
        count = 0
        for index in range(len(deck_converted)):
            if card == deck_converted[index]:
                count += 1
                if count > 1:
                    is_error = 'ERROR'

        for sdhc in card:
            if sdhc[0] == 'S':
                S -= 1
            elif sdhc[0] == 'D':
                D -= 1
            elif sdhc[0] == 'H':
                H -= 1
            elif sdhc[0] == 'C':
                C -= 1

    if is_error == 'ERROR':
        result = 'ERROR'
    else:
        result = ' '.join(map(str, [S, D, H, C]))
    print('#{} {}'.format(tc, result))