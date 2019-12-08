import main
import random


class Player:

    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance
        self.hand = dict()

    def __str__(self):
        return f'{self.name} has ${self.balance} at their disposal.'

    def check_balance(self):
        print(f'{self.name} has a balance of ${self.balance}')

    def bet(self, withdrawal):
        if withdrawal > self.balance:
            print('Insufficient balance!')
        else:
            self.balance -= withdrawal
            print(f'{self.name} bet ${withdrawal}')

    def hit(self):
        suit = random.choice(list(main.deck.keys()))    # pick random card suit
        rank = random.choice(list(main.deck.keys()))    # picks random key in dictionary
        print(suit)
        #print(f'Drew rank: {suit} {rank}')
        #self.hand.append(suit + rank)
        #print(self.hand)
        # take out rank from the deck is not done properly
        #main.deck.pop([suit][rank])
        # main.deck.remove([suit])
        for rank_suit in main.deck[0]:
            if rank_suit == suit:
                del main.deck[1][rank]
        print('Test')
