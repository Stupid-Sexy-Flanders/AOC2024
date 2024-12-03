import sys
sys.path.append("../")
from get_input import get_input

input = get_input(2).split("\n")
count = 0

def check_direction(numbers):
    if int(numbers[0]) > int(numbers[1]):
        direction = "down"
    else:
        direction = "up"
    return direction

def check_if_safe(direction, numbers):
    x = 0
    safe = True
    if direction == "down": 
        while x < (len(numbers) - 1) and safe == True:
            if int(numbers[x]) < int(numbers[x+1]): # If next number ascends
                safe = False
            else:
                diff = abs(int(numbers[x]) - int(numbers[x+1]))
                if diff < 1 or diff > 3:
                    safe = False
            x += 1

    if direction == "up":
        while x < (len(numbers) - 1) and safe == True:
            if int(numbers[x]) > int(numbers[x+1]): # If next number descends
                safe = False
            else:
                diff = abs(int(numbers[x]) - int(numbers[x+1]))
                if diff < 1 or diff > 3:
                    safe = False
            x += 1
    return safe

for line in input:
    numbers = line.rstrip().split(" ")
    direction = check_direction(numbers)
    if check_if_safe(direction, numbers):
        count += 1
    else:
        new_number_safe = []
        y = 0
        while y < len(numbers):
            new_numbers = numbers[0:]
            del new_numbers[y]
            direction = check_direction(new_numbers)
            new_number_safe.append(check_if_safe(direction, new_numbers))
            y += 1
        if True in new_number_safe:
            count += 1

print(count)
