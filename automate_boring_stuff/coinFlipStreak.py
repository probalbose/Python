import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for i in range(101):
        if random.randint(0, 1):
            flips.append('H')
        else:
            flips.append('T')

    print(''.join(flips))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    

print('Chance of streak: %s%%' % (numberOfStreaks / 100))