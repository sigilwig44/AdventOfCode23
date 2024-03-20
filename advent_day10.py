def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    return array

def find_start(grid):
    """Finds the starting point (S) in the grid."""
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == "S":
                return row_index, col_index

def find_pipe_loop_length(grid):
    """Finds the length of the pipe loop using a simplified iterative approach."""

    start_position = find_start(grid)
    if not start_position:
        return None  # No starting point found

    row, col = start_position
    prev_row, prev_col = -1, -1  # Initial invalid positions
    steps = 0

    while True:
        steps += 1
        print(steps)
        current_char = grid[row][col]

        next_moves = get_next_moves(current_char, row, col, prev_row, prev_col)

        if not next_moves:  # Dead-end
            return None  # No loop found

        if current_char == "S" and steps > 1:  # Loop completed
            return steps

        # Move to the next valid position
        for move in next_moves:
            next_row, next_col = move
            next_char = grid[next_row][next_col]
            if next_char == "|" and next_col == col:
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "-" and next_row == row:
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "7" and (next_row < row or next_col > col):
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "F" and (next_row < row or next_col < col):
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "L" and (next_row > row or next_col < col):
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "J" and (next_row > row or next_col > col):
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "S":
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break

def get_next_moves(current_char, row, col, prev_row, prev_col):
    """
    Returns possible next moves based on the current pipe character and 
    the previous position to avoid backtracking.
    """
    next_moves = []
    if current_char in ("|", "S"):
        if (row - 1, col) != (prev_row, prev_col):
            next_moves.append((row - 1, col))  # Up
        if (row + 1, col) != (prev_row, prev_col):
            next_moves.append((row + 1, col))  # Down
    if current_char in ("-", "S"):
        if (row, col - 1) != (prev_row, prev_col):
            next_moves.append((row, col - 1))  # Left
        if (row, col + 1) != (prev_row, prev_col):
            next_moves.append((row, col + 1))  # Right
    if current_char == "L":
        if (row - 1, col) != (prev_row, prev_col):
            next_moves.append((row - 1, col))
        if (row, col + 1) != (prev_row, prev_col):
            next_moves.append((row, col + 1))
    if current_char == "J":
        if (row - 1, col) != (prev_row, prev_col):
            next_moves.append((row - 1, col))
        if (row, col - 1) != (prev_row, prev_col):
            next_moves.append((row, col - 1))
    if current_char == "7":
        if (row + 1, col) != (prev_row, prev_col):
            next_moves.append((row + 1, col))
        if (row, col - 1) != (prev_row, prev_col):
            next_moves.append((row, col - 1))
    if current_char == "F":
        if (row + 1, col) != (prev_row, prev_col):
            next_moves.append((row + 1, col))
        if (row, col + 1) != (prev_row, prev_col):
            next_moves.append((row, col + 1))

    return next_moves

grid = create_2d_array_from_file("day10_input.txt")

loop_length = find_pipe_loop_length(grid)

if loop_length is not None:
    print("Loop length:", loop_length)
else:
    print("No closed loop found")