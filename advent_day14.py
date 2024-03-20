with open("day14_input.txt", "r") as file:
    data = file.read().splitlines()

# transpose the data to get columns
cols = list(zip(*data))

# remove empty columns
cols = [list(col) for col in cols if any(char != ' ' for char in col)]

def roll_stones(col):
    col = col[:]
    # Loop through the list
    for i in range(len(col)):
        # Check if the current element is 'O'
        if col[i] == 'O':
            # Check if the space to the left is not '#'
            j = i
            while j - 1 >= 0 and (col[j - 1] != '#'):
                # Move the 'O' to the left by swapping
                col[j], col[j - 1] = col[j - 1], col[j]
                j -= 1
    return col

def tally_score(col):
    total_score = 0
    num_cols = len(col)
    for i in range(num_cols):
        if col[i] == 'O':
            total_score += (num_cols - i)
    return total_score

count = 0
for i in range(1000000000):
    total_grid_score = 0
    for column in cols:
        count += 1
        total_grid_score += tally_score(roll_stones(column))
    print(count)
    print(count/1000000000)
print(total_grid_score)