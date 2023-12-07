import sys
from collections import Counter

hand_to_score = {
    (1, 1, 1, 1, 1): 0,
    (1, 1, 1, 2): 1,
    (1, 2, 2): 2,
    (1, 1, 3): 3,
    (2, 3): 4,
    (1, 4): 5,
    (5, ): 6
}

translate = {
    'J' : 1,
    'T' : 10,
    'Q' : 11,
    'K' : 12,
    'A' : 13
}

def evaluate_hand(hand):
    count = Counter(hand)
    joker = count[1]
    del count[1]
    
    cards = list(sorted(count.values()))
    if not cards:
        cards = (joker, )
    else:
        cards[-1] += joker
    
    return hand_to_score[tuple(cards)]


with open(sys.argv[1], 'r') as file:
    hands = map(lambda line: line.split(), file.read().split('\n'))
    trans_func = lambda card: translate[card] if card in translate else int(card)
    hands = list(map(lambda hand: [tuple(map(trans_func, hand[0])), int(hand[1])], hands))


for i, hand in enumerate(hands):
    score = evaluate_hand(hand[0])
    hands[i].append(score)

hands.sort(key=lambda hand: (hand[2], hand[0]))
total = sum(i * hand[1] for i, hand in enumerate(hands, 1))

print(total)