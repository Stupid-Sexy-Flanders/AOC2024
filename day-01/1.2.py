import sys
sys.path.append("../")
from AOC2024.get_input import get_input

column_a = []
column_b = []
similarity_score = 0

input = get_input(1).split("\n")

for line in input:
    line = line.split("  ")
    column_a.append(int(line[0]))
    column_b.append(int(line[1]))

for x in column_a:
    appearances = 0
    for y in column_b:
        if x == y:
            appearances += 1
    similarity_score += (x * appearances)

print(similarity_score)
