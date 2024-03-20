import re
import json

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

def parse_workflows(filename):
    with open(filename, 'r') as file:
        workflows = []
        for line in file:
            workflow = {}
            for item in line.strip('{}\n').split(','):
                key, value = item.split('=')
                workflow[key] = int(value)
            workflows.append(workflow)
    return workflows

def workflow_sum(workflow):
    return sum(workflow.values())

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
    
def check_rule(rule, workflow):
    if rule[2] == -1:
        return False
    if rule[0] not in workflow:
        return False
    elif rule[1] == '<' and workflow[rule[0]] < rule[2]:
        return True
    elif rule[1] == '>' and workflow[rule[0]] > rule[2]:
        return True
    return False

def process_rules(workflow, rules):
    queue = []
    for rule in rules['in']:
        queue.append(rule)

    while len(queue) > 0:
        rule = queue.pop(0)
        condition = parse_rule(rule['condition'])
        if condition[2] == -1:
            destination = rule['destination']
            if destination == 'A' or destination == 'R':
                return destination
            else:
                rule = rules[destination]
                queue = []
                for item in rule:
                    queue.append(item)
                continue
            
        if check_rule(condition, workflow):
            destination = rule['destination']
            if destination == 'A' or destination == 'R':
                return destination
            else:
                rule = rules[destination]
                queue = []
                for item in rule:
                    queue.append(item)
    return 'No match'

rules = parse_rules(text)
workflows = parse_workflows("day19_input_workflows.txt")

total_sum = 0
for workflow in workflows:
    if process_rules(workflow, rules) == 'A':
        total_sum += workflow_sum(workflow)
print(total_sum)