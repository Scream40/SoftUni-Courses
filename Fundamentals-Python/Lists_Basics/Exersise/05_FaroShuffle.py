cards = input().split(" ")
shuffles_count = int(input())
half_deck = len(cards) // 2

for current_shuffle in range(shuffles_count):

    top_half = []
    bottom_half = []
    shuffled_deck = []

    for i in range(len(cards)):
        if i < half_deck:
            top_half.append(cards[i] )
        else:
            bottom_half.append(cards[i] )

    for x in range(half_deck):
        shuffled_deck.append(top_half[x])
        shuffled_deck.append(bottom_half[x] )

    cards = shuffled_deck
    if current_shuffle == shuffles_count - 1:
        print(shuffled_deck)




