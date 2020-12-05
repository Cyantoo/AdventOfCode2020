from aoc.utils import read_file

def get_seat(s):
    row = s[:7]
    column = s[8:]
    row = row.replace("F", "0").replace("B", "1")
    row = int(row, 2)
    column = column.replace("L", "0").replace("R", "1")
    column = int(column, 2)
    return(row, column)

def get_id(row, column):
    return(row * 8 + column)


lines = read_file("input.txt")

max_id = 0
for line in lines:
    row, column = get_seat(line.strip())
    id = get_id(row, column)
    if id > max_id:
        max_id = id

print(max_id) 
