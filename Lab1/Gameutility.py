
Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def identifyHand(hand):

    rank_counts = {}

    for cards in hand:
        rank = cards[0]
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    if 3 in rank_counts.values():
        # Three of a Kind: Directly retrieve the rank with a count of 3
        three_kind_rank = [rank for rank, count in rank_counts.items() if count == 3][0]
        return 27 + Rank.index(three_kind_rank)

    elif 2 in rank_counts.values():
        # Pair: Directly retrieve the rank with a count of 2
        pair_rank = [rank for rank, count in rank_counts.items() if count == 2][0]
        return 14 + Rank.index(pair_rank)
    else:
        # High Card: Find the highest card by rank
        high_card_rank = max(rank_counts.keys(), key=lambda r: Rank.index(r))
        return Rank.index(high_card_rank) + 1
