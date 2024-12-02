
column_a = []
column_b = []
similarity_score = 0

with open("data.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.split("  ")
    column_a.append(int(line[0]))
    column_b.append(int(line[1]))

for x in column_a:
    appearances = 0
    for y in column_b:
        if x == y:
            appearances += 1
    similarity_score = similarity_score + (x * appearances)

print(similarity_score)
