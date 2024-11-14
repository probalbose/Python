# Conway's Game of Life
import random, time, copy

WIDTH = 60
HEIGHT = 20

# Create a list of lists for the cells:
nextCells = []
for x in range(WIDTH):
    column = []  # Create a new column.
    for y in range(HEIGHT):
        # if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)): # For glider pattern.
        if random.randint(0, 1) == 0:
            column.append("#")  # Add a living cell.
        else:
            column.append(" ")  # Add a dead cell.
    nextCells.append(column)  # nextCells is a list of column lists.
# Now start the main program loop.
while True:
    print("\n\n\n\n\n")  # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)  # deecopy() copies the inner lists.
    # Print currentCells on the screen:
    # currentCells[x][y] gives the value at outer list index x and inner list index y.
    """
        e.g.:
        2d_arr = [
                   <0>[<0>1,<1>2,<2>3], <1>[<0>4,<1>5,<2>6],<2>[<0>7,<1>8,<2>9]
                 ]
        2d_arr[1][2] is 6, 2d_arr[2][1] is 8
    """
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")  # Print the # or space.
            print()  # Print a newline.
    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates.
            # `% WIDTH` ensures leftCoord is always between 0 and -1.
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbours:
            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbours += 1  # Top-left  neighbour is alive.
            if currentCells[x][aboveCoord] == "#":
                numNeighbours += 1  # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbours += 1  # Top-right neighbour is alive.
            if currentCells[leftCoord][y] == "#":
                numNeighbours += 1  # Left neighbour is alive.
            if currentCells[rightCoord][y] == "#":
                numNeighbours += 1  # Right neighbour is alive.
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbours += 1  # Bottom-left neighbour is alive.
            if currentCells[x][belowCoord] == "#":
                numNeighbours += 1  # Below neighbour is alive.
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbours += 1  # Bottom-right neighbour is alive.
            # Set cell based on Conway's game of life rules.
            if currentCells[x][y] == "#" and (numNeighbours == 2 or numNeighbours == 3):
                # Living cells with 2 or 3 neighbours stay alive:
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbours == 3:
                # Dead cells with 3 neighbours become alive:
                nextCells[x][y] = "#"
            else:
                # Everything else dies or stays alive:
                nextCells[x][y] = " "
    time.sleep(1)  # Add a 1 sec pause to reduce flickering.
