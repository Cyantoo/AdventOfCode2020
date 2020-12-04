from aoc.utils import read_file

lines = read_file("input.txt")

def count_trees(lines, right, down):
    x_index = 0
    y_index = 0
    trees = 0
    while y_index < len(lines):
        # check if there is a tree at the current index
        line = lines[y_index]
        if line[x_index % (len(line)-1)] == '#':
            trees += 1
        x_index +=right
        y_index +=down
    return(trees)

print(count_trees(lines, 1,1)*count_trees(lines, 3,1)*count_trees(lines, 5,1)*count_trees(lines, 7,1)*count_trees(lines, 1,2))
