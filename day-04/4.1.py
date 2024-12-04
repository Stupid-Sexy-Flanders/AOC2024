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
        if letter == "X":
            # Check East
            if x_index + 3 < len(row):
                if row[x_index+1] == "M":
                    if row[x_index+2] == "A":
                        if row[x_index+3] == "S":
                            count += 1

            # Check West
            if x_index - 3 >= 0:
                if row[x_index-1] == "M":
                    if row[x_index-2] == "A":
                        if row[x_index-3] == "S":
                            count += 1

            # Check North
            if y_index - 3 >= 0:
                if grid[y_index-1][x_index] == "M":
                    if grid[y_index-2][x_index] == "A":
                        if grid[y_index-3][x_index] == "S":
                            count += 1

            # Check South
            if y_index + 3 < len(grid):
                if grid[y_index+1][x_index] == "M":
                    if grid[y_index+2][x_index] == "A":
                        if grid[y_index+3][x_index] == "S":
                            count += 1

            # Check North East
            if ( y_index - 3 >= 0 ) and ( x_index + 3 < len(row) ):
                if grid[y_index-1][x_index+1] == "M":
                    if grid[y_index-2][x_index+2] == "A":
                        if grid[y_index-3][x_index+3] == "S":
                            count += 1

            # Check South East
            if ( y_index + 3 < len(grid) ) and ( x_index + 3 < len(row) ):
                if grid[y_index+1][x_index+1] == "M":
                    if grid[y_index+2][x_index+2] == "A":
                        if grid[y_index+3][x_index+3] == "S":
                            count += 1

            # Check North West
            if ( y_index - 3 >= 0 ) and ( x_index - 3 >= 0 ):
                if grid[y_index-1][x_index-1] == "M":
                    if grid[y_index-2][x_index-2] == "A":
                        if grid[y_index-3][x_index-3] == "S":
                            count += 1

            # Check South West
            if ( y_index + 3 < len(grid) ) and ( x_index - 3 >= 0 ):
                if grid[y_index+1][x_index-1] == "M":
                    if grid[y_index+2][x_index-2] == "A":
                        if grid[y_index+3][x_index-3] == "S":
                            count += 1

print(count)
