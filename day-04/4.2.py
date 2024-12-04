import sys
sys.path.append("../")
from get_input import get_input

count = 0
grid = []

input = get_input(4).split("\n")

for line in input:
    grid.append(list(line.rstrip()))

for y_index, row in enumerate(grid):
    for x_index, letter in enumerate(row):
        if letter == "A":
            mas = 0
            if ( y_index + 1 < len(grid) ) and ( x_index + 1 < len(row) ) and ( y_index - 1 >= 0 ) and ( x_index - 1 >= 0 ):
                
                if ( grid[y_index+1][x_index+1] == "S" ) and ( grid[y_index-1][x_index-1] == "M" ):
                    mas += 1
                elif ( grid[y_index+1][x_index+1] == "M" ) and ( grid[y_index-1][x_index-1] == "S" ):
                    mas += 1

                if ( grid[y_index-1][x_index+1] == "S" ) and ( grid[y_index+1][x_index-1] == "M" ):
                     mas += 1
                elif ( grid[y_index-1][x_index+1] == "M" ) and ( grid[y_index+1][x_index-1] == "S" ):
                    mas += 1
                
                if mas == 2:
                    count += 1

print(count)
