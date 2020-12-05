from aoc.utils import read_file

def get_seat(s):
    row = s[:7]
    column = s[7:]
    row = row.replace("F", "0").replace("B", "1")
    row = int(row, 2)
    column = column.replace("L", "0").replace("R", "1")
    column = int(column, 2)
    return(row, column)

def get_id(row, column):
    return(row * 8 + column)


lines = read_file("input.txt")

list_ids = []
for line in lines:
    row, column = get_seat(line.strip())
    list_ids.append(get_id(row, column))

list_ids.sort()
for i in range(0,len(list_ids)-1):
      if list_ids[i+1] != list_ids[i]+1: print(list_ids[i]+1)
# As usual, there might be a more efficient way, but this is pretty instinctive and readable.
    