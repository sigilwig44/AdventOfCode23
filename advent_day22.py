from collections import deque

def parse_input(filename):
    with open(filename, 'r') as file:
        cubes = []
        for line in file.readlines():
            cube_str = line.strip().split('~')
            cube = [tuple(map(int, coord.split(','))) for coord in cube_str]
            cubes.append(cube)
        return cubes
    
def init_spaces(cubes):
    # Initialize x_max, y_max, and z_max with -1
    x_max, y_max, z_max = -1, -1, -1

    # Loop over the cubes
    for cube in cubes:
        for point in cube:
            # If the x, y, or z value is greater than the current maximum, update it
            if point[0] > x_max:
                x_max = point[0]
            if point[1] > y_max:
                y_max = point[1]
            if point[2] > z_max:
                z_max = point[2]

    # Create the spaces 3D array with size (x_max+1, y_max+1, z_max+1)
    spaces = [[[-1 for _ in range(z_max+1)] for _ in range(y_max+1)] for _ in range(x_max+1)]
    return spaces

def fill_spaces(cubes, spaces):
    # Loop over the cubes
    for i, cube in enumerate(cubes):
        # Get the start and end points of the cube
        start_point = cube[0]
        end_point = cube[1]

        # Loop over each space that is a part of the cube
        for x in range(start_point[0], end_point[0]+1):
            for y in range(start_point[1], end_point[1]+1):
                for z in range(start_point[2], end_point[2]+1):
                    # Set the value at the current space to the cube's index
                    spaces[x][y][z] = i

    return spaces

def fall_cubes(cubes, spaces):
    # Loop over the cubes
    for i, cube in enumerate(cubes):
        # Get the start and end points of the cube
        start_point = cube[0]
        end_point = cube[1]

        bottom_z = min(start_point[2], end_point[2])

        # Check if there is enough space below the cube
        while bottom_z > 1 and all(spaces[x][y][bottom_z - 1] == -1 for x in range(start_point[0], end_point[0]+1) for y in range(start_point[1], end_point[1]+1)):
            # Move the cube down by one space
            new_start_point = (start_point[0], start_point[1], start_point[2] - 1)
            new_end_point = (end_point[0], end_point[1], end_point[2] - 1)

            # Update the spaces array
            for x in range(start_point[0], end_point[0]+1):
                for y in range(start_point[1], end_point[1]+1):
                    for z in range(start_point[2], end_point[2]+1):
                        spaces[x][y][z] = -1
                    for z in range(new_start_point[2], new_end_point[2]+1):
                        spaces[x][y][z] = i

            # Update the cube's position
            cubes[i] = [new_start_point, new_end_point]
            start_point = new_start_point
            end_point = new_end_point
            bottom_z = min(start_point[2], end_point[2])

    return cubes, spaces

def count_destroyable_cubes(cubes, spaces):
    destroyable_cubes = 0
    for supporting_cube, cube in enumerate(cubes):
        start_point = cube[0]
        end_point = cube[1]
        top_z = max(start_point[2], end_point[2])

        cubes_above = set()
        for x in range(start_point[0], end_point[0] + 1):
            for y in range(start_point[1], end_point[1] + 1):
                if spaces[x][y][top_z + 1] != -1:
                    cubes_above.add(spaces[x][y][top_z + 1])
        safe = True
        for cube_index in cubes_above:
            cube = cubes[cube_index]
            above_start_point, above_end_point = cube[0], cube[1]
            bottom_z = min(above_start_point[2], above_end_point[2])

            if all(spaces[x][y][bottom_z - 1] == -1 or spaces[x][y][bottom_z - 1] == supporting_cube for x in range(above_start_point[0], above_end_point[0] + 1) for y in range(above_start_point[1], above_end_point[1] + 1)):
                safe = False
                break

        if safe:
            destroyable_cubes += 1
    return destroyable_cubes

def get_cubes_above(cube, spaces):
    start_point = cube[0]
    end_point = cube[1]
    max_z = max(start_point[2], end_point[2])
    cubes_above = set()
    for x in range(start_point[0], end_point[0] + 1):
        for y in range(start_point[1], end_point[1] + 1):
            if spaces[x][y][max_z + 1] != -1:
                cubes_above.add(spaces[x][y][max_z + 1])
    return list(cubes_above)

def get_cubes_below(cube, spaces):
    start_point = cube[0]
    end_point = cube[1]
    min_z = min(start_point[2], end_point[2])
    cubes_below = set()
    for x in range(start_point[0], end_point[0] + 1):
        for y in range(start_point[1], end_point[1] + 1):
            if min_z - 1 >= 0 and spaces[x][y][min_z - 1] != -1:
                cubes_below.add(spaces[x][y][min_z - 1])
    return list(cubes_below)

def count_falling_cubes(cubes, spaces):
    total_fallers = 0
    for cube_index, cube in enumerate(cubes):
        queue = deque()
        fallers = set()
        fallers.add(cube_index)
        for cube_above in get_cubes_above(cube, spaces):
            queue.append(cube_above)
        while len(queue) > 0:
            cur_cube = queue.popleft()
            cubes_below = get_cubes_below(cubes[cur_cube], spaces)
            if all(cube_below in fallers for cube_below in cubes_below) and cur_cube not in fallers:
                total_fallers += 1
                fallers.add(cur_cube)
                cubes_above = get_cubes_above(cubes[cur_cube], spaces)
                for cube_above in cubes_above:
                    queue.append(cube_above)
    return total_fallers

cubes = parse_input("day22_input.txt")
cubes = sorted(cubes, key=lambda x: x[1][2])
spaces = init_spaces(cubes)
spaces = fill_spaces(cubes, spaces)
cubes, spaces = fall_cubes(cubes, spaces)
print(count_destroyable_cubes(cubes, spaces))
print(count_falling_cubes(cubes, spaces))