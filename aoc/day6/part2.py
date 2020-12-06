from aoc.utils import read_file

lines = read_file("input.txt")


count = 0
group_letters = set()
start_group = True
for line in lines:
    if line =="\n":
        count += len(group_letters)
        group_letters.clear()
        start_group = True
    else:
        line = line.strip()
        if start_group:
            start_group = False
            for char in line:
                group_letters.add(char)
        else:
            to_remove = []
            for letter in group_letters:
                if letter not in line:
                    to_remove.append(letter)
            for letter in to_remove: group_letters.remove(letter)
        
        
# don't forget last group
count += len(group_letters)

print(count)