import math

def parse_data(file_name):
    with open(file_name, 'r') as file:
        data = []
        for line in file:
            direction, distance, color = line.split(' ')
            color = color.rstrip()
            data.append((direction, int(distance), color))
    return data

def get_points(data):
    start = (0, 0)
    result = [start]
    for direction, distance, color in data:
        distance = int(color[2:7], 16)  # Convert the first 5 characters from hex to decimal
        direction = 'RDLU'[int(color[7])]  # Convert the last character to direction
        if direction == 'R':
            result.append((result[-1][0], result[-1][1] + distance))
        elif direction == 'L':
            result.append((result[-1][0], result[-1][1] - distance))
        elif direction == 'D':
            result.append((result[-1][0] + distance, result[-1][1]))
        elif direction == 'U':
            result.append((result[-1][0] - distance, result[-1][1]))
    return result

def calculate_perimeter(points):
    # Initialize the perimeter
    perimeter = 0

    # Iterate over each pair of points
    for i in range(len(points) - 1):
        # Calculate the distance between the current and next point
        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]

        # Add the distance to the perimeter
        perimeter += math.sqrt(dx ** 2 + dy ** 2)

    return int(perimeter)

def calculate_area(points):
    # Initialize the area
    area = 0

    # Iterate over each pair of points
    for i in range(len(points) - 1):
        # Calculate the x and y coordinates of the current and next point
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        # Calculate the area of the triangle formed by the current and next point
        area += (x1 * y2) - (x2 * y1)

    # Add the area of the last triangle
    xn, yn = points[-1]
    x1, y1 = points[0]
    area += (xn * y1) - (x1 * yn)

    # Divide by 2 to get the area of the polygon
    area /= 2

    # Return the area
    return int(abs(area))

data = parse_data('day18_input.txt')
points = get_points(data)
print(((calculate_perimeter(points) / 2) + 1) + calculate_area(points))