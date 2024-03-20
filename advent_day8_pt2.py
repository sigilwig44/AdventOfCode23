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

current_locations = list((key for key in locations if key.endswith('A'))) # Iterate over the keys as needed

total_steps = 0
current_index = 0
steps_per_path = []
for current_location in current_locations:
  while not current_location.endswith("Z"):
      if steps[current_index] == 'L':
          current_location = locations[current_location][0]
      else:
          current_location = locations[current_location][1]
      total_steps += 1
      if current_index < len(steps) - 1:
        current_index += 1
      else:
        current_index = 0
  steps_per_path.append(total_steps)
  total_steps = 0
  current_index = 0
print(steps_per_path)