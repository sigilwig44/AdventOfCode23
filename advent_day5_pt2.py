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

def expand_seed_ranges(seeds):
    expanded_ranges = []
    for i in range(0, len(seeds), 2):
        # Create a tuple for the current range
        expanded_ranges.append([seeds[i], seeds[i] + (seeds[i + 1] - 1)])

    return expanded_ranges

def expand_map_ranges(maps):
 expanded_maps = {}
 for map_name, map_data in maps.items():
     expanded_maps[map_name] = [[[e[0], e[0] + (e[2] - 1)], [e[1], e[1] + (e[2] - 1)]] for e in map_data]

 return expanded_maps

def union_seeds(seeds, map):
    output = []

    for start, end in seeds:
        transformed_ranges = []
        current_start = start

        while current_start <= end:
            for destination, source in map:
                from_start = source[0]
                from_end = source[1]
                to_start = destination[0]
                overlap_start = max(current_start, from_start)
                overlap_end = min(end, from_end)

                if overlap_start <= overlap_end:
                    # If there's overlap, append any remaining non-overlapping part
                    if current_start < overlap_start:
                        transformed_ranges.append([current_start, overlap_start - 1])

                    # Apply the mapping
                    transformed_ranges.append([to_start + (overlap_start - from_start), to_start + (overlap_end - from_start)])

                    current_start = overlap_end + 1
                    break  # Move to the next seed range

            else:
                # No mapping rule applied, append the remaining range
                transformed_ranges.append([current_start, end])
                break

        output.extend(transformed_ranges)

    return output


with open("seed_maps.txt", 'r') as file:
       lines = file.readlines()

seeds, sections = parse_seeds_and_sections(lines)
seeds = expand_seed_ranges(seeds)
maps = parse_sections_into_lists(sections)
maps = expand_map_ranges(maps)

soil = union_seeds(seeds, maps['seed-to-soil'])
fertilizer = union_seeds(soil, maps['soil-to-fertilizer'])
water = union_seeds(fertilizer, maps['fertilizer-to-water'])
light = union_seeds(water, maps['water-to-light'])
temperature = union_seeds(light, maps['light-to-temperature'])
humidity = union_seeds(temperature, maps['temperature-to-humidity'])
location = union_seeds(humidity, maps['humidity-to-location'])

lowest_location = float('inf')
for location_pair in location:
    if location_pair[0] < lowest_location:
        lowest_location = location_pair[0]
print(lowest_location)