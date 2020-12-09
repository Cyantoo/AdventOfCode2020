from aoc.utils import read_file


def find_weakness(start, end, numbers): # from part 1
    for new_number in numbers[end:]:
        # find out if it is the sum of two previous
        is_sum = False
        for i in numbers[start:end]:
            for j in numbers[start:end]:
                if i+j == new_number : is_sum = True
        if not is_sum:
            return(new_number)            
        start +=1
        end +=1

lines =  read_file("input.txt")
numbers = [int(l) for l in lines]

start = 0
end = start +25

weakness = find_weakness(start, end, numbers)


def contiguous_sum(start, end, numbers):
    return sum([n for n in numbers[start:end+1]])

def sol(weakness, numbers):
    for start in range(0, len(numbers)):
        for end in range(start, len(numbers)):
            if contiguous_sum(start, end, numbers) == weakness:
                return min(numbers[start:end+1]) + max(numbers[start:end+1])

print(sol(weakness, numbers)) # Takes a couple seconds, would need to be optimized for larger input
    