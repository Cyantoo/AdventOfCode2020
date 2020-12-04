from aoc.utils import read_file

lines = read_file("input.txt")

def check_password(first_pos, second_pos, letter, password):
    counter = 0
    if password[first_pos-1] == letter: counter +=1
    if password[second_pos-1] == letter: counter+=1
    if counter ==1: return True
    else: return False


correct_passwords = 0
for line in lines:
    line_splits = line.split(' ')
    password = line_splits[2]
    positions = line_splits[0].split('-')
    first_pos = int(positions[0])
    second_pos = int(positions[1])
    if check_password(first_pos, second_pos, line_splits[1][0], password):
        correct_passwords +=1
print(correct_passwords)

