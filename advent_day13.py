def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    input = []
    grid = []
    for line in lines:
        if line.strip():  # If line is not empty
            grid.append(line.strip())
        else:  # Empty line indicates end of a grid
            if grid:
                input.append("\n".join(grid))
                grid = []

    # Append the last grid if it exists
    if grid:
        input.append("\n".join(grid))

    return input

def check_horizontal_mirror(pattern):
    rows = pattern.splitlines()
    num_rows = len(rows)
    for mirror_pos in range(1, num_rows):
        match_found = True
        for i in range(mirror_pos):
            if 0 <= mirror_pos - 1 - i < num_rows and 0 <= mirror_pos + i < num_rows and rows[mirror_pos - 1 - i] != rows[mirror_pos + i]:
                match_found = False
                break
        if match_found:
            return mirror_pos

def check_vertical_mirror(pattern):
    cols = list(zip(*pattern.splitlines()))
    num_cols = len(cols)
    for mirror_pos in range(1, num_cols):
        match_found = True
        for i in range(mirror_pos):
            if 0 <= mirror_pos - 1 - i < num_cols and 0 <= mirror_pos + i < num_cols and cols[mirror_pos - 1 - i] != cols[mirror_pos + i]:
                match_found = False
                break
        if match_found:
            return mirror_pos
        
input = parse_input("day13_input.txt")

total = 0
for grid in input:
    position = 0
    position = check_horizontal_mirror(grid)
    if position == None:
        position = check_vertical_mirror(grid)
        total += position
    else :
        total += (100 * position)
print("Total value: ", total)