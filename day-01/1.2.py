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
    similarity_score += (x * column_b.count(x))

print(similarity_score)
