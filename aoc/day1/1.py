from aoc import utils

lines = utils.read_file("input.txt")

for i in lines:
    i = int(i)
    for j in lines:
        j = int(j)
        for k in lines:
            k = int(k)
            if not i ==j and not i==k and not k==j and i + j+k == 2020:
                print(i*j*k)