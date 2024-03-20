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

def hamming_distance(str1, str2):
    """Calculates the Hamming distance between two strings of equal length."""
    if len(str1) != len(str2):
        raise ValueError("Strings must have equal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

def check_horizontal_mirror(pattern):
    rows = pattern.splitlines()
    num_rows = len(rows)
    total_mismatches = 0
    for mirror_pos in range(1, num_rows):
        for i in range(mirror_pos):
            if 0 <= mirror_pos - 1 - i < num_rows and 0 <= mirror_pos + i < num_rows:
                total_mismatches += hamming_distance(rows[mirror_pos - 1 - i], rows[mirror_pos + i])
        if total_mismatches == 1:  # Valid mirror
            return mirror_pos
        total_mismatches = 0

def check_vertical_mirror(pattern):
    cols = list(zip(*pattern.splitlines()))
    num_cols = len(cols)
    total_mismatches = 0
    for mirror_pos in range(1, num_cols):
        for i in range(mirror_pos):
            if 0 <= mirror_pos - 1 - i < num_cols and 0 <= mirror_pos + i < num_cols:
                total_mismatches += hamming_distance(cols[mirror_pos - 1 - i], cols[mirror_pos + i])
        if total_mismatches == 1:  # Valid mirror
            return mirror_pos
        total_mismatches = 0
        
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