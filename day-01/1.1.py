
column_a = []
column_b = []
total_difference = 0

with open("data.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.split("  ")
    column_a.append(int(line[0]))
    column_b.append(int(line[1]))

column_a.sort()
column_b.sort()

x = 0
while x < 1000:
    if column_a[x] > column_b[x]:
        difference = column_a[x] - column_b[x]
    else:
        difference = column_b[x] - column_a[x]
    total_difference = total_difference + difference
    x += 1

print(total_difference)
