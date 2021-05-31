import random
def coinFlip(flips):
    
    flipped_sides = dict()

    for _ in range(flips):
        # Simulate flipping a coin. 0 = Heads, 1 = Tails.
        side = random.randint(0,1)
        if side == 0:
            if 'Heads' in flipped_sides:
                flipped_sides['Heads'] += 1
            else:
                flipped_sides['Heads'] = 1
        elif side == 1:
            if 'Tails' in flipped_sides:
                flipped_sides['Tails'] += 1
            else:
                flipped_sides['Tails'] = 1
    print(f"You flipped a coin {flips} times. The outcomes were:\n\
            Number of heads: {flipped_sides['Heads']} \n\
            Number of tails: {flipped_sides['Tails']}")

    


if __name__ == '__main__':
    
    while True:
        try:
            n_flips = int(input('How many times would you like to flip a coin?\n'))
            coinFlip(n_flips)
            # To keep the script prompt open.
            again = input('Would you like to flip again? (y/n)').lower()
            if again == 'y':
                continue
            elif again == 'n':
                break

        except:
            print('Error: Number of flips must be an integer.')
            continue
    