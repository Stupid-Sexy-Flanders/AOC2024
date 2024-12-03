import re
import sys
sys.path.append("../")
from get_input import get_input

input = get_input(3)

total = 0
pattern = "mul\(\d*\,\d*\)"

dos = input.split("do()")

for do in dos:
    if "don't()" in do:
        do = do.split("don't()")[0]
    mul = re.findall(pattern, do)
    for i in mul:
        num_1 = i.split("(")[1].split(",")[0]
        num_2 = i.split(",")[1].split(")")[0]
        answer = int(num_1) * int(num_2)
        total += answer
            
print(total)
