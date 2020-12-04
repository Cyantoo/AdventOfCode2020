from aoc.utils import read_file

lines = read_file("input.txt")

def check_fields(fields):
    return("byr" in fields and "iyr" in fields and "eyr" in fields and "hgt" in fields and "hcl" in fields and "ecl" in fields and "pid" in fields)

valid_passports = 0
fields = []

for line in lines:
    if line =="\n":
        if check_fields(fields): valid_passports +=1 # i added one newline at the end of input.txt to make sure the last line was processed correctly
        fields = []
    else:
        splits = line.split(" ")
        for split in splits:
            fields.append(split.split(':')[0])
print(valid_passports)
        
