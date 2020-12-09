from aoc.utils import read_file

lines =  read_file("input.txt")
numbers = [int(l) for l in lines]

start = 0
end = start +25

for new_number in numbers[end:]:
    # find out if it is the sum of two previous
    is_sum = False
    for i in numbers[start:end]:
        for j in numbers[start:end]:
            if i+j == new_number : is_sum = True
    if not is_sum:
        print(new_number)
        break
    start +=1
    end +=1
    