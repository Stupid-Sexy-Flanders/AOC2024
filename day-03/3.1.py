import re
import sys
sys.path.append("../")
from get_input import get_input

input = get_input(3)

total = 0
pattern = "mul\(\d*\,\d*\)"

mul = re.findall(pattern, input)
for i in mul:
    num_1 = i.split("mul(")[1].split(",")[0]
    num_2 = i.split(",")[1].split(")")[0]
    answer = int(num_1) * int(num_2)
    total += answer

print(total)
