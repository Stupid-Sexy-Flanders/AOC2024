import sys
sys.path.append("../")
from AOC2024.get_input import get_input

column_a = []
column_b = []
total_difference = 0

input = get_input(1).split("\n")

for line in input:
    line = line.split("  ")
    column_a.append(int(line[0]))
    column_b.append(int(line[1]))

column_a.sort()
column_b.sort()

for (x, y) in zip(column_a, column_b):
    total_difference += abs(x-y)

print(total_difference)
