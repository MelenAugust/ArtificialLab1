
import random
import numpy as np
from Poker_agents import RandomAgent, FixedAgent, ReflexAgent, MemoryAgent
from Gameutility import  identifyHand, Rank, BettingPhase_number
Suit = ["s", "h", "d", "c"]
card_amount = 3
Total_pot = 0
Player1_total_winnings = 0
Player2_total_winnings = 0
Total_rounds = 50
deck = []
hand1 = []
hand2 = []
player1_wins = 0
player2_wins = 0
All_Game_winning_p1 = 0
All_Game_winning_p2 = 0



player1 = MemoryAgent(hand = [])
player2 = RandomAgent(hand = [])


# Randomly generate two hands of n cards
def generate_2hands(deck,card_amount):
    random.shuffle(deck)

    player1.hand = [deck.pop(0) for _ in range(card_amount)]
    player2.hand = [deck.pop(0) for _ in range(card_amount)]

    return hand1, hand2

# identify hand category using IF-THEN rule





# Print out the result

player1_wins = 0
player2_wins = 0
All_Game_winning_p1 = 0
All_Game_winning_p2 = 0
player1_round_wins = 0
player2_round_wins = 0

player1_winnings_list = []
player2_winnings_list = []

# Run 100 games of 50 rounds each
for game_num in range(100):
    # Reset winnings for each game
    Player1_total_winnings = 0
    Player2_total_winnings = 0

    #########################
    #      Game flow        #
    #########################
    for round_num in range(50):  # 50 rounds per game
        # Reset the pot and deck for each round
        Total_pot = 0
        deck.clear()

        # Generate a new deck and reset hands
        for rank in Rank:
            for suit in Suit:
                deck.append(rank + suit)

        #########################
        # phase 1: Card Dealing #
        #########################
        print("                                    Round " + str(round_num + 1))
        hand1, hand2 = generate_2hands(deck, card_amount)
        print("Player1 hand: " + str(player1.hand))
        print("Player2 hand: " + str(player2.hand))
        print("\n")
        print("Player1 actual handvalue: " + str(identifyHand(player1.hand)))
        print("Player2 actual handvalue: " + str(identifyHand(player2.hand)))
        print("\n")

        #########################
        # phase 2:   Bidding    #
        #########################
        for AmountOfRounds in range(3):
            bid1 = player1.bid()
            bid2 = player2.bid()
            if isinstance(player1,MemoryAgent):
             player1.observe(bid2, game_num, round_num)
            Total_pot += bid1 + bid2


            print("Phase " + str(AmountOfRounds + 1) + " player1 bid " + str(bid1) + " and player2 bid " + str(bid2))
        print("\n")

        #########################
        # phase 3:   Showdown   #
        #########################
        if identifyHand(player1.hand) > identifyHand(player2.hand):
            Player1_total_winnings += Total_pot
            player1_round_wins += 1
            print("Player1 takes it home with a total pot of:  " + str(Total_pot))
            print("\n")
        elif identifyHand(player1.hand) < identifyHand(player2.hand):
            Player2_total_winnings += Total_pot
            player2_round_wins += 1
            print("Player2 takes it home with a total pot of: " + str(Total_pot))
            print("\n")
        else:
            print("It´s a tie, no one wins")

    # Track who won the game of 50 rounds
    if Player1_total_winnings > Player2_total_winnings:
        player1_wins += 1
    elif Player2_total_winnings > Player1_total_winnings:
        player2_wins += 1


    All_Game_winning_p1 += Player1_total_winnings
    All_Game_winning_p2 += Player2_total_winnings

    player1_winnings_list.append(Player1_total_winnings)
    player2_winnings_list.append(Player2_total_winnings)


    print("Game " + str(game_num + 1) + " results:")
    print("Total winnings for Player 1 in this game: " + str(Player1_total_winnings))
    print("Total winnings for Player 2 in this game: " + str(Player2_total_winnings))
    print("\n")

player1_avg_winnings = np.mean(player1_winnings_list)
player2_avg_winnings = np.mean(player2_winnings_list)
player1_std_dev = np.std(player1_winnings_list)
player2_std_dev = np.std(player2_winnings_list)


print("After 100 games of 50 rounds:")
if isinstance(player1,MemoryAgent):
 print(f"MemoryAgent deduced opponent type as: {player1.opponent_type}")
print("Player 1 won " + str(player1_wins) + " games with a total pot of " + str(All_Game_winning_p1))
print("Player 2 won " + str(player2_wins) + " games with a total pot of " + str(All_Game_winning_p2))
print("Player 1 won a total of " + str(player1_round_wins) + " rounds.")
print("Player 2 won a total of " + str(player2_round_wins) + " rounds.")

print("Player 1: Average winnings per game = {:.2f}, Standard deviation = {:.2f}".format(player1_avg_winnings, player1_std_dev))
print("Player 2: Average winnings per game = {:.2f}, Standard deviation = {:.2f}".format(player2_avg_winnings, player2_std_dev))














