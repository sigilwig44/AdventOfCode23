class FlipFlop:
    def __init__(self, on=False, destinations=[], name=""):
        self.on = on
        self.destinations = destinations
        self.name = name

class Conjunction:
    def __init__(self, recent_high={}, destinations=[], name =""):
        self.recent_high = recent_high
        self.destinations = destinations
        self.name = name

class Broadcast:
    def __init__(self, destinations=[], name=""):
        self.destinations = destinations
        self.name = name

def create_map(filename):
    # Read the input file and split into lines
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    # Initialize the map
    input = {}

    # Process each line
    for line in lines:
        # Split the line into destinations and sources
        destinations, sources = line.split(' -> ')

        # Create a list of sources
        sources = sources.split(', ')

        # Create a Broadcast, FlipFlop, or Conjunction based on the destinations
        if destinations == 'broadcaster':
            input[destinations] = Broadcast(sources, destinations)
        elif destinations.startswith('%'):
            input[destinations[1:]] = FlipFlop(destinations=sources, name=destinations[1:])
        elif destinations.startswith('&'):
            input[destinations[1:]] = Conjunction(destinations=sources, name=destinations[1:], recent_high={})

    return input

def init_conjunctions(input):
    for key, item in input.items():
        for destination in item.destinations:
            if destination in input.keys() and type(input[destination]).__name__ == 'Conjunction':
                input[destination].recent_high[key] = False

first_highs = {}
low_count = 0
high_count = 0
def process_pulse(queue):
    global low_count
    global high_count
    while len(queue) > 0:
        module, high, sender = queue.pop(0)
        if high == True:
            high_count += 1
        else:
            low_count += 1
        if module == '':
            continue
        if isinstance(module, FlipFlop) and not high:
            module.on = not module.on
            for destination in module.destinations:
                if destination not in input.keys():
                    queue.append(('', module.on, module.name))
                else:
                    queue.append((input[destination], module.on, module.name))
        elif isinstance(module, Broadcast):
            for destination in module.destinations:
                if destination not in input.keys():
                    queue.append(('', high, module.name, True))
                else:
                    queue.append((input[destination], high, module.name))
        elif isinstance(module, Conjunction):
            module.recent_high[sender] = high
            all_true = all(module.recent_high.values())
            for destination in module.destinations:
                if destination not in input.keys():
                    queue.append(('', not all_true, module.name))
                else:
                    queue.append((input[destination], not all_true, module.name))

input = create_map("day20_input.txt")
init_conjunctions(input)
for i in range(1000):
    process_pulse([(input['broadcaster'], False, 'button')])
print(low_count * high_count)