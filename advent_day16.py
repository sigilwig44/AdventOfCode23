def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    return array

grid = create_2d_array_from_file("day16_input.txt")

def move(cur_position, dir):
    visited = set()
    visited_with_direction = set()

    stack = [(cur_position, dir, set(), set())]
    visited.add(cur_position) #?

    while stack:
        cur_position, dir, visited, visited_with_direction = stack.pop()

        if cur_position[0] < 0 or cur_position[0] >= len(grid) or cur_position[1] < 0 or cur_position[1] >= len(grid[0]) or ((cur_position), dir) in visited_with_direction:
            continue

        visited.add(cur_position)
        visited_with_direction.add((cur_position, dir))

        current_space = grid[cur_position[0]][cur_position[1]]

        if current_space == '.':
            if dir == 'u': stack.append(((cur_position[0] - 1, cur_position[1]), 'u', visited, visited_with_direction))
            elif dir == 'd': stack.append(((cur_position[0] + 1, cur_position[1]), 'd', visited, visited_with_direction))
            elif dir == 'l': stack.append(((cur_position[0], cur_position[1] - 1), 'l', visited, visited_with_direction))
            else: stack.append(((cur_position[0], cur_position[1] + 1), 'r', visited, visited_with_direction))
        elif current_space == '|':
            if dir == 'u': stack.append(((cur_position[0] - 1, cur_position[1]), 'u', visited, visited_with_direction))
            elif dir == 'd': stack.append(((cur_position[0] + 1, cur_position[1]), 'd', visited, visited_with_direction))
            else: 
                stack.append(((cur_position[0] - 1, cur_position[1]), 'u', visited, visited_with_direction))
                stack.append(((cur_position[0] + 1, cur_position[1]), 'd', visited, visited_with_direction))
        elif current_space == '-':
            if dir == 'r': stack.append(((cur_position[0], cur_position[1] + 1), 'r', visited, visited_with_direction))
            elif dir == 'l': stack.append(((cur_position[0], cur_position[1] - 1), 'l', visited, visited_with_direction))
            else:
                stack.append(((cur_position[0], cur_position[1] + 1), 'r', visited, visited_with_direction))
                stack.append(((cur_position[0], cur_position[1] - 1), 'l', visited, visited_with_direction))
        elif current_space == '/':
            if dir == 'u': stack.append(((cur_position[0], cur_position[1] + 1), 'r', visited, visited_with_direction))
            elif dir == 'd': stack.append(((cur_position[0], cur_position[1] - 1), 'l', visited, visited_with_direction))
            elif dir == 'l': stack.append(((cur_position[0] + 1, cur_position[1]), 'd', visited, visited_with_direction))
            else: stack.append(((cur_position[0] - 1, cur_position[1]), 'u', visited, visited_with_direction))
        elif current_space == '\\':
            if dir == 'u': stack.append(((cur_position[0], cur_position[1] - 1), 'l', visited, visited_with_direction))
            elif dir == 'd': stack.append(((cur_position[0], cur_position[1] + 1), 'r', visited, visited_with_direction))
            elif dir == 'l': stack.append(((cur_position[0] - 1, cur_position[1]), 'u', visited, visited_with_direction))
            else: stack.append(((cur_position[0] + 1, cur_position[1]), 'd', visited, visited_with_direction))
    return len(visited)

print(move((0, 0), 'r'))