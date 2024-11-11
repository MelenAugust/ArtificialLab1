# identify if there is one or more pairs in the hand
import random
from Poker_agents import RandomAgent,FixedAgent,ReflexAgent
from Gameutility import game_round,identifyHand,Rank

Suit = ["s", "h", "d", "c"]
card_amount = 3
Total_pot = 0
Player1_total_winnings = 0
Player2_total_winnings = 0
Total_rounds = 50
deck = []
hand1 = []
hand2 = []


player1 = ReflexAgent(hand = [])
player2 = RandomAgent(hand = [])

# Randomly generate two hands of n cards
def generate_2hands(deck,card_amount):
    random.shuffle(deck)

    player1.hand = [deck.pop(0) for _ in range(card_amount)]
    player2.hand = [deck.pop(0) for _ in range(card_amount)]

    return hand1, hand2

# identify hand category using IF-THEN rule





# Print out the result



#########################
#      Game flow        #
#########################
for round_num in range(50):  # Repeat for 50 hands
    # Reset the pot for each round
    game_round = round_num
    Total_pot = 0
    deck.clear()

    for rank in Rank:
        for suit in Suit:
            deck.append(rank + suit)

    #########################
    # phase 1: Card Dealing #
    #########################
    print("                                    Round " + str(round_num + 1))
    hand1,hand2 = generate_2hands(deck,card_amount)
    print("Player1 hand: " + str(player1.hand))
    print("Player2 hand: " + str(player2.hand))
    print("\n")
    print("Player1 actual handvalue: " + str(identifyHand(player1.hand)))
    print("Player2 actual handvalue: " + str(identifyHand(player2.hand)))
    print("\n")





    #########################
    # phase 2:   Bidding    #
    #########################
    for AmountOfRounds in range(0,3):
        if isinstance(player1, FixedAgent):
            bid1 = player1.bid(game_round)
        else:
            bid1 = player1.bid()
        if isinstance(player2, FixedAgent):
            bid2 = player2.bid(game_round)
        else:
            bid2 = player2.bid()
        Total_pot += bid1 + bid2
        print("Phase " + str(AmountOfRounds + 1) + " player1 bid " + str(bid1) + " and player2 bid " + str(bid2))
    print("\n")
    #########################
    # phase 2:   Showdown   #
    #########################

    if(identifyHand(player1.hand) > identifyHand(player2.hand)):
     Player1_total_winnings += Total_pot
     print("Player1 takes it home with o total pot of:  " + str(Total_pot))
     print("\n")
    elif(identifyHand(player1.hand) < identifyHand(player2.hand)):
     Player2_total_winnings += Total_pot
     print("Player2 takes it home with a total pot of: " + str(Total_pot))
     print("\n")
    else:
     print("It´s a tie, noone wins")


print("Total wins player1: " + str(Player1_total_winnings))
print("Total wins player2: " + str(Player2_total_winnings))







