def parse_seeds_and_sections(lines):
   seeds = [int(value) for value in lines[0].split()[1:]]
   sections = []

   current_section = ""
   for i in range(2, len(lines)):
       if lines[i] != "\n":
           current_section += lines[i]
       else:
           sections.append(current_section)
           current_section = "" 
   sections.append(current_section)

   return seeds, sections

def parse_sections_into_lists(sections):
    maps = {}
    for section in sections:
        lines = section.splitlines()
        map_name = lines[0].split()[0]  # Extract the map name from the first line
        maps[map_name] = [[int(value) for value in line.split()] for line in lines[1:]]  # Start from the second line (index 1)

    return maps

def expand_map_ranges(maps):
 expanded_maps = {}
 for map_name, map_data in maps.items():
     expanded_maps[map_name] = [[e[0], e[0] + (e[2] - 1), e[1], e[1] + (e[2] - 1)] for e in map_data]

 return expanded_maps

def lookup(id, map):
  for entry in map:
      source_start = entry[2]
      source_end = entry[3]
      if source_start <= id <= source_end:
          return entry[0] + (id - source_start)

  return id  # No match found, return the original ID


with open("seed_maps.txt", 'r') as file:
       lines = file.readlines()

seeds, sections = parse_seeds_and_sections(lines)
maps = parse_sections_into_lists(sections)
maps = expand_map_ranges(maps)

lowest_location = float('inf')
for seed in seeds:
    soil = lookup(seed, maps['seed-to-soil'])
    fertilizer = lookup(soil, maps['soil-to-fertilizer'])
    water = lookup(fertilizer, maps['fertilizer-to-water'])
    light = lookup(water, maps['water-to-light'])
    temperature = lookup(light, maps['light-to-temperature'])
    humidity = lookup(temperature, maps['temperature-to-humidity'])
    location = lookup(humidity, maps['humidity-to-location'])
    if location < lowest_location:
        lowest_location = location
print(lowest_location)