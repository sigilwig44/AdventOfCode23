class GridCell:
    def __init__(self, char, is_original=False):
        self.char = char
        self.is_original = is_original

path = set()

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
            if cell.char == "S":
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
        path.add((row, col))

        steps += 1
        current_char = grid[row][col].char

        next_moves = get_next_moves(current_char, row, col, prev_row, prev_col)

        if not next_moves:  # Dead-end
            return None  # No loop found

        if current_char == "S" and steps > 1:  # Loop completed
            return steps

        # Move to the next valid position
        for move in next_moves:
            next_row, next_col = move
            next_char = grid[next_row][next_col].char
            if next_char == "|" and next_col == col:
                path.add((next_row, next_col))
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "-" and next_row == row:
                path.add((next_row, next_col))
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "7" and (next_row < row or next_col > col):
                path.add((next_row, next_col))
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "F" and (next_row < row or next_col < col):
                path.add((next_row, next_col))
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "L" and (next_row > row or next_col < col):
                path.add((next_row, next_col))
                prev_row = row
                prev_col = col
                row = next_row
                col = next_col
                break
            if next_char == "J" and (next_row > row or next_col > col):
                path.add((next_row, next_col))
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

def add_border(grid):
    width = len(grid[0]) + 2  # Width of the new grid with border
    height = len(grid) + 2    # Height of the new grid with border

    # Create an empty grid with the calculated width and height
    bordered_grid = [[GridCell('*', False) for _ in range(width)] for _ in range(height)]

    # Copy the original elements into the middle of the new grid
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            bordered_grid[y+1][x+1] = grid[y][x]

    return bordered_grid

def expand_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    expanded_rows = 2 * rows
    expanded_cols = 2 * cols
    expanded_grid = [[GridCell('X', False)] * expanded_cols for _ in range(expanded_rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                expanded_grid[2*i][2*j] = GridCell('.', True)
                expanded_grid[2*i][2*j+1] = GridCell('*', False)
                expanded_grid[2*i+1][2*j] = GridCell('*', False)
                expanded_grid[2*i+1][2*j+1] = GridCell('*', False)
            if grid[i][j] == '-':
                expanded_grid[2*i][2*j] = GridCell('-', True)
                expanded_grid[2*i][2*j+1] = GridCell('-', False)
                expanded_grid[2*i+1][2*j] = GridCell('*', False)
                expanded_grid[2*i+1][2*j+1] = GridCell('*', False)
            if grid[i][j] == '|':
                expanded_grid[2*i][2*j] = GridCell('|', True)
                expanded_grid[2*i][2*j+1] = GridCell('*', False)
                expanded_grid[2*i+1][2*j] = GridCell('|', False)
                expanded_grid[2*i+1][2*j+1] = GridCell('*', False)
            elif grid[i][j] == 'F':
                expanded_grid[2*i][2*j] = GridCell('F', True)
                expanded_grid[2*i][2*j+1] = GridCell('-', False)
                expanded_grid[2*i+1][2*j] = GridCell('|', False)
                expanded_grid[2*i+1][2*j+1] = GridCell('*', False)
            elif grid[i][j] == 'L':
                expanded_grid[2*i][2*j] = GridCell('L', True)
                expanded_grid[2*i][2*j+1] = GridCell('-', False)
                expanded_grid[2*i+1][2*j] = GridCell('*', False)
                expanded_grid[2*i+1][2*j+1] = GridCell('*', False)
            elif grid[i][j] == 'J':
                expanded_grid[2*i][2*j] = GridCell('J', True)
                expanded_grid[2*i][2*j+1] = GridCell('*', False)
                expanded_grid[2*i+1][2*j] = GridCell('*', False)
                expanded_grid[2*i+1][2*j+1] = GridCell('*', False)
            elif grid[i][j] == '7':
                expanded_grid[2*i][2*j] = GridCell('7', True)
                expanded_grid[2*i][2*j+1] = GridCell('*', False)
                expanded_grid[2*i+1][2*j] = GridCell('|', False)
                expanded_grid[2*i+1][2*j+1] = GridCell('*', False)
            elif grid[i][j] == 'S':
                expanded_grid[2*i][2*j] = GridCell('S', True)
                expanded_grid[2*i][2*j+1] = GridCell('-', False)
                expanded_grid[2*i+1][2*j] = GridCell('|', False)
                expanded_grid[2*i+1][2*j+1] = GridCell('*', False)

    return expanded_grid

def mark_border(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in path:
                grid[i][j] = GridCell('X', False)

def get_number_inside(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = [(10, 74)]  # Start at the origin or (10, 74)
    tile_count = 0  # Initialize a counter for '.'

    while queue:
        i, j = queue.pop()
        if 0 <= i < rows and 0 <= j < cols and grid[i][j].char != 'X' and grid[i][j].char != 'O':
            if grid[i][j].is_original:
                tile_count += 1
            grid[i][j].char = 'O'  # Mark as filled
            for dx, dy in directions:
                queue.append((i + dx, j + dy))

    return tile_count

grid = create_2d_array_from_file("day10_input.txt")
grid = expand_grid(grid)
grid = add_border(grid)
find_pipe_loop_length(grid)
mark_border(grid)

print("Number of tiles encountered:", get_number_inside(grid))