from aoc.utils import read_file

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

def how_many_bags(target, containers):
    if len(containers[target]) == 0: return 1
    else : return 1+ sum([containers[target][color] * how_many_bags(color, containers) for color in containers[target]])

print(how_many_bags('shiny gold', containers) -1 ) # We don't count the initial shiny gold bag

