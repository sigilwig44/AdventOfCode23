def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    return array

def add_rows_and_columns(grid):
    original_rows = len(grid)
    original_cols = len(grid[0])
    added_rows = 0
    added_cols = 0

    i = 0
    while i < original_rows + added_rows:
        row = grid[i]
        if all(cell == '.' for cell in row):
            grid.insert(i + 1, ['.' for _ in range(original_cols + added_cols)])
            added_rows += 1
            i += 2  # skip the newly added row
        else:
            i += 1

    j = 0
    while j < original_cols + added_cols:
        col = [row[j] for row in grid]
        if all(cell == '.' for cell in col):
            for row in grid:
                row.insert(j + 1, '.')
            added_cols += 1
            j += 2  # skip the newly added column
        else:
            j += 1

    return grid

def find_pairs(grid):
    hashtags = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                hashtags.append((row, col))

    pairs = []
    for i in range(len(hashtags)):
        for j in range(i + 1, len(hashtags)):
            pairs.append([hashtags[i], hashtags[j]])

    return pairs

def calculate_total_distance(pairs):
    total_distance = 0

    for pair in pairs:
        point1 = pair[0]
        point2 = pair[1]
        x1, y1 = point1
        x2, y2 = point2

        distance = abs(x2 - x1) + abs(y2 - y1)
        total_distance += distance

    return total_distance

grid = create_2d_array_from_file('day11_input.txt')
grid = add_rows_and_columns(grid)
pairs = find_pairs(grid)
total_distance = calculate_total_distance(pairs)
print(total_distance)

# with open('day11_output.txt', 'w') as f:
#     for row in grid:
#         f.write(''.join(map(str, row)) + '\n')