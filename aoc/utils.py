def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def read_ints(filename):
    lines = read_file(filename)
    return [int(l) for l in lines]