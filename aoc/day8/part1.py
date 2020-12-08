from aoc.utils import read_file
from copy import deepcopy

def check_finish(index, accumulator, indices):
    i = index
    acc= accumulator
    indices_treated = deepcopy(indices)

    while i not in indices_treated and i < len(lines):
        indices_treated.add(i)
        instruction, value = lines[i].split(' ')
        value = int(value)
        if instruction == 'acc':
            acc += value
            i+=1
        elif instruction == 'jmp':
            i+= value
        else:
            i+=1
    if i >= len(lines): 
        print(acc)
        return True
    else : return False

lines = read_file("input.txt")
indices_treated = set()
i = 0
acc = 0
while i not in indices_treated and i < len(lines):
    indices_treated.add(i)
    instruction, value = lines[i].split(' ')
    value = int(value)
    if instruction == 'acc':
        acc += value
        i+=1
    elif instruction == 'jmp':
        # we try changing to nope
        if check_finish(i+1, acc, indices_treated) :
            break
        else:
            # if it doesn't work, as usual
            i+= value
    else:
        # we try changing to jmp
        if check_finish(i+value, acc, indices_treated):
            break
        else:
            i+=1





        

# Just try every possibility : if it is a jmp or a nop, we change it and see what happens. Need to keep track of changes though
