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
    return f"You flipped a coin {flips} times. The outcomes were:\n\
            Number of heads: {flipped_sides['Heads']} \n\
            Number of tails: {flipped_sides['Tails']}"

    


if __name__ == '__main__':
    print(coinFlip(1000))