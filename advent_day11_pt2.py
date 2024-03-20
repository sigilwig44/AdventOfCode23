def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    return array

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

def count_empty_rows_and_cols(grid, row1, row2, col1, col2):
    empty_rows = 0
    for row in range(min(row1, row2), max(row1, row2)):
        row_is_empty = True
        for col in range(len(grid[0])):
            if grid[row][col] != '.':
                row_is_empty = False
                break
        if row_is_empty:
            empty_rows += 1

    empty_cols = 0
    for col in range(min(col1, col2), max(col1, col2)):
        col_is_empty = True
        for row in range(len(grid)):
            if grid[row][col] != '.':
                col_is_empty = False
                break
        if col_is_empty:
            empty_cols += 1

    return empty_rows, empty_cols

def calculate_total_distance(pairs, grid):
    total_distance = 0

    for pair in pairs:
        point1 = pair[0]
        point2 = pair[1]
        x1, y1 = point1
        x2, y2 = point2
        empty_rows, empty_cols = count_empty_rows_and_cols(grid, x1, x2, y1, y2)

        distance = ((abs(x2 - x1) - empty_rows) + empty_rows * 1000000) + ((abs(y2 - y1) - empty_cols) + empty_cols * 1000000)
        total_distance += distance

    return total_distance

grid = create_2d_array_from_file('day11_input.txt')
pairs = find_pairs(grid)
total_distance = calculate_total_distance(pairs, grid)
print(total_distance)