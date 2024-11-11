import random

from Gameutility import game_round,identifyHand



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

    def bid(self, game_round):

        if(game_round < 10):
            return 10
        elif (game_round < 20):
            return 20
        elif (game_round < 30):
            return 30
        elif (game_round < 40):
            return 40
        else:
            return 50

class ReflexAgent(Player):

    def bid(self):
        return int(identifyHand(self.hand) + 13)



