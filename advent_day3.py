def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    return array

def sum_part_numbers(schematic):
    """Calculates the sum of all part numbers in the given engine schematic.

    Args:
        schematic: A 2D array representing the engine schematic, where each
                   element is a string containing a number, symbol, or period.

    Returns:
        The sum of all part numbers in the schematic.
    """

    rows, cols = len(schematic), len(schematic[0])
    part_number_sum = 0

    for row in range(rows):
        number_start = -1
        number_string = ""

        for col in range(cols):
            if schematic[row][col].isdigit() and col + 1 < cols:
                if number_start == -1:
                    number_start = col
                number_string += schematic[row][col]
            elif number_start != -1 or (col + 1 == cols and number_start != -1) or (col + 1 == cols and number_start != -1 and schematic[row][col].isdigit()):  # End of a number (either a non-digit character or end of row)
                if col + 1 == cols and schematic[row][col].isdigit() and number_start != 1:
                    number_string += schematic[row][col]
                temp_sum = int(number_string)

                # Check for adjacent symbols, covering all sides and diagonals
                breakout = False
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        for offset in range(number_start, col):  # Check all cells within the number's width
                            neighbor_row, neighbor_col = row + dr, offset + dc
                            if (0 <= neighbor_row < rows) and (0 <= neighbor_col < cols) and schematic[neighbor_row][neighbor_col] != "." and not schematic[neighbor_row][neighbor_col].isdigit():
                                part_number_sum += temp_sum
                                breakout = True
                                break  # Move on to the next number once a symbol is found
                        if breakout:
                            break
                    if breakout:
                        break

                number_start = -1
                number_string = ""

    return part_number_sum

engine_schematic = create_2d_array_from_file("engine_schematic.txt")
print(sum_part_numbers(engine_schematic))