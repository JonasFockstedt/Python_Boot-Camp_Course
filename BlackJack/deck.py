import random


class Deck:

    def __init__(self):
        self.deck = list()

    def create_deck(self):
        cardSuits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        cardRanks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                     'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        cardValues = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
                      "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

        for suit in cardSuits:
            for rank in cardRanks:
                self.deck.append(suit + ' ' + rank)
        random.shuffle(self.deck)

    # Deals the top card to the player.

    def deal_cards(self, player):
        player.hand.append(self.deck.pop(0))
