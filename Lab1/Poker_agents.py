import random

from Gameutility import identifyHand,BettingPhase_number


class Player:
    def __init__(self,  hand):
        self.hand = hand
        self.total_winnings = 0   # Track winnings for the player

    def bid(self):
        print("The bid mechanism is defined in the different agent classes")

class RandomAgent(Player):

    def bid(self):
        return random.randint(1,50)

class FixedAgent(Player):

    def bid(self):
        #if higher pairs or better, All in!
        if(int(identifyHand(self.hand)) > 13):
            return 50
        else:
            return 10

class ReflexAgent(Player):

    def bid(self):
        return int(identifyHand(self.hand) + 13)


class MemoryAgent(Player):
    def __init__(self, hand):
        super().__init__(hand)
        self.opponent_bets = []  # Array for storing opponent bet
        self.opponent_type = None  #

    def decide_opponent(self):
       # decide opponent after 3 rounds (very low chance of being wrong)
        if all(bet in [10, 50] for bet in self.opponent_bets[:3]):  # Check if all bets in the current array are either 10 or 50
            self.opponent_type = "Fixed"
        elif len(set(self.opponent_bets[:3])) == len(self.opponent_bets[:3]): #Check if all bets are different
            self.opponent_type = "Random"
        elif len(set(self.opponent_bets[:3])) == 1: #Check if all bets are the same
            self.opponent_type = "Reflex"
        else:
            self.opponent_type = "Unknown"

    def observe(self, player2_bid, game_num, round_num):
         #tracks latest bet
        self.opponent_bets.append(player2_bid)
         # we use the 3 first rounds to analyze what agent we are up against
        if game_num == 0 and round_num == 0 and len(self.opponent_bets) == 3:
            self.decide_opponent()

    def bid(self):
        # No typ has been identified first 3 rounds
        #So we bet 1 beacuse at this point is it just a 50/50 situation
        if self.opponent_type is None:

         return 1

        if self.opponent_type == "Fixed":
           # If fixed_agent bets 10 it indicates that it has high card at most. if that is the case and
           # we have atleast King high we go all in beacuse we should have the better chance, otherwise bet 1
            x = int(identifyHand(self.hand))
            last_opponent_bid = self.opponent_bets[-1]
            if last_opponent_bid == 10 and x > 11:
                return 50
            else:
                return 1


        elif self.opponent_type == "Random":
            # We go all in if we have atleast King high beacuse we should be favored else bet minimum
            if int(identifyHand(self.hand)) > 12:
                return 50
            else:
                return 1
        elif self.opponent_type == "Reflex":
            # Beacuse reflex is programmed so that is bets depending on its card strength,
            # We can easily identify what hand strengh they have just by looking at there bet
            last_opponent_bid = self.opponent_bets[-1]
            reflex_hand_value_estimate = last_opponent_bid - 13

            if int(identifyHand(self.hand)) > reflex_hand_value_estimate:
                return 50  # Bet aggressively if your hand value is better
            else:
                return 1  # Bet minimally if your hand value is worse



























