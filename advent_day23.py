from collections import deque
import sys
sys.setrecursionlimit(10**6)

def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    return array

def longest_path_only_downhill(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(0, 1, 0, set())])  # (row, col, path_length, visited_set)
    longest_path_length = 0

    while queue:
        row, col, path_length, visited_set = queue.popleft()
        if row == rows - 1:  # Reached the bottom row
            longest_path_length = max(longest_path_length, path_length)
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#' and (new_row, new_col) not in visited_set:
                if grid[new_row][new_col] == '.' or (grid[new_row][new_col] == '>' and new_col > col) or (grid[new_row][new_col] == '<' and new_col < col) or (grid[new_row][new_col] == 'v' and new_row > row) or (grid[new_row][new_col] == '^' and new_row < row):
                    new_visited_set = visited_set.copy()
                    new_visited_set.add((new_row, new_col))
                    queue.append((new_row, new_col, path_length + 1, new_visited_set))

    return longest_path_length

def longest_path(grid, point, visited, cost):
    rows, cols = len(grid), len(grid[0])
    row, col = point[0], point[1]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if row == rows - 1:
        return cost
    
    visited[row][col] = True
    max_val = -1
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#' and visited[new_row][new_col] == False:
            max_val = max(max_val, longest_path(grid, (new_row, new_col), visited, cost + 1))
    visited[row][col] = False
    return max_val

grid = create_2d_array_from_file("day23_input.txt")
print(longest_path_only_downhill(grid))
print(longest_path(grid, (0, 1), [[False for _ in range(len(grid[0]))] for _ in range(len(grid))], 0))