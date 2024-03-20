from collections import deque

def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    return array

def find_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'S':
                arr[i][j] = '.'
                return (i, j)
    return None

def count_dots_within_range(grid, starting_point, total_steps):
    queue = deque([(0, starting_point)])
    within_range = set()
    visited = [starting_point]
    while len(queue) > 0:
        steps, (row, col) = queue.popleft()
        if steps % 2 == 0:
            within_range.add((row, col))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '.') and (new_row, new_col) not in visited:
                if steps <= total_steps:
                    visited.append((new_row, new_col))
                    queue.append((steps + 1, (new_row, new_col)))
    return len(within_range)

input = create_2d_array_from_file("day21_input.txt")
starting_point = find_start(input)
print(count_dots_within_range(input, starting_point, 64))

# with open('day21_output.txt', 'w') as f:
#     for row in input:
#         f.write(''.join(map(str, row)) + '\n')