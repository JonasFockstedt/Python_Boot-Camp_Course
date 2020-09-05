import main
import deck
import random


class Player:

    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance
        self.hand = list()
        self.opponent = None
        self.handStrength = 0
        self.last_bet = 0
        self.last_action = None

    def __str__(self):
        return f'{self.name} has ${self.balance} at their disposal.'

    def check_balance(self):
        print(f'{self.name} has a balance of ${self.balance}')

    def bet(self, amount):
        self.balance -= amount
        self.last_bet = amount

    def hit(self, deck):
        if self.name == 'Dealer':
            deck.deal_cards(self)

        elif self.name == 'Human':
            deck.deal_cards(self)
            # print(f'Your{self.hand}')

    def compute_hand_strength(self):
        cardValues = {"Two": 2, "Three": 3, "Four": 4, "Five": 5,
                      "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                      "Ten": 10, "Jack": 10, "Queen": 10,
                      "King": 10, "Ace": 11}
        self.handStrength = 0
        for card in self.hand:
            self.handStrength += cardValues[card.split()[1]]

        # If player has an Ace at hand, and has a hand strength of over 21, consider the Ace as value of 1.
        if any('Ace' in card for card in self.hand) and self.handStrength > 21:
            self.handStrength -= 10
