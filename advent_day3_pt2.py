def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    return array

def calculate_gear_ratios(schematic):
    """Calculates the sum of all gear ratios in the given engine schematic.

    Args:
        schematic: A 2D array representing the engine schematic, where each
                   element is a string containing a number, symbol, or period.

    Returns:
        The sum of all gear ratios in the schematic.
    """

    rows, cols = len(schematic), len(schematic[0])
    gear_ratio_sum = 0
    gear_ratios = {}  # Dictionary to store gear ratios, keyed by gear IDs

    for row in range(rows):
        number_start = -1
        number_string = ""

        for col in range(cols):
            if schematic[row][col].isdigit() and col + 1 < cols:
                if number_start == -1:
                    number_start = col
                number_string += schematic[row][col]
            elif number_start != -1 or (col + 1 == cols and number_start != -1) or (col + 1 == cols and number_start != -1 and schematic[row][col].isdigit()):  # End of a number
                if col + 1 == cols and number_start != -1 and schematic[row][col].isdigit():
                    number_string += schematic[row][col]
                temp_num = int(number_string)

                # Check for adjacent '*' symbols, covering all sides and diagonals
                visited_cells = []
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        for offset in range(number_start, col):
                            neighbor_row, neighbor_col = row + dr, offset + dc
                            if (
                                0 <= neighbor_row < rows
                                and 0 <= neighbor_col < cols
                                and schematic[neighbor_row][neighbor_col] == "*"
                            ):
                                gear_id = neighbor_row * cols + neighbor_col
                                # Check if this star-number pair hasn't already been counted
                                if (neighbor_row * cols) + neighbor_col not in visited_cells:  # Use neighbor_row and neighbor_col
                                    if len(gear_ratios.get(gear_id, [])) == 0:
                                        gear_ratios[gear_id] = [temp_num, 1]
                                    else:
                                        gear_ratios.get(gear_id)[0] *= temp_num
                                        gear_ratios.get(gear_id)[1] += 1

                                    # Initialize the list here to ensure it's a list before appending
                                    visited_cells.append(neighbor_row * cols + neighbor_col)
    # ... (rest of the code remains the same)

                number_start = -1
                number_string = ""

    # Add up all gear ratios
    for gear_ratio in gear_ratios.values():
        if gear_ratio[1] > 1:
            gear_ratio_sum += gear_ratio[0]

    return gear_ratio_sum

engine_schematic = create_2d_array_from_file("engine_schematic.txt")
print(calculate_gear_ratios(engine_schematic))