import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, list(input())))

    most_frequent_card = 0
    number_of_cards = 0
    count = 0
    for idx in range(len(cards)):
        for card in cards:
            if card == cards[idx]:
                count += 1
        if count == number_of_cards:
            if most_frequent_card < cards[idx]:
                most_frequent_card = cards[idx]
        if count > number_of_cards:
            most_frequent_card = cards[idx]
            number_of_cards = count
        count = 0
    print('#{} {} {}'.format(tc, most_frequent_card, number_of_cards))
