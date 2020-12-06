from aoc.utils import read_file

lines = read_file("input.txt")


count = 0
group_letters = set()
for line in lines:
    if line =="\n":
        count += len(group_letters)
        group_letters.clear()
    else:
        line = line.strip()
        for char in line:
            group_letters.add(char)
# don't forget last group
count += len(group_letters)

print(count)