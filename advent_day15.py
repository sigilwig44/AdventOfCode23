with open('day15_input.txt', 'r') as f:
    data = f.read().split(',')

def hash(string):
    current_value = 0
    for char in string:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

total_sum = 0
for item in data:
    total_sum += hash(item)

print(total_sum)