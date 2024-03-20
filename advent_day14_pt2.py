import matplotlib.pyplot as plt

def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    return array

def up(grid):
    for j in range(len(grid[0])):
        # Loop through the list
        for i in range(len(grid)):
            # Check if the current element is 'O'
            if grid[i][j] == 'O':
                # Check if the space above is not '#'
                k = i
                while k - 1 >= 0 and (grid[k - 1][j] != '#'):
                    # Move the 'O' up by swapping
                    grid[k][j], grid[k - 1][j] = grid[k - 1][j], grid[k][j]
                    k -= 1

def down(grid):
    for j in range(len(grid[0])):
        # Loop through the list
        for i in range(len(grid) - 1, -1, -1):
            # Check if the current element is 'O'
            if grid[i][j] == 'O':
                # Check if the space below is not '#'
                k = i
                while k + 1 < len(grid) and (grid[k + 1][j] != '#'):
                    # Move the 'O' down by swapping
                    grid[k][j], grid[k + 1][j] = grid[k + 1][j], grid[k][j]
                    k += 1

def left(grid):
    for i in range(len(grid)):
        # Loop through the list
        for j in range(len(grid[i])):
            # Check if the current element is 'O'
            if grid[i][j] == 'O':
                # Check if the space to the left is not '#'
                k = j
                while k - 1 >= 0 and (grid[i][k - 1] != '#'):
                    # Move the 'O' to the left by swapping
                    grid[i][k], grid[i][k - 1] = grid[i][k - 1], grid[i][k]
                    k -= 1

def right(grid):
    for i in range(len(grid)):
        # Loop through the list
        for j in range(len(grid[i]) - 1, -1, -1):
            # Check if the current element is 'O'
            if grid[i][j] == 'O':
                # Check if the space to the right is not '#'
                k = j
                while k + 1 < len(grid[i]) and (grid[i][k + 1] != '#'):
                    # Move the 'O' to the right by swapping
                    grid[i][k], grid[i][k + 1] = grid[i][k + 1], grid[i][k]
                    k += 1

def tally_score(grid):
    total_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                total_score += (len(grid) - i)
    return total_score

def cycle(grid):
    up(grid)
    left(grid)
    down(grid)
    right(grid)

grid = create_2d_array_from_file("day14_input.txt")

scores = []
for i in range(10000):
    print(i)
    cycle(grid)
    scores.append(tally_score(grid))

# Create a figure
fig = plt.figure(figsize=(8,6))

# Create a plot
plt.plot(scores)

# Show the plot
plt.show()