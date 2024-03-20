from collections import deque
import numpy as np

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
    num_rows, num_columns = len(grid), len(grid[0])

    queue = deque()
    queue.append((0, starting_point))
    within_range = set()
    visited = set()
    while len(queue) > 0:
        steps, (row, col) = queue.popleft()
        if (steps, (row, col)) in visited:
            continue
        visited.add((steps, (row, col)))
        if steps == total_steps:
            within_range.add((row, col))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if (grid[new_row % num_rows][new_col % num_columns] == '.'):
                if steps <= total_steps:
                    queue.append((steps + 1, (new_row, new_col)))
    return len(within_range)

def evaluate_quadratic_equation(points, x):
    # Fit a quadratic polynomial (degree=2) through the points
    coefficients = np.polyfit(*zip(*points), 2)

    # Evaluate the quadratic equation at the given x value
    result = np.polyval(coefficients, x)
    return round(result)

input = create_2d_array_from_file("day21_input.txt")
starting_point = find_start(input)
points = [(i, count_dots_within_range(input, starting_point, 65 + i * 131)) for i in range(3)] #[(0, 3947), (1, 35153), (2, 97459)]
print(evaluate_quadratic_equation(points, 202300))