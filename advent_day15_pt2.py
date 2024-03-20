class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length
    
    def __str__(self):
        return f"[{self.label} {self.focal_length}]"
    
    def __repr__(self):
        return self.__str__()

with open('day15_input.txt', 'r') as f:
    data = f.read().split(',')

boxes = [[] for _ in range(256)]

def hash(string):
    current_value = 0
    for char in string:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def insert_lens(lens):
    box_number = hash(lens.label)
    already_contains = False
    for existing_lens in boxes[box_number]:
        if existing_lens.label == lens.label:
            already_contains = True
            existing_lens.focal_length = lens.focal_length
    if not already_contains:
        boxes[box_number].append(lens)

def remove_lens(label):
    box_number = hash(label)
    for lens in boxes[box_number]:
        if lens.label == label:
            boxes[box_number].remove(lens)

def parse_string(s):
    # Split the string into parts
    parts = s.split('=', 1)
    if len(parts) == 1:
        label = parts[0].rstrip('-')
        operation = '-'
        focal_length = None
    else:
        label = parts[0]
        parts = parts[1].split('-', 1)
        if len(parts) == 1:
            operation = '='
            focal_length = int(parts[0])
        else:
            operation = '-'
            focal_length = None
    return label, operation, focal_length

for item in data:
    label, operation, focal_length = parse_string(item)
    if operation == '=':
        insert_lens(Lens(label, focal_length))
    else:
        remove_lens(label)

total_sum = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        total_sum += (i + 1) * (j + 1) * (lens.focal_length)

print(total_sum)