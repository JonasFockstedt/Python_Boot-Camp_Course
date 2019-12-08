import sys


# POSSIBLE CHANGES THAT COULD HAVE BEEN BETTER
# When prompting a player, use within a while-loop that runs until desired input is retrieved
# clear_output() method to clear output instead of leaving a trail
# Randomize which player starts
# Function that checks if space is available on board


board_positions = [None] * 9
turn = 0

def begin_game():
    global p1sign
    global p2sign
    p1sign = input('\nWelcome to the game Tic Taco Toe! \n'
      'The board is displayed below and what number corresponds to what position.\n'
      '| 1 | 2 | 3 |\n'
      '|---|---|---|\n'
      '| 4 | 5 | 6 |\n'
      '|---|---|---|\n'
      '| 7 | 8 | 9 |\n'
      '\n Please select which sign player 1 is going to use (X or O)\n')


    if p1sign == 'X' or p1sign == 'O':
        if p1sign is 'X':
            p2sign = 'O'
        elif p1sign is 'O':
            p2sign = 'X'
    else:
        raise ValueError('Wrong sign, must be either "X" or "O"')


    print('Player 1: ' + p1sign + '\n' + 'Player 2: ' + p2sign)

    print_board()


def print_board():
    global turn

    print('| ' + print_symbol(0) + ' | ' + print_symbol(1) + ' | ' + print_symbol(2) + ' |\n'
            '|---|---|---|\n'
            '| ' + print_symbol(3) + ' | ' + print_symbol(4) + ' | ' + print_symbol(5) + ' |\n'
            '|---|---|---|\n'
            '| ' + print_symbol(6) + ' | ' + print_symbol(7) + ' | ' + print_symbol(8) + ' |\n')

    next_move = input(f'Player {turn % 2 + 1}, type in the position you want your symbol: ')

    if board_positions[int(next_move)] is not None:
        raise ValueError('That position is already occupied!')
    else:
        if turn % 2 + 1 is 1:
            board_positions[int(next_move)] = p1sign
            check_win()
            turn += 1
            print_board()
        elif turn % 2 + 1 is 2:
            board_positions[int(next_move)] = p2sign
            check_win()
            turn += 1
            print_board()


def check_win():
    occupied = 0
    for element in board_positions:
        if element is not None:
            occupied += 1
            if occupied == 9:
                board_full()

    if (board_positions[0] == p1sign) and (board_positions[1] == p1sign and (board_positions[2]) == p1sign) or \
            (board_positions[0] == p2sign) and (board_positions[1] == p2sign) and (board_positions[2] == p2sign): # If first row is completed
        win()
    elif ((board_positions[3] == p1sign) and (board_positions[4] == p1sign) and (board_positions[5]) == p1sign) or \
            (board_positions[3] == p2sign) and (board_positions[4] == p2sign) and (board_positions[5] == p2sign): # If second row is completed
        win()
    elif (board_positions[6] == p1sign) and (board_positions[7] == p1sign) and (board_positions[8] == p1sign) or \
            (board_positions[6] == p2sign) and (board_positions[7] == p2sign) and (board_positions[8] == p2sign): # If third row is completed
        win()
    elif (board_positions[0] == p1sign) and (board_positions[3] == p1sign) and (board_positions[6] == p1sign) or \
            (board_positions[0] == p2sign) and (board_positions[3] == p2sign) and (board_positions[6] == p2sign): # If first column is completed
        win()
    elif (board_positions[1] == p1sign) and (board_positions[4] == p1sign) and (board_positions[7] == p1sign) or \
            (board_positions[1] == p2sign) and (board_positions[4] == p2sign) and (board_positions[7] == p2sign): # If second column is completed
        win()
    elif (board_positions[2] == p1sign) and (board_positions[5] == p1sign) and (board_positions[8] == p1sign) or \
            (board_positions[2] == p2sign) and (board_positions[5] == p2sign) and (board_positions[8] == p2sign): # If third column is completed
        win()
    elif (board_positions[0] == p1sign) and (board_positions[4] == p1sign) and (board_positions[8] == p1sign) or \
            (board_positions[0] == p2sign) and (board_positions[4] == p2sign) and (board_positions[8] == p2sign): # If diagonal, from top left to bottom right is completed
        win()
    elif (board_positions[2] == p1sign) and (board_positions[4] == p1sign) and (board_positions[6] == p1sign) or \
            (board_positions[2] == p2sign) and (board_positions[4] == p2sign) and (board_positions[6] == p2sign): # If diagonal, from top right to bottom left is completed
        win()


def player_turn():
    if turn % 2 + 1 is 1:
        return 'Player 1'
    elif turn % 2 + 1 is 2:
        return 'Player 2'


def win():
    global board_positions
    global p1sign
    global p2sign
    global turn

    print_winning_board()
    play_again = input('Congratulations ' + player_turn() + ', you won! \n'
                                                            'would you like to play again?(Y/N)')
    if play_again == 'Y':
        board_positions = [None] * 9
        p1sign = None
        p2sign = None
        turn = 0
        begin_game()
    elif play_again == 'N':
        sys.exit()


def board_full():
    global board_positions
    global p1sign
    global p2sign
    global turn
    print_winning_board()
    play_again = input('The board is full! No possible moves left, would you like to play again?(Y/N)')

    if play_again is 'Y':
        board_positions = [None] * 9
        p1sign = None
        p2sign = None
        turn = 0
        begin_game()
    elif play_again is 'N':
        sys.exit()

def print_symbol(index):
    if board_positions[index] is not None:
        return board_positions[index]
    else:
        return ' '


def print_winning_board():
    print('| ' + print_symbol(0) + ' | ' + print_symbol(1) + ' | ' + print_symbol(2) + ' |\n'
                                                                                       '|---|---|---|\n'
                                                                                       '| ' + print_symbol(
        3) + ' | ' + print_symbol(4) + ' | ' + print_symbol(5) + ' |\n'
                                                                 '|---|---|---|\n'
                                                                 '| ' + print_symbol(6) + ' | ' + print_symbol(
        7) + ' | ' + print_symbol(8) + ' |\n')


begin_game()
