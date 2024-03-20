from functools import lru_cache

springs = None
key = None

def create_input_list(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    output_list = []
    for line in lines:
        characters, numbers = line.split(' ', 1)
        characters = characters.rstrip()
        numbers = list(map(int, numbers.split(',')))
        new_list = [list(characters)]
        new_list.append(numbers)
        output_list.append(new_list)
    return output_list

def set_springs(springs_input):
    global springs
    springs = []
    for _ in range(5):
        springs += springs_input + ['?']
    springs.pop()  # Remove the last added '?'

def set_key(key_input):
    global key
    key = []
    for _ in range(5):
        key += key_input

@lru_cache(maxsize=None)
def count_possibilities(current_index=0, key_index=0, current_chain=0):
    global springs, key
        
    if current_index == len(springs):
        if key_index == len(key) and current_chain == 0:
            return 1
        elif key_index == len(key) - 1 and key[key_index] == current_chain:
            return 1
        else:
            return 0
    
    ans = 0
    for c in ['.', '#']:
        if springs[current_index] == c or springs[current_index] == '?':
            if c == '.' and current_chain == 0:
                ans += count_possibilities(current_index + 1, key_index)
            elif c == '.' and  current_chain > 0 and key_index < len(key) and current_chain == key[key_index]:
                ans += count_possibilities(current_index + 1, key_index + 1)
            elif c == '#':
                ans += count_possibilities(current_index + 1, key_index, current_chain + 1)
    return ans

input_list = create_input_list('day12_input.txt')
ans = 0
for springs_item, key_item in input_list:
    set_springs(springs_item)
    set_key(key_item)
    score = count_possibilities()
    count_possibilities.cache_clear()
    ans += score
print(ans)