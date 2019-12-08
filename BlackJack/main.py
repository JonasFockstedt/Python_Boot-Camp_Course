# TODO
# Define cards (52 of them) DONE!
# Jack, Queen, King has value of 10 DONE!
# Aces can be treated as a 1 or 11, whichever the player prefers
# A human and computer player
# Closest to a card value of 21 wins
# Human player has a balance of money
# Human places bet
# Hands for both players
# Visualize hands
# Computer starts with one card facing up, the other down
# Human starts with two cards facing up
# Human goes first
# Prompt player to "Hit" or "Stay" (drawing new card, or don't)
# Computer "hits" until having a higher value than player, or busts (over 21 in value)
# If player loses, player loses money they did bet
# If player wins, player gets doubled money back


import player

deck = dict()
cardSuit = {'Hearts': {}, 'Diamonds': {}, 'Clubs': {}, 'Spades': {}}
cardRank = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,"Ten": 10,
            "Jack": 10, "Queen": 10, "King": 10}


# create deck
def create_deck():
    global deck
    deck = cardSuit
    for category in deck:
        deck[category] = cardRank


def start_game():
    while True:
        create_player(input('Please type in your player name: '))
        moreplayers = input('Are there more players that wants to play? (Y/N)')
        if moreplayers == 'N':
            break


def create_player(name):
    return player.Player(name)


if __name__ == '__main__':
    create_deck()
    player1 = create_player('Fred')
    print(player1)
    player1.bet(50)
    player1.check_balance()

    computer = create_player('Computer')
    print(computer)

    #for suit in deck:
     #   print(suit)
      #  for rank in deck[suit]:
       #     print(rank)
    player1.hit()




