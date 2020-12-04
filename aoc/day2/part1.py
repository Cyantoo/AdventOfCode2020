from aoc.utils import read_file

lines = read_file("input.txt")

def check_password(min, max, letter, password):
    counter = 0
    for char in password:
        if char == letter:
            counter +=1
    if counter >= min and counter <= max:
        return True
    else:
        return False


correct_passwords = 0
for line in lines:
    line_splits = line.split(' ')
    password = line_splits[2]
    min_max = line_splits[0].split('-')
    min = int(min_max[0])
    max = int(min_max[1])
    if check_password(min, max, line_splits[1][0], password):
        correct_passwords +=1
print(correct_passwords)

