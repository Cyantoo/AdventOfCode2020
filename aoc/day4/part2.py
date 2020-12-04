from aoc.utils import read_file
import re

def check_fields(fields):
    return("byr" in fields and "iyr" in fields and "eyr" in fields and "hgt" in fields and "hcl" in fields and "ecl" in fields and "pid" in fields)

def check_byr(byr):
    return(re.search(r"^\d{4}$", byr) is not None and 1920 <= int(byr) <= 2002)

def check_iyr(iyr):
    return(re.search(r"^\d{4}$", iyr) is not None and 2010 <=int(iyr)<= 2020)

def check_eyr(eyr):
    return(re.search(r"^\d{4}$", eyr) is not None and 2020 <=int(eyr)<= 2030)

def check_hgt(hgt):
    if hgt[-2:] == 'in' :
        return (re.search(r"^\d{2}$", hgt[:-2]) is not None and 59 <= int(hgt[:-2]) <=76)
    elif hgt[-2:] == 'cm':
        return (re.search(r"^\d{3}$", hgt[:-2]) is not None and 150 <= int(hgt[:-2]) <=193)
    else : return(False)

def check_hcl(hcl):
    return re.search(r"^#([0-9]|[a-f]){6}$", hcl) is not None

def check_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_pid(pid):
    return re.search(r"^\d{9}$",pid) is not None  



def check_passport(passport):

    return(
        check_byr(passport['byr']) and check_iyr(passport['iyr']) and check_eyr(passport['eyr']) and check_hgt(passport['hgt']) and check_hcl(passport['hcl']) and check_ecl(passport['ecl']) and check_pid(passport['pid'])
    )

lines = read_file("input5.txt")

valid_passports = 0
passport = {}

for line in lines:
    if line =="\n":
        if check_fields(passport) and check_passport(passport): valid_passports +=1
        passport = {}
    else:
        splits = line.split(" ")
        for split in splits:
            key, value = split.split(":")
            if value[-1:] =="\n":
                value = value[:-1]
            passport[key] = value
if check_fields(passport) and check_passport(passport): valid_passports +=1 
print(valid_passports)

