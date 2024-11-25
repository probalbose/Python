import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = [] # Reset the list for each sample
    for i in range(100):
        flips.append(random.randint(0, 1))
    # checking multiple 0s and 1s in a row


    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1 # streak starts from 1 because there will be at least 1 H ot T
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            streak += 1 # if the value is same as previous increase the streak
        else:
            streak = 1

        if streak == 6:
            numberOfStreaks += 1
            break # when the streak reaches to 6 we break as we only want to count one streak of 6 per sample

print('Chance of streak: %s%%' % (numberOfStreaks / 100))