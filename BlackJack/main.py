import player
import deck
import sys


def run_game(balance=100):
    game = True

    # Initialize deck.
    card_deck = deck.Deck()
    card_deck.create_deck()
    # Create computer and human player.
    human = player.Player('Human', balance=balance)
    dealer = player.Player('Dealer')
    human.opponent = dealer
    dealer.opponent = human

    active_player = human

    # Deal two cards to each player.
    for number in range(2):
        card_deck.deal_cards(dealer)
        card_deck.deal_cards(human)

    while game:
        # Human turn
        if active_player == human and human.last_action != 'Stay' and game:
            if human.last_bet == 0 and human.balance != 0:
                print(f'Dealer has {dealer.hand[0]} at hand.')
                print(f'You have {human.hand} at hand.')
                while True:
                    try:
                        bet_amount = int(input(
                            f'How much do you want to bet? You have {human.balance} credits available.\n'))
                        if bet_amount > human.balance:
                            print(
                                f'You can not bet more credits than you already have!')
                        else:
                            human.bet(bet_amount)
                            print(
                                f'You bet {human.last_bet} amount of credits. Your balance is now {human.balance} credits.')
                            break
                    except:
                        print('Invalid format.')

            human.compute_hand_strength()
            print(f'Your hand: {human.hand} (Strenght: {human.handStrength})')
            print(f'Opponent hand: {dealer.hand[0]}')
            action = input(f'Hit or stay? (Hit/Stay) ')
            if action == 'Hit':
                human.hit(card_deck)
                human.last_action = 'Hit'
                human.compute_hand_strength()
                print(f'Your hand: {human.hand}')
                if human.handStrength > 21:
                    game = False
                    print('Human busts, dealer wins!')
                    return human.balance
            elif action == 'Stay':
                active_player = dealer
                human.last_action = 'Stay'

        # Dealer turn
        elif active_player == dealer and game:
            dealer.compute_hand_strength()
            human.compute_hand_strength()
            print(f'Dealer hand: {dealer.hand}')
            if dealer.handStrength <= human.handStrength and dealer.handStrength <= 21:
                dealer.hit(card_deck)
                print('Dealer hits.')
                dealer.compute_hand_strength()
                print(
                    f'Dealer hand: {dealer.hand} (Strength: {dealer.handStrength})')
                if dealer.handStrength > 21:
                    print('Dealer busts, human player wins!')
                    game = False
                    human.balance += human.last_bet*2
                    return human.balance

                active_player = human

            elif dealer.handStrength > human.handStrength and human.last_action == 'Stay':
                print(
                    f'Human player hand: {human.hand} (Strength: {human.handStrength})')
                print('Dealer wins!')
                return human.balance

        elif dealer.handStrength > human.handStrength and human.last_action == 'Stay' and game:
            game = False
            print('Dealer wins!')
            return human.balance

        elif dealer.handStrength < human.handStrength and human.last_action == 'Stay' and game:
            game = False
            print('Human wins!')
            return human.balance + human.last_bet*2

        elif dealer.handStrength == human.handStrength and game:
            print('It\'s a tie!')
            return human.balance + human.last_bet


if __name__ == '__main__':
    continue_playing = True
    remaining_credits = 100
    while continue_playing:
        remaining_credits = run_game(remaining_credits)
        if remaining_credits > 0:
            another_game = input(
                f'Your balance is {remaining_credits}, do you want to play another round?(Yes/No) ')
            if another_game == 'No':
                continue_playing = False
        else:
            print('You have insufficient funds to play another game.')
            sys.exit()
