from aoc.utils import read_ints
from functools import cache
import sys

jolts = read_ints("input.txt")

jolts.sort()
max_jolt = jolts[-1]

# même avec @cache, problème d'overflow et de maximum depth recursion en récursif.
@cache
def count_arrangements(start, previous): # pour illustrer le récursif
    arrangements = 0
    if start >= len(jolts):
        return 0
    if jolts[start] >= max_jolt -3:
        arrangements+=1
    for i in range(1,4):
        if previous+i in jolts[start:start+3]:
            index = jolts[start:start+3].index(previous+i)
            arrangements += count_arrangements(index+1, jolts[index])
    return(arrangements)
# Faisons donc de la programmation dynamique !


# arrangements[start] est le nombre d'arrangements trouvés dans jolts[start:]
# à la fin, on veut arrangements[0]
# on peut calculer arrangemets[start] à partir de tous les arrangements[start+1,2,3]
jolts = [0]+jolts # Pour inclure la prise dans le mur qui n'est pas dans l'input
arrangements = {}
arrangements[len(jolts)-1] = 1 # rend compte du fait qu'on peut toujours brancher le plus haut à notre device
for start in range(len(jolts)-2, -1, -1):
    arrangements[start] = 0
    for i in range(1,4):
        if  start+i < len(jolts) and jolts[start+i] -jolts[start] <=3:
            arrangements[start] += arrangements[start+i]
    
print(arrangements[0])
