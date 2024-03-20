def load_map_data(filename):
 """Loads map data from the given file into variables."""

 with open(filename, 'r') as file:
   lines = file.readlines()

 steps = list(lines[0].strip())

 locations = {}
 for line in lines[2:]:
   key, values = line.strip().split(' = ')
   values = values.strip('()').split(', ')  # Remove parentheses and split into a tuple
   locations[key] = tuple(values)

 return steps, locations

# Example usage:
steps, locations = load_map_data('map.txt')

current_location = 'AAA'
total_steps = 0
current_index = 0
while current_location != 'ZZZ':
    if steps[current_index] == 'L':
        current_location = locations[current_location][0]
    else:
        current_location = locations[current_location][1]
    total_steps += 1
    if current_index < len(steps) - 1:
       current_index += 1
    else:
       current_index = 0

print(total_steps)