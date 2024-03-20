with open('day12_input.txt', 'r') as file:
    contents = file.read()

arrangements = []
keys = []

for line in contents.splitlines():
    line_split = line.split(' ')
    arrangement = list(line_split[0])
    key = [int(x) for x in line_split[1].split(',')]
    arrangements.append(arrangement)
    keys.append(key)

def generate_possible_arrangements(arr, key):
    result = []
    unknown_indexes = [i for i, x in enumerate(arr) if x == '?']
    key_sum = sum(key)

    def generate_arrangements(indexes, current_arr):
        if not indexes:
            if key_sum == current_arr.count('#'):
                result.append(current_arr[:])
            return

        current_index = indexes[0]
        for possibility in ['#', '.']:
            new_arr = current_arr[:]
            new_arr[current_index] = possibility
            generate_arrangements(indexes[1:], new_arr)

    generate_arrangements(unknown_indexes, arr)
    return result

def validate(arrangement, key):
    group_size = 0
    groups = []
    for element in arrangement:
        if element == '#':
            group_size += 1
        elif group_size > 0:
            groups.append(group_size)
            group_size = 0
    if group_size != 0:
        groups.append(group_size)
    return groups == key

total_valid_arrangements = 0
for i, arrangement in enumerate(arrangements):
    key = keys[i]
    possible_arrangements = generate_possible_arrangements(arrangement, key)
    for possible_arrangement in possible_arrangements:
        if validate(possible_arrangement, key) == True:
            total_valid_arrangements += 1
print(total_valid_arrangements)