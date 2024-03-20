import re
import copy

with open("day19_input_rules.txt") as file:
    text = file.read()

def parse_rules(text):
    rules = {}
    pattern = re.compile(r"([a-z]{2,3})\{(.*?)\}")
    for line in text.splitlines():
        match = pattern.match(line)
        if match:
            key, conditions = match.groups()
            rules[key] = []
            for condition in conditions.split(","):
                condition = condition.strip()
                if condition:
                    parts = condition.split(":")
                    if len(parts) == 2:
                        rules[key].append({"condition": parts[0], "destination": parts[1]})
                    else:
                        rules[key].append({"condition": "", "destination": parts[0]})
    return rules

def parse_rule(rule):
    if rule == "":
        return "", "", -1
    else:
        parts = rule.split(">")
        if len(parts) > 1:
            condition = ">"
            number = parts[1]
        else:
            parts = rule.split("<")
            if len(parts) > 1:
                condition = "<"
                number = parts[1]
            else:
                return None
        category = parts[0]
        return (category, condition, int(number))

total_count = 0
def count_paths(workflow, cur_rules):
    global total_count

    for rule in cur_rules:
        condition = parse_rule(rule['condition'])
        destination = rule['destination']

        true_workflow = copy.deepcopy(workflow)
        if condition[1] == '<':
            true_workflow[condition[0] + '_max'] = condition[2] - 1
            workflow[condition[0] + '_min'] = condition[2]
        elif condition[1] == '>':
            true_workflow[condition[0] + '_min'] = condition[2] + 1
            workflow[condition[0] + '_max'] = condition[2]
        else:
            if destination != 'A' and destination != 'R':
                count_paths(workflow, rules[destination])
                continue
                
            elif destination == 'A':
                total_count += (workflow['x_max'] - workflow['x_min'] + 1) * (workflow['m_max'] - workflow['m_min'] + 1) * (workflow['a_max'] - workflow['a_min'] + 1) * (workflow['s_max'] - workflow['s_min'] + 1)
                continue
        if destination != 'A' and destination != 'R':
            count_paths(true_workflow, rules[destination])
            continue
            
        elif destination == 'A':
            total_count += (true_workflow['x_max'] - true_workflow['x_min'] + 1) * (true_workflow['m_max'] - true_workflow['m_min'] + 1) * (true_workflow['a_max'] - true_workflow['a_min'] + 1) * (true_workflow['s_max'] - true_workflow['s_min'] + 1)

rules = parse_rules(text)
count_paths({"x_min": 1, "x_max": 4000, "m_min": 1, "m_max": 4000, "a_min": 1, "a_max": 4000, "s_min": 1, "s_max": 4000}, rules['in'])
print(total_count)