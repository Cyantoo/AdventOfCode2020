from aoc.utils import read_file


# Faire une classe custom?
def parse_line(line):
    colour, list_bags = line.split(" bags contain ")
    list_bags = list_bags.strip().split(', ')
    parsed_bags = {}
    for bag in list_bags:
        s = bag.split(' ')
        if s[0] != 'no':
            parsed_bags[s[1]+' '+s[2]] = int(s[0])   
    return colour, parsed_bags

lines = read_file("input.txt")
containers = {}

for line in lines:
    colour, contains = parse_line(line)
    containers[colour] = contains

# find all bags that can contain a shiny gold bag

# We start by finding all those which contain directly a shiny gold bag
# Then for each of them we find bags that can contain those
# and we continue until there is no new one
# handled with a set
target = 'shiny gold'

contains_gold = set()

for color in containers:
    if target in containers[color]:
        contains_gold.add(color)
to_treat = set(contains_gold)
while len(to_treat) > 0:
    target = to_treat.pop()
    for color in containers:
        if target in containers[color]:
            if color not in contains_gold:
                contains_gold.add(color)
                to_treat.add(color)
print(len(contains_gold))

