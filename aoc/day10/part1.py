from aoc.utils import read_ints

jolts = read_ints("input.txt")

jolts.sort()

one_diff = 0
three_diff = 0

# début boucle
if jolts[0] ==1:
    one_diff += 1
if jolts[0] == 3:
    three_diff += 1

for i in range(1,len(jolts)):
    if jolts[i]- jolts[i-1] ==1:
        one_diff += 1
    if jolts[i] - jolts[i-1] == 3:
        three_diff += 1
three_diff+= 1 # plugging into seat
print(one_diff*three_diff)
